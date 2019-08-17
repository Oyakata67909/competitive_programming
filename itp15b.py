while True: 
    h, w = map(int, input().split())
    if h == 0 and w == 0:break
    for j in range(h):
        for i in range(w):
            if j == 0 or j == h-1 or i == 0 or i == w-1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()            
