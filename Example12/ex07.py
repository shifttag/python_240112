import turtle as pet
from turtle import *
'''
pet.speed(1)
forward(140)
'''

# shape를 turtle로 지정하면 화살표가 아닌
# 거북이 모양으로 바뀐다
pet.shape('turtle')
color('red')    # 거북이 색상 지정

pet.begin_fill()    # begin_fill()로 색실할 준비를 한다
for i in range(5):
    pet.forward(100)
    pet.left(360 / 5)

pet.end_fill()  # 도형을 다 그린뒤에 도형에 현재 펜 색이 칠해진다

pet.exitonclick()

