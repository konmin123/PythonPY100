# if __name__ == "__main__":
#     matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#
#     for row in range(len(matrix)):
#         for col in range(len(matrix[0])):
#             print(matrix[row][col], end=" ")
#         print()

matrix_1 = [
    [i * j for j in range(1, 10)]
    for i in range(1, 10)
]
for row in range(len(matrix_1)):
    for col in range(len(matrix_1[row])):
        ceil = matrix_1[row][col]
        print(f"{ceil:2}", end=" ")
    print()