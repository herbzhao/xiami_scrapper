import re
import requests
import json
from bs4 import BeautifulSoup
import time

def use_ajax_page(playlist_id):
    # method 1 finds a awesome url which contains the song information
    ########## even better way
    # ask user to input this value
    playlist_id = playlist_id
    url = 'https://www.xiami.com/collect/ajax-get-list?_=&id={}&p={}'.format(playlist_id, 1)

    # create a new session, probably not needed 
    s = requests.session()

    # user agents of newest Chrome
    user_agents = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    #page = s.get(url, cookies=simplified_cookies, headers=headers)
    # use GET to download the content of the url
    page = s.get(url, headers=headers)
    # use beautifulsoup for better parsing
    soup = BeautifulSoup(page.text, 'html.parser')
    #print(soup.prettify())

    # save to local files - easier for dev
    temp_file = 'C:/Users/My Pc/Documents/GitHub/Xiami Scrapping/xiami_page.json'
    temp_file = open(temp_file, 'w+', encoding="utf8")
    temp_file.write(soup.prettify())
    temp_file.close()

    # parsing - easy! It's Json
    songs_info = json.loads(soup.text, strict=False)
    # the json file tells us how many pages are there for the song list
    total_page = songs_info['result']['total_page']

    # parsing the list using JSON
    parsed_playlist = []
    for i in range(total_page):
        url = 'https://www.xiami.com/collect/ajax-get-list?_=&id={}&p={}'.format(playlist_id, i+1)
        page = s.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        # parsing the file as JSON, but sometimes the song names are illegal... trying to fix
        try:
            songs_info = json.loads(soup.text)
        except json.decoder.JSONDecodeError:
            # if there is an error in JSON file, require user input
            print("an error has been found on \n" + url)
            print("go to parse the JSON and feed it back")
            songs_info = json.loads(input('paste parsed JSON here \n'))

        parsed_playlist += ["{} - {}".format(song['name'], song['artist_name']) for song in songs_info['result']['data']]
            

    # convert the list into a string with line break
    parsed_playlist_str = ''
    for i in parsed_playlist:
        parsed_playlist_str = parsed_playlist_str + i +'\n'

    playlist_cleaned = open("C:/Users/My Pc/Documents/GitHub/Xiami Scrapping/playlist_cleaned.txt","w+", encoding="utf8")
    playlist_cleaned.write(parsed_playlist_str)
    playlist_cleaned.close()
    
    
    print('The parsed list is ready, you can copy it to http://www.playlist-converter.net/')

    return (parsed_playlist_str)


def use_list_page():
    ## method 2 requires login and can only load first 50 songs, use requests

    #### working with html files
    #from bs4 import BeautifulSoup
    #soup = BeautifulSoup(html_file, "lxml")

    # load files
    url = 'https://www.xiami.com/collect/32713355'
    #url = 'http://httpbin.org/cookies'

    # read cookies
    cookies_file = 'C:/Users/My Pc/Documents/GitHub/Xiami Scrapping/xiami_cookies.json'
    cookies_file = open(cookies_file, 'r', encoding="utf8").read()
    cookies_json = json.loads(cookies_file)
    simplified_cookies = {}
    for cookies in cookies_json:
        simplified_cookies[cookies['name']] = cookies['value']

    user_agents = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    s = requests.session()

    page = s.get(url, cookies=simplified_cookies, headers=headers)

    url_2 = 'https://www.xiami.com/collect/ajax-get-list?_=1533333513276&id=32713355&p=2&limit=50'
    r = s.post(url)



    soup = BeautifulSoup(page.text, 'html.parser')

    # save to local files 
    temp_file = 'C:/Users/My Pc/Documents/GitHub/Xiami Scrapping/xiami_page.txt'
    temp_file = open(temp_file, 'w+', encoding="utf8")
    temp_file.write(soup.prettify())
    temp_file.close()

    #print(soup.prettify())

    songs_info = soup.findAll("span", {"class": "song_name"})
    #print(songs_info)



    cleaned_songs_info = [song.get_text() for song in songs_info]
    cleaned_songs_info = [song.replace('\t','').replace('\n','').replace('...','').replace('-—','-').replace('--','-') for song in cleaned_songs_info]

    print(cleaned_songs_info)
    """ for song_info in songs_info:
        print(song_info)
        song_info = str(song_info)
        song_info = re.sub(head, '', song_info)
        song_info = re.sub(middle, '-', song_info)
        song_info = re.sub(middle2, '', song_info)
        song_info = re.sub(tail, '', song_info)
        cleaned_playlist = cleaned_playlist + song_info
    """




example_text = '''01 +? Relationship -— Young Thug;Future MV
02 +? Psycho -— Post Malone;Ty Dolla $ign MV
03 +? Nowadays -— Lil Skies;Landon Cube 试听分享添加Nowadays到歌单下载发送到
04 +? TR666 -— Trippie Redd;Swae Lee 试听分享添加TR666到歌单下载发送到'''


def paste_text_from_browser(playlist_info=example_text, special_symbols='+>'):
    ## method 3 requires user to copy paste the list and python will parse it.
    ####################################################

    # regex patterns for the begining and end of string
    #head = re.compile('\d\d\d*\s*@*=*\s*')
    head_re = '\d\d\d*\s*\{}*\{}*\s*'.format(special_symbols[0], special_symbols[1])
    head = re.compile(head_re)
    middle = re.compile('-—|--')
    middle2 = re.compile('\.\.\.')
    tail = re.compile('试.*')


    # file = open("C:/Users/My Pc/Documents/GitHub/Xiami Scrapping/playlist.txt","w+", encoding="utf8")
    # file.write(playlist_info)
    # file.close()
    # file = open("C:/Users/My Pc/Documents/GitHub/Xiami Scrapping/playlist.txt","r", encoding="utf8")
    # playlist = file.readlines()
    # file.close()

    # split into lines for legacy reason
    playlist_info = playlist_info.splitlines()

    parsed_playlist = ''
    for i in range(len(playlist_info)):
        song = playlist_info[i]
        song = re.sub(head, '', song)
        song = re.sub(middle, '-', song)
        song = re.sub(middle2, '', song)
        song = re.sub(tail, '', song)
        parsed_playlist = parsed_playlist + song + '\n'

    new_file = open("C:/Users/My Pc/Documents/GitHub/Xiami Scrapping/playlist_cleaned.txt","w+", encoding="utf8")
    new_file.write(parsed_playlist)
    new_file.close()

    #print(parsed_playlist)
    return (parsed_playlist)

# method 1 is the smartest
#use_ajax_page(playlist_id = 353034283)

# method 3 is the most user friendly
paste_text_from_browser(special_symbols='+?')
