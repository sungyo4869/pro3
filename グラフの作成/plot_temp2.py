import matplotlib.pyplot as plt
import japanize_matplotlib

temp = dict()

temp[1999] = [18.0,17.4,20.9,21.7,23.7,27.5,28.3,28.4,28.2,26.3,22.6,18.4]
temp[2009] = [16.7,19.9,19.6,20.5,23.7,26.4,29.2,29.5,29.0,25.3,22.7,18.3]
temp[2019] = [18.1,20.0,19.9,22.3,24.2,26.5,28.9,29.2,28.0,26.0,23.1,20.0]

months = list()
for i in range(1, 13):
    months.append("%d月"%i)
    
plt.plot(months, temp[1999])
plt.plot(months, temp[2009])
plt.plot(months, temp[2019])

# 凡例の追加
plt.legend([1999, 2009, 2019])
# 表題の追加
plt.title("沖縄の月別平均気温")
# x軸、y軸のラベルを追加
plt.xlabel("月")
plt.ylabel("気温[℃]")
# x軸、y軸の最大値、最小値を設定
plt.axis(xmin=-0.5,xmax=11.5,ymin=0,ymax=35)
# グリッドラインを表示
plt.grid()

plt.show()