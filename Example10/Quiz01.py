'''
함수를 사용하세요
두 수를 입력받아 계산기 프로그램을 작성하세요
계산기 기능
1. 더하기
2. 빼기
3. 곱하기
4. 나누기 (0으로 나누려 하면 0으로 나눌 수 없습니다 라고 출력
5. 프로그램 종료
5번을 누르기 전까지는 각 메뉴를 입력받아 그에 해당하는
기능을 수행하도록 작성하세요
'''

def na(num1, num2):
    if num2 == 0:
        print("0으로 나눌수 없습니다")
    else :
        print("{} / {} = {}" .format(num1, num2, num1/num2))

while True:
    num1 = int(input("첫번 째 정수 >> "))
    num2 = int(input("두번 째 정수 >> "))
    num = int(input("1. 더하기 | 2. 빼기 | 3. 곱하기 | 4. 나누기 | 5. 프로그램 종료"))

    if num == 1:
        print("{} + {} = {}" .format(num1, num2, num1+num2))
    elif num == 2:
        print("{} - {} = {}" .format(num1, num2, num-num2))
    elif num == 3:
        print("{} * {} = {}" .format(num1, num2, num*num2))
    elif num == 4:
        na(num1, num2)
    elif num == 5:
        print("프로그램 종료!")
        break




