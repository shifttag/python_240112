'''
수를 입력받아서 입력받은 수의 총 합계를 구하시오
-1을 입력하면 반복이 종료되고 현재까지 입력받은
수의 총 합계를 구하세요 !!~~
'''
sum = 0

while True:
    num = int(input("정수를 입력하세요 -1을 입력시 종료됩니다 "))
    if (num == -1):
        break
    sum = sum + num
print(sum)
