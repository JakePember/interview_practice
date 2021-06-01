# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# Utility Function

def print_results(matrix):
    for row in matrix:
        print(row)


def rotate_matrix_clockwise(matrix):
    result = []
    rotated = [list(reversed(col)) for col in zip(*matrix)]
    for row in rotated:
        result.append(row)

    return result


def rotate_matrix_counter_clockwise(matrix):
    result = []
    rotated = [list(reversed(col)) for col in zip(*matrix)]

    for row in reversed(rotated):
        result.append(list(reversed(row)))

    return result


user_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(f"Original Matrix")
print_results(user_matrix)

print(f"Rotated Matrix:")
# print_results(rotate_matrix_clockwise(user_matrix))
print_results(rotate_matrix_counter_clockwise(user_matrix))
