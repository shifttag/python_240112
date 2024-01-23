'''
파이썬 정수 변환 - int()
파이썬 실수 변환 - float()
파이썬 문자열 변환 - str()
파이썬 문자 변환 - chr()
파이썬 bool 변환 - bool()
'''

# 파이썬 int 타입 변환
a1 = 10
print("정수를 정수로 변환 :",int(a1))

a2 = 3.141592
print("실수를 정수로 변환 :", int(a2))

a3 = True
print("bool을 정수로 변환 :", int(a3))

a4 = False
print("bool을 정수로 변환 :", int(a4))

# a5='a'
# print("문자열 a를 정수로 변환 :", int(a5))     -Error

# 파이썬 float 타입 변환
b1 = float(3.141592)
print("실수를 실수로 변환 :", b1)

# 정수를 실수로 변환
b2 = 10
print("정수를 실수로 변환 :", float(b2))

# bool을 실수로 변환
b3 = True
print("bool을 실수로 변환 :", float(b3))

b4 = False
print("bool을 실수로 변환:", float(b4))

# b5 = float("윤")
# print(b5)         -Error

# str타입 변환
c1 = str(10)
print("정수를 문자열로 변환 :", c1)
print("형 변환 타입 확인 :", type(c1))
c2 = str(3.141592)
print("실수를 문자열로 변환 :", c2)
print("형 변환 타입 확인 :", type(c2))

c3 = str(True)
print("bool을 문자열로 변환 :", c3)
print("형 변환 타입 확인 :", type(c3))

# char 타입 변환
chr_a = chr(65)     # 'A'
print(chr_a)

chr_b = chr(66)     # 'B'
print(chr_b)

chr_c = chr(97)     # 'a'
print(chr_c)