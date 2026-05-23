def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    pontUm = 0
    pontDois = 0

    menorGap = float("inf")
    par = []

    while pontUm < len(arrayOne) and pontDois < len(arrayTwo):
        num1 = arrayOne[pontUm]
        num2 = arrayTwo[pontDois]

        gap = abs(num1 - num2)

        if gap < menorGap:
            menorGap = gap
            par = [num1, num2]

        if num1 < num2:
            pontUm += 1
        elif num1 > num2:
            pontDois += 1
        else:
            return [num1, num2]  

    return par