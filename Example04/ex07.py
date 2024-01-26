'''
연산자(Operator)
- 연산자란 특정한 작업을 수행하기 위해서 사용하는 기호
- 기능이 있는 특수문자

연산자의 우선순위
1. 단항연산자
2. 산술연산자
3. 비트연산자
4. 관계연산자
5. 논리연산자
6. 삼항연산자
7. 대입연산자
'''
# 산술 연산자
# +, -. *, ** /, //, %
a = 7; b = 2
print("{} + {} = {}".format(a, b, (a + b)))     # a + b
print("{} - {} = {}".format(a, b, (a - b)))     # a - b
print("{} * {} = {}".format(a, b, (a * b)))     # a * b
print("{} ** {} = {}".format(a, b, (a ** b)))   # a^(b)
print("{} / {} = {}".format(a, b, (a / b)))     # a / b
print("{} // {} = {}".format(a, b, (a // b)))   # a / b 의 몫
print("{} % {} = {}".format(a, b, (a % b)))     # a / b 의 나머지