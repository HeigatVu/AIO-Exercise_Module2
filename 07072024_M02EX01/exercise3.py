import pandas as pd
import numpy as np


df = pd.read_csv('advertising.csv')
df.head()
data = df.to_numpy()

# ----------------------------Question 15----------------------------
print(
    f"max: {np.max(data[ : , 3], axis = 0)} - index: {np.argmax(data[ : , 3], axis = 0)}")

# ----------------------------Question 16----------------------------
print(np.average(data[:, 0], axis=0))

# ----------------------------Question 17----------------------------
print(np.count_nonzero(data[:, 3] >= 20))

# ----------------------------Question 18----------------------------
ind = np.where(data[:, 3] >= 15)
print(ind)
print(np.average(data[ind, 1]))

# ----------------------------Question 19----------------------------
average_newspaper = np.mean(data[:, 2])
print(average_newspaper)

print(data[:, 2].shape)

newspaper_greater_than_avg = np.where(
    data[:, 2] > average_newspaper, data[:, 3], 0)

print(newspaper_greater_than_avg)

print(np.sum(newspaper_greater_than_avg))

# ----------------------------Question 20----------------------------
A = np.mean(data[:, 3])
scores = np.array([])

for i in range(0, data[:, 3].shape[0]):
    if data[i, 3] > A:
        scores = np.append(scores, "Good")
    elif data[i, 3] < A:
        scores = np.append(scores, "Bad")
    else:
        scores = np.append(scores, "Average")

print(scores[7:10])

# ----------------------------Question 21----------------------------
average_sales = np.mean(data[:, 3])
idx_nearest_avg_sales = np.argmin(np.abs(data[:, 3] - average_sales))
A = data[idx_nearest_avg_sales, 3]
print(average_sales)
print(A)

for i in range(0, data[:, 3].shape[0]):
    if data[i, 3] > A:
        scores = np.append(scores, "Good")
    elif data[i, 3] < A:
        scores = np.append(scores, "Bad")
    else:
        scores = np.append(scores, "Average")

print(scores[7:10])
