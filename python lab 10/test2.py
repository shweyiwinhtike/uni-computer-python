def merge(list1, list2):
    result = []
    
    while list1 and list2: 
        if list2[0] < list1[0]:
            result.append(list2.pop(0))
            print(result)
        else:
            result.append(list1.pop(0))
            print(result)

    
        

    result += list1
    result += list2

    return result

list1 = [1, 5, 16, 61, 111]
list2 = [2, 4, 5, 6]
print(merge(list1, list2))

