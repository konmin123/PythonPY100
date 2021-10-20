EPSILON = 0.0001
N = 2
START = 1 / N


def search_eps(epsilon=EPSILON):
    sum_ = 0
    current_number = START
    while current_number > epsilon:
        sum_ = sum_ + current_number
        current_number = current_number / 2
        print("текущее число множества", current_number, "сумма", sum_)


if __name__ == "__main__":
    search_eps()

