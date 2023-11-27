class Usuarios:
    def __init__(self,  codigo: int, rol: str, nombre:str, contra, correo, numero,estado) -> None:
        self.__rolUsuario = rol.capitalize()
        self.__codigoUsuario = codigo
        self.__nombreUsuario = nombre.capitalize()
        self.__contrasenaUsuario = contra
        self.__correoUsuario = correo
        self.__numeroUsuario = '+569 ' + numero
        self.__estadoUsuario = estado


    def Codigo(self) -> int:
        return self.__codigoUsuario

    def Rol(self) -> str:
        return self.__rolUsuario

    def Nombre(self) -> str:
        return self.__nombreUsuario

    def Contraseña(self) -> str:
        return self.__contrasenaUsuario

    def Correo(self) -> str:
        return self.__correoUsuario

    def Numero(self) -> str:
        return self.__numeroUsuario

    def Estado(self) -> str:
        return self.__estadoUsuario