class Empleado:
   

    def __init__(self):
        self.nombre=input("ingrese el nombre del empleado:")
        self.apellido=input("ingrese el apellido del empleado:")
        self.edad=int(input("ingrese la edad del empleado:"))
        self.sexo=input("ingrese el sexo del empleado:")
        self.direccion=input("ingrese la dirección del empleado:")
        self.email=input("ingrese el email del empleado:")

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("Dirección:", self.direccion)
        print("Email:", self.email)

    def Afp(selt, sb):
        return sb * 0.0287
    
    def Irs(selt, sb):
        if sueldo <= 416220.00:            
         return sb * 0,    print("NO PAGA IMPUESTOS SOBRE LA RENTA")           
        if sueldo >= 416220.01 and sueldo <= 624329.00:
            return sb * 0.15
        if sueldo > 624329.01 and sueldo <=  867123.00:
            return sb * 0.20
        else:
            return sb * 0.25
                  
    def Sfs(selt, sb):
        return sb * 0.0304
    
    def TotalDesc(setl, afp, irs, sfs):

        if sueldo < 416220.00:
            return afp+sfs
        else:   
            return afp+irs+sfs
    
    def SueldoNeto(selt, sb, td):
        return sb -td

emp = Empleado()

sueldo = float(input("Entre sueldo :"))
sueldo= sueldo*12
afp=emp.Afp(sueldo)
sfs=emp.Sfs(sueldo)
irs=emp.Irs(sueldo)
descuento= emp.TotalDesc(afp, irs, sfs)
sn= emp.SueldoNeto(sueldo, descuento)

emp.imprimir()
print("Afp          : {:0.2f}".format(afp))
print("Sfs          : {:0.2f}".format(sfs))

if sueldo > 416220.00:
    print("Irs          : {:0.2f}".format(irs))


print("Descuento    : {:0.2f}".format(descuento))
print("Sueldo Neto  : {:0.2f}".format(sn))

