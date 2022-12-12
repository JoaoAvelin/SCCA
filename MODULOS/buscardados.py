import requests
from requests.auth import HTTPProxyAuth

proxy_string = 'http://10.31.220.23:3218'



r = requests.get('https://www.google.com/',
          proxies={"http": proxy_string, "https": proxy_string})
print(r.text)
