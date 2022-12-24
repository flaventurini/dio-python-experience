# Loop infinito

while True:
  numero = int(input("Informe um número: "))

  if numero == 10:
    break

  print(numero)


# Usando for, range e break (corta/para a estrutura de repetição)

for numero in range(100):
  if numero == 10:
    break

  print(numero, end=" ")


# Usando for, range e continue (pula a condição)

for numero in range(100):
  if numero % 2 == 0:
    continue

  print(numero, end=" ")

