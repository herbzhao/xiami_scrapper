import re
import requests
import json
from bs4 import BeautifulSoup
import time


url = 'http://127.0.0.1:5000/'

# create a new session, probably not needed 
s = requests.session()

# user agents of newest Chrome
user_agents = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}


# s.post(url+'xiami', data={"playlist_ID":"353034283"})
# print(s.get(url+'xiami', data={"playlist_ID":"353034283"}).json()) 


# 虾米 2
# cURL to python https://curl.trillworks.com/

# playlist_ID = 353034283
# print(s.post(url+'xiami2/{}'.format(playlist_ID), data={"playlist_ID":playlist_ID}))
# print(s.get(url+'xiami2/{}'.format(playlist_ID)).json())

playlist_info = '''01 +? Relationship -— Young Thug;Future MV
02 +? Psycho -— Post Malone;Ty Dolla $ign MV'''



# xiami post/get (xiami3)
playlist_ID = 353034283
s.post(url+'xiami_ID', data={"playlist_ID":playlist_ID})
#s.post(url+'xiami_info', data={'playlist_info': playlist_info, 'special_symbols':'+?'})
print(s.get(url+'xiami_parsed_result').json())