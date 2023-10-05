#help(str.capitalize) el metodo capitalize convierte la primer letra del string en Mayuscula, y las demas las deja en minuscula

mensaje1= "hola mundo"
mensaje2=mensaje1.capitalize()
print(f'Mensaje 1: {mensaje1}, id:{id(mensaje1)}')
print(f'Mensaje 2: {mensaje2}, id:{id(mensaje2)}') ##id muestra la direccion hexadecimal donde se guarda

mensaje1 += ' Adios'
print(f'Mensaje 1: {mensaje1}, id:{id(mensaje1)}')