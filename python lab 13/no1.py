# def f(k):
#     if k == 0 or k % 2 == 1:
#         return 0
#     return 2 * f(k // 2) + 1

# def display_f(n):
#     for i in range(n + 1):
#         print(f"f({i}:)", end="")
#         print(f(i))
# display_f(10)

def display_f(n):
    for i in range(n + 1):
        def f(k):
            if k == 0 or k % 2 == 1:
                return 0
            return 2 * f(k // 2) + 1
        print(f"f({i}:) {f(i)}", end="\n")
display_f(10)