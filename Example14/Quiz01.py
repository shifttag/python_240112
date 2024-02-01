'''
책 제목과 책 저자의 정보를 담고있는 book 클래스를
생성하세요
1. 책 제목과 책 저자 정보를 출력하는 print_info() 메소드를
구현하세요
2. 다음과 같은 방법으로 book1 book2 인스턴스를 생성하세요
'''
class Book:
    def set_book(self, title, writer):
        self.title = title
        self.writer = writer
    def print_info(self):
        print("책 제목 : {}".format(self.title), end='\t\t')
        print("책 저자 : {}".format(self.writer))

book1 = Book()
book1.set_book('ㅇㅇㅇ', 'ㄹㄹㄹ')
book1.print_info()

book2 = Book()
book2.set_book('ㄴㄴㄴ', 'ㄴㄴㄴ')
book2.print_info()

'''
calss Book:
    title = ""
    writer = ""
    
    def info(self, title, writer):
        self.title = title
        self.writer = writer
        print("책 제목 : ", self.title)
        print("책 저자 : ", self.writer)
        
book1 = Book()
book2 = Book()
book1.info("파이썬", "민경태")
book2.info("어린왕자","생태쥐페리")
'''