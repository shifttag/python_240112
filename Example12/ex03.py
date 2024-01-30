'''
파이썬의 라이브러리(표준 라이브러리, 외부 라이브러리)

표준 라이브러리
- 기본적으로 제공되는 라이브러리

외부 라이브러리
- 별도의 파일을 설치해야 사용할 수 있다
'''

import datetime
from datetime import timedelta
'''
datetime : 날짜와 시간을 다루는 모듈
'''
print(timedelta(days=5, hours=17, minutes=30, seconds=20))      # 시간 설정하는 명령어

day1 = datetime.date(2024, 1, 30)
day2 = datetime.date(2017,5,31)
diff = day1 - day2
print("두 날짜 간 차이 : ", diff.days)

import math

r1 = math.gcd(12, 24)      # 최대 공약수
print(r1)

r2 = math.lcm(15, 27)       # 최소 공배수
print(r2)

'''
모듈을 하나 생성하여
짝수인지 홀수 인지 판단하는 프로그램을 작성하세요
'''
import even
num1 = int(input("정수 입력 >> "))
even.even(num1)









