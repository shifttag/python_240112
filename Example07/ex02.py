'''
1부터 10까지의 모든 숫자를 더한 값
'''
i = 0 # 초기값
sum = 0
while i < 10:
    i = i + 1
    sum = sum + i
print("1부터 10까지의 총 합 : ", sum)

'''
1 ~ 100 까지의 숫자 중 짝수의 합을 출력하는
프로그램을 작성하세요
'''
i = 1
sum = 0
while i < 100:
    i = i + 1
    if i % 2 == 0:
        sum = sum + i
print("짝수의 합 : " ,sum)
