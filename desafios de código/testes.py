#teste 1: criar um input no saldo inicial, deposito e retirada. Realizar o cálculo desses valores e retornar o valor final na conta.

saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

saldo_atual = (saldo_atual + valor_deposito) - valor_retirada

print(f"Saldo atualizado é: {saldo_atual} ")

#teste 2: 