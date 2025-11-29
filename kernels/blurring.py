import numpy as np

box_blur = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
], dtype=np.float32)

gaussian_blur = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
], dtype=np.float32) / 16

binomial_blur = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
], dtype=np.float32) / 16

motion_blur = np.array([
    [1/3, 0,   0],
    [0,   1/3, 0],
    [0,   0,   1/3]
], dtype=np.float32)

collection = {
    "box_blur": box_blur,
    "gaussian_blur": gaussian_blur,
    "binomial_blur": binomial_blur,
    "motion_blur": motion_blur
}

