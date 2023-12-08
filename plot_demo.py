import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(0,3*np.pi,100)
y = np.sin(x)
plt.plot(x,y,color='blue', label='hihi')
plt.title('hi title')
plt.xlabel('x axis')
plt.ylabel('y axis')

'''
fig,ax = plt.subplots() # 创建一个画布和四个子图
ax.plot(x,y,color='red',label='hi')
ax.set_title = 'title' # 图标标题
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
fig.suptitle('title')
'''
plt.show()



'''
# 创建画布和子图，并绘制数据
fig, axs = plt.subplots(2,2)  # 创建一个画布和四个子图
x = np.linspace(0, 10, 100)  # 创建一个包含 0 到 10 的 100 个点的数组
y = np.sin(x)  # 计算正弦函数的值
axs[0][0].plot(x, y, label='Sine Curve')  # 在子图上绘制正弦函数曲线
axs[0][0].set_xlabel('X-axis')  # 设置 X 轴标签
axs[0][0].set_ylabel('Y-axis')  # 设置 Y 轴标签
axs[0][0].set_title('Sine Curve Plot')  # 设置图表标题
#ax.legend()  # 显示图例

plt.show()  # 显示图形
