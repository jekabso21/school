import re #import regex

user_input = input("Enter your numbers: \n") #Gets user input
unique = [] #saves the unique numbers


def unique_num(nums): #Starts the function
    numbs = re.findall('\-?\d+', nums) #Finds all the numbers in the string
    for i in numbs: #For each number in the string
        if i not in unique: #If the number is not in the unique list
            unique.append(i) #Add the number to the unique list
    return unique #Return the unique list


print(unique_num(user_input)) #Prints the returned list
