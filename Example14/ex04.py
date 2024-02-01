'''
super()
- 상속관계에서 상속의 대상인 부모 클래스를 호출하는 함수
- 자식클래스에서 부모클래스의 기능을 사용하고 싶을 때 사용하면 된다

'''

class Coffee:
    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print("원두 : {}" .format(self.bean))

class Espresso(Coffee):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print("물 : {}ml" .format(self.water))

coffee = Espresso("콜롬비아", 30)
coffee.espresso_info()
# coffee.coffee_info()