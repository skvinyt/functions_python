def maximum_of_two(a, b):
    """
    Функция принимает два числа и возвращает наибольшее из них.
    """
    if a > b:
        return a
    else:
        return b

def maximum_of_three(a, b, c):
    """
    Функция принимает три числа и возвращает наибольшее из них,
    используя функцию maximum_of_two.
    """
    max_ab = maximum_of_two(a, b)
    max_abc = maximum_of_two(max_ab, c)
    return max_abc

# Пример использования функций
if __name__ == "__main__":
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    num3 = int(input("Введите третье число: "))

    max_num = maximum_of_three(num1, num2, num3)
    print(f"Максимальное число из трёх: {max_num}")
