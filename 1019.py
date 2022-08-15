ts = int(input())

h = ts//3600

ts = ts - h*3600

min = ts//60

ts = ts - min * 60

s = ts

print(f"{h}:{min}:{s}")
