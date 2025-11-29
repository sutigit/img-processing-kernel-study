import numpy as np

line_h = np.array([
    [-1, -1, -1],
    [ 2,  2,  2],
    [-1, -1, -1]
], dtype=np.float32)

line_v = np.array([
    [-1,  2, -1],
    [-1,  2, -1],
    [-1,  2, -1]
], dtype=np.float32)

line_45 = np.array([
    [-1, -1,  2],
    [-1,  2, -1],
    [ 2, -1, -1]
], dtype=np.float32)

line_135 = np.array([
    [ 2, -1, -1],
    [-1, 2, -1],
    [-1, -1, 2]
], dtype=np.float32)

collection = {
    "line_h": line_h,
    "line_v": line_v,
    "line_45": line_45,
    "line_135": line_135
}
