while True:
    try:
        marcado = str(input()).split(":")
        horas = int(marcado[0])
        minutos = int(marcado[1])
        total_minutos = horas*60 + minutos
        if total_minutos <= 420:
            print("Atraso maximo: 0")
        else:
            print(f"Atraso maximo: {total_minutos-420}")
    except EOFError:
        break