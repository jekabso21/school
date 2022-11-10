import re

user_input = input("Enter your numbers: \n")
unique = []


def unique_num(nums):
    numbs = re.findall('\-?\d+', nums)
    for i in numbs:
        if i not in unique:
            unique.append(i)
    return unique


print(unique_num(user_input))
