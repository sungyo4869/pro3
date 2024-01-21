import matplotlib.pyplot as plt
import japanize_matplotlib

temp = dict()

temp[2019] = [17.4,19.2,19.5,21.9,23.8,26.1,28.8,29.1,27.9,25.6,22.6,19.3]
temp[2020] = [17.9,17.8,19.4,19.1,24.1,27.9,29.0,29.3,27.4,25.0,23.0,18.5]
temp[2021] = [16.0,17.6,20.2,21.3,25.4,26.9,28.6,28.5,28.4,25.3,20.9,17.9]
temp[2022] = [16.9,16.6,19.8,22.1,22.9,26.7,29.3,29.6,28.1,25.5,23.3,17.9]
temp[2023] = [16.7,18.4,19.5,22.2,23.9,27.0,29.4,28.5,28.7,25.5,22.0,19.0]

months = list()
for i in range(1, 13):
    months.append("%d月"%i)
    
plt.plot(months, temp[2019])
plt.plot(months, temp[2020])
plt.plot(months, temp[2021])
plt.plot(months, temp[2022])
plt.plot(months, temp[2023])

# 凡例の追加
plt.legend([2019, 2020, 2021, 2022, 2023])
# 表題の追加
plt.title("過去五年分の沖縄の月別平均気温")
# x軸、y軸のラベルを追加
plt.xlabel("月")
plt.ylabel("気温[℃]")
# x軸、y軸の最大値、最小値を設定
plt.axis(xmin=-0.5,xmax=11.5,ymin=0,ymax=35)
# グリッドラインを表示
plt.grid()

#savefig でファイルに保存
plt.savefig("temp_5year.svg")