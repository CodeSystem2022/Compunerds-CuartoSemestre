#help(str.split)

cursos='Java Python Javascript Diseño Node'
lista_cursos=cursos.split()
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma= 'Java, Python, Javascript, Diseño,Node'
lista_cursos=cursos_separados_coma.split(',',2)
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos))