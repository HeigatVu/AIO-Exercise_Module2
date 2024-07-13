import numpy as np
# ----------------------------Question 1----------------------------
arr1 = np.arange(0, 10, 1)
arr2 = np.arange(1, 10, 1)
arr3 = np.arange(0, 9, 1)
arr4 = np.arange(1, 11, 1)
print(arr1)
print(arr2)
print(arr3)
print(arr4)

# ----------------------------Question 2----------------------------
arr4 = np.ones((3, 3)) > 0
ar5 = np.ones((3, 3), dtype=bool)
arr6 = np.full((3, 3), fill_value=True, dtyp=bool)
print(arr4)
print(arr5)
print(arr6)

# ----------------------------Question 3----------------------------
arr7 = np.arrange(0, 10)
print(arr7[arr7 % 2 == 1])

# ----------------------------Question 4----------------------------
arr8 = np.arange(0, 10)
arr[arr8 % 2 == 1] = -1
print(arr8)

# ----------------------------Question 5----------------------------
arr9 = np.arrange(10)
arr_2d = arr9.reshape(2, -1)
print(arr_2d)

# ----------------------------Question 6----------------------------
arr10 = np.arange(10).reshape(2, -1)
arr11 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr9, arr10], axis=0)
print(arr10)
print(arr11)
print("result: \n", c)

# ----------------------------Question 7----------------------------
arr11 = np.arrange(10).reshape(2, -1)
arr12 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr11, arr12], axis=1)
print("C = ", c)

# ----------------------------Question 8----------------------------
arr13 = np.array([1, 2, 3])
print(np.repeat(arr13, 3))
print(np.tile(arr13, 3))

# ----------------------------Question 9----------------------------
a = np.array([2, 6, 1, 9, 10, 3, 27])
idx = np.where((a >= 5) & (a <= 10))
print(f"result: {idx}")

# ----------------------------Question 10----------------------------


def maxx(x, y):
    if x >= y:
        return x
    else:
        return y

    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])


pair_max = np.vectorize(max, otypes=[float])
print(pair_max(a, b))

# ----------------------------Question 11----------------------------
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print(f"result: {np.where(a < b, b ,a)}")
