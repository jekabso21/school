import re
import random

student_ids = input("Enter student IDs: \n")
max_sent = 3
sent_work = {}
recived_work = {}
students = []
max_limit = 0


def set_each_student():
    Values = re.findall('\-?\d+', student_ids)
    for elem in Values:
        sent_work[elem] = 0
        recived_work[elem] = False
        students.append(elem)

    send_rnd()


def send_rnd():
    for elem in students:
        #print(elem)
        #print(recived_work[elem])
        if recived_work[elem] == False:
            rnd_files = random.sample(range(0, len(students)), int(max_sent))
            if elem in rnd_files:
                check_if_not_same_id(rnd_files, elem)
            if rnd_files[0] == rnd_files[1] or rnd_files[0] == rnd_files[2] or rnd_files[1] == rnd_files[2]:
                check_if_not_same(rnd_files)
            for i in rnd_files:
                #print(sent_work[students[i]] <= max_sent)
                if sent_work[students[i]] <= max_sent:
                    check_if_has_more_then(rnd_files)
                sent_work[students[i]] += 1
                recived_work[elem] = True

    print(recived_work)
    print(sent_work)

def check_if_not_same(rnd_files):
    same = True
    while same == True:
        if rnd_files[0] == rnd_files[1]:
            rnd_files[1] = random.randint(0, len(students))
        elif rnd_files[0] == rnd_files[2]:
            rnd_files[2] = random.randint(0, len(students))
        elif rnd_files[1] == rnd_files[2]:
            rnd_files[2] = random.randint(0, len(students))
        else:
            same = False

def check_if_not_same_id(rnd_files, std_id):
    samestd = True
    while samestd == True:
        for elem in rnd_files:
            if elem == std_id:
                rnd_files.remove(elem)
                rnd_files.append(random.randint(0, len(students)))
    else:
        samestd = False

        
def check_if_has_more_then(rnd_files):
    print("check_if_has_more_then")
    max_limit = True
    while max_limit == True:
        for elem in students:
            if sent_work[elem] > max_sent:
                rnd_files[2] = random.randint(0, len(students))
                print(rnd_files[2])
            else:
                max_limit = False
    
print(set_each_student())

