n = int(input())
for c in range(n):
    s = str(input())
    if len(s) != 20 or s[0] != 'R' or s[1] != 'A' or s[2:21].isnumeric() == False or int(s[2:21]) == 0:
        print('INVALID DATA')
    else:
        print(int(s[2:21]))

