def bublesort(lista):
    tam = int(len(lista))
    for i in lista:
        troca = False
        for j in range(tam -1):
            if lista[j]> lista[j+1]:
                [lista[j], lista[j+1]] = [lista[j+1], lista[j]]
                troca= True
                j = j+1
        if troca == False:    
            break
    return lista


lista = [32, 2, 88, 11, 19, 66, 5, 25, 43, 54, 77]
arrumei = bublesort(lista)
print(arrumei)