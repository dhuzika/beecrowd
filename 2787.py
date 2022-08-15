i = int(input())
j = int(input())
if i % 2 == 0 and j % 2 == 0:
    print(1)
if i % 2 == 0 and j % 2 == 1:
    print(0)
if i % 2 == 1 and j % 2 == 0:
    print(0)
if i % 2 == 1 and j % 2 == 1:
    print(1)

