# def only_even(n):
#     list_1 = []
#     for numbers_even in range(n):
#         if numbers_even % 2 == 0:
#             list_1.append(numbers_even)
#     print(list_1)
#     print(len(list_1))
#
#
#
# if __name__ == "__main__":
#     only_even(10)

def only_even(n, m):
    return [i for i in range(n, m+1) if i % 2 == 0]


print(len(only_even(3, 26)))