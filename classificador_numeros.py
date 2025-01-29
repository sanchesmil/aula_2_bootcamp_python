print('Classificador de números: positivo, negativo, par, impar')
print('------------------------')

try:
    num = int(input('Digite um número: '))

    if num >= 0: 
        print(f'O número {num} é positivo. \n')
    elif num < 0:
        print(f'O número {num} é negativo. \n')
    if num % 2 == 0:
        print(f'O número {num} é par. \n')
    else: 
        print(f'O número {num} é impar. \n')
except ValueError:
    print('Entrada inválida.')