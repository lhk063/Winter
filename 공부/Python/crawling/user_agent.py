import requests

res = requests.get('https://www.daangn.com/') # 당근마켓
# res.raise_for_status()
with open('my.html', 'w', encoding='utf8') as f:
    f.write(res.text)