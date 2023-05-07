# Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores
# são positivos e quantos são negativos. Determine, também, qual é o menor desses
# valores. Utilize o comando de repetição que desejar.


numeros = []
positivos = 0
negativos = 0

while True:
    valor = float(input("Digite um número real (ou 0 para sair): "))

    if valor == 0:
        break

    numeros.append(valor)

    if valor > 0:
        positivos += 1
    else:
        negativos += 1

menor_valor = min(numeros)

print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Menor valor: {menor_valor}")
