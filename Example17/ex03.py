from collections import deque
'''
데크(Deque) 
- 큐와 스택의 장점을 모두 갖춘 자료구조
- 삽입과 삭제가 리스트의 양쪽 끝에서 모두 발생할 수 있는
자료구조
'''
queue = deque()
queue.append(10)
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print(queue)
queue.appendleft(100)
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)

print(queue.count(10))  # 큐 안에 그 값이 몇개있는지 확인
queue.remove(20)
print(queue)
queue.remove(10)
print(queue)
queue.clear()
print(queue)