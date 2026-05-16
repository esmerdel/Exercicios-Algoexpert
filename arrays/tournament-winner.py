def tournamentWinner(competitions, results):
    pontos = {} 

    for i in range(len(competitions)):
        casa, visitante = competitions[i]

        if results[i] == 1:
            vencedor = casa
        else:
            vencedor = visitante

        if vencedor not in pontos:
            pontos[vencedor] = 0
        pontos[vencedor] += 3

    return max(pontos, key=pontos.get)