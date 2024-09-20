def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    def normalizar_nome(nome):
      return ' '.join(word.capitalize() for word in nome.split())
    
    visuais = lista_visuais.split(", ")
    
    conjunto_visuais = {normalizar_nome(visual.strip().lower()) for visual in visuais}
    # TODO: Converta o conjunto de volta para uma lista ordenada:
    lista_final = sorted(conjunto_visuais)
    
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)