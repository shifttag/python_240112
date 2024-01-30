import turtle as pet
from turtle import *
'''
반복문을 사용하여 사각형 그려보세요
'''
pet.color('red')
pet.shape('turtle')
begin_fill()
for i in range(4):
    forward(100)
    left(360 / 4)
    forward(100)
end_fill()
exitonclick()