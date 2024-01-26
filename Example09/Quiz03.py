'''
# 현재 리스트의 최대값을 구하세요!!
# 단) max() 함수 사용하지 마세요!!
# 최소값 min() 함수 사용하지 말고 최소값 구하시요
'''
arrayList = [20,10,5,3,100]
ma = arrayList[0]
for i in range(len(arrayList)):
    if(arrayList[i] > ma):
        ma = arrayList[i]
print(ma)

mi = arrayList[0]
for i in range(len(arrayList)):
    if(mi > arrayList[i]):
        mi = arrayList[i]
print(mi)