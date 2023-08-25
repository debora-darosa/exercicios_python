#teste 2: Ordenar uma lista de entradas, que inicia com um indice e depois os produtos

ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(float(input()))

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
lista_ativos = sorted(ativos)
# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.

for ativos in lista_ativos:
    print(ativos)