#230509
a, b, c, d, e, f = map(int, input().split())
div = a * e - b * d
x, y = (c * e - b * f)//div, (a * f - c * d)//div
print(x, y)