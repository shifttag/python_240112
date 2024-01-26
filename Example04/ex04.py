'''
튜플을 리스트 변환
* 튜플에 저장되어 있는 데이터를 변경이 필요할 경우
튜플 -> 리스트 변환
'''
a = (1,2,3,4,5)
print(a); print(type(a))
# a[1] = 20
# print(a) - Error - 튜플은 요소 변경이 불가능 하므로

change_list_a = list(a)
print(change_list_a);print(type(change_list_a))
change_list_a[1] = 20
print(change_list_a)

'''
리스트를 튜플로 변환
'''
change_tuple_a = tuple(change_list_a)
print(change_tuple_a); print(type(change_tuple_a))
# change_tuple_a[3] = 40
# print(change_tuple_a) - Error