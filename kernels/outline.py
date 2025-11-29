import numpy as np

outline = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
], dtype=np.float32)

edge_detect1 = np.array([
    [1, 0, -1],
    [0, 0,  0],
    [-1, 0, 1]
], dtype=np.float32)

edge_detect2 = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
], dtype=np.float32)

collection = {
    'outline': outline,
    'edge_detect1': edge_detect1,
    'edge_detect2': edge_detect2
}