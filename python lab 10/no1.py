list1 = []


def name_list():
    count = 1
    while True:
        name = input(f"Enter name {count}: " )
        count += 1
        if name: 
            list1.append(name)
        else: 
            break
    return list1


x = name_list()
print(x)
        