# CREACION DE LA BASE DE DATOS
create database usuarios;
# USAMOS LA BASE DE DATOS
use usuarios;

# CREACION DE LA TABLA
create table usuarios(
    cod_usuario int auto_increment primary key,
    rol varchar(100),
    nombre varchar(100),
    contraseña varchar(50),
    correo varchar(60),
    numero_telefono varchar(30),
    estado varchar(40)
);


