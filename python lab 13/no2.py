def list_member(key, arr):
    if not arr: return False
    if arr[0] == key:
        return True
    return list_member(key, arr[1:])

print(list_member(2, [1, 2, 3, 5]))
print(list_member(9, [1, 2, 3, 5]))
print(list_member(25, [1, 2, 3, 5]))
print(list_member(1, [1, 2, 3, 5]))