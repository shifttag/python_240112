class Oper:
    def __init__(self):
        self.res = 0
        self.seq = 1
    def plus(self, num):
        self.res = self.res + num
        return self.res
    def cal(self, num):
        self.seq = self.seq * num
        return self.seq

student1 = Oper()
student2 = Oper()
print("student1의 메모리 번지수 : ", id(student1))
print("student2의 메모리 번지수 : ", id(student2))

print(student1.plus(10))
print(student1.plus(20))
print(student1.plus(30))
print("=================")
print(student2.plus(30))
print(student2.plus(40))
print("=================")
print(student1.cal(3))
print(student1.cal(4))
print(student1.cal(5))

