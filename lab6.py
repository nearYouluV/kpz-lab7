nRows = int(input("Введіть розмір квадратної матриці: "))
firstLayer = nRows // 4
secondLayer = firstLayer * 2
arr = []
for i in range(nRows):
    if i < firstLayer or i > nRows - firstLayer - 1:
        arr.append([''] * nRows)
    else:
        arr.append([''] * secondLayer)
        
filler = input("\nВведіть символ заповнювач:")
counterForColl = nRows - secondLayer
counterForRows = 0
run = True

for i in range(nRows):
    run = True
    counterForRows = 0
    for j in range(len(arr[i])):
        if len(filler) == 1:
            arr[i][j] = filler
            if i > firstLayer - 1 and i < nRows - firstLayer:
                if j == (len(arr[i]) // 2):
                    while run:
                        print("  ", end="")
                        counterForRows += 1
                        if counterForRows == counterForColl:
                            run = False
            print(arr[i][j] + " ", end="")
        elif len(filler) == 0:
            print("\nНе ввдено символ заповнювач")
            break
        else:
            print("\nЗабагато символів заповнювачів")
            break
    print("\n")
