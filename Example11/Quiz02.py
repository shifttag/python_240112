'''
2. 자신의 이름 전체를 영어로 입력받고
'성'과 '이름'을 바꾸는 함수를 만들어 해당 함수를
통해 바뀐 영문 이름을 출력하세요
입력) Yun JunHyeong           출력) JunHyeong Yun
'''
name = input("영어 이름을 입력하세요 ")
list1 = name.split(' ')
iga = list1[0]
list1[0] = list1[1]
list1[1] = iga
print(' '.join(list1))


'''
def listToString(name):
    result = name.split()
    temp = result[0]
    result[0] = result[1]
    result[1] = temp

    str_name = ' '.join(s for s in result)
    return str_name


name = input("이름 입력 >> ")
print(listToString(name))
'''