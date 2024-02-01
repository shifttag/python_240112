'''
클래스 상속
* 상속이란 부모가 자식에게 어떤 것을 물려준다는 것을 의미

상속
- 다른 클래스의 기능을 물려받는것
부모클래스(슈퍼클래스), 자식클래스(서브클래스)

부모클래스 : 상속해주는 클래스
자식클래스 : 상속받는 클래스

형식)
class 부모:
    내용

class 자식(상속받을 클래스 이름 = 부모):
    내용
'''

'''
* 서브클래스가 슈퍼클래스를 상속받으면
서브클래스는 슈퍼클래스의 변수, 메소드 기능들을
사용할 수 있다
'''
class Person:
    def __init__(self,name):
        self.name = name

    def eat(self, food):
        print(self.name + "가" + food + "를 먹습니다")

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(self.name + "는" + self.school + "에서 공부합니다")

potter = Student("해리포터", "호그와트")
potter.eat("피자")
potter.study()