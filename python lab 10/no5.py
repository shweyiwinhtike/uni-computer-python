list1_in = input("Enter list1: ")
list2_in = input("Enter list2: ")

list1 = list1_in.split(" ")
# print(list1)
list2 = list2_in.split(" ")
# print(list2)
result = []
 
while list1 and list2: 
    if list1[0] < list2[0]:
        result.append(list1.pop(0))
    elif list2[0] < list1[0]:
        result.append(list2.pop(0))

print("The merged list is: ", end="")
for i in result:
    print(i, end=" ")

