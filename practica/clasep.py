class persona:

    def ClasePersona( selt , nombre, apellido, edad, sexo, direccion):
        return nombre +" "+ apellido +" " + edad +" " + sexo +" " + direccion

Per = persona()
nombre=input("Nombre...:")
apellido=input("Apellido...:")
edad=input("Edad....:")
sexo=input("Sexo...:")
direccion=input("Direccion....:")

print(" Informacion de la persona:...", Per.ClasePersona(nombre, apellido, edad, sexo, direccion))
