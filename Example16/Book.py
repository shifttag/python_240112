import  urllib.request  # url을 열기 위한 확장 라이브러리
from urllib.parse import quote
import json
''' naver 
Client ID : fAjunZ49hsTnUUljLrL9
Client Secret : xiZBpPuvk6
'''
search = quote(input("검색할 단어를 입력해 주세요 >> "))
start = quote(input("시작 위치 번호를 입력해 주세요 >>"))
client_id = "fAjunZ49hsTnUUljLrL9"
client_secret = "xiZBpPuvk6"

'''
쿼리스트링
- 쿼리스트링이란 URL 뒤에 입력 데이터를 함께 제공하는 가장
단순한 데이터 전달 방법(파라미터)
- 웹 개발에서 데이터를 요청하는 방식 중 GET, POST 방식이 있는데
주로 GET 방식에서 사용
- URL 주소뒤에 물음표(?) key1=value&key2=value
방식으로 데이터 요청
'''

API_URL = "https://openapi.naver.com/v1/search/book.json?query=" + search + "&start=" + start
request = urllib.request.Request(API_URL)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()    # Http 상태코드를 얻음

if rescode == 200:
    response_body = response.read()
    json_str = response_body.decode('utf-8')
    print(json_str)
    data = json.loads(json_str)
    data_parse = data['items']
    for i in data_parse:
        print("===================================")
        print("제목 : ", i['title'])
        print("출판사 : ", i['publisher'])
        print("저자 : ", i['author'])
else:
    print("Error Code : ", rescode)
