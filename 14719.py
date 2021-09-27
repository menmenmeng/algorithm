H, W = map(int, input().split())
lands = list(map(int, input().split()))
local_first_high = lands[0]
local_first_high_index = 0
pool = []
res = 0
for i in range(1, len(lands)):
    if lands[i] < local_first_high:
        pool.append(i)
        if i == 1:
            continue
        elif (i == len(lands)-1) & (lands[i-1] < lands[i]):
            local_first_high = lands[i]
            for k in pool:
                res+=local_first_high-lands[k]
        elif i == len(lands)-2:
            if (lands[i-1] < lands[i]) & (lands[i+1] < lands[i]) :
                local_first_high = lands[i]
                for k in pool:
                    res+=local_first_high-lands[k]
                pool = []
    elif lands[i] >= local_first_high:
        if i-1 == local_first_high_index:
            local_first_high = lands[i]
            local_first_high_index = i
            continue
        else:
            for k in pool:
                res+=local_first_high-lands[k]
            pool = []
            local_first_high = lands[i]
            local_first_high_index = i
print(res)