'''
1. 2단부터 9단까지 메뉴 선택에 따라
구구단을 출력하는 프로그램을 만드세요
1. 홀수 구구단
2. 짝수 구구단
3. 프로그램 종료
'''
select = int(input("구구단 종류를 선택하시요"))
while True:
    if select == 1:
        for i in range(3,10,2):
            for j in range (1,10):
                print("{} * {} = {}" .format(i, j, i*j), end ='   ')
            print("")
        break
    elif select == 2:
        for i in range(2,10,2):
            for j in range (1,10):
                print("{} * {} = {}" .format(i, j, i*j), end = '   ')
            print("")
        break
    elif select == 3:
        print("프로그램 종료!")
        break
    else:
        print("1 ~ 3 중에 입력하세요")
'''

def odd_func():     # 홀수 구구단
    for i in range(2,10):
        if i % 2 != 0:
            for j in range(1,10):
                print("{} * {} = {}" .format(i, j, i*j))
            print()

def even_func():    # 짝수 구구단
    for i in range(2,10):
        if i % 2 == 0:
            for j in range(1,10):
                print("{} * {} = {}" .format(i, j, i*j))
            print()

while True:
    print("1. 홀수 구구단")
    print("2. 짝수 구구단")
    print("3. 종료")

    choice = int(input("메뉴 선택 >> "))
    if choice == 1:
        odd_func()
    elif choice == 2:
        even_func()
    elif choice == 3:
        print("프로그램 종료")
        break
'''
