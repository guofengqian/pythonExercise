import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from manim import *

# 单摆
class Pendulum:
    def __init__(self, length=1, gravity=3, damping = 0.1):
        self.length = length # 摆长
        self.gravity = gravity # 重力加速度
        self.damping = damping # 阻力系数
        [self.theta, self.omega] = np.meshgrid(
                            np.linspace(-3*np.pi, 3*np.pi, 16), 
                            np.linspace(-4, 4, 16)) #16x16的 角度，角速度
        self.dtheta = self.omega
        self.domega = -self.damping*self.dtheta - (self.gravity/self.length)*np.sin(self.theta)


# 三个方向场的向量数组 
pendulumsAry = []
for i in range(10):
    pendulumsAry.append([Pendulum(1+i,3,0.1), Pendulum(1,3+i,0.1), Pendulum(1,3,0.1+0.1*i)])

# 创建1张画布figure
fig = plt.figure(figsize=(16,10))

# 添加三个子图,及方向场
axs = []
qvr = []
for i in range(3):
    print(i)
    axs.append(fig.add_subplot(2,2,i+1))
    axs[i].set_title('{r} subplot')
    qvr.append(axs[i].quiver(pendulumsAry[0][i].theta,
                           pendulumsAry[0][i].omega,
                           pendulumsAry[0][i].dtheta,
                           pendulumsAry[0][i].domega))

# 更新三张子图的方向场
def updateF(frame):
    for i in range(3):
        axs[i].set_title(f"length={frame[i].length},gravity={frame[i].gravity},damping={frame[i].damping}")
        qvr[i].set_UVC(frame[i].dtheta, frame[i].domega) # 方向场中的向量箭头

# 动画
ani1 = animation.FuncAnimation(fig, updateF, frames=pendulumsAry,interval=500 )
plt.show()
