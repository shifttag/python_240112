'''
계산기 기능을 하는 Calculator 클래스를 만들고
덧셈, 뺄셈, 곱셈, 나눗셈 연산을 할 때마다 어떠한
연산을 몇번 수행했는지 출력하세요

5번을 누르면
덧셈 연산을 두번했다면 덧셈 2
뺄셈 연산을 한번했다면 뺄셈 1

1. 덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈, 5. 프로그램 종료
'''
class Calculator:
    def __init__(self):
        self.addCount = 0
        self.minCount = 0
        self.mulCount = 0
        self.divCount = 0

    def add(self, num1, num2):
        self.addCount = self.addCount + 1
        return num1 + num2
    def min(self, num1, num2):
        self.minCount = self.minCount + 1
        return num1 - num2
    def mul(self, num1, num2):
        self.mulCount = self.mulCount + 1
        return num1 * num2
    def div(self, num1, num2):
        self.divCount = self.divCount + 1
        return num1 / num2
    def info(self):
        print("덧셈 : {}".format(self.addCount))
        print("뺄셈 : {}".format(self.minCount))
        print("곱셈 : {}".format(self.mulCount))
        print("나눗셈 : {}".format(self.divCount))

cal = Calculator()

while True:
    choice = int(input("1. 덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈, 5. 프로그램 종료 >> "))

    if choice == 1:
        num1 = int(input("숫자 입력 >> "))
        num2 = int(input("숫자 입력 >> "))
        print(cal.add(num1, num2))
    elif choice == 2:
        num1 = int(input("숫자 입력 >> "))
        num2 = int(input("숫자 입력 >> "))
        print(cal.min(num1, num2))
    elif choice == 3:
        num1 = int(input("숫자 입력 >> "))
        num2 = int(input("숫자 입력 >> "))
        print(cal.mul(num1, num2))
    elif choice == 4:
        num1 = int(input("숫자 입력 >> "))
        num2 = int(input("숫자 입력 >> "))
        print(cal.div(num1, num2))
    elif choice == 5:
        cal.info()
        break