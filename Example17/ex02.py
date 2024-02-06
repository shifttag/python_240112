'''
큐(Queue)
- 스택과 다르게 선입선출(FIFO) 구조를 가지고 있다
- 스택은 먼저 들어온 데이터가 가장 나중에 나가는 구조
큐는 먼저 들어온 데이터가 가장 먼저 나가는 구조
- 큐 자료구조는 한쪽에서는 데이터 삽입만 이뤄지고
다른 한쪽에서는 데이터 추출만 한다
- 삽입을 enQueue 라고 하며, 삭제를 deQueue 라고 한다
front(머리), rear(꼬리)

큐의 연산
enQueue() : 큐에 데이터를 넣는다
deQueue() : 큐에 데이터를 뺀다
isEmpty() : 큐가 비었는지 확인
isFull() : 큐가 꽉 찼는지 확인
peek() : 앞에 있는 원소를 삭제하지 않고 반환
'''
class Queue():
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        if not self.queue:
            return "큐 비었어요"
        else:
            return "큐 안비었어요"
    def enQueue(self,value):
        self.queue.append(value)
    def deQueue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return 0
queue = Queue()
print("큐 상태 체크 : ", queue.isEmpty())
queue.enQueue(10)
print("큐 상태 체크 : ", queue.isEmpty())
queue.enQueue(20)
queue.enQueue(30)
queue.enQueue(40)
print(queue.queue)
queue.deQueue()
print(queue.queue)  # [20, 30, 40]
queue.deQueue()
print(queue.queue)  # [30, 40]
queue.deQueue()
queue.deQueue()
queue.deQueue()
print(queue.queue)
print("큐 상태 체크 : ", queue.isEmpty())