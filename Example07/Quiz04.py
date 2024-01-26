'''
while문을 이용해 두 개의 주사위를 던졌을 때 나우는 눈을
출력하고 눈의 합이 5가 아니면 계속 주사위를 던지고
눈의 합이 5이면 실행을 멈추세요
그리고 주사위의 눈의 합을 모두 출력하세요
'''
import random
sum = 0
while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    print("{} + {} = {} ".format(dice1, dice2, sum))
    if sum == 5:
        break
