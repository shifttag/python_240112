treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d 번 찍었습니다" %treeHit)

    if treeHit == 10:
        print("나무 넘어갑니다")

# 입력받은 숫자만큼 while문 반복
num = int(input("반복횟수 입력 >>"))
i = 0;
while i < num:
    i += 1
    print(i)