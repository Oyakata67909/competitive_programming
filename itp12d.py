W, H, x, y, r = map(int, input(). split())
if x + r <= W and 0 <= x - r and y + r <= H and 0 <= y - r:
    print("Yes")
else:
    print("No")