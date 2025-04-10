puntaje = 53

if puntaje > 100 or puntaje < 0:
    print("puntaje no valido")
else:
  if puntaje >= 95 and puntaje <= 100:
    print("aprobado con honores")
  elif puntaje >= 50 and puntaje < 95:
    print("aprobado") 
  else: 
    print("reprobado")

print("fin de condicional if") 