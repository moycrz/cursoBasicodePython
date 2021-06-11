import random

def run():
  numero_random = random.randint(1, 100)
  numero_usuario = int(input("Adivina el numero \nEscoge un numero del 1 al 100: "))
  
  
  while numero_random != numero_usuario:
    if numero_random < numero_usuario:
      print("Escoge un numero mas pequeño")
    elif numero_random > numero_usuario:
      print("Elige un numero mas grande")
    numero_usuario = int(input("Escoge otro numero: "))
  else:
    print("¡Ganaste!")


if __name__ == '__main__':
  run()
