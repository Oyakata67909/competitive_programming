while True:
    c = input()
    if c == "-":break
    m = int(input())
    for i in range(m):
        h = int(input())
        c = c[h:] + c[:h]
    print(c)

