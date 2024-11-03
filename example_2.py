import random

def rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(choices)
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()

    if user_choice not in choices:
        print("Неверный выбор. Попробуйте еще раз.")
        return

    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы победили!")
    else:
        print("Вы проиграли!")

def guess_the_number():
    target_number = random.randint(1, 100)
    while True:
        user_guess = int(input("Угадайте число от 1 до 100: "))
        if user_guess < target_number:
            print("Загаданное число больше.")
        elif user_guess > target_number:
            print("Загаданное число меньше.")
        else:
            print("Вы угадали!")
            break

def main_menu():
    while True:
        print("Выберите игру:")
        print("1. Камень, ножницы, бумага")
        print("2. Угадай число")
        print("3. Выход")
        choice = input("Введите номер игры: ")

        if choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            guess_the_number()
        elif choice == "3":
            print("Выход из игры.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main_menu()
