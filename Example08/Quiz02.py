'''
while 문을 활용하여 키보드로부터
입력된 데이터로 예금, 출금, 조회, 종료 기능을
제작하세요
'''
money = 0
while True:
    print("-----------------------------------")
    print("1. 예금 | 2. 출금 | 3. 잔금 | 4. 종료")
    print("-----------------------------------")
    choice = int(input(">> "))
    if(choice == 1):
        input_money = int(input("예금액 :"))
        money = input_money + money
    elif(choice == 2):
        output_money = int(input("출금액 :"))
        if money < output_money:
            print("잔고가 부족합니다")
        else:
            money = money - output_money
            print("출금되었습니다")
    elif(choice == 3):
        print("잔고 :", end = ' ')
        print(money)
    elif(choice == 4):
        print("프로그램을 종료합니다.")
        break

