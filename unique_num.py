import random
import re

user_input = input("Enter your numbers: \n")
unique = []
rnd = random.sample(range(0, 100), 10)
print(rnd)


def unique_num(nums):
    numbs = re.findall('\-?\d+', nums)
    for i in numbs:
        if i not in unique:
            unique.append(i)
    return unique


print(unique_num(user_input))
