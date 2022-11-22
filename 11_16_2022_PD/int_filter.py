input = input("Enter numbers: \n")


def filter_ints(input):
    numbers = []
    for i in input:
        if i.isdigit():
            numbers.append(int(i))
    return numbers


print(filter_ints(input))
