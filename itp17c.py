r, c = map(int, input().split())
listA = []
for i in range(r):
	listA.append(list(map(int, input().split())))
	listA[i].append(sum(listA[i]))
temp = []
for  i in range(c+1):
    number = 0
    for j in range(r):
        number += listA[j][i]
    temp.append(number)
# s = 0
# for i in range(r):
#     for j in range(c):
#         s += listA[i][j]
# temp.append(s)
listA.append(temp)

for line in listA:
    print(*line)