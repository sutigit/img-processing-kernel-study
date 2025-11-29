import numpy as np

ridge = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
], dtype=np.float32)

spot = np.array([
    [1, 1, 1],
    [1, -7, 1],
    [1, 1, 1]
], dtype=np.float32)

gradientX = np.array([
    [-1, 1, 0],
    [-1, 1, 0],
    [-1, 1, 0]
], dtype=np.float32)

gradientY = np.array([
    [-1, -1, -1],
    [1,  1,  1],
    [0,  0,  0]
], dtype=np.float32)
