# 1- Solicite ao usuário que digite o seu nome:
nome_user = input("Digite o seu nome: ")

# Solkicita ao usuário que digite o valor do salário
# Converta a entrada para float
salario_user = float(input("Digite seu salário: "))

# 3) Solicite ao usuário o valor do Bonus
# converte a entrada para float
bonus_user = float(input("Digite seu bonus: "))

# 4) Calcule o bonus final:
CONSTANTE_BONUS = 1000
valor_bonus = CONSTANTE_BONUS + salario_user * bonus_user

# 5) Imprima o calculo do KPI para o usuário
print(f"O usuário {nome_user} possui o bonus de {valor_bonus}")

