a = int(input())
b = int(input())
c = a % b
d = 1 % (2 ** c)
yes = (d + 1) % 2
print('NO' * d + 'YES' * yes)
