'''
함수 내용만 있는 함수
'''

def sayHello():
    print("Hello")
    print("Python very very easy")
    print("good boy")
sayHello()

# 매개변수만 있는 함수
def signGood(when):
    if when == 1:
        print("Good Morning")
    elif when == 2:
        print("Good Afternoon")
    elif when == 3:
        print("Good evening")
    else :
        print("Good Night")

signGood(1);signGood(2);signGood(3);signGood(4);

def hap(a, b):
    result = a + b
    print("전달받은 두 수의 합은 : ", result)

hap(100, 200)