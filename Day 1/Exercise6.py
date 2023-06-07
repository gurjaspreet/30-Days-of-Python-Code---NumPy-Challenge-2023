'''
Exercise 6

Using NumPy create any 3-dimensional array of the shape (2, 3, 4) and assign it to variable arr.


Example:

    [[[4 5 4 2]
      [6 3 5 1]
      [5 2 1 2]]
     
     [[7 2 3 1]
      [6 2 0 9]
      [0 1 9 1]]]

'''

import numpy as np

arr = np.array(
    [
        [
            [4, 5, 4, 2], 
            [6, 3, 5, 1], 
            [5, 2, 1, 2]
        ], 
        [
            [7, 2, 3, 1], 
            [6, 2, 0, 9], 
            [0, 1, 9, 1]
        ]
    ]
)
print(arr)