'''
어느 직사각형의 정보를 출력하고
넓이를 구하는 클래스 만들기
'''

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 메소드 : 클래스의 어떠한 행위를 표현하는 것
    def arga(self):
        self.result = self.height * self.width
        return self.result

    def info(self):
        print("가로 길이는 : {}".format(self.width))
        print("세로 길이는 : {}".format(self.height))


width = int(input("가로 입력 >> "))
height = int(input("세로 입력 >> "))
rectangle = Rectangle(width, height)

# rectangle의 width라는 속성에 값을 할당
rectangle.width = width
rectangle.height = height
print("직사각형의 넓이 : ", rectangle.arga())
rectangle.info()