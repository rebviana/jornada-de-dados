# #### Inteiros (`int`)
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

def resto_divisao_por_cinco():
    try:
        numero = int(input("Digite um número: "))
        resto = numero % 5
        print(f"O resto da divisão de {numero} por 5 é: {resto}")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    resto_divisao_por_cinco()

