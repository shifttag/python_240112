'''
튜플(Tuple)
- 튜플은 몇가지 특징을 제외하고 리스트와 거의 비슷하다
- 프로그램이 실행되는 동안 그 값이 변경되면 안되는 경우 튜플을 사용한다
- 튜플은 리스트에 비해 더 적은 메모리를 필요로 하고 리스트보다 속도가 더 빠르다

리스트와 차이점
- 리스트 : []
- 튜플 : ()
- 리스트 :  생성 수정 삭제가 가능하다
- 튜플 : 요소값을 바꿀 수 없다
'''

t1 = ()     # 빈 튜플
# 튜플은 1개의 요소만 가질 때 요소 뒤에 콤마를 반드시 붙혀야 한다
t2 = (2,)
print(t1); print(type(t1))
print(t2); print(type(t2))

t3 = (1,2,3)
t4 = 1,2,3
print(t3); print(type(t3))
print(t4); print(type(t4))

t5 = ('a', 'b', ('ab', 'cd'))
print(t5); print(type(t5))

tuple1 = (1,2,'a','b')
# 튜플 인덱싱
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])

# 튜플 슬라이싱
print(tuple1[1:3]); print(tuple1[0:2])

# 튜플 더하기
tuple2 = (3,4);
result = tuple1 + tuple2
print("튜플 덧셈 결과 : ", result)

# 튜플 곱하기
tuple3 = (3,4)
result = tuple3 * 10
print(result)

tuple_len = (1,2,'a','b')
print("tuple_len 튜플 길이 :", len(tuple_len))

a = 1,2,3,4,5,
b = 'o',[1,2],'apple','coffee'
print(a); print(type(a))
print(b); print(type(b))

c = tuple([100,3.14,'Hellp'])
print(c); print(type(c))

