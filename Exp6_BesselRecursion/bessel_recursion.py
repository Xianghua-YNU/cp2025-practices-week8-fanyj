import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn

def bessel_up(x, lmax):
    """向上递推计算球贝塞尔函数
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
        
    Returns:
        numpy.ndarray, 从0到lmax阶的球贝塞尔函数值
    """
    # 学生在此实现向上递推算法
    # 提示:
    # 1. 初始化结果数组
    # 2. 计算j_0和j_1的初始值
    # 3. 使用递推公式计算高阶项
    j = np.zeros(lmax + 1)
    j[0] = np.sin(x) / x if x != 0 else 1
    j[1] = (np.sin(x) / x ** 2) - (np.cos(x) / x)
    for l in range(2, lmax + 1):
        j[l] = (2 * l - 1) / x * j[l - 1] - j[l - 2]
    return j


def bessel_down(x, lmax, m_start=None):
    """向下递推计算球贝塞尔函数
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
        m_start: int, 起始阶数，默认为lmax + 15
        
    Returns:
        numpy.ndarray, 从0到lmax阶的球贝塞尔函数值
    """
    # 学生在此实现向下递推算法
    # 提示:
    # 1. 设置足够高的起始阶数
    # 2. 初始化临时数组并设置初始值
    # 3. 使用递推公式向下计算
    # 4. 使用j_0(x)进行归一化
    if m_start is None:
        m_start = lmax + 15
    j = np.zeros(m_start + 1)
    j[m_start] = 1
    j[m_start - 1] = 1
    for l in range(m_start - 1, 0, -1):
        j[l - 1] = (2 * l + 1) / x * j[l] - j[l + 1]
    norm = (np.sin(x) / x) / j[0] if x != 0 else 1 / j[0]
    return j[:lmax + 1] * norm


def plot_comparison(x, lmax):
    """绘制不同方法计算结果的比较图
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
    """
    # 学生在此实现绘图功能
    # 提示:
    # 1. 计算三种方法的结果
    # 2. 绘制函数值的半对数图
    # 3. 绘制相对误差的半对数图
    # 4. 添加图例、标签和标题
    l_values = np.arange(0, lmax + 1)
    j_up = bessel_up(x, lmax)
    j_down = bessel_down(x, lmax)
    j_scipy = spherical_jn(l_values, x)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.semilogy(l_values, np.abs(j_up), label='Upward recursion')
    plt.semilogy(l_values, np.abs(j_down), label='Downward recursion')
    plt.semilogy(l_values, np.abs(j_scipy), label='Scipy')
    plt.xlabel('Order l')
    plt.ylabel('|$j_l(x)$|')
    plt.title(f'Ball Bessel Function Values at x = {x}')
    plt.legend()

    plt.subplot(1, 2, 2)
    err_up = np.abs((j_up - j_scipy) / j_scipy)
    err_down = np.abs((j_down - j_scipy) / j_scipy)
    plt.semilogy(l_values, err_up, label='Upward recursion error')
    plt.semilogy(l_values, err_down, label='Downward recursion error')
    plt.xlabel('Order l')
    plt.ylabel('Relative Error')
    plt.title(f'Relative Errors at x = {x}')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    """主函数"""
    # 设置参数
    lmax = 25
    x_values = [0.1, 1.0, 10.0]
    
    # 对每个x值进行计算和绘图
    for x in x_values:
        plot_comparison(x, lmax)
        
        # 打印特定阶数的结果
        l_check = [3, 5, 8]
        print(f"\nx = {x}:")
        print("l\tUp\t\tDown\t\tScipy")
        print("-" * 50)
        for l in l_check:
            j_up = bessel_up(x, l)[l]
            j_down = bessel_down(x, l)[l]
            j_scipy = spherical_jn(l, x)
            print(f"{l}\t{j_up:.6e}\t{j_down:.6e}\t{j_scipy:.6e}")

if __name__ == "__main__":
    main()
