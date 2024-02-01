'''
다음 Tv 클래스가 있다
Tv 클래스를 상속받은 ColorTv 클래스를 작성하세요

출력 결과)
64인치
Blue
'''
class Tv:
    size = 0
    def __init__(self, size):
        self.size = size

    def getSize(self):
        print("{}인치" .format(self.size))

class ColorTv(Tv):
    def __init__(self, size, color):
        super().__init__(size)
        self.color = color

    def info(self):
        super().getSize()
        print(self.color)


colortv = ColorTv(64, "Blue")
colortv.info()