'''
국어, 영어, 수학 세 과목의 점수를 입력받아
Grade 클래스를 생성하고
총점과 평균을 구하세요!!
'''
class Grade:
    def __init__(self, Korean, English, Math):
        self.Korean = Korean
        self.English = English
        self.Math = Math

    def sum(self):
        sum = self.Korean + self.English + self.Math
        print("총점 : ",sum)
    def avg(self):
        avg = (self.Korean + self.English + self.Math) / 3
        print("평균 : ",avg)

korean = int(input("국어 점수를 입력하세요 >> "))
english = int(input("영어 점수를 입력하세요 >> "))
math = int(input("수학 점수를 입력하세요 >> "))
grade = Grade(korean, english, math)
grade.sum()
grade.avg()

'''
class Grade:
    kor = 0
    eng = 0
    mat = 0
    
    def __init__(self, kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat
        
    def total(self):
        sum = self.kor + self.eng + self.mat
        return sum
        
    def avg(self):
        sum = grade.total()
        avg = sum / 3
        return avg
        
kor = int(input("국어 점수 입력 >>")
eng = int(input("영어 점수 입력 >>")
mat = int(input("수학 점수 입력 >>")

grade = Grade(kor, eng, mat)
print("총점 : ", grade.total())
print("평균 : ", grade.avg())
'''