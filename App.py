from DataBase.ConeccionDB import Conexion
from Model.Usuarios import Usuarios
import os
    # --- PRIMER MENU ----
while True:
    print('\nIndica tu Rol')
    print('[1]SuperAdministrador\n[2]Administrador\n[3]Usuario\n'
        '[4]Vendedor')
    eleccion = input('>>>>>  ')
    if eleccion != '3' and eleccion != '4':
        dao = Conexion()
        os.system('cls')
        print('\n-- AUTENTICACION --\n ')
        nombre = str(input("Ingrese el nombre del usuario:  ")).capitalize()
        contra = str(input(f"Ingresa contraseña {nombre}:  "))
        if dao.Autorizacion(nombre,contra):
            input('Este Usuario esta Bloqueado')
            continue
        else:
            if dao.Autenticacion(nombre,contra):
                input(f'Usuario {nombre} Auntenticado y Autorizado correctamente\nEnter para salir')
                while True: # --- SEGUNDO MENU ---
                    print("-- Bienvenido al Sistema de Administracion de Usuarios --\n")
                    print("1 - Registrar Usuario\n2 - Eliminar Usuario\n3 - Bloquear Usuario\n"
                        "4 - Desbloquear Usuario\n5 - Cambiar contraseña a un usuario\n"
                        "6 - Cambiar datos de un usuario\n7 - Salir\n")
                    op = input("Ingrese una opcion:  ")
                    os.system("cls")
                    if op == '1':
                        os.system("cls")
                        print('\n -- REGISTRO DE USUARIO --\n')
                        rol = input("Ingrese el rol del usuario:  ")
                        nombre = input("Ingrese el nombre del usuario:  ")
                        contra = input(f"Ingresa contraseña {nombre}: ")
                        correo = input(f"Ingrese su coreo {nombre}:  ")
                        numero = input(f"Ingrese su numero {nombre}:  ")
                        user = Usuarios(0, rol, nombre, contra, correo, numero,'Activado')
                        dao.InsertarUsuario(user)
                        input('Usuario registrado correctamente\n Enter para salir')
                        os.system('cls')
                        continue
                    # -- ELIMINAR USUARIO --
                    elif op == '2':
                        os.system("cls")
                        print('\n -- ELIMINAR USUARIO --\n')
                        print('|         cod_usuario        |                       rol                       |                nombre                |               estado                |')
                        dao.ListarUsuarios()
                        print('Ingrese el codigo del usuario a eliminar ')
                        cod = int(input('>>>>>  '))
                        if dao.ImpedirEliminacion(cod):
                            input('Este usuario tiene un rol de Superadministrador no se puede eliminar\nEnter para salir ')
                            os.system('cls')
                            continue
                        else:
                            dao.EliminarUsuarios(cod)
                            input('Usuario eliminado correctamente\n Enter para salir ')
                            os.system('cls')
                            continue
                # -- BLOQUEAR USUARIO --
                    elif op == '3':
                        print('\n -- BLOQUEAR USUARIO --\n')
                        print(' |         cod_usuario        |                       rol                       |                nombre                |               estado                |')
                        # COLUMNAS DE LA TABLA DE USUARIOS --
                        dao.ListarUsuarios()
                        cod = int(input('Ingrese el codigo del usuario a bloquear:  '))
                        if dao.ImpedirBloqueo(cod):
                            input('Este es un usuario con rol Superadministrador no se puede bloquear\nEnter para salir')
                            continue
                        else:
                            dao.BloquearUsuario(cod)
                        os.system('cls')
                        continue
                    # -- DESBLOQUEAR USUARIO --
                    elif op == '4':
                        print('\n -- DESBLOQUEAR USUARIO --\n')
                        # COLUMNAS DE LA TABLA DE USUARIOS --
                        print(' |         cod_usuario        |                       rol                       |                nombre                |               estado                |')
                        dao.ListarUsuarios()
                        cod = int(input('Ingrese el codigo del usuario a desbloquear:  '))
                        dao.DesbloquearUsuario(cod)
                        os.system('cls')
                        continue
                # -- CAMBIAR CONTRASEÑA --
                    elif op == '5':
                        os.system("cls")
                        print('\n -- CAMBIO DE CONTRASEÑA --\n ')
                        print('Ingrese la contraseña antigua y la contraseña nueva para cambiar la contraseña ')
                        nueva = input('contraseña nueva >>>>>  ')
                        antigua = input('contraseña antigua >>>>>  ')
                        dao.CambiarContraseña(nueva, antigua)
                        os.system('cls')
                        continue
                # -- CAMBIAR DATOS --
                    elif op == '6':
                        os.system('cls')
                        print('\n-- CAMBIO DE DATOS DE USUARIO --\n')
                        print(' |         cod_usuario        |                       rol                       |                nombre                |               estado                |')
                        dao.ListarUsuarios()
                        contraseña = input('Ingresa la nueva contraseña:  ')
                        correo = input('Ingresa el nuevo correo:  ')
                        numero = input('Ingresa el nuevo numero:  ')
                        cod = int(input('Ingresa el codigo del usuario:  '))
                        dao.CambiarDatosUsuario(contraseña, correo, numero,cod)
                        os.system('cls')
                        continue
                    elif op == '7':
                        break
            else:
                input('Usuario no autorizado')