import turtle

# 각종 설정
player = turtle.Turtle()
player.color("green")  # 색깔 정하기(원하는 색깔 기입 가능)
player.shape("turtle")  # 모양 정하기
player.speed(10)  # 속도는 숫자가 작을수록 빠름
screen = player.getscreen()

for i in range() :
    player.forward(10)
    player.left(355)

screen.listen()  # 프로그램 활성화
screen.mainloop()  # 프로그램이 계속 동작하는 상태를 유지하겠다!