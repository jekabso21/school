input = input("Enter numbers: \n")


def Even_or_Odd(input):
    numbers = []
    for i in input:
        numbers.append(int(i))
    for i in numbers:
        num = i % int(2)
        if num == 0:
            print(i, "is even")
        else:
            print(i, "is odd")


Even_or_Odd(input)
