import  requests

proxies = dict(http='socks5h://127.0.0.1:6005',
          https='socks5h://127.0.0.1:6005')
res = requests.get('https://www.google.com',proxies=proxies)
print(res.text)

from betterreads import client

key = 'UnJEUENuYcvAB9ZAWrD7Q'

secret = 'RgEtOdnNHFxnkumatFOLgzPnfMeN0dQEJ8DbjLV4'

gc = client.GoodreadsClient(key,secret)

author = gc.author(2618)
