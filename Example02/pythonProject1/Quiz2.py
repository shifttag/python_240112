'''
1. 변수 one과 two를 선언하여 문자열 더하기를 하세요
one = "Hello"
two = "Python"
'''
'''
2. str_lang = "python" 
위 변수를 선언하여 str_lang 문자열에서 첫번째 문자와 세번째 물자를 출력하세요
'''
'''
3. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요
차 번호 : 24가 2210
'''
'''
4. 인덱싱을 사용해서 '홀'만 출력하세요
str_lan = "홀짝홀짝홀짝"
'''
one = "Hello"
two = "Python"
print(one + " " + two)

str_lang = "python"
print (str_lang[0])
print (str_lang[2])

car = "24가 2210"
print(car[4:])

str_lan = "홀짝홀짝홀짝"
print(str_lan[::2])

for i in range(6) :
    if(str_lan[i] == "홀") :
        print(str_lan[i])