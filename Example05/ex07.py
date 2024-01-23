'''
두 정수 a와 b를 입력받아서
두 정수의 크기를 비교하여 왼쪽수가 크면 >
오른쪽 수가 크면 <
같으면 = 을 출력!!
'''
a = int(input("a 정수 입력 >> "))
b = int(input("b 정수 입력 >> "))

if a > b :
    print(">")
elif a < b:
    print("<")
else :
    print("=")