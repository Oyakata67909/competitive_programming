n = int(input())
tmp = 0
lis = []
for i in range(1, n+1):
    if i % 3 == 0:
        lis.append(i)
    else:
        tmp = i
        while i > 0:
            if i % 10 == 3:
                lis.append(tmp)
                break
            else:
                i //= 10
print(" ", end="")
print(*lis)
