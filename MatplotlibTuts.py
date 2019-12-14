from Matplotib import pylot as pit
from Matplotib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,5,7]

plt.plot(x,y,'g',lable='lineone',linewidth=5)
plt.plot(x2,y2,'c',lable='linetwo',linewidth=5)
plt.title('epic info')
plt.ylable('x axis')
plt.legend()

plt.grid(True,color='k')

plt.show()