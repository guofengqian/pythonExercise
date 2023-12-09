import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 单摆方向场
class PendulumDirField:
    def __init__(self, length=1, gravity=3, damping=0.1):
        # 单摆物理参数
        self.length = 1 # 摆长
        self.gravity = 3 # 重力加速度
        self.damping = 0.1 # 阻力系数
        print(f"length={self.length},gravity={self.gravity},damping={self.damping}")
        
        # 创建16x16网格
        [self.theta, self.omega] = np.meshgrid(
                            np.linspace(-3*np.pi, 3*np.pi, 16), 
                            np.linspace(-4, 4, 16)) 
        self.dtheta = self.omega
        self.domega = -self.damping*self.dtheta - (self.gravity/self.length)*np.sin(self.theta)

        # 创建一张画布，一个子图箭头群，一个子图按键 
        self.fig,self.axs = plt.subplots(2,2)
        self.fig.suptitle("pendulum direction field")
        self.q0 = self.axs[0,0].quiver(self.theta, self.omega,self.dtheta,self.domega) # 第一个子图
        self.q1 = self.axs[0,1].quiver(self.theta, self.omega,self.dtheta,self.domega) # 第二个子图
        self.q2 = self.axs[1,0].quiver(self.theta, self.omega,self.dtheta,self.domega) # 第三个子图
        
        
    def update(self,paras):
        self.length = paras[0]
        self.gravity = paras[1]
        self.damping = paras[2]
        self.dtheta = self.omega
        self.domega = -self.damping*self.dtheta - (self.gravity/self.length)*np.sin(self.theta)
       
        # 第一张子图数据更新
        self.q0.set_UVC(self.dtheta,self.domega)
        self.axs[0,0].set_title(f"length={self.length},gravity={self.gravity},damping={self.damping}")

        # 第二张子图数据更新

        
# 创建1张画布figure
p1 = PendulumDirField()
frame = [[],[],[]]
sub_array = [[],[],[]]
for j in range(10):
    sub_array[0] = [1+j,9,0.5]
    sub_array[1] = [1,1+j,0.5]
    sub_array[2] = [1,9,0.1*j]
    frame[0].append(sub_array[0])
    frame[1].append(sub_array[1])
    frame[2].append(sub_array[2])

'''    
p2 = PendulumDirField()
frame2 = []
for i in range(15):
    sub_array = [1,1+i,0.1]
    frame2.append(sub_array)
'''
# 调整第二个figure在第一个figure的右边

# 动画
ani1 = animation.FuncAnimation(p1.fig, p1.update,frame[0],interval=500 )
#ani2 = animation.FuncAnimation(p2.fig, p2.update,frame2,interval=500 )
plt.show()
