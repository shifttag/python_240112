def myFunc(*args):
    for arg in args:
        print(arg)

myFunc(10,20,'a')
myFunc('apple', 'banana', 1.0, 10, 3.141592)
p1 = [10, 20, 30]
myFunc(p1)

print("===============================================================================================================")

def total_sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
'''
사용자로부터 입력된 문자열을 받아 공백을 기준으로 나눈 후
나뉜 각각의 문자열을 정수로 변환하여 리스트에 저장
'''
num_list = list(map(int, input("숫자 입력 >> ") .split()))
print(total_sum(*num_list))

