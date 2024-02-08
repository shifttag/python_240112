'''
입력된 문자열을 역순으로 출력하는
함수를 작성하세요

실행결과)
입력 >> python
출력 >> nohtyp
'''
string = input("문자열 입력")
list = []
for i in range(len(string)):
    list.append(string[i])

for i in range(len(string)-1,-1,-1):
    print(str(list[i]), end='')
