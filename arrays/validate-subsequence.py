def validarSequencia (array, sequencia):
    ponteiroArray = 0
    ponteiroSequencia = 0
    
    while ponteiroSequencia < len(sequencia) and ponteiroArray < len(array):
        if array[ponteiroArray] == sequencia[ponteiroSequencia]:
            ponteiroArray += 1
            ponteiroSequencia += 1
        else:
            ponteiroArray += 1

    if ponteiroSequencia == len(sequencia):
        return True
    return False
    

        

    