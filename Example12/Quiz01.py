'''
월을 입력받아 계절 이름이 출력되는 프로그램을 작성하세요 (함수버전)
12, 1, 2 : 겨울
3, 4, 5 : 봄
6, 7, 8 : 여름
9, 10, 11
'''

def Spring():
    print("겨울")
def Summer():
    print("여름")
def Fall():
    print("가을")
def Winter():
    print("겨울")


num = int(input("월을 입력하세요"))
if num == 12 or num == 1 or num == 2:
    Spring()
elif num == 3 or num == 4 or num == 5:
    Summer()
elif num == 6 or num == 7 or num == 8:
    Fall()
else :
    Winter()

'''
def inputWeater(weater)
    if weater == 12 or weater == 1 or weater == 2:
        print("겨울")
    elif weater == 3 or weater == 4 or weater == 5:
        print("봄")
    elif weater == 6 or weater == 7 or weater == 8:
        print("여름")
    elif weater == 9 or weater == 10 or weater == 11:
        print("가을")
    
weater = int(input("월 입력 >>")
inputWeater(weater)
'''