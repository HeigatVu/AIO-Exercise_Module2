import numpy as np

# Matrix and vector


def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)

    return len_of_vector


vector = np.array([-2, 4, 9, 21])
result = compute_vector_length([vector])
print(round(result, 2))


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)

    return result


v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print(round(result, 2))


x = np.array([[1, 2], [3, 4]])
k = np.array([1, 2])
print(x.dot(k))


x = np.array([[-1, 2], [3, -4]])
k = np.array([1, 2])
print(x@k)


def matrix_multi_vector(matrix, vector):
    return np.dot(matrix, vector)


m = np.array([[-1, 1, 1], [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multi_vector(m, v)
print(result)


def matrix_multi_matrix(matrix1, matrix2):
    len_of_vector = np.dot(matrix1, matrix2)
    return len_of_vector


m1 = np.array([[0, 1, 2], [2, -3, 1]])
m2 = np.array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print(result)

# Hadamard product
m1 = np.eye(3)
m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1@m2
print(result)

m1 = np.eye(2)
m1 = np.reshape(m1, (-1, 4))[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)


m1 = np.array([[1, 2], [3, 4]])
m1 = np.reshape(m1, (-1, 4), "F")[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2  # Hadamad product
print(result)


def inverse_matrix(matrix):
    matrix_t = np.linalg.inv(matrix)
    return matrix_t


matrix = np.array([[-2, 6], [8, -4]])
print(inverse_matrix(matrix))