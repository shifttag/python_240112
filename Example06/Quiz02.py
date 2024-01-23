'''
실행 결과와 같은 간단한 계산 기능을 수행하는 프로그램을 작성
하세요

실행 예)
기능선택
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
계산기 기능을 선택하세요 (1/2/3/4) >> 3
첫번째 숫자를 입력하세여 >> 5
두번째 숫자를 입력하세요 >> 10
5 x 10 = 50
'''
calculator = int(input("계산기 기능을 선택하세요 (1. 더하기 / 2. 빼기 / 3. 곱하기 / 4. 나누기)"))
first = int(input("첫번째 숫자를 입력하세요"))
second = int(input("두번째 숫자를 입력하세요"))
if(calculator == 1):
    print("{} + {} = {}" .format(first, second, first+second))
elif (calculator == 2):
        print("{} - {} = {}".format(first, second, first - second))
elif (calculator == 3):
    print("{} x {} = {}".format(first, second, first * second))
elif (calculator == 4):
    if(second == 0):
        print("0으로는 나눌수 없습니다")
    else:
        print("{} / {} = {}".format(first, second, (first / second)))
else :
    print("계산기 기능을 잘못 선택하셨습니다")
