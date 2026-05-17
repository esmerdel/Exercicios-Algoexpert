def nonConstructibleChange(moedas):
    alcance = 0
    moedas.sort()

    for i in range(len(moedas)):
        if moedas[i] <= alcance + 1:
            alcance += moedas[i]
        else:
            return alcance + 1

    return alcance + 1