def zeroSumSubarray(nums):
    soma = 0
    somas_vistas = set()

    for num in nums:
        soma += num

        if soma == 0 or soma in somas_vistas:
            return True

        somas_vistas.add(soma)

    return False