'''
월을 입력받아 계절 이름이 출력되는 프로그램을 작성하세요

12, 1, 2 : 겨울
3, 4, 5 : 봄
6, 7, 8 : 여름
9, 10, 11 : 가을
'''
month = int(input("월을 입력하세요 >>"))
if month == 12 or month == 1 or month == 2:
    print("겨울")
elif month == 3 or month == 4 or month ==5 :
    print("봄")
elif month == 6 or month == 7 or month == 8 :
    print("여름")
elif month == 9 or month == 10 or month == 11:
    print("가을")
else :
    print("월을 똑바로 입력하지 않으셨습니다")