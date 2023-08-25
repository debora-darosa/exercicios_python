print("Hello, World!")

age, name = (27, 'Débora')
print(f"Meu nome é {name} e eu tenho {age} anos de idade")

visitant = input('Informe o seu nome: ')
print(f"Prazer, {visitant}! ")

age_visitant = int(input('Informe a sua idade: '))

if age_visitant == age:
    print("Que legal. Temos a mesma idade!")

elif age_visitant < age:
    print("Que legal. Sua idade é menor que a minha!")

else:
    print("Que legal. Sua idade é maior que a minha!")

text = str(input('Qual a sua vogal favorita? '))
vogais = 'AEIOU'
name_for = 'DEBORA'

for letra in text:
    if letra.upper() in name_for and vogais:
        print( letra, end= " existe no meu nome")
else:
    if letra.upper() not in name_for and vogais:
        print( letra, end=" não existe no meu nome")

print()

option = -1

while option != 0:
    option = int(input("Quer ver a tabuada do 5? Aperte [1] para sim, [2] para não e [0] para sair:  "))

    if option == 1:
        for numero in range(0, 51, 5):
            print(numero, end=" \n")
    elif option == 2:
        print("Tudo bem. Sem tabuada para você!")
