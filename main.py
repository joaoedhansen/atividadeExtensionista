# Função para validaçãog
def obter_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("O valor precisa ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números (ex: 70.5).")

# Entrada de dados com validação
peso = obter_numero("Digite o seu peso em kg: ")
altura = obter_numero("Digite a sua altura em metros: ")

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do resultado numérico
print("\nSeu IMC é: {:.2f}".format(imc))

# Classificação de acordo com a OMS
if imc < 18.5:
    print("Classificação: Baixo peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Classificação: Obesidade grau I")
elif 35 <= imc < 39.9:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III (mórbida)")