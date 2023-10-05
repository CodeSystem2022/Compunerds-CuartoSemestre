#help(str.join) ##    La cadena cuyo método se llama se inserta entre cada cadena dada.
#El resultado se devuelve como una nueva cadena.
#Ejemplo: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

tupla_str=('Hola','alumnos','Tecnicatura','Universitaria')
mensaje=' '.join(tupla_str)
print(mensaje)

lista_cursos=['Java','JavaScript','Python','Spring','Angular']
mensaje=',  '.join(lista_cursos)
print(f'Mensaje : {mensaje}')

cadena='Hola Mundo'
mensaje='-'.join(cadena)
print(f'Mensaje : {mensaje}')

diccionario= {'nombre':'Juan','spellido':'Perez','edad':'18'}
llaves='-'.join(diccionario.keys())
valores= '-'.join(diccionario.values())
print(f'LLaves :{llaves}, Type:{type(llaves)}')
print(f'Valores :{valores}, Type:{type(valores)}')