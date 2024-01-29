'''
1 ~ 100 까지의 범위의 수를 입력받아
50보다 큰 수를 콘솔창에 출력하세요
몇 번을 입력받는지는 아무도 모릅니다

입력 >> 10 60 20 40 70 80
출력 >> [60, 70, 80]
'''

'''
def up(*args):
    if args > 50:
        for i in args:
            print(args)
        return args


args = int(input("1 ~ 100 까지의 수를 입력하세요 >> ").split())
up(args)
'''
def func_list(*args):
    result = []
    numList = list(map(int, input("입력 >> ").split()))
    for i in range(0, len(numList)):
        if numList[i] > 50:
            result.append(numList[i])
        else:
            continue
    print(result)
func_list()