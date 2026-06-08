def sweetAndSavory(dishes, target):


    melhorPrato = None
    target = 8

    for i in range(0, len(dishes) -1 ):
        
        for j in range(i + 1, len(dishes) - 1):
            
            soma = dishes[i] + dishes[j]
    
            if soma >= melhorPrato and soma <= target:
                melhorPrato = soma
                melhorDoce = dishes[i]
                melhorSalgado = dishes[j]
                j += 1
                
            else:
                j += 1
    
    return [melhorDoce, melhorSalgado]
