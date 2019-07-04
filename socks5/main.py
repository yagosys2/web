import  requests

proxies = dict(http='socks5h://127.0.0.1:6005',
          https='socks5h://127.0.0.1:6005')
res = requests.get('https://www.google.com',proxies=proxies)
print(res.text)
