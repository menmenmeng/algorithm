lands = [3, 1, 2, 3, 4, 1, 1, 2]
i = 7
print(i == len(lands)-1 & lands[i-1] < lands[i])
print(i == len(lands)-1)
print(lands[i-1] < lands[i])