def factorial(n):
    factorial_ = 1
    for i in range(2, n+1):
        factorial_ *= i
        print(i, "количество чисел", ",факториал =", factorial_)


if __name__ == "__main__":
    factorial(15)
