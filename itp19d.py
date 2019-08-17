t = list(input())
n = int(input())
for i in range(n):
    cmd, a, b, *c = input().split()
    a = int(a)
    b = int(b)
    if cmd == "print":
        print(*t[a:b+1], sep='')
    elif cmd == "reverse":
        t[a:b+1] = reversed(t[a:b+1])
    else:
        t[a:b+1] = c[0]
