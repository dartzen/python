def find_numbers(S, P):
    for X in range(1, S):
        Y = S - X
        if X * Y == P:
            return X, Y
    return "No solution"

# Ввод данных
S = int(input("Введите сумму чисел S: "))
P = int(input("Введите произведение чисел P: "))

# Поиск чисел X и Y
X, Y = find_numbers(S, P)

# Вывод результата
if X == "No solution":
    print("Нет решения.")
else:
    print(f"Числа X и Y: {X}, {Y}")
