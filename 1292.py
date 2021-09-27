a, b = map(int, input().split())
import math
an, bn = int(math.ceil((-1+math.sqrt(1+8*a))/2)), int(math.ceil((-1+math.sqrt(1+8*b))/2))
# print(an, bn)
# print(((an-1)*an)/2, (an*(an+1))/2, ((bn-1)*bn)/2, (bn*(bn+1))/2)
res = int(((an*(an+1))/2-a+1)*an) + int((b-((bn-1)*bn)/2)*bn)
for i in range(an+1, bn):
    res+=i**2
print(int(res))

# 정답 코드
li = []
for i in range(1, 45):
    li += [i]*i
print(sum(li[a-1:b]))
print(len(li))