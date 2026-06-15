def majorityElement(array):

    contadorFrequencia = 0
    maiorFrequente = None

    for num in array:
        if contadorFrequencia == 0:
            maiorFrequente = num
            contadorFrequencia = 1
        elif num == maiorFrequente:
            contadorFrequencia += 1
        else:
            contadorFrequencia -= 1

    count = 0
    for num in array:
        if num == maiorFrequente:
            count += 1

    if count > len(array) // 2:
        return maiorFrequente

    return -1  