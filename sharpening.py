import numpy as np

sharpen = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], dtype=np.float32)

high_boost = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
], dtype=np.float32)

edge_enhance = np.array([
    [ 0,  0, 0],
    [-1,  1, 0],
    [ 0,  0, 0]
], dtype=np.float32)
