'''
내장 함수
- 파이썬에서는 항상 사용할 수 있는 많은 함수가 내장되어 있으며
이를 내장함수라고 한다
- print(), input()
'''
# chr() 함수
# chr() 함수는 특정 문자의 유니코드 값을 전달하면 해당 유니코드 값을 가진 문자를 반환하는 함수
print(chr(48)); print(chr(65)); print(chr(66))
print(chr(97)); print(chr(98))

print("==============================")

'''
ord() 함수
- 문자를 전달하면 해당 문자의 유니코드 값을 반환
'''
print(ord('A')); print(ord('a'))
print("==============================")

# max() : 전달된 인수 중 가장 큰 값을 반환
list1 = [1,2,3,4,5,6,7,8,9,10]
print(max(list1))

#min() : 전달된 인수 중 가장 작은 값을 반환
print(min(list1))