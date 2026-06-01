def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])  

    resultado = []
    intervaloAtual = intervals[0]  

    for i in range(1, len(intervals)):
        inicio, fim = intervals[i]  

        if inicio <= intervaloAtual[1]:
            intervaloAtual[1] = max(intervaloAtual[1], fim)
        else:

            resultado.append(intervaloAtual)
            intervaloAtual = intervals[i]

    resultado.append(intervaloAtual)

    return resultado