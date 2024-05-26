# 实验5.3 实现一种传染病模型，并给出实例演示。
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def sirs_model(y, t, beta, alpha, gamma, N):
    S, I, R = y
    dSdt = -beta * S * I / N + gamma * R
    dIdt = beta * S * I / N - alpha * I
    dRdt = alpha * I - gamma * R
    return [dSdt, dIdt, dRdt]

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义模型参数
N = 1000   # 总人口数量
alpha = 0.1 # 康复率
beta = 0.3 # 传播率
gamma = 0.05 # 再感染率

# 初始状态：假设只有一个感染者，其他人都是易感者
I0 = 1
S0 = N - I0
R0 = 0

# 时间点
t = np.linspace(0, 200, 200)

# 解微分方程组
solution = odeint(sirs_model, [S0, I0, R0], t, args=(beta, alpha, gamma, N))
S, I, R = solution.T
print(S[-1], I[-1], R[-1])
# 绘图
plt.figure(figsize=(10, 6))
plt.plot(t, S, 'b', alpha=0.7, linewidth=2, label='易感者')
plt.plot(t, I, 'r', alpha=0.7, linewidth=2, label='感染者')
plt.plot(t, R, 'g', alpha=0.7, linewidth=2, label='康复者')
plt.xlabel('时间')
plt.ylabel('人数')
plt.title('SIRS 模型演化')
plt.legend(loc='best')
plt.grid()
manager = plt.get_current_fig_manager()
manager.window.wm_title("SIRS模型演化")
plt.show()
