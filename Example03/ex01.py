'''
print() 함수
- 출력할 문장을 ' ' 또는 " " 로 감싸야 한다
- 콤마로 문자열을 나열할 경우 공백이 자동으로 추가된다
- + 기호를 사용하여 문자열을 공백없이 연결할 수 있다

print() 속성
- End 속성 : print 함수를 여러 줄을 써서 실행해보면 각각 줄바꿈이 되어 출력되는걸 확인할 수 있다.
- End 속성에 "\n" 이 설정되어 있는데 이를 end 구문을 사용하여 변경가능하다

Separator
- 출력할 데이터가 여럿이면 괄호 안에 출력할 데이터들을 print 함수 내부에는 구분자로 불리는 sep이라는 속성이 있어 값들이 나란히 출력된다
- 기본값으로 공백 문자열이 지정되어 있는데 sep 구문을 사용하여 변경 가능

제어 문자 종류
\n : 줄바꿈, 개행문자
\t : 위 아래 줄 간격 맞춰 띄기 (tab)의 약자
\\ : 역슬래시 표현
\" : "표현
\' : '표현
'''
print("Hello", "World")
print("Hello" + "World")
print("ddddd")
print("Python ", end=' ')       # , end = '' 는 다음줄을 이어서 출력한다는 말
print("Java ", end=' ')
print("C ", end=' ')
print("React ", end='\n')
print("===================================")

# end 사용 예
print("Spring", end = ', ')
print("Spring Boot", end = ', ')
print("Android", end = '\n')

print("=================================")
print("자기소개", end='\n')
print("이름 : ", end = '')
print("윤준형 \n나이 :",150, "살")

# 제어 문자 사용 예
print("나는\t\t\t", "학교에", "갑니다")
print("I\'am a good boy")
print("he said \"python is easy\"")

# sep 사용 예
print("Python", "Java", "C", sep ='  ')
print("Python", "쉽다.", sep = '은 엄청')        # ,sep = '' 는 ,자리에 '@'를 추가
