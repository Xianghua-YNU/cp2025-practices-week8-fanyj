import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """定义测试函数 f(x) = x(x-1)
    
    参数:
        x (float): 输入值
        
    返回:
        float: 函数计算结果
    """
    # 学生在此实现函数计算
    return x * (x - 1)

def forward_diff(f, x, delta):
    """前向差分法计算导数
    
    参数:
        f (function): 要求导的函数
        x (float): 求导点
        delta (float): 步长
        
    返回:
        float: 导数的近似值
    """
    # 学生在此实现前向差分公式
    # 提示: 使用 (f(x + delta) - f(x)) / delta
    return (f(x + delta) - f(x)) / delta

def central_diff(f, x, delta):
    """中心差分法计算导数
    
    参数:
        f (function): 要求导的函数
        x (float): 求导点
        delta (float): 步长
        
    返回:
        float: 导数的近似值
    """
    # 学生在此实现中心差分公式
    # 提示: 使用 (f(x + delta) - f(x - delta)) / (2 * delta)
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def analytical_derivative(x):
    """解析导数 f'(x) = 2x - 1
    
    参数:
        x (float): 求导点
        
    返回:
        float: 导数的精确值
    """
    # 学生在此实现解析导数公式
    return 2 * x - 1

def calculate_errors(x_point=1.0):
    """计算不同步长下的误差
    
    参数:
        x_point (float): 求导点，默认为1.0
        
    返回:
        tuple: (deltas, forward_errors, central_errors)
            deltas: 步长数组
            forward_errors: 前向差分误差数组
            central_errors: 中心差分误差数组
    """
    # 学生在此实现误差计算
    # 提示:
    # 1. 使用np.logspace生成步长序列
    # 2. 对每个步长计算前向和中心差分
    # 3. 计算相对误差 = |近似值 - 精确值| / |精确值|
    # 生成从10^-16到10^0的等比数列，共30个点
    deltas = np.logspace(-16, 0, 30)
    
    # 计算精确导数值
    exact = analytical_derivative(x_point)
    
    forward_errors = []
    central_errors = []
    
    for delta in deltas:
        # 计算前向差分误差
        fd = forward_diff(f, x_point, delta)
        forward_errors.append(np.abs(fd - exact) / np.abs(exact))
        
        # 计算中心差分误差
        cd = central_diff(f, x_point, delta)
        central_errors.append(np.abs(cd - exact) / np.abs(exact))
    
    return deltas, np.array(forward_errors), np.array(central_errors)

def plot_errors(deltas, forward_errors, central_errors):
    """绘制误差-步长关系图
    
    参数:
        deltas (array): 步长数组
        forward_errors (array): 前向差分误差数组
        central_errors (array): 中心差分误差数组
    """
    # 学生在此实现绘图功能
    # 提示:
    # 1. 使用plt.loglog绘制双对数坐标图
    # 2. 添加参考线表示理论收敛阶数
    # 3. 添加图例、标题和坐标轴标签
    plt.figure(figsize=(10, 6))
    
    # 绘制误差曲线
    plt.loglog(deltas, forward_errors, 'b-', label='前向差分', linewidth=2)
    plt.loglog(deltas, central_errors, 'r--', label='中心差分', linewidth=2)
    
    # 绘制理论收敛阶数参考线
    plt.loglog(deltas, deltas, 'k:', label='O(Δ)')
    plt.loglog(deltas, deltas**2, 'k-.', label='O(Δ²)')
    
    # 添加图例和标签
    plt.legend(fontsize=12)
    plt.xlabel('步长 Δ', fontsize=14)
    plt.ylabel('相对误差', fontsize=14)
    plt.title('数值微分误差分析', fontsize=16)
    plt.grid(True, which='both', linestyle='--')
    
    plt.tight_layout()
    plt.show()

def print_results(deltas, forward_errors, central_errors):
    """打印计算结果表格
    
    参数:
        deltas (array): 步长数组
        forward_errors (array): 前向差分误差数组
        central_errors (array): 中心差分误差数组
    """
    # 学生在此实现结果打印
    # 提示: 格式化输出步长和对应误差
    print("\n步长\t\t前向差分误差\t\t中心差分误差")
    print("--------------------------------------------------")
    for i in range(0, len(deltas), 3):  # 每隔3个点打印一次
        print(f"{deltas[i]:.2e}\t{forward_errors[i]:.4e}\t{central_errors[i]:.4e}")

def main():
    """主函数"""
    # 学生可以修改测试点
    x_point = 1.0
    
    # 计算误差
    deltas, forward_errors, central_errors = calculate_errors(x_point)
    
    # 打印结果
    print(f"函数 f(x) = x(x-1) 在 x = {x_point} 处的解析导数值: {analytical_derivative(x_point)}")
    print_results(deltas, forward_errors, central_errors)
    
    # 绘制误差图
    plot_errors(deltas, forward_errors, central_errors)
    
    # 以下分析代码可以保留或修改
    forward_best_idx = np.argmin(forward_errors)
    central_best_idx = np.argmin(central_errors)
    
    print("\n最优步长分析:")
    print(f"前向差分最优步长: {deltas[forward_best_idx]:.2e}, 相对误差: {forward_errors[forward_best_idx]:.6e}")
    print(f"中心差分最优步长: {deltas[central_best_idx]:.2e}, 相对误差: {central_errors[central_best_idx]:.6e}")
    
    print("\n收敛阶数分析:")
    mid_idx = len(deltas) // 2
    forward_slope = np.log(forward_errors[mid_idx] / forward_errors[mid_idx-2]) / np.log(deltas[mid_idx] / deltas[mid_idx-2])
    central_slope = np.log(central_errors[mid_idx] / central_errors[mid_idx-2]) / np.log(deltas[mid_idx] / deltas[mid_idx-2])
    
    print(f"前向差分收敛阶数约为: {forward_slope:.2f}")
    print(f"中心差分收敛阶数约为: {central_slope:.2f}")

if __name__ == "__main__":
    main()
