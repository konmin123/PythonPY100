if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }

    sum_ = 0# TODO посчитать через ключи
    for fruit in cart:
        sum_ += cart[fruit]
        print(sum_)  # получаем значение по ключу

    # TODO посчитать через метод values


    print(sum(cart.values()))
    print(cart.items())