inp = input("Enter numbers: \n")


def get_sum(input):
    numbers = []
    new_nums = 0
    for i in input:
        if i != " ":
            numbers.append(int(i))
    for elem in numbers:
        new_nums = new_nums + int(elem)
    return new_nums


print(get_sum(inp))
