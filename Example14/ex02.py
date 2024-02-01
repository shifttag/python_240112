class User:
    def __init__(self, id, password, name, email):
        self.id = id
        self.password = password
        self.name = name
        self.email = email

    # 소멸자 : 리소스 해제 등 객체를 제거할 때 사용
    def __del__(self):
        print(self.id + "객체 소멸")
        print(self.password + "객체 소멸")
        print(self.name + "객체 소멸")
        print(self.email + "객체 소멸")

user1 = User("zzpp7979", "123456", "홍길동", "네이버")
user2 = User("aa3", "1234444", "김길동", "다음")

del user1
del user2