import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[1,1,1,1],'-', color='b', linewidth = '12.4')   # 실선 그래프
plt.plot([1,2,3,4],[2,2,2,2],':', color='#BDBDBD')   # 점선 그래프
plt.plot([1,2,3,4],[3,3,3,3],'-.', color='red')
plt.plot([1,2,3,4],[4,4,4,4],'--', color='g')
plt.show()