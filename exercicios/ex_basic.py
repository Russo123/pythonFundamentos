#  n1 = int(input('Digite o primeiro número:  ' ))
#  n2 = int(input('Digite o segundo número: '))
#  n3 = int(input('Digite o segundo número: '))
#  n4 = int(input('Digite o segundo número: '))

# nota total = (n1 + n2 + n3 + n4) /4
#  print(total)

lista = ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']

print(lista[1][2],lista[4][3],lista[6])

print(lista[1][3],lista[3],lista[4][4])

print(lista[0],lista[1][1],lista[4][0],lista[4][4])

# print 3, 13, vasco
#print 4, São Paulo, 14
# print Corinthians, 2, 10, 14

lista.append('Bragantino')
lista.insert('0,'sport')
lista.remove('vasco')
lista.pop(0)
lista02 = [1,2,5,4]
lista02.sort(reverse=True)
print(lista02)