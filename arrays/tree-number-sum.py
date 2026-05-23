def threeNumberSum(array, targetSum):
    array.sort()
    arrayFinal = []
    for i in range(len(array)):
        numAtual = array[i]
        left = i + 1
        right = len(array) - 1

        while left < right:
            soma = (numAtual + array[left] + array[right])
            
            if (soma < targetSum):
                left += 1

            elif (soma > targetSum):
                right -= 1
            else:
                arrayNovo = [numAtual, array[left], array[right]]
                arrayFinal.append(arrayNovo)
                left += 1
                right -= 1
                
    return arrayFinal
