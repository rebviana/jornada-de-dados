# #### Números de Ponto Flutuante (`float`)
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math

def area_do_circulo():
    try:
        raio = float(input("Digite o raio do círculo: "))

        area = math.pi * raio ** 2

        print(f"A área do círculo é: {area:.2f}")
    except ValueError:
        print("Por favor, digite um raio válido.")

if __name__ == "__main__":
    area_do_circulo()
