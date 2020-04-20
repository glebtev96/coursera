n = int(input())
a = str(n // 1000)
b = str(n % 1000 // 100)
print(int(b + a) - n % 100 + 1)
