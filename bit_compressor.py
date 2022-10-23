import re

user_input = input("Enter your Bits: \n")
bits = []

def sepprate_each_num(bit):
    for i in bit:
        bits.append(i)
    res = compress()
    return res

#TODO fix the range bug that when you reach the last digit it detects that there are no more on the right
def compress():
    for i in range(len(bits)):
        if i <= len(bits):
            print(bits[i + 1])
            if bits[i] == bits[i + 1]:
                bits.remove(bits[i + 1])
        else:
            return bits



print(sepprate_each_num(user_input))

