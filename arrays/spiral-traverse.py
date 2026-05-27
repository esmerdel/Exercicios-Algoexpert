def spiralTraverse(array):
    resultado = []

    topo = 0
    baixo = len(array) - 1
    esquerda = 0
    direita = len(array[0]) - 1

    while topo <= baixo and esquerda <= direita:

        for j in range(esquerda, direita + 1):
            resultado.append(array[topo][j])

        for i in range(topo + 1, baixo + 1):
            resultado.append(array[i][direita])

        if topo < baixo:
            for j in range(direita - 1, esquerda - 1, -1):
                resultado.append(array[baixo][j])

        if esquerda < direita:
            for i in range(baixo - 1, topo, -1):
                resultado.append(array[i][esquerda])

        topo += 1
        baixo -= 1
        esquerda += 1
        direita -= 1

    return resultado