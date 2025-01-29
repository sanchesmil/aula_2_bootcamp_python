
print('Conversor de temperatura de Celsius para Fahrenheit')
print('------------------------')

try:
    celsius = float(input('Digite a temperatura em graus Celsius: '))

    fahrenheit = celsius * 9/5 + 32

    print(f"A temperatura {celsius} °C é equivalente a {fahrenheit} °F")
except ValueError:
    print('Digite um número válido para a temperatura.')