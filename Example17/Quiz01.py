'''
N개의 숫자가 공백 없이 쓰여있다 이 숫자를 모두 합해서
출력하는 프로그램을 작성하세요

입력
첫째 줄에 숫자의 개수  N(1 <= N <= 100)이 주어진다
둘째 줄에 숫자 N개가 공백없이 주어진다

입력) 1 1         출력) 1
입력) 5 54321     출력) 15
입력) 11 10987654321
'''
'''
num1 = int(input("N"))
sum = 0
array = []
for i in range(num1):
    array.append(i)

print(num1);
for i in range(num1-1,0,-1):
    print(array[i])
    sum = sum + array[i]

print(sum)
'''

n = int(input())
numbers = input()
sum = 0
for i in range(n):
  sum = sum + int(numbers[i])
print(sum)
