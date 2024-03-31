# #### Inteiros (`int`)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

def soma():
    try:
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro: "))
        soma = numero1 + numero2
        return soma
    except ValueError:
        print("Por favor, insira apenas números inteiros.")

# Essa estrutura garante que o código dentro do bloco if __name__ == "__main__": só será executado quando o arquivo
# for executado diretamente e não quando for importado como um módulo em outro programa.
# Isso é útil para organizar e reutilizar código.
if __name__ == "__main__":
    resultado = soma()
    if resultado is not None:
        print("A soma dos dois números é: ", resultado)
