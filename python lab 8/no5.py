def LCS(s1, s2):
    longest = ""
    size = len(s1)
    for i in range(size):
        for j in range(i, size):
            substring = s1[i:j+1]
            # print(substring)
            if substring in s2 and len(substring) > len(longest):
                longest = substring
    return longest


print(LCS("ingenious", "intelligent"))
print(LCS("philosophically", "zoophilous"))
print(LCS("longevity", "individual"))
print(LCS("nft", "clever"))
print(LCS("millimeter", "meters"))
print(LCS("parabellum", "aluminium"))