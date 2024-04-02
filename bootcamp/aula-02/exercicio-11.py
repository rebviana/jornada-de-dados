# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

def maiusculas():
    try:
        entrada = input("Digite uma palabvra ou frase: ")
        
        resultado = entrada.upper()

        print(f"String em maiúsculas: {resultado}")
    except ValueError:
        print("Por favor, digite uma string válida.")

if __name__ == "__main__":
    maiusculas()
