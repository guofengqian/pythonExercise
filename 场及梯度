import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义函数
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# 创建一个网格
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
print("f(x,-5):",Z[0]) # f(x,-5)

# 计算梯度
grad_x = np.gradient(Z,edge_order=1,axis=0)
grad_y = np.gradient(Z,edge_order=1,axis=1)
print("gradient of f(x,-5)=", np.gradient(Z[0]))

'''
# underlying gradient caculation:
# default edge_order = 1
g = np.ones(10)
g[0] = (Z[0][1]-Z[0][0])/1 # first order forward differece.(edge_order=1)
print("g[0]:",g[0])
for i in np.arange(1,9):
  g[i] = (Z[0][i+1]-Z[0][i-1])/2 # second order central difference
  print(g[i])
g[9] = (Z[0][9]-Z[0][8])/1 # first order backward differece.(edge_order=1)
print("g:",g)
'''

# 绘制三维图
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='3d')

# 绘制函数表面
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)

# 绘制底面的等高线
contour = ax.contour(X, Y, Z, zdir='z', offset=np.min(Z), cmap='coolwarm')

# 绘制梯度投影
scale = 0.4  # 调整箭头大小
#ax.quiver(X, Y, Z, grad_x, grad_y, np.zeros_like(Z), color='blue', length=scale, normalize=True)
ax.quiver(X, Y, np.min(Z)*np.ones_like(Z), grad_x, grad_y, np.zeros_like(Z), color='black', length=scale, normalize=True)

# 设置坐标轴标签和标题
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Plot with Gradient Projection')

plt.show()
