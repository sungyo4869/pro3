import matplotlib.pyplot as plt

temp = [18.1, 20.2, 19.9, 22.3, 24.2, 26.5, 28.9, 29.2, 28.0, 26.0, 23.1, 20.0]

months = list()
for i in range(1, 13):
    months.append("%d月"%i)
plt.plot(months, temp, marker='o')

plt.show()