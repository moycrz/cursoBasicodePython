def conversor(moneda, valor_dolar):
  pesos = float(input(f"¿Cuantos pesos de {moneda.capitalize()} tienes?: "))
  dolar = round(valor_dolar * pesos, 2)
  if dolar == 1:
    print(f"Tienes ${dolar} dolar")
  else:
    print(f"Tienes ${dolar} dolares")

print("Bienvenido, este es un conversor de monedas 🤑, \n Aqui podras convertir pesos mexicanos, argentinos y colombianos \n")
moneda = input("¿Con que moneda vas a trabajar? \n Argentina, Colombia o Mexico: ").lower()

if moneda == "argentina":
  conversor('Argentina', 0.011)
elif moneda == "colombia":
  conversor('Colombia', 0.00027)
elif moneda == "mexico":
  conversor('Mexico', 0.050)
else:
  print(f"El valor '{moneda}' esta fuera de rango")
  
  
  def conversor(tipo_peso, valor_dolar):
    pesos= float(input("¿Cuántos pesos " + tipo_peso + " tienes?: "))
    dolares = round(pesos / valor_dolar, 2)
    print(f"Tienes ${dolares} dolares")