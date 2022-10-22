import re

user_input = input("Enter your Bits: \n")
bits = []

def sepprate_each_num(bit):
    for i in bit:
        bits.append(i)
    res = compress()
    return res

def compress():
    for i in range(len(bits)):
        if i <= len(bits):
            print(bits[i + 1])
            if bits[i] == bits[i + 1]:
                bits.remove(bits[i + 1])
        else:
            return bits



print(sepprate_each_num(user_input))

# str1 = "Geeks123for127geeks"
#
# # printing initial ini_string
# print("initial string : ", str1)
#
# # using loop and in
# # to remove numeric digits from string
# num = "1234567890"
# str2 = ""
# for i in str1:
#     if i not in num:
#         str2 += i
#
# # printing result
# print("final string : ", str2)
