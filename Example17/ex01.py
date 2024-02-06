'''
스택(Stack)
- "쌓다" 라는 의미로 데이터를 차곡차곡 쌓아 올리는 형태의 자료구조
- 가장 최근에 들어온 데이터가 가장 먼저 나간다 LIFO(후입선출)
- 삽입과 삭제가 리스트의 한족에서 이뤄진다
- 출력순서와 입력순서가 역순으로 이뤄진다

스택 연산
push - 스택 맨 위에 항목을 삽입
pop - 스택 맨 위에 항목 삭제
peek or top - 스택의 맨 위 표시
isEmpty - 스택이 비었는지 확인
isFull - 스택이 가득 차 있는지 확인
'''
class Stack(list):
    push = list.append
    pop = list.pop

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("현재 Stack 데이터 : ", stack)
stack.append(4)
stack.append(5)
print("현재 Stack 데이터 : ", stack)
stack.pop()
print("현재 Stack 데이터 : ", stack)
stack.pop()
print("현재 Stack 데이터 : ", stack)
stack.pop()
stack.pop()
stack.pop()
print("현재 Stack 데이터 : ", stack)
