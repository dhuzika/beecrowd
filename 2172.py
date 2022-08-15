while True:
    a = str(input()).split()
    if a[0] == "0" and a[1] == "0":
        break
    r = int(a[0]) * int(a[1])
    print(r)
    
