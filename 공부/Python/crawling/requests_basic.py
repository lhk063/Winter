import requests
# res = requests.get("https://www.naver.com/")
# res = requests.get('https://www.danawa.com/') # 다나와
res = requests.get('https://www.daangn.com/') # 당근마켓
res.raise_for_status()
# print('응답코드 :', res.status_code) # 200이면  정상

# if 예외처리 code
'''
if res.status_code == requests.codes.ok:
    print('정상입니다')
else:
    print('문제가 생겼습니다. [에러코드', res.status_code, "]")
'''

print(len(res.text))

with open('my.html', 'w', encoding='utf8') as f:
    f.write(res.text)