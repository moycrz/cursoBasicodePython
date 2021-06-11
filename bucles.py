# todas las potencias de 2 hasta llegar a 1000 de resultado
def run():
  LIMITE = 1000
  potencia = 0
  resultado = 2 ** potencia
  while resultado < LIMITE:
    print(f"2 elevado a {potencia} es igual a {resultado}")
    potencia += 1
    resultado = 2 ** potencia
  else:
    print(f"{potencia-1} es la ultima potencia de 2, antes de llegar a {LIMITE}")

if __name__ == '__main__':
  run()
  
# # todas las potencias de 2, de 0 hasta 1000
# def run():
#   contador = 0
#   resultado = 0
#   while contador <= 1000:
#     resultado = 2 ** contador
#     print(f"2 elevado a {contador} es igual a {resultado}")
#     contador += 1
#   else:
#     print("El bucle terminó")
    
    
# if __name__ == '__main__':
#   run()
