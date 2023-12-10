class Estudiante:
 

    def ClasePersona( selt , nombre, apellido, edad, sexo, direccion, Carrera, email, telefono):
        return nombre +" "+ apellido +" " + edad +" " + sexo +" " + direccion +" "+ Carrera+" "+  email +" "+ telefono

estu = Estudiante()
nombre=input("Nombre...:")
apellido=input("Apellido...:")
edad=input("Edad....:")
sexo=input("Sexo...:")
direccion=input("Direccion....:")
Carrera=input("Carrera....:")
email=input("Email...:")
telefono=input("Telefono....:")

print(" Informacion del Estudiante:...", estu.ClasePersona (nombre, apellido, edad, sexo, direccion, Carrera, email, telefono))
