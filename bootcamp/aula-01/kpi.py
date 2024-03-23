CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario =  float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor do bônus: "))

# 4) Calcule o valor do bônus final
bonus_final = CONSTANTE_BONUS + salario * bonus

# 5) Imprima cálculo do KPI para o usuário
print(bonus_final)

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome} , seu bônus final é de R${bonus_final:.2f}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?