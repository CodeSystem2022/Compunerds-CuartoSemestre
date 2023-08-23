opcion = None
while opcion != 5:
    print('Opciones: ')
    print('1. Listar Usuarios')
    print('2. Agregar Usuarios')
    print('3. Modificar Usuarios')
    print('4. Eliminar Usuarios')
    print('5. salir')
    opcion = int(input('Digite la opción (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usurios:
            log.info(usuario)

else:
    log.info('Salimos de la aplicación. ¡Hasta pronto!')