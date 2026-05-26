def isMonotonic(array):
    crescente = True
    decrescente = True

    for i in range(len(array) - 1):
        
        if array[i] < array[i + 1]:
            decrescente = False

        elif array[i] > array[i + 1]:
            crescente = False

    return crescente or decrescente