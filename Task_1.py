num = input("Введите число: ")
sum = 0
for i in num:
    if i!=".":
        sum = sum + int(i)
print(f"Сумма цифр {num} равна: ", sum)