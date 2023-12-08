import numpy as np
import matplotlib.pyplot as plt

g = 9.81  # 重力加速度
L = 1     # 单摆长度

theta = np.linspace(-3*np.pi, 3*np.pi, 20)
omega = np.linspace(-10, 10, 20)
theta, omega = np.meshgrid(theta, omega)

dtheta = omega
domega = -(g / L) * np.sin(theta)

len = np.sqrt(dtheta**2 + domega**2)
dtheta /= len
domega /= len

plt.figure(figsize=(16, 12))
plt.quiver(theta, omega, dtheta, domega, linewidth=0.1)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\omega$')
plt.title('Pendulum Direction Field\n g=9.81, L=1')
plt.show()

'''
second modify
'''