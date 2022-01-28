import requests
from fake_useragent import UserAgent
ua = UserAgent()
#ua.chrome
#ua.random

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'http://localhost:8000/snippets/'
#url = 'https://google.com'
header = {'User-Agent':str(ua.chrome)}
r = requests.get(url, headers=header)
print(r.cookies)

# url = 'http://localhost:8000/snippets/3/'
# cookies = dict(cookies_are='working')
# r = requests.post(url, cookies=cookies, data={
#   "title": "test",
#   "code": "print('this is a test')",
#   "linenos": 'false',
#   "language": "python",
#   "style": "friendly"
# })
# print(r.status_code)
# print(r.text)