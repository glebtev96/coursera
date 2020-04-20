hour1 = int(input())
min1 = int(input())
sec1 = int(input())
hour2 = int(input())
min2 = int(input())
sec2 = int(input())
delta = str(hour2 * 60 * 60 + min2 * 60 + sec2 -
            hour1 * 60 * 60 - min1 * 60 - sec1)
print(delta)
