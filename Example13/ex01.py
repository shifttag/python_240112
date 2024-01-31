'''
pip install matplotlib
'''
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# matplotlib의 rc에 한글 폰트를 설정
font_path = "C:\Windows\Fonts\HMKMRHD.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
plt.plot([1,2,3,4], [2,8,10,16])
plt.xlabel("X축"); plt.ylabel("Y축")
plt.show()