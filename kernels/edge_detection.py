import numpy as np

sobelX = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float32)

sobelY = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

scharrX = np.array([
    [-3, 0, 3],
    [-10, 0, 10],
    [-3, 0, 3]
], dtype=np.float32)

scharrY = np.array([
    [-3, -10, -3],
    [ 0,   0,  0],
    [ 3,  10,  3]
], dtype=np.float32)

prewittX = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)

prewittY = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
], dtype=np.float32)

robertsX = np.array([
    [1, 0],
    [0, -1]
], dtype=np.float32)

robertsY = np.array([
    [0, 1],
    [-1, 0]
], dtype=np.float32)

laplacian = np.array([
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0]
], dtype=np.float32)

laplacian8 = np.array([
    [1,  1, 1],
    [1, -8, 1],
    [1,  1, 1]
], dtype=np.float32)

kirschN = np.array([
    [5,  5,  5],
    [-3, 0, -3],
    [-3, -3, -3]
], dtype=np.float32)

kirschS = np.array([
    [-3, -3, -3],
    [-3,  0, -3],
    [5,   5,  5]
], dtype=np.float32)

kirschE = np.array([
    [-3, -3, 5],
    [-3,  0, 5],
    [-3, -3, 5]
], dtype=np.float32)

kirschW = np.array([
    [5, -3, -3],
    [5,  0, -3],
    [5, -3, -3]
], dtype=np.float32)

collection = {
    "sobelX": sobelX,
    "sobelY": sobelY,
    "scharrX": scharrX,
    "scharrY": scharrY,
    "prewittX": prewittX,
    "prewittY": prewittY,
    "robertsX": robertsX,
    "robertsY": robertsY,
    "laplacian": laplacian,
    "laplacian8": laplacian8,
    "kirschN": kirschN,
    "kirschS": kirschS,
    "kirschE": kirschE,
    "kirschW": kirschW
}
