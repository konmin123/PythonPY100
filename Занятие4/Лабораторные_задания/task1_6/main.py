# def skolko():
#     list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
#     once_val = list_[0]
#     kol_ = 0
#     for i in list_:
#         if i > once_val:
#             kol_ += 1
#             print(kol_)
#
#
# if __name__ == "__main__":
#     skolko()

def skolko():
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(len([i for i in list_ if i > list_[0]]))


skolko()
