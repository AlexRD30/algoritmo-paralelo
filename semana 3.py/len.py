diccionario = {
"Nombre": "Sara",
"Edad" : 27,
"Documento": 1003882
}
d1= {'Matricula': 1, 'carrera': 'ISC', 'Cuidad': 'Mao'}

diccionario.update(d1)
print(diccionario)


print(len(diccionario))

Documento = diccionario.get('Documento')
print (Documento)

print(diccionario.items())

claves = diccionario.keys()
print(claves)

valores = diccionario.values()
print (valores)

valor = diccionario.pop('Edad')
print (valor)
print(diccionario)

eliminar= diccionario.popitem()
print(eliminar)
print(diccionario)

