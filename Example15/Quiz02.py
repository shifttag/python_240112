'''
학생 클래스를 만들고
이름, 나이, 성별, 거주지를 입력받아
출력하세요
'''

class Student():
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def info(self):
        print("이름 : ",self.name)
        print("나이 : ", self.age)
        print("성별 : ", self.gender)
        print("주소 : ", self.address)

name = input("이름을 입력하세요")
age = int(input("나이를 입력하세요"))
gender = input("성별을 입력하세요")
address = input("주소를 입력하세요")
student1 = Student(name, age, gender, address)


Student.info(student1)
