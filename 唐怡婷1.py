import numpy as np
import matplotlib.pyplot as plt


# 生成随机数据
def generate_random_data(num_points):
    x = np.random.randn(num_points)
    y = np.random.randn(num_points)
    return x, y


# 计算两点之间的距离
def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# 寻找最近邻点
def find_nearest_neighbor(x, y, target_x, target_y):
    min_distance = float('inf')
    nearest_x = None
    nearest_y = None
    for i in range(len(x)):
        distance = calculate_distance(target_x, target_y, x[i], y[i])
        if distance < min_distance:
            min_distance = distance
            nearest_x = x[i]
            nearest_y = y[i]
    return nearest_x, nearest_y


# 主函数
def main():
    num_points = 100
    while True:
        # 获取用户输入的目标点坐标，如果输入非数字则结束循环
        try:
            target_x = float(input("请输入目标点的x坐标（输入非数字退出）："))
            target_y = float(input("请输入目标点的y坐标（输入非数字退出）："))
        except ValueError:
            break

        nearest_x, nearest_y = find_nearest_neighbor(x, y, target_x, target_y)

        plt.scatter(x, y, c='b', label='Data Points')
        plt.scatter(target_x, target_y, c='r', label='Target Point')
        plt.scatter(nearest_x, nearest_y, c='g', label='Nearest Neighbor')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    main()
