def quick_sort(lista):
    if len(lista) <= 1:  
        return lista
    
    pivô = lista[0]  #definir meu pivô como o primeiro número (no caso 5)
    esquerda = [x for x in lista[1:] if x <= pivô]  #Dizer que a partir do segundo número, colocar todos os números menores ou iguais ao pivô para a esquerda
    direita = [x for x in lista[1:] if x > pivô] #Dizer que a partir do segundo número, colocar todos os números maiores que o pivô para a direita.

    return quick_sort(esquerda) + [pivô] + quick_sort(direita) #juntar todos os números 


lista = [5, 2, 9, 1, 5, 6] #definir os números da minha lista
lista_organizada = quick_sort(lista) #chamar a minha lista
print(lista_organizada)
