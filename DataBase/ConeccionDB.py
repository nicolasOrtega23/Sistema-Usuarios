import mysql.connector
from mysql.connector import errorcode
from Model.Usuarios import Usuarios
from typing import List
# CLASE
class Conexion:
    def __init__(self):
        try:  # DEFINIMOS LA CONEXION
            self.conex = mysql.connector.connect(
                user='nicolas',
                password='yuyu25',
                host='localhost',
                database='usuarios'
            )
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuario o contraseña incorrectos")
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe la base de datos")
            else:
                print(error)
    def Autenticacion(self, nombre, contra):
        cursor = self.conex.cursor()
        query = ("SELECT nombre,rol,contraseña FROM usuarios WHERE  nombre = %s AND contraseña = %s AND (rol = 'Superadministrador' or rol =  'Administrador');")
        data = (nombre, contra,)
        cursor.execute(query, data)
        usuario = cursor.fetchone()
        return usuario
    def Autorizacion(self,nombre,contra):
        try:
            cursor = self.conex.cursor()
            query = ("SELECT nombre,estado,contraseña FROM usuarios WHERE nombre = %s AND contraseña =%s  AND estado = 'Bloqueado';")
            data = (nombre, contra)
            cursor.execute(query,data)
            usuario = cursor.fetchone()
            return usuario
        except Exception as error:
            print(error)
    # -- METODOS SQL (CRUD) --
    def InsertarUsuario(self, user: Usuarios):
        # INICIAMOS LA CONEXION
        cursor = self.conex.cursor()
        query = ("INSERT INTO usuarios (rol, nombre, contraseña, correo, numero_telefono, estado) "
                 "VALUES (%s,%s,%s,%s,%s,%s);")
        data = (user.Rol(), user.Nombre(), user.Contraseña(),user.Correo(), user.Numero(),user.Estado(),)
        cursor.execute(query, data)
        self.conex.commit()
    # -- LEER USUARIOS --
    def ListarUsuarios(self):
        # INICIAMOS LA CONEXION
        cursor = self.conex.cursor()
        query = ("SELECT * FROM usuarios;")
        cursor.execute(query)
        usuarios: List[Usuarios] = []
        for (cod_usuario, rol, nombre, contra ,correo,numero, estado) in cursor:
            user = Usuarios(cod_usuario, rol, nombre, None,None,'+569 ', estado)
            usuarios.append(user)
            print(f' |   {str(cod_usuario).center(30)}              {str(rol).center(26)}              {str(nombre).center(24)}            {str(estado).center(20)}      |\n')
    # -- ELIMINAR USUARIO --
    def EliminarUsuarios(self, cod: int):
        cursor = self.conex.cursor()
        query = ("DELETE FROM usuarios WHERE cod_usuario = %s;")
        data = (int(cod),)
        cursor.execute(query, data)
        self.conex.commit()
    def ImpedirEliminacion(self,cod):
        try:
            cursor = self.conex.cursor()
            query = ("SELECT cod_usuario,nombre,rol FROM usuarios WHERE rol = 'SuperAdministrador' AND cod_usuario =%s;")
            data = (int(cod),)
            cursor.execute(query,data)
            usuario = cursor.fetchone()
            return usuario
        except Exception as error:
            print(error)
# -- CAMBIAR CONTRASEÑA --
    def CambiarContraseña(self, nueva:str,antigua:str):
        try:
            cursor = self.conex.cursor()
            query = ("UPDATE usuarios SET contraseña = %s WHERE contraseña = %s ;")
            data = (str(nueva),str(antigua),)
            cursor.execute(query, data)
            update1 = cursor.rowcount
            if update1 > 0:
                input('La contraseña se actualizo correctamente')
                self.conex.commit()
            else:
                input('No se pudo actualizar la contraseña')
        except Exception as error:
            input(f'Error de actualización de contraseña : {error}')
            self.conex.rollback()
# -- CAMBIAR DATOS --
    def CambiarDatosUsuario(self, contraseña, correo, numero, cod):
           try:
                cursor = self.conex.cursor()
                query = ("UPDATE usuarios SET contraseña = %s,correo = %s,numero_telefono = %s WHERE cod_usuario = %s;")
                data = (str(contraseña),str(correo),str(numero),int(cod),)
                cursor.execute(query, data)
                update2 = cursor.rowcount
                if update2 > 0:
                    input('Los datos se actualizaron correctamente')
                    self.conex.commit()
                else:
                    input('No se pudo actualizar los datos')
           except Exception as error:
                input(f'Error de actualización de datos : {error}')
                self.conex.rollback()
        # -- BLOQUEAR USUARIO --
    def BloquearUsuario(self, cod: int):
        try:
            cursor = self.conex.cursor()
            query = ("UPDATE usuarios SET estado = 'Bloqueado' WHERE  estado = 'Activado'  AND cod_usuario = %s; ")
            data = (int(cod),)
            cursor.execute(query, data)
            update3 = cursor.rowcount
            if update3 > 0:
                input('El usuario se bloqueo correctamente')
                self.conex.commit()
            else:
                input('No se pudo bloquear el usuario')
        except Exception as error:
            input(f'Error de bloqueo de usuario : {error}')
            self.conex.rollback()
    def ImpedirBloqueo(self,cod):
        try:
            cursor = self.conex.cursor()
            query = ("SELECT cod_usuario,nombre,rol FROM usuarios WHERE rol = 'SuperAdministrador' AND cod_usuario =%s;")
            data = (int(cod),)
            cursor.execute(query,data)
            usuario = cursor.fetchone()
            return usuario
        except Exception as error:
            print(error)
        # -- DESBLOQUEAR USUARIO --
    def DesbloquearUsuario(self, cod: int):
        try:
            cursor = self.conex.cursor()
            query = ("UPDATE usuarios SET estado = 'Activado' WHERE  estado = 'Bloqueado'  AND cod_usuario = %s; ")
            data = (int(cod),)
            cursor.execute(query, data)
            update4 = cursor.rowcount
            if update4 > 0:
                input('El usuario se desbloqueo correctamente')
                self.conex.commit()
            else:
                input('No se pudo desbloquear el usuario')
        except Exception as error:
            input(f'Error de desbloqueo de usuario : {error}')
            self.conex.rollback()