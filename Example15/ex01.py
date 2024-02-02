'''
예외처리
- 예외(Exception)란 코드를 실행하는 도중에 발생한 에러
- 에러가 발생하면 프로그램이 죽지 않도록 막아주는 역할

형식)
try:
    코드
except:
    코드
'''
a = 10
b = 0
try:
    result = a / b
    print(result)
except ZeroDivisionError:       # (에러 종류 생략가능)
    print("0으로 나눌수 없습니다")
