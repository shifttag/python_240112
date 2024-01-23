'''
다음 리스트에 저장되어 있는 값들의 평균을 구하세요
'''
nums = [10,20,30,40,50]
sum = nums[0] + nums[1] + nums[2] + nums[3] + nums[4]
ave = sum / len(nums)
print(int(ave))

for i in range(5) :
    sum = nums[i]

    aver = sum / 5
    print(int(aver))