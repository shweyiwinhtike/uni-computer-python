def display_f(n):
    for i in range(n + 1):
        def f(k):
            if k == 0 or k % 2 == 1:
                return 0
            return 2 * f(k // 2) + 1

        print(f(i))