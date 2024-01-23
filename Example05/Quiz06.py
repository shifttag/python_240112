'''
정수 하나를 입력받아 초 라고 가정하고
몇시간 몇 분 몇 초인지 계산하는 프로그램을
작성하세요
'''
time = int(input("몇 초 : "))
min = (time // 60) % 60
hour = time // 3600
sec = time % 60
print(hour,"시",min,"분",sec,"초")

# 답
time = int(input("몇 초 >> "))
hour1 = time // (60 * 60)
minute = time // 60 - (hour * 60)
second = time % 60

print("{} 시간".format(hour1))
print("{} 분".format(minute))
print("{} 초".format(second))