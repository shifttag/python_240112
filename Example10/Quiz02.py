'''
세 개의 숫자를 입력받아 가장 큰 수를 출력하는
print_max 함수를 정의하고 가장 큰 수를 출력하세요
'''
def print_max(a, b, c):
    return max(a, b, c)

def print_min(a, b, c):
    return min(a, b, c)

a, b, c = input("세 개의 숫자를 입력하시요 >> ").split()
print("최대값 : " + print_max(a, b, c))
print("최소값 : " + print_min(a, b, c))

'''
def print_max(a,b,c):
    print(max(a,b,c))

num1 = int(input("숫자 입력 >> "))
num2 = int(input("숫자 입력 >> "))
num3 = int(input("숫자 입력 >> "))
print_max(num1,num2,num3)
'''