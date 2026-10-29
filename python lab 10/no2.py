def remove_the_thirds(list1):
    del list1[2::3]
    print(list1)

list1 = [0,1,2,3,4,5,6,7,8,9]
remove_the_thirds(list1)

# list1 = [0, 1, 3, 4, 6, 7, 9]
# remove_the_thirds(list1)

# list1 = [0, 1, 4, 6, 9]
# remove_the_thirds(list1)

# list1 = [0, 1, 6, 9]
# remove_the_thirds(list1)

# list1 = [0, 1, 9]
# remove_the_thirds(list1)

# list1 = [0, 1]
# remove_the_thirds(list1)