def missingNumbers(nums):

    resultado = []
    n = len(nums) + 2

    for num in range(1, n + 1):
        if num not in nums:
            resultado.append(num)

    return resultado