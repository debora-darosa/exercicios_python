# realizar saques de uma conta, onde o usuario coloca o valor de saldo e o valor de saque
# Entrada de dados
#Regras do saque:
""" - Cada cliente digitará o valor do seu saldoTotal de sua conta bancária e o valorSaque.
- Um saque só pode ser realizado se o saldoDisponível na conta for igual ou superior ao valor solicitado.
- Se o saldo for suficiente, o valor solicitado deve ser subtraído do saldo disponível, indicando que o saque foi realizado.
- Se o saldo for insuficiente, o saque não deve ser realizado e uma mensagem adequada deve ser exibida.
 """
saldo_total = int(input())
valor_saque = int(input())

# Todo: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if saldo_total >= valor_saque:
    saldo_disponivel = saldo_total - valor_saque
    print(f"Saque realizado com sucesso! Novo saldo: {saldo_disponivel}")
else:
    print("Saldo insuficiente. Saque nao realizado!")