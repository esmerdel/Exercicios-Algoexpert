def firstDuplicateValue(array):
    duplicados = {}

    for valor in array:
        if valor in duplicados:
            return valor

        duplicados[valor] = True

    return -1