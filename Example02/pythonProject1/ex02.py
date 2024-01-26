'''
자료형
-int(정수), float(실수), complex(복소수), str(문자열), bool(논리)

'''
num1 = 10 # 양의 정수
num2 = -10 # 음의 정수
num3 = 0
print(num1);print(num2);print(num3)
print(type(num1));print(type(num2));print(type(num3))

# 파이썬에서는 기본적으로 원하는 값을 크기에 제한없이 사용 가능함
num4 = 9*9*9*9*9*9*9*9999*99999*9999999*99999999*99999999*999999999*99999999*9999999*999999999*99999999*999999999*9999999
print(num4); print(type(num4))

# 10진수, 2진수, 8진수, 16진수
num1_int = 10
print(bin(num1_int))    # 2진수
print(oct(num1_int))    # 8진수
print(hex(num1_int))    # 16진수

# 실수(flaot)
# 소수점이 있는 숫자를 실수라고 한다
num_float = 10.0
print(num_float); print(type(num_float))
num1_float = 3.141592
print(num1_float); print(num1_float)

# 문자열
a_str = 'Good Student'
b_str = "Bad Student"
print(a_str); print(type(a_str))
print(b_str); print(type(b_str))

c_str = "fadfdsffdsfsdfasd"
print(c_str);print(type(c_str))

# 논리(bool)
# True, False 값을 가질 수 있다
# 숫자 0 , 빈 문자열, [] 빈 리스트 모두 false로 변환
a= 1; b=0
print(bool(a));print(bool(b))
str1 = ""
print(bool(str1));
list1 = []
print(bool(list1))

# 복소수(complex)
# 실수부오 허수부를 구분하여 표현할 수 있다.
a1 = 2 + 3j
print(type(a1));print(a1)

# 기본적인 사칙연산
a1 = 20
b1 = 3
print("덧셈 결과 : ", a1 + b1)
print("뺄셈 결과 : ", a1 + b1)
print("곱셈 결과 : ", a1 * b1)
print("나눗셈 결과 : ", a1 / b1)
print("나눗셈 나머지 : ", a1 % b1)
print("나눗셈 몫만 출력 : ", a1 // b1)
print("2를 4번 제곱한 결과 : ", 2 ** 4)