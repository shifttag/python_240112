'''
두 수를 입력받아
두 수의 공약수와 최대공약수를 구하세요
입력) 12, 24
출력
공약수 : 1, 2, 3, 4, 6, 12
최대 공약수 : 12
'''

num1 = int(input("첫번째 수 >>"))
num2 = int(input("두번째 수 >>"))
ma = 0
for i in range(1, max(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        print(i, end=' ')
        ma = i

print("\n최대공약수는 : ",ma)
'''

num1 = int(input("첫번째 수 >>"))
num2 = int(input("두번째 수 >>"))
max = 0
tmp = 0
if num1 > num2:
    tmp = num1
    num1 = num2
    num2 = tmp

print("공약수 : ", end = '')
for i in range(1, num2 - 1):
    if num1 % i == 0 and num2 % i == 0:
        print("%d " %i, end = ' ')
        max = i
print("최대 공약수 : {}" .format(max))

'''
