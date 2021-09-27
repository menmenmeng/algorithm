# strings = list(str(input()))
strings = '(()[([])()])'
o = set(['(','['])
c = set([')',']'])
s = set(['[',']'])
r = set(['(',')'])
def mul(iter):
    res = 1
    for i in iter:
        res*=i
    return res

plus = []
mply = []
done = []

for i in range(len(strings)):
    if (strings[i] in o)&(strings[i+1] in o):
        ((strings[i] in s)+2)*((strings[i] in s+2))
