n = int(input())
x = 0
y = 0
for i in range(n):
    t, h = input().split()
    if t < h:
        y += 3
    elif t == h:
        x += 1
        y += 1
    else:
        x += 3
print(x, y)
    
    
