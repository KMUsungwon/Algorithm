from math import gcd
n, m = map(int, input().split(":"))
a = gcd(n, m)
print(str(n//a) + ":" + str(m//a))