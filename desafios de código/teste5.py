""" O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for 
informado e o saldo da conta for atualizado. Caso um valor 
inválido seja digitado, o 
programa deve exibir uma mensagem de erro e solicitar um novo valor """

valor = float(input())

if valor > 0:
  saldo_atual = (valor)
  print(f'Deposito realizado com sucesso! \n Saldo atual: R$ {saldo_atual:.2f}')
    #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
elif valor == 0:
  print("Encerrando o programa...")
   #TODO: Imprimir a mensagem de valor inválido.
else:
  print("Valor invalido! Digite um valor maior que zero.")
  #TODO: Imprimir a mensagem de encerrar o programa.
