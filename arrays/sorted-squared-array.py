def sortedSquaredArray(array):

    left = 0
    right = len(array) -1
    novoArray = [0] * len(array)
    posAtual = len(array) -1

    while left <= right:
        left_sq = array[left] ** 2
        right_sq = array[right] ** 2

        if left_sq > right_sq:
            novoArray[posAtual] = left_sq
            left += 1
        else:
            novoArray[posAtual] = right_sq
            right -= 1

        posAtual -= 1

    return novoArray
    
    return []
