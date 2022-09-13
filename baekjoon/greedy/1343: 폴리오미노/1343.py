pol = input()
a = pol.replace('XXXX', 'AAAA').replace('XX', 'BB')
if 'X' in a:
    print(-1)
else:
    print(a)