input = input("Enter Full Name: \n")


def name_to_initials(name):
    initials = []
    nextone = False
    new_initials = ""
    initials += name[0].upper()

    for i in range(len(name)):
        if nextone:
            initials += name[i].upper()
            nextone = False
        if name[i] == " ":
            nextone = True

    for i in initials:
        new_initials += i + ". "
    return new_initials


print(name_to_initials(input))
