import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 单摆方向场
class PendulumDirField:
    def __init__(self, length=1, gravity=3, damping=0.1,
                 theta=np.zeros((16,16)),
                 omega=np.zeros((16,16)),
                 dtheta=np.zeros((16,16)),
                 domega=np.zeros((16,16)),
                 fig=object(),ax=object(),q=object()):
        # 单摆物理参数
        self.length = length # 摆长
        self.gravity = gravity # 重力加速度
        self.damping = damping # 阻力系数
        print(f"length={self.length},gravity={self.gravity},damping={self.damping}")
        
        # 创建16x16网格
        self.theta = theta #
        self.omega = omega #
        self.dtheta = dtheta
        self.domega = domega
        [self.theta, self.omega] = np.meshgrid(
                            np.linspace(-3*np.pi, 3*np.pi, 16), 
                            np.linspace(-4, 4, 16)) 
        self.dtheta = self.omega
        self.domega = -self.damping*dtheta - (self.gravity/self.length)*np.sin(self.theta)

        # 箭头群
        self.fig,self.ax = plt.subplots()
        self.q = self.ax.quiver(self.theta, self.omega,self.dtheta,self.domega)
        
    def update(self,paras):
        self.length = paras[0]
        self.gravity = paras[1]
        self.damping = paras[2]
        self.dtheta = self.omega
        self.domega = -self.damping*self.dtheta - (self.gravity/self.length)*np.sin(self.theta)
        print(f"length={self.length}")
        
        self.q.set_UVC(self.dtheta,self.domega)
        self.ax.set_title(f"length={self.length},gravity={self.gravity},damping={self.damping}")
        
# 创建画布figure和四个子图axs
p1 = PendulumDirField()
p2 = PendulumDirField()
frame1 = []
for i in range(10):
    sub_array = [1+i,9,0.1]
    frame1.append(sub_array)
    
frame2 = []
for i in range(15):
    sub_array = [1,1+i,0.1]
    frame2.append(sub_array)

ani = animation.FuncAnimation(p1.fig, p1.update,frame1,interval=500 )
ani1 = animation.FuncAnimation(p2.fig, p2.update,frame2,interval=500 )
plt.show()
