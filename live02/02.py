# Um vendedor recebe uma comissão por suas vendas. Dependendo do valor da venda, 
# a comissão varia. A comissão é calculada da seguinte forma:
# - 5% para vendas de até R$1.000,00
# - 7.5% para vendas entre R$1.000,01 e R$5.000,00
# - 10% para vendas entre R$5.000,01 e R$10.000,00
# - 15% para vendas acima de R$10.000,00
# Escreva um programa em Python que calcule a comissão do vendedor, dado o 
# valor da venda e o nome do vendedor.

nome_vendedor = input ('Digite o nome do Vendedor: ')
valor_venda = float(input('Digite o valor da venda: '))

if valor_venda <= 1000:
    taxa = 0.05
elif valor_venda <= 5000:
    taxa = 0.075
elif valor_venda <= 10000:
    taxa = 0.10
else:
    taxa = 0.15

comissao = valor_venda * taxa

print (f'{nome_vendedor} sua comissão é de: R$ {comissao}')
