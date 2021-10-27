# def quad_esc(n, m):
#     list_ = []
#     n = int(n)
#     m = int(m+1)
#     for number in range(n, m):
#         if n < number < m:
#             number = number * number
#             list_.append(number)
#         print(list_)
#
#
# if __name__ == "__main__":
#     quad_esc(5, 23)

def list_comprehension(n, m):
    return [i ** 2 for i in range(n, m+1)]


print(list_comprehension(2, 5))


