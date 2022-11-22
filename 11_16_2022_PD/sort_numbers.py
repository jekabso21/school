user_input = input("Enter numbers: \n")


def sorting(user_input):
    nums = []
    new_nums = ""
    for i in user_input:
        if i != " ":
            nums.append(int(i))

    for i in range(len(nums)):
        for elem in range(len(nums) - i - 1):
            if nums[elem] < nums[elem + 1]:
                nums[elem], nums[elem + 1] = nums[elem + 1], nums[elem]
    for i in nums:
        new_nums += str(i)
    return new_nums


print(sorting(user_input))
