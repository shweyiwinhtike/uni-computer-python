def get_the_difference(list1, list2):
    result = []

    for x in list1:
        if x not in list2:
            result.append(x)
    for x in list2:
        if x not in list1:
            result.append(x)
            
    return result
    

print(get_the_difference([3,1,1,1,7], [4,1,1,2,2,5]))