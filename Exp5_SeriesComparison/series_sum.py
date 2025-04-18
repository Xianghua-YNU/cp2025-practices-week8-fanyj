import numpy as np
import matplotlib.pyplot as plt

def sum_S1(N):
    """计算第一种形式的级数和：交错级数
    S_N^(1) = sum_{n=1}^{2N} (-1)^n * n/(n+1)
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 级数和
    """
    # 学生在此实现第一种级数求和
    # 提示: 使用循环从1到2N，计算(-1)^n * n/(n+1)并累加
    result = 0
    for n in range(1, 2 * N + 1):
        result += (-1) ** n * n / (n + 1)
    return result

def sum_S2(N):
    """计算第二种形式的级数和：两项求和相减
    S_N^(2) = -sum_{n=1}^N (2n-1)/(2n) + sum_{n=1}^N (2n)/(2n+1)
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 级数和
    """
    # 学生在此实现第二种级数求和
    # 提示: 
    # 1. 计算两个独立求和部分
    # 2. 将结果相减
    sum1 = 0
    sum2 = 0
    for n in range(1, N + 1):
        sum1 += (2 * n - 1) / (2 * n)
        sum2 += (2 * n) / (2 * n + 1)
    return -sum1 + sum2


def sum_S3(N):
    """计算第三种形式的级数和：直接求和
    S_N^(3) = sum_{n=1}^N 1/(2n(2n+1))
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 级数和
    """
    # 学生在此实现第三种级数求和
    # 提示: 使用循环从1到N，计算1/(2n(2n+1))并累加
    result = 0
    for n in range(1, N + 1):
        result += 1 / (2 * n * (2 * n + 1))
    return result

def calculate_relative_errors(N_values):
    """计算相对误差
    
    参数:
        N_values (list): 不同N值列表
        
    返回:
        tuple: (err1, err2)
            err1: S1相对于S3的误差列表
            err2: S2相对于S3的误差列表
    """
    # 学生在此实现误差计算
    # 提示: 对每个N值计算三种级数和，然后计算相对误差
    err1 = []
    err2 = []
    for N in N_values:
        s1 = sum_S1(N)
        s2 = sum_S2(N)
        s3 = sum_S3(N)
        err1.append(abs(s1 - s3) / s3 if s3 != 0 else 0)
        err2.append(abs(s2 - s3) / s3 if s3 != 0 else 0)
    return err1, err2

def plot_errors(N_values, err1, err2):
    """绘制误差分析图
    
    参数:
        N_values (list): 不同N值列表
        err1 (list): S1相对于S3的误差列表
        err2 (list): S2相对于S3的误差列表
    """
    # 学生在此实现绘图功能
    # 提示:
    # 1. 使用plt.loglog绘制双对数坐标图
    # 2. 添加网格、标签和图例
    plt.loglog(N_values, err1, label='S1 relative error to S3')
    plt.loglog(N_values, err2, label='S2 relative error to S3')
    plt.grid(True)
    plt.xlabel('N')
    plt.ylabel('Relative Error')
    plt.title('Relative Errors of S1 and S2 compared to S3')
    plt.legend()
    plt.show()
def print_results():
    """打印典型N值的计算结果"""
    # 学生在此实现结果打印
    # 提示:
    # 1. 选择几个典型N值(如10,100,1000,10000)
    # 2. 计算并格式化输出三种级数和及相对误差
    typical_N = [10, 100, 1000, 10000]
    for N in typical_N:
        s1 = sum_S1(N)
        s2 = sum_S2(N)
        s3 = sum_S3(N)
        err1 = abs(s1 - s3) / s3 if s3 != 0 else 0
        err2 = abs(s2 - s3) / s3 if s3 != 0 else 0
        print(f"N = {N}:")
        print(f"  S1 = {s1:.10f}")
        print(f"  S2 = {s2:.10f}")
        print(f"  S3 = {s3:.10f}")
        print(f"  Relative error of S1 to S3: {err1:.10f}")
        print(f"  Relative error of S2 to S3: {err2:.10f}")


def main():
    """主函数"""
    # 生成N值序列
    N_values = np.logspace(0, 4, 50, dtype=int)
    
    # 计算误差
    err1, err2 = calculate_relative_errors(N_values)
    
    # 打印结果
    print_results()
    
    # 绘制误差图
    plot_errors(N_values, err1, err2)

if __name__ == "__main__":
    main()
