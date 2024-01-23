'''
다음 튜플에 저장되어 있는 값 중 네이버를 넥슨으로 변경하세요
'''
company = ('삼성', 'LG', '카카오', '네이버')
company_list = list(company)
company_list[3] = '넥슨'
print(company_list);print(type(company_list))

'''
5자리로 구성된 학번 '31025'를 학년, 반, 번호로 나누어 출력하는 프로그램을 작성하세요
출력 예) 3학년 10반 25번
'''
str = "31025"
str1 = str[0]; str2 = str[1:3]; str3 = str[3:5]
print("{}학년 {}반 {}번".format(str1, str2, str3))

