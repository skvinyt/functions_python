def calculate_danger(x):
    """
    Функция принимает глубину x и возвращает уровень опасности,
    рассчитанный по формуле D = x^3 - 3x^2 - 12x + 10.
    """
    return x**3 - 3*x**2 - 12*x + 10

def find_safe_depth(max_danger):
    """
    Функция принимает максимальное допустимое отклонение max_danger и
    возвращает глубину, при которой уровень опасности максимально близок к нулю.
    """
    left, right = 0, 4
    while right - left > max_danger:
        mid = (left + right) / 2
        danger = calculate_danger(mid)
        if danger > 0:
            right = mid
        else:
            left = mid
    return (left + right) / 2

def main():
    """
    Основная функция, которая запрашивает у пользователя ввод максимально
    допустимого уровня опасности и находит безопасную глубину.
    """
    while True:
        try:
            max_danger = float(input("Введите максимально допустимый уровень опасности: "))
            if max_danger < 0:
                print("Уровень опасности не может быть отрицательным. Попробуйте еще раз.")
            else:
                break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите числовое значение.")

    safe_depth = find_safe_depth(max_danger)
    print(f"Приблизительная глубина безопасной кладки: {safe_depth} м")

if __name__ == "__main__":
    main()
