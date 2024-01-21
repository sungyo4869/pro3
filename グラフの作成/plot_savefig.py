import matplotlib.pyplot as plt
import numpy as np

x = np.linspace (0,10,100) # 0 から10 の間に100 点作成する。
y = np.exp(-x)# y にx に対応するexp の値を代入する。

plt.plot(x,y,'o')

#savefig でファイルに保存
plt.savefig("fig.svg")