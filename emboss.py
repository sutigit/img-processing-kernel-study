import numpy as np

emboss1 = np.array([
    [-2, -1, 0],
    [-1,  1, 1],
    [ 0,  1, 2]
], dtype=np.float32)

emboss2 = np.array([
    [-1, -1, 0],
    [-1,  1, 1],
    [ 0,  1, 1]
], dtype=np.float32)

emboss3 = np.array([
    [0,  1, 1],
    [-1, 1, 1],
    [-1, -1, 0]
], dtype=np.float32)
