while True:
    try:
        r=""
        a=0
        n=int(input())
        b=n-1
        for c in range(n):
            for i in range(n):
                if i == b:
                    r+="2"
                elif i == a:
                    r+="1"
                else:
                    r+="3"
            if c != n-1:
                r+="\n"
            a+=1
            b-=1
        print(r)

    except:
        break