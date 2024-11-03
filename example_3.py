def reversal(x):
    revers_x = 0
    while x > 0:
        revers_x = revers_x * 10 + x % 10
        x //= 10
    return revers_x

def main():
    N = int(input("Введите первое число: "))
    K = int(input("Введите второе число: "))

    reversed_N = reversal(N)
    reversed_K = reversal(K)

    print(f"Первое число наоборот: {reversed_N}")
    print(f"Второе число наоборот: {reversed_K}")

    sum_reversed = reversed_N + reversed_K
    print(f"Сумма: {sum_reversed}")

    final_result = reversal(sum_reversed)
    print(f"Сумма наоборот: {final_result}")

if __name__ == "__main__":
    main()
