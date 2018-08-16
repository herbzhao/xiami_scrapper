import json

cookies_file = 'C:/Users/My Pc/Documents/GitHub/Xiami Scrapping/xiami_cookies.json'

cookies_file = open(cookies_file, 'r', encoding="utf8").read()

#print(cookies_file)

cookies_json = json.loads(cookies_file)
simplified_cookies = {}
for cookies in cookies_json:
    simplified_cookies[cookies['name']] = cookies['value']


print(simplified_cookies)