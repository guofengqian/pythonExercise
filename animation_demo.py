import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 创建画布和子图
fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], 'o-', lw=2)

# 设置初始条件
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# 初始化绘图元素
def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    fig.suptitle("animation of sin function")
    return line,

# 更新函数用于绘制动画
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    line.set_data(xdata, ydata)
    return line,

# 创建动画
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                              init_func=init, blit=True)

plt.show()
