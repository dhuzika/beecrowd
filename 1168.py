n = int(input())
d = {"1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6, "0":6}
for c in range(n):
    s = str(input())
    soma=0
    for i in range(len(s)):
        soma += d[s[i]]
    print(f"{soma} leds")
