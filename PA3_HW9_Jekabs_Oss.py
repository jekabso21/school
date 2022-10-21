#enc variables
mytxt = input("enter text:\n") #gets the users word input
user_shift = input("enter shift:\n") #gets the users shift number that the letters number is shifted
shift_txt = [] #in this variable saves the shifted letters

#deencryption variables
new_letters = [] #saves back the letters that have been removed shift number
new_txt = [] #saves the full text

#gets For each letter from text trensfers it to number and then addes the shift, and then treansfers it to letter, and puts it in shift_text variable
for elem in mytxt:
    new_num = ord(elem) #changes the selected letter to number
    shift_num = int(new_num) + int(user_shift) #addes to that letter users shift number
    shift_txt.append(chr(shift_num)) #addes to the variable shift_text the letter


print(shift_txt) #prints the shifted letters

#decrypts the text
for elem in shift_txt:
    new_txt = ord(elem) #shifted text to numbers
    num_back = int(new_txt) - int(user_shift) #removes the shifted number from letters number
    new_letters.append(chr(num_back)) #new number converts to letter
    

print("".join(new_letters)) #prints the new letters as normal text without any not needed spaces