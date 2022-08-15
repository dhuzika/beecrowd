import math
while True:
    n = int(input())
    if n > 10:
        n == 10
    coordx = []
    coordy = []
    coordz = []
    distancias1 = []
    distancias2 = []
    distancias3 = []
    distancias4 = []
    distancias5 = []
    distancias6 = []
    distancias7 = []
    distancias8 = []
    distancias9 = []
    distancias10 = []
    distancias11 = []
    distancias12 = []
    distancias13 = []
    distancias14 = []
    distancias15 = []
    distancias16 = []
    distancias17 = []
    distancias18 = []
    distancias19 = []
    distancias20 = []
    distancias21 = []
    distancias22 = []
    distancias23 = []
    distancias24 = []
    distancias25 = []
    
    for c in range(n):
        linha = input().split()
        x = int(linha[0])
        y = int(linha[1])
        z = int(linha[2])
        coordx.append(x)
        coordy.append(y)
        coordz.append(z)

    try:
        for i in range(n):
            try:
                distancias1.append(math.sqrt((coordx[0] - coordx[i+1])**2 + (coordy[0] - coordy[i+1])**2 + (coordz[0] - coordz[i+1])**2))
            except:
                break
        if min(distancias1) <= 20:
            print("A")
        elif 20 < min(distancias1) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break


    try:
        for i in range(n):
            try:
                if i == 1:
                    continue
                distancias2.append(math.sqrt((coordx[1] - coordx[i])**2 + (coordy[1] - coordy[i])**2 + (coordz[1] - coordz[i])**2))
            except:
                break
        if min(distancias2) <= 20:
            print("A")
        elif 20 < min(distancias2) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 2:
                    continue
                distancias3.append(math.sqrt((coordx[2] - coordx[i])**2 + (coordy[2] - coordy[i])**2 + (coordz[2] - coordz[i])**2))
            except:
                break
        if min(distancias3) <= 20:
            print("A")
        elif 20 < min(distancias3) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 3:
                    continue
                distancias4.append(math.sqrt((coordx[3] - coordx[i])**2 + (coordy[3] - coordy[i])**2 + (coordz[3] - coordz[i])**2))
            except:
                break
        if min(distancias4) <= 20:
            print("A")
        elif 20 < min(distancias4) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 4:
                    continue
                distancias5.append(math.sqrt((coordx[4] - coordx[i])**2 + (coordy[4] - coordy[i])**2 + (coordz[4] - coordz[i])**2))
            except:
                break
        if min(distancias5) <= 20:
            print("A")
        elif 20 < min(distancias5) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 5:
                    continue
                distancias6.append(math.sqrt((coordx[5] - coordx[i])**2 + (coordy[5] - coordy[i])**2 + (coordz[5] - coordz[i])**2))
            except:
                break
        if min(distancias6) <= 20:
            print("A")
        elif 20 < min(distancias6) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 6:
                    continue
                distancias7.append(math.sqrt((coordx[6] - coordx[i])**2 + (coordy[6] - coordy[i])**2 + (coordz[6] - coordz[i])**2))
            except:
                break
        if min(distancias7) <= 20:
            print("A")
        elif 20 < min(distancias7) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 7:
                    continue
                distancias8.append(math.sqrt((coordx[7] - coordx[i])**2 + (coordy[7] - coordy[i])**2 + (coordz[7] - coordz[i])**2))
            except:
                break
        if min(distancias8) <= 20:
            print("A")
        elif 20 < min(distancias8) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 8:
                    continue
                distancias9.append(math.sqrt((coordx[8] - coordx[i])**2 + (coordy[8] - coordy[i])**2 + (coordz[8] - coordz[i])**2))
            except:
                break
        if min(distancias9) <= 20:
            print("A")
        elif 20 < min(distancias9) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 9:
                    continue
                distancias10.append(math.sqrt((coordx[9] - coordx[i])**2 + (coordy[9] - coordy[i])**2 + (coordz[9] - coordz[i])**2))
            except:
                break
        if min(distancias10) <= 20:
            print("A")
        elif 20 < min(distancias10) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 10:
                    continue
                distancias11.append(math.sqrt((coordx[10] - coordx[i])**2 + (coordy[10] - coordy[i])**2 + (coordz[10] - coordz[i])**2))
            except:
                break
        if min(distancias11) <= 20:
            print("A")
        elif 20 < min(distancias11) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 11:
                    continue
                distancias12.append(math.sqrt((coordx[11] - coordx[i])**2 + (coordy[11] - coordy[i])**2 + (coordz[11] - coordz[i])**2))
            except:
                break
        if min(distancias12) <= 20:
            print("A")
        elif 20 < min(distancias12) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break


    try:
        for i in range(n):
            try:
                if i == 12:
                    continue
                distancias13.append(math.sqrt((coordx[12] - coordx[i])**2 + (coordy[12] - coordy[i])**2 + (coordz[12] - coordz[i])**2))
            except:
                break
        if min(distancias13) <= 20:
            print("A")
        elif 20 < min(distancias13) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 13:
                    continue
                distancias14.append(math.sqrt((coordx[13] - coordx[i])**2 + (coordy[13] - coordy[i])**2 + (coordz[13] - coordz[i])**2))
            except:
                break
        if min(distancias14) <= 20:
            print("A")
        elif 20 < min(distancias14) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 14:
                    continue
                distancias15.append(math.sqrt((coordx[14] - coordx[i])**2 + (coordy[14] - coordy[i])**2 + (coordz[14] - coordz[i])**2))
            except:
                break
        if min(distancias15) <= 20:
            print("A")
        elif 20 < min(distancias15) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 15:
                    continue
                distancias16.append(math.sqrt((coordx[15] - coordx[i])**2 + (coordy[15] - coordy[i])**2 + (coordz[15] - coordz[i])**2))
            except:
                break
        if min(distancias16) <= 20:
            print("A")
        elif 20 < min(distancias16) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 16:
                    continue
                distancias17.append(math.sqrt((coordx[16] - coordx[i])**2 + (coordy[16] - coordy[i])**2 + (coordz[16] - coordz[i])**2))
            except:
                break
        if min(distancias17) <= 20:
            print("A")
        elif 20 < min(distancias17) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 17:
                    continue
                distancias18.append(math.sqrt((coordx[17] - coordx[i])**2 + (coordy[17] - coordy[i])**2 + (coordz[17] - coordz[i])**2))
            except:
                break
        if min(distancias18) <= 20:
            print("A")
        elif 20 < min(distancias18) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 18:
                    continue
                distancias19.append(math.sqrt((coordx[18] - coordx[i])**2 + (coordy[18] - coordy[i])**2 + (coordz[18] - coordz[i])**2))
            except:
                break
        if min(distancias19) <= 20:
            print("A")
        elif 20 < min(distancias19) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 19:
                    continue
                distancias20.append(math.sqrt((coordx[19] - coordx[i])**2 + (coordy[19] - coordy[i])**2 + (coordz[19] - coordz[i])**2))
            except:
                break
        if min(distancias20) <= 20:
            print("A")
        elif 20 < min(distancias20) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break
    
    try:
        for i in range(n):
            try:
                if i == 20:
                    continue
                distancias21.append(math.sqrt((coordx[20] - coordx[i])**2 + (coordy[20] - coordy[i])**2 + (coordz[20] - coordz[i])**2))
            except:
                break
        if min(distancias21) <= 20:
            print("A")
        elif 20 < min(distancias21) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break

    try:
        for i in range(n):
            try:
                if i == 21:
                    continue
                distancias22.append(math.sqrt((coordx[21] - coordx[i])**2 + (coordy[21] - coordy[i])**2 + (coordz[21] - coordz[i])**2))
            except:
                break
        if min(distancias22) <= 20:
            print("A")
        elif 20 < min(distancias22) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break
    
    try:
        for i in range(n):
            try:
                if i == 22:
                    continue
                distancias23.append(math.sqrt((coordx[22] - coordx[i])**2 + (coordy[22] - coordy[i])**2 + (coordz[22] - coordz[i])**2))
            except:
                break
        if min(distancias23) <= 20:
            print("A")
        elif 20 < min(distancias23) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break
    
    try:
        for i in range(n):
            try:
                if i == 23:
                    continue
                distancias24.append(math.sqrt((coordx[23] - coordx[i])**2 + (coordy[23] - coordy[i])**2 + (coordz[23] - coordz[i])**2))
            except:
                break
        if min(distancias24) <= 20:
            print("A")
        elif 20 < min(distancias24) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break
        
    try:
        for i in range(n):
            try:
                if i == 24:
                    continue
                distancias25.append(math.sqrt((coordx[24] - coordx[i])**2 + (coordy[24] - coordy[i])**2 + (coordz[24] - coordz[i])**2))
            except:
                break
        if min(distancias25) <= 20:
            print("A")
        elif 20 < min(distancias25) <= 50:
            print("M")
        else:
            print("B")
    except ValueError:
        break


    break
