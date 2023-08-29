#A função deve retornar o valor final do investimento após o período determinado, considerando os juros compostos. 
#O valor final deve ser arredondado para duas casas decimais.

valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final =  round(valor_inicial * (1 + taxa_juros) ** periodo, 2)

# TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

print("Valor final do investimento: R$", valor_final)