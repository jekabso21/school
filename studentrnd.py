#TODO Jāpabeidz vēl viens cikls, kurš pārbauda vai ir sasniegts maksimālais skaitlis, kādu var nosūtīt vienam studentam
import re
import random

student_ids = input("Enter student IDs: \n")
max_sent = 3
sent_work = {}
recived_work = {}
max_limit = 0
r_files = []

def set_each_student():
    ids = re.findall('\-?\d+', student_ids)
    students = []
    for elem in ids:
        sent_work[elem] = 0
        recived_work[elem] = False
        students.append(elem)
    print("I got this: ", students)
    send_rnd(students)



def send_rnd(students):
    for elem in students:
        files = []
        #print(recived_work[elem])
        if recived_work[elem] == False:
            files = random.sample(range(0, len(students)), int(max_sent))
            if elem in files:
                files = check_if_not_same_id(files, elem, students)
                print(files)
            if files[0] == files[1] or files[0] == files[2] or files[1] == files[2]:
                files = check_if_not_same(files, students)
            for i in files:
                if sent_work[students[i]] <= max_sent:
                    files = check_if_has_more_then(files, students)
                sent_work[students[i]] += 1
                recived_work[elem] = True
                print("Student: ", students[i], " got file from: ", elem, " files: ", files)
        #return r_files, recived_work

def check_if_not_same(rnd_files, student):
    same = True
    while same == True:
        if rnd_files[0] == rnd_files[1]:
            rnd_files[1] = random.randint(0, len(student))
        elif rnd_files[0] == rnd_files[2]:
            rnd_files[2] = random.randint(0, len(student))
        elif rnd_files[1] == rnd_files[2]:
            rnd_files[2] = random.randint(0, len(student))
        else:
            return rnd_files

def check_if_not_same_id(rnd_files, std_id, stud):
    samestd = True
    while samestd == True:
        for elem in rnd_files:
            if elem == std_id:
                rnd_files.remove(elem)
                rnd_files.append(random.randint(0, len(stud)))
    else:
        return rnd_files

        
def check_if_has_more_then(rnd, student):
    max_limit = True
    while max_limit == True:
        for elem in student:
            if sent_work[elem] > max_sent:
                rnd[2] = random.randint(0, len(student))
                print(rnd[2])
            else:
                return rnd
    
print(set_each_student())

