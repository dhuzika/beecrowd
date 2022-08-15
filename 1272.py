n = int(input())
for c in range(n):
    a=False
    r=""
    s = str(input())
    for c in range(len(s)):
        if s[c] != "." and s[c] != " " and a == False:
            r+=s[c]
            a = True
        if s[c] == "." or s[c] == " ":
            a = False
    print(r)