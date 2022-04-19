# Crea diccionarios de posibles contraseñas para ataques de fuerza bruta personalizada


"""
Se crea un diccionario a partir de un nombre o usuario y se le añaden posibles simbolos y numeros
"""

variables = ['!', '@', '#', '€', '&', '$', '(', ')', '=', '?', '¿', '¡', '+', '*', 'ç', '-', '_', ':', ]
dct = open('diccionario1.txt', 'w+', encoding='utf-8')
dct1 = open('diccionario2.txt', 'w+', encoding='utf-8')
dic1 = []
dic2 = []
dic3 = []
name = input("Indique el nombre del usuario: ")
for i in variables:
    for j in variables:
        for z in range(10):
            for o in range(10):
                dic1.append('{}{}{}{}{}'.format(z, o, name, j, i))
                dic1.append('{}{}{}{}{}'.format(j, i, name, z, o))
                dic1.append('{}{}{}{}{}'.format(z, o, name, o, z))
                dic1.append('{}{}{}{}{}'.format(i, j, name, j, i))
                dic1.append('{}{}{}{}{}'.format(name, o, z, j, i))
                dic1.append('{}{}{}{}{}'.format(j, i, name, j, i))
                dic1.append('{}{}{}{}{}'.format(z, o, name, z, o))
                dic1.append('{}{}{}{}{}'.format(z, o, z, o, name))

for i in variables:
    for j in variables:
        for z in range(10):
            for o in range(10):
                dic2.append('{}{}{}{}{}'.format(z, o, name.upper(), j, i))
                dic2.append('{}{}{}{}{}'.format(j, i, name.upper(), z, o))
                dic2.append('{}{}{}{}{}'.format(z, o, name.upper(), o, z))
                dic2.append('{}{}{}{}{}'.format(i, j, name.upper(), j, i))
                dic2.append('{}{}{}{}{}'.format(z, o, name.capitalize(), j, i))
                dic2.append('{}{}{}{}{}'.format(j, i, name.capitalize(), z, o))
                dic2.append('{}{}{}{}{}'.format(z, o, name.capitalize(), o, z))
                dic2.append('{}{}{}{}{}'.format(i, j, name.capitalize(), j, i))
                dic2.append('{}{}{}{}{}'.format(z, o, name.lower(), j, i))
                dic2.append('{}{}{}{}{}'.format(j, i, name.lower(), z, o))
                dic2.append('{}{}{}{}{}'.format(z, o, name.lower(), o, z))
                dic2.append('{}{}{}{}{}'.format(i, j, name.lower(), j, i))


for i in dic1:
    dct.write(i + '\n')
for i in dic2:
    dct1.write(i + '\n')
dct.close()
dct1.close()
print('Diccionario Listo!')
