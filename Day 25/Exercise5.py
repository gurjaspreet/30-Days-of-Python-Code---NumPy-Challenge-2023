import numpy as np


arr = np.array(
    [
        [5, 8, 16],
        [4, 1, 8],
        [-4, 4, -11],
    ]
)

inv = np.linalg.inv(arr)
print(inv)