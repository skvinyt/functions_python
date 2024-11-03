def sum_of_digits(number):
    """Возвращает сумму цифр числа."""
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def max_digit(number):
    """Возвращает максимальную цифру числа."""
    max_digit = 0
    while number > 0:
        digit = number % 10
        if digit > max_digit:
            max_digit = digit
        number //= 10
    return max_digit

def min_digit(number):
    """Возвращает минимальную цифру числа."""
    min_digit = 9
    while number > 0:
        digit = number % 10
        if digit < min_digit:
            min_digit = digit
        number //= 10
    return min_digit

def main():
    while True:
        try:
            number = int(input("Введите число: "))
            action = int(input("Выберите действие (1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра, 4 - выход): "))

            if action == 1:
                result = sum_of_digits(number)
                print(f"Сумма цифр числа {number} равна {result}")
            elif action == 2:
                result = max_digit(number)
                print(f"Максимальная цифра числа {number} равна {result}")
            elif action == 3:
                result = min_digit(number)
                print(f"Минимальная цифра числа {number} равна {result}")
            elif action == 4:
                print("Программа завершена.")
                break
            else:
                print("Неверное действие. Пожалуйста, выберите 1, 2, 3 или 4.")

        except ValueError:
            print("Неверный ввод. Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()
