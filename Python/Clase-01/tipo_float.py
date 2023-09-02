# Profundizamos en el TIPO FLOAT
a = 3.0
print(f'a: {a:.2f}')  # a: 3.00 (.2f muestra 2 decimales. Si no hay valor, agrega ceros)

# Constructor de tipo float → puede recibir INT y STR
a = float(10)  # Le pasamos un tipo entero (int)
print(f'a: {a:.2f}')  # a: 10.00

# Notación exponencial (valores positivos o negativos)
print('notacion exponencial positiva')
a = 3e5  # le agregamos cinco 0
print(f'a: {a}')  # a: 300000.0
a = 3e50
print(f'a: {a}')  # a: 3e+50, forma simplificada de mostrar un número muy alto

print('notacion exponencial negativa')
a = 3e-5
print(f'a: {a:.5f}')  # a: 0.00003

# Cualquier cálculo que incluya un FLOAT, TODO CAMBIA A FLOAT
a = 4.0 + 5
print(a)  # 9.0
print(type(a))