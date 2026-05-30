def arrayOfProducts(array):
    resultado = []

    for i in range(len(array)):
        produto = 1

        for j in range(len(array)):
            if j == i:
                continue
                
            produto *= array[j]

        resultado.append(produto)
    return resultado
  
