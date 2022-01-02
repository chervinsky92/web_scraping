# more practical to use a weather API for applications

# pip install requests-html 
from requests_html import HTMLSession

s = HTMLSession()

location = input('Enter location: ')
url = f'https://www.google.com/search?q=weather+{location}'

# https://httpbin.org/get to get personal User-Agent info
r = s.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'})

temp = r.html.find('span#wob_tm', first = True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text
condition = r.html.find('div.VQF4g span#wob_dc', first = True).text

# print(f'The current weather at {location} is {temp}{unit} and {condition}.')
print(f'{location} {temp}{unit} {condition}')