while True:
    try:
        n = int(input())
        i = 1
        j = 1
        while i % n != 0:
            i = (10 * i + 1) % n
            j += 1
        print(j)

    except:
        break