#array 10 positions
lista = [1,2,3,4,5,6,7,8,9,10]
print("My list complet: ", lista)

#mostre a posição 6
x=6
print("My list in position: ", x, ":", lista[x])

#modificando o valor da posição 3
lista[3]=100
print("Minha lista modificada", lista)

#adicionando um valor no array
lista.append(11)
print("Minha lista com valor adicionado", lista)

#delete o valor da posição 2
del lista[2]
print("Minha lista com valor deletado", lista)
