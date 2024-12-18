import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Union, Optional


# 生成指定数量的随机数据点的坐标
def generate_random_data(num_points: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    生成随机的二维数据点坐标。

    参数:
    num_points (int): 要生成的数据点数量。

    返回:
    tuple: 包含两个numpy数组，分别表示x坐标和y坐标。
    """
    try:
        if not isinstance(num_points, int) or num_points < 0:
            raise ValueError("输入的点数参数应为非负整数类型，请检查参数类型！")
        x = np.random.randn(num_points)
        y = np.random.randn(num_points)
        return x, y
    except (TypeError, ValueError) as e:
        print(e)
        return np.array([]), np.array([])


# 计算两点之间的欧式距离
def calculate_distance(x1: Union[float, np.ndarray], y1: Union[float, np.ndarray],
                       x2: Union[float, np.ndarray], y2: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    计算二维空间中两点之间的欧式距离。

    参数:
    x1 (float or numpy.ndarray): 第一个点的x坐标。
    y1 (float or numpy.ndarray): 第一个点的y坐标。
    x2 (float or numpy.ndarray): 第二个点的x坐标。
    y2 (float or numpy.ndarray): 第二个点的y坐标。

    返回:
    float or numpy.ndarray: 两点之间的距离，如果输入是标量则返回标量距离，如果是数组则返回相应的距离数组。
    """
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# 寻找给定目标点在数据集中的最近邻点
def find_nearest_neighbor(x: np.ndarray, y: np.ndarray, target_x: float, target_y: float) -> Tuple[float, float]:
    """
    在给定的数据点集中找到距离目标点最近的点。

    参数:
    x (numpy.ndarray): 数据点的x坐标数组。
    y (numpy.ndarray): 数据点的y坐标数组。
    target_x (float): 目标点的x坐标。
    target_y (float): 目标点的y坐标。

    返回:
    tuple: 最近邻点的坐标 (nearest_x, nearest_y)，如果没有有效数据点则返回 (None, None)。
    """
    if len(x) == 0 or len(y) == 0:
        return None, None
    distances = np.sqrt((x - target_x) ** 2 + (y - target_y) ** 2)
    nearest_index = np.argmin(distances)
    return x[nearest_index], y[nearest_index]


# 寻找给定目标点在数据集中的k个最近邻点
def find_k_nearest_neighbors(x, y, target_x, target_y, k=1):
    """
    在给定的数据点集中找到距离目标点最近的k个点。

    参数:
    x (numpy.ndarray): 数据点的x坐标数组。
    y (numpy.ndarray): 数据点的y坐标数组。
    target_x (float): 目标点的x坐标。
    target_y (float): 目标点的y坐标。
    k (int): 要找到的最近邻点数量，默认为1。

    返回:
    tuple: 包含两个列表，分别是k个最近邻点的x坐标和y坐标，如果没有有效数据点则返回包含None的列表。
    """
    if len(x) == 0 or len(y) == 0:
        return [None] * k, [None] * k
    distances = np.sqrt((x - target_x) ** 2 + (y - target_y) ** 2)
    nearest_indices = np.argsort(distances)[:k]
    return x[nearest_indices], y[nearest_indices]


# 计算所有数据点到目标点的平均距离
def calculate_average_distance(x, y, target_x, target_y):
    """
    计算所有数据点到目标点的平均距离。

    参数:
    x (numpy.ndarray): 数据点的x坐标数组。
    y (numpy.ndarray): 数据点的y坐标数组。
    target_x (float): 目标点的x坐标。
    target_y (float): 目标点的y坐标。

    返回:
    float: 所有数据点到目标点的平均距离，如果没有有效数据点则返回None。
    """
    if len(x) == 0 or len(y) == 0:
        return None
    distances = np.sqrt((x - target_x) ** 2 + (y - target_y) ** 2)
    return np.mean(distances)


# 绘制数据点、目标点以及最近邻点的可视化图像
def plot_data(x: np.ndarray, y: np.ndarray, target_x: float, target_y: float,
              nearest_x: Optional[float], nearest_y: Optional[float]):
    """
    使用matplotlib绘制散点图展示数据情况。

    参数:
    x (numpy.ndarray): 数据点的x坐标数组。
    y (numpy.ndarray): 数据点的y坐标数组。
    target_x (float): 目标点的x坐标。
    target_y (float): 目标点的y坐标。
    nearest_x (float or None): 最近邻点的x坐标，若不存在则为None。
    nearest_y (float or None): 最近邻点的y坐标，若不存在则为None。
    """
    plt.scatter(x, y, c='b', label='Data Points')
    plt.scatter(target_x, target_y, c='r', label='Target Point')
    if nearest_x is not None and nearest_y is not None:
        plt.scatter(nearest_x, nearest_y, c='g', label='Nearest Neighbor')
    plt.legend()
    plt.show()


# 主函数
def main():
    num_points = 100
    x, y = generate_random_data(num_points)

    target_x = np.random.randn()
    target_y = np.random.randn()

    nearest_x, nearest_y = find_nearest_neighbor(x, y, target_x, target_y)
    plot_data(x, y, target_x, target_y, nearest_x, nearest_y)


if __name__ == "__main__":
    main()
