'''
A ~ Z 까지의 알파벳을 입력받아
대문자는 소문자로 소문자는 대문자로 변경하는 프로그램을 작성하세요

아스키코드표 참조
ord() 함수 이용 : 문자의 유니코드 숫자값을 리턴하는 함수
'''
alphaBat = str(input("알파벳을 입력하세요"))
if ord(alphaBat)> 95:
    alphaBat= ord(alphaBat) - 32
    print(chr(alphaBat))
else :
    alphaBat = ord(alphaBat) + 32
    print(chr(alphaBat))