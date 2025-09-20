CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
# codigo padrão:
# nome = input("Digite seu nome: ")

# codigo melhorado:
while True:
    nome = input("Digite seu nome: ")

    if nome.isalpha():
        break
    else:
        print("nome inválido digite corretamente! MULA")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
# codigo original
#salario = float(input(f"{nome}, Por favor digite seu salário: "))

# melhorado
while True:
    salario = input(f"{nome}, Por favor digite seu salário: ")

    try:
        salario = float(salario)
        break
    except:
        print("Erro: digite apenas números (ex: 10 ou 10.5).")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input(f"{nome}, Agora digite o bonus: "))



# 4) Calcule o valor do bônus final
calculo = CONSTANTE_BONUS + salario * bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus

print(f"{nome}, o Bonus atual é de {CONSTANTE_BONUS}, o calculo do seu sálario com todos os bonus é de {calculo}!!")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# 1. incluir uma validação no input nome (só aceitar string) -- OK
# 2. input salario/bonus: incluir uma validação (só aceita numeros) --
# 3. input salario/bonus: não deixar digitar número negativos
# 4. input salario/bonus: limitar a quantidade de números visando não explodir o INT
