import re
import random

student_ids = input("Enter student IDs: \n")
sent_work = {}
recived_work = {}
students = []
same = True

#from input set get names or numbers and then in new variable set the each input = 0
def set_each_student():
    Values = re.findall('\-?\d+', student_ids)
    for elem in Values:
        sent_work[elem] = 0
        recived_work[elem] = False
        students.append(elem)

    print(students)
    print(sent_work)
    print(recived_work)
    send_rnd()


def send_rnd():
    for elem in students:
        print(elem)
        print(recived_work[elem])
        if recived_work[elem] == False:
            rnd_files = random.sample(range(0, len(students)), 3)
            #check if in rnd_files is the same number as elem
            if elem in rnd_files:
                check_if_not_same_id(rnd_files, elem)
                if rnd_files[0] == rnd_files[1] or rnd_files[0] == rnd_files[2] or rnd_files[1] == rnd_files[2]:
                    check_if_not_same(rnd_files)

        print(rnd_files)

def check_if_not_same(rnd_files):
    while same == True:
        if rnd_files[0] == rnd_files[1]:
            rnd_files[1] = random.randint(0, len(students))
        elif rnd_files[0] == rnd_files[2]:
            rnd_files[2] = random.randint(0, len(students))
        elif rnd_files[1] == rnd_files[2]:
            rnd_files[2] = random.randint(0, len(students))
        else:
            same = False
            return rnd_files

def check_if_not_same_id(rnd_files, std_id):
    while samestd == True:
        for elem in rnd_files:
            if elem == std_id:
                rnd_files.remove(elem)
                rnd_files.append(random.randint(0, len(students)))
    else:
        samestd = False
        return rnd_files
        
                    
                    
    
print(set_each_student())

