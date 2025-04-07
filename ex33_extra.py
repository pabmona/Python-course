def listado_aumento(inicial, final, paso):
    i = inicial
    numbers = []

    while i <= final:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + paso
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    return numbers

numbers = listado_aumento(1, 6, 2)

print("The numbers: ")

for num in numbers:
    print(num)
