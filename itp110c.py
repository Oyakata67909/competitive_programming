import math
while True:
    n = int(input())
    if n == 0:break
    s = list(map(int, input().split()))
    m = sum(s) / n
    print("{0:.5f}".format(math.sqrt(sum([(x-m)**2 for x in s])/n)))
