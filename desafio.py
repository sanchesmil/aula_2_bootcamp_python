# Programa que realiza o cálculo de bônus com entrada do usuário

""" 
1 O programa deve começar solicitando ao usuário que insira seu nome.
2 Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
3 Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
4 O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
5 Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
    Exemplo de Saída:
    Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:

    Olá Luciano, o seu bônus foi de 8500
# Salve esse script python como kpi.py
# Faça uma documentação simples de como executar esse programa, utilize o README
# Salve no Git e no Github
"""

CONSTANTE_BONUS = 1000

# Solicita ao usuário que digite seu nome
try:
    nome = input('Digite seu nome: ')

    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")

    elif any(char.isdigit() for char in nome):
        raise ValueError('Seu nome não pode conter dígitos numéricos.')

    elif nome.isspace():
        raise ValueError('Seu nome não pode ser formado somente por espaços vazios.')

except ValueError as e:
    print('Entrada inválida: ', e)
    exit()

# Solicita ao usuário que digite seu salário
try:
    salario = float(input('Informe seu salário: '))

    if salario <= 0:
        raise ValueError('Salário deve ser maior que zero')

except ValueError as e:
    print('Entrada inválida para o salário.', e)
    exit()

# Solicita ao usuário que digite seu bonus
try:
    bonus = float(input('Informe o valor da porcentagem de bonus recebido (Ex. 10% = 10): '))

    if bonus <= 0:
        raise ValueError('Bônus deve ser maior que zero.')

except ValueError as e:
    print('Entrada inválida para o bônus.', e)
    exit()

# realiza o cálculo do bônus final
bonus_recebido = CONSTANTE_BONUS + salario * (1 + bonus/100)

# Imprime as informações para o usuário
print(f"{nome.capitalize()}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")






