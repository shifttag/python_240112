'''
A와 B가 한 오디션 프로의 결승전에 진출했다
결승전의 승자는 심사위원으 투표로 결정된다
심사위원의 투표 결과가 주어졌을 때 어떤사람이 우승하는지 구하세요
소문자로 입력 받아도 제대로 작동하도록 만드세요

실행결과)
입력 >> AABBBBABABB
(A는 4표, B는 7표)
'''
'''
def sss(*args):
    choice_a = 0
    choice_b = 0
    for i in args:
        if choice == 'a' or choice == 'A':
            choice_a = choice_a + 1
        elif choice == 'b' or choice == 'B':
            choice_b = choice_b + 1

    if choice_a > choice_b:
        print("A가 승리하였습니다")
    elif choice_b > choice_a:
        print("B가 승리하였습니다")
    else:
        print("무승부 입니다.")

choice = input("입력 >> ")
sss(choice)
'''

str1 = input("입력 >> ")
str1_upper = str1.upper()
result1 = str1_upper.count('A')
result2 = str1_upper.count('B')
print("(A는 {}표, B는 {}표)" .format(result1, result2))