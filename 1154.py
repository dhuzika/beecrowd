media = 0
i = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    i += 1
    media += idade

print(f"{(media/i):.2f}")