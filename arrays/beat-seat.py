def bestSeat(seats):
    melhorDistancia = -1
    melhorIndice = -1

    for i in range(len(seats)):

        if seats[i] == 0:
            esquerda = i - 1
            direita = i + 1
            
            contEsquerda = 0
            while esquerda >= 0 and seats[esquerda] == 0:
                esquerda -= 1
                contEsquerda += 1
                
            contDireita = 0
            while direita < len(seats) and seats[direita] == 0:
                direita += 1
                contDireita += 1

            if esquerda < 0:
                distancia = contDireita
            elif direita >= len(seats):
                distancia = contEsquerda
            else:
                distancia = min(contEsquerda, contDireita)

            if distancia > melhorDistancia:
                melhorDistancia = distancia
                melhorIndice = i

    return melhorIndice