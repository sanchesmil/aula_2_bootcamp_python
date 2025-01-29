print('Cálculadora simples')
print('------------------------')

operacoes = ['+','-','*','/','**']
print_operacoes = str(operacoes).replace("'",'')

try: 
    n1 = int(input('Digite o primeiro valor: '))
    op = input(f"Digite a operação {print_operacoes}: ")
    n2 = int(input('Digite o segundo valor: '))

    if op not in operacoes:
        raise ValueError
    elif op == '+':
        resultado = n1 + n2
    elif op == '-':
        resultado = n1 - n2
    elif op == '*':
        resultado = n1 * n2
    elif op == '/':
        resultado = n1 / n2
    elif op == '**':
        resultado = n1 ** n2
except ValueError:
    print('Entrada de dados inválida.')
except ZeroDivisionError:
    print('Divisão por zero não permitida.')
else:
    print(f'Resultado: {resultado}')