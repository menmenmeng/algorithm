N = int(input())
numli = [i for i in map(int, input().split())]
calli = [i for i in map(int, input().split())]
def calculate(nums, cals):
    if len(nums)==2:
        if cals[0]==1:
            return [nums[0]+nums[1]]
        elif cals[1]==1:
            return [nums[0]-nums[1]]
        elif cals[2]==1:
            return [nums[0]*nums[1]]
        else:
            return [((nums[0]*(2*int(nums[0]>0)-1))//nums[1])*(2*int(nums[0]>0)-1)]
    else:
        res = []
        if cals[0]>0:
            for k in calculate(nums[:-1], [cals[0]-1]+cals[1:]):
                res.append(k+nums[-1])
        if cals[1]>0:
            for k in calculate(nums[:-1], cals[:1]+[cals[1]-1]+cals[2:]):
                res.append(k-nums[-1])
        if cals[2]>0:
            for k in calculate(nums[:-1], cals[:2]+[cals[2]-1]+cals[3:]):
                res.append(k*nums[-1])
        if cals[3]>0:
            for k in calculate(nums[:-1], cals[:3]+[cals[3]-1]):
                res.append(((k*(2*int(k>0)-1))//nums[-1])*(2*int(k>0)-1))
    return res
resli = calculate(numli, calli)
print(max(resli))
print(min(resli))