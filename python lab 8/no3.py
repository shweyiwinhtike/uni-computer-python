s = input("Enter a short string: ")
l = input("Enter a long string: ")
match = False
for i in range(len(l)):
    for j in range(len(l)+1):
        if l[i:j] == s:
            match = True

print(match)