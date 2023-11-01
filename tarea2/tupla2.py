tupla = ('manzana', 'banana', 'cereza', 'dátil', 'frambuesa')

contador = 0
for palabra in tupla:
    contador += palabra.count('a')

print(contador)