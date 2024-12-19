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


# 寻找k个最近邻点
def find_k_nearest_neighbors(x, y, target_x, target_y, k):
    distances = []
    for i in range(len(x)):
        distance = calculate_distance(target_x, target_y, x[i], y[i])
        distances.append((distance, x[i], y[i]))
    distances.sort(key=lambda x: x[0])  # 对距离及对应的坐标元组进行排序
    nearest_neighbors = distances[:k]  # 取前k个元素作为最近的k个邻点
    return [(item[1], item[2]) for item in nearest_neighbors]


# 主函数
def main():
    num_points = 100
    x, y = generate_random_data(num_points)

    target_x = np.random.randn()
    target_y = np.random.randn()

    k = 5  # 设定要查找的最近邻点个数
    nearest_neighbors = find_k_nearest_neighbors(x, y, target_x, target_y, k)

    plt.scatter(x, y, c='b', label='Data Points', alpha=0.6)  # <-- 此处修改，标注：添加alpha参数，设置散点透明度为0.6，使数据点展示更美观，便于观察整体分布情况
    plt.scatter(target_x, target_y, c='r', label='Target Point', s=80)  # <-- 此处修改，标注：添加s参数，设置目标点的大小为80，使其在图中更突出
    for neighbor in nearest_neighbors:
        plt.scatter(neighbor[0], neighbor[1], c='g', label='Nearest Neighbors', s=60)  # <-- 此处修改，标注：添加s参数，设置最近邻点的大小为60，使其在图中更醒目易区分
    plt.legend(loc='upper right')  # <-- 此处修改，标注：添加loc参数，指定图例位置为右上角，让图表布局更合理美观
    plt.title('K Nearest Neighbors Visualization')  # <-- 此处修改，标注：添加图表标题，使查看图表的人能更快理解图表所展示的内容
    plt.show()


if __name__ == "__main__":
    main()
    
