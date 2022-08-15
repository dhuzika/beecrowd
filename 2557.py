while True:
  try:
    eq = str(input())
    R=""
    L=""
    J=""
    a=False
    for c in range(len(eq)):
      if eq[c] == "+":
        break
      else:
        R+=eq[c]
    if "R" not in eq:
      R=int(R)
    for c in range(len(eq)):
      if eq[c] == "=":
        break
      if eq[c] == "+":
        a=True
      else:
        if a == True:
          if eq[c].isnumeric():
            L+=eq[c]
        else:
          continue
    if "L" not in eq:
      L = int(L)
    
    eq_reverso = eq[::-1]
    for c in range(len(eq_reverso)):
      if eq_reverso[c] == "=":
        break
      else:
        J+=eq_reverso[c]
    J=J[::-1]
    if "J" not in eq:
      J=int(J)
    if "J" in eq:
      print(L+R)
    elif "L" in eq:
      print(J-R)
    elif "R" in eq:
      print(J-L)
   
  except:
    break





