import numbers

list = input("enter number: \n")
lists = []


def bubble(lists):
    for i in range(len(lists)):
        for j in range(len(lists)-i-1):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
                print(lists)
    print(lists)
    return lists


for i in list:
    if i.isdigit():
        lists.append(int(i))


print(bubble(lists))
    






    
