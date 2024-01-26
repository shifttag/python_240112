'''
딕셔너리(Dict)
- 키(key), 값(value)가 한 쌍이 하나의 대응 관계를 가지고 있다
- key는 중복이 불가능 하다
- vlaue은 중복이 가능하다
- key는 수정이 불가능 하고 value 값은 수정이 가능
- 덧셈, 곱셈 등 산술 연산이 불가능 하다

형식)
{key1:value1, key2:value2, key3:value3, ....}
'''

dic = {'name':'윤준형', 'phone':'010-3528-8515', 'birth':'19950816'}
print(dic); print(type(dic))

a = {'a':[1,2,3]}
print(a)

# 딕셔너리 쌍 추가
a['b'] = "윤준형"
print(a)

a['c'] = 10
print(a)

# 딕셔너리 요소 삭제
# 딕셔너리 삭제는 키값으로 접근하여 삭제해야 한다
del a['b']
print(a)

# 해당 key값이 딕셔너리에 존재하는지 확인하는 방법
print('c' in a)






