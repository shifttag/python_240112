'''
점수를 입력받아 학점을 계산하세요
95이상 100 이하 : A+
90이상 95 미만 : A
85이상 90미만 : B+
80이상 85미만 : B
75이상 80미만 : C+
70이상 75미만 : C
65이상 70미만 : D+
60이상 65미만 : D
60미만 : F
'''
score = int(input("점수를 입력하세요"))
if(score > 100 or score < 0):
    print("점수를 잘못 입력하셨습니다")
elif(score >= 95 and score <= 100):
    print("A+ 학점입니다")
elif(score >= 90 and score < 95):
    print("A 학점입니다")
elif(score >= 85 and score < 90):
    print("B+ 학점입니다")
elif(score >= 80 and score < 85):
    print("B 학점입니다")
elif(score >= 75 and score < 80):
    print("C+ 학점입니다")
elif(score >= 70 and score < 75):
    print("C 학점입니다")
elif(score >= 65 and score < 70):
    print("D+ 학점입니다")
elif(score >= 60 and score < 65):
    print("D 학점입니다")
else:
    print("F 학점입니다")


