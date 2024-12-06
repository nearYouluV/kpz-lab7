def main():
    n_rows = int(input("Введіть розмір квадратної матриці: "))
    filler = input("Введіть символ-заповнювач: ")

    arr = []  # Створення порожнього списку для матриці
    half_n_rows = (n_rows // 2) + 1  # Розрахунок половини кількості рядків
    point = half_n_rows - 1
    if n_rows % 2 == 0:
        point -= 1

    row = 0
    if n_rows % 2 == 0:
        row = n_rows - 1
        n_rows -= 1
    else:
        row = n_rows
    # Заповнення верхньої половини матриці
    for i in range(half_n_rows - 1):
        arr.append([filler] * row)
        row -= 2

    if row == -1 and n_rows % 2 == 1:
        row += 4
    else:
        row = 1
    # Заповнення нижньої половини матриці
    for i in range(half_n_rows - 1, n_rows):
        arr.append([filler] * row)
        row += 2
    # Перевірка символу-заповнювача на наявність та коректність
    if filler == "":
        print("\nСимвол-заповнювач не введено.")
    elif len(filler) != 1:
        print("\nВведено забагато символів-заповнювачів.")
    else:
        counter = 0  # Змінна для ведення лічильника розташування символів-заповнювачів
        col_arr = 0  # Змінна для ведення лічильника стовпців
        row_arr = 0  # Змінна для ведення лічильника рядків

        with open("Lab7.txt", "w") as fout: # Відкриття файлу для запису результату
            for row in arr:
                if len(row) > 0:
                    row[0] = '*'
                    row[-1] = '*'
            for i in range(n_rows):
                for j in range(n_rows):
                    if j >= counter and len(arr[row_arr]) > col_arr and j != '*':
                        print(arr[row_arr][col_arr] + " ", end="")
                        fout.write(arr[row_arr][col_arr] + " ")
                        col_arr += 1
                    else:
                        print("  ", end="")
                        fout.write("  ")

                if counter < point:
                    counter += 1
                else:
                    counter -= 1
                    point -= 1

                row_arr += 1
                col_arr = 0
                print()
                fout.write("\n")

if __name__ == "__main__":
    main()