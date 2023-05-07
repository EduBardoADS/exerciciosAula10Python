# Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a
# altura de cada pessoa, calcule e mostre a altura média das mulheres e dos homens
# separadamente. Utilize o comando de repetição que desejar

altura_mulheres = 0
qtd_mulheres = 0
altura_homens = 0
qtd_homens = 0

while True:
    sexo = input("Digite o sexo da pessoa (M/F) ou digite 0 para sair: ")

    if sexo == "0":
        break

    altura = float(input("Digite a altura da pessoa (em metros): "))

    if sexo == "F":
        altura_mulheres += altura
        qtd_mulheres += 1
    elif sexo == "M":
        altura_homens += altura
        qtd_homens += 1
    else:
        print("Sexo inválido. Digite apenas M ou F.")

if qtd_mulheres > 0:
    media_altura_mulheres = altura_mulheres / qtd_mulheres
    print(f"Média de altura das mulheres: {media_altura_mulheres:.2f} m")
else:
    print("Não há mulheres no grupo.")

if qtd_homens > 0:
    media_altura_homens = altura_homens / qtd_homens
    print(f"Média de altura dos homens: {media_altura_homens:.2f} m")
else:
    print("Não há homens no grupo.")
