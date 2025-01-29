print('Verifica se palavra é palíndromo')
print('------------------------')

palavra = input('Digite uma palavra: ')

if isinstance(palavra,str):

    palavra_formatada = palavra.replace(" ","").lower()

    if palavra_formatada == palavra_formatada[::-1]:
        print(f'A palavra "{palavra_formatada}" é um palíndromo.')
    else:
        print(f'A palavra "{palavra_formatada}" não é um palíndromo.')

else:
    print('Digite uma entrada válida.')
