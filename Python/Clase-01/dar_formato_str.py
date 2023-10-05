# Dar formato a un string

nombre = 'Ariel'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre, edad)
print(mensaje_con_formato)

# Creamos una tupla
persona = ('Carla', 'Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f' # % persona # aquí le pasamos el objeto que es una tupla
print(mensaje_con_formato % persona)

nombre = 'Juan'
edad = 19
sueldo = 3000
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
#print(mensaje_con_formato)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)
# nombre → {0}; edad → {1}; sueldo → {2}. Sus valores se respetan y pueden ser colocados
# en cualquier lado dentro del string
# 'Nombre {2:.2f} Edad {0} Sueldo {1}' → Nombre 3000 Edad Juan Sueldo 19

mensaje_con_formato = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 8000.00}
mensaje = 'Nombre {persona[nombre]}'.format(persona=diccionario)
print(mensaje)
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]}'.format(dic=diccionario)
print(mensaje)