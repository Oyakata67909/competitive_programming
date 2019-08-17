import math
a, b, c = map(float, input().split())
s = 0.5 * a * b * math.sin(c * math.pi / 180)
l = a + b + (a ** 2 + b ** 2 - 2 * a * b * math.cos(c * math.pi / 180)) ** 0.5
h = 2 * s / a
print("% f\n%f\n%f" % (s, l, h))
