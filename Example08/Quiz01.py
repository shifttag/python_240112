'''
컴퓨터가 1~100 숫자(정수 범위) 중 하나를 랜덤으로 정합니다. (이를 알려주지 않습니다.)
사용자는 이 숫자를 맞추어야 합니다.
입력한 숫자보다 정답이 크면 → "UP" 출력,
입력한 숫자보다 정답이 작으면 → "DOWN" 출력.
정답을 맞추면 → "정답"을 출력하고, 지금까지 숫자를 입력한 횟수를 알려줍니다.
'''
'''
import random

ans = random.randint(1, 100)
num = 0
a= 0
while(ans != num):
    num = int(input("정수를 입력하세요"))
    a= a+1
    if ans > num:
        print("UP")
    elif ans < num:
        print("Down")
    else:
        print("정답")
        break
print("%d 번만에 맞췄습니다" %a)
'''
import random
count = 0
computer = random.randint(1,100)
# print(computer)
while True :
    user = int(input("숫자 입력 >>"))
    count += 1
    if computer > user:
        print("UP")
    elif computer < user:
        print("DOWN")
    elif computer == user:
        print("정답입니다 . {}회 만에 맞췄어요" .format(count))
        break
