def twoNumberSum(array, targetSum):
    vistos = set()

    for num in array:
        complemento = targetSum - num

        if complemento in vistos:
            return [num, complemento]
        else:
            vistos.add(num)
    return[]
