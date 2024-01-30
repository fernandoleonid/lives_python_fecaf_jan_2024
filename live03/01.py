# Crie um programa que solicite ao usuário que 
# digite um número inteiro positivo maior que zero.
# Em seguida, exiba todos os números pares 
# de 0 até o número informado pelo usuário.

numero = int(input('Digite um número: '))

contador = 0
while contador <= numero:
    if contador % 2 == 0:
        print (contador)
    contador += 1



