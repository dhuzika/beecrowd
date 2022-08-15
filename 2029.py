while True:
    try:
        volume = float(input())
        diametro = float(input())
        raio = diametro/2
        altura = volume/(raio*raio*3.14)
        area = raio*raio*3.14
        print(f"ALTURA = {altura:.2f}")
        print(f"AREA = {area:.2f}")
    except EOFError:
        break