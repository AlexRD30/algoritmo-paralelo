class Banco:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self, numero_cuenta, saldo, limite_credito, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.limite_credito = limite_credito
        self.tipo_cuenta = tipo_cuenta

class Cliente:
    def __init__(self, nombre, direccion, numero_cuenta, saldo, contrasena):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.contrasena = contrasena

class Cajero:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

class CajeroAutomatico:
    def __init__(self, banco, clientes):
        self.banco = banco
        self.clientes = clientes
        self.cliente_autenticado = None

    def validar_usuario(self, numero_cuenta, contrasena):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta and cliente.contrasena == contrasena:
                self.cliente_autenticado = cliente
                return True
        return False

    def mostrar_menu(self):
        print("¿Qué desea hacer?")
        print("1. Retirar efectivo")
        print("2. Ingresar efectivo")
        print("3. Pagar factura")
        print("    a. Pago de préstamo")
        print("    b. Factura de tarjeta de crédito")
        print("4. Transferir fondos")
        print("5. Ver saldo")
        print("0. Salir")

    def ingresar_efectivo(self, cantidad):
        self.cliente_autenticado.saldo += cantidad
        print(f"Se ingresaron {cantidad} a la cuenta de {self.cliente_autenticado.nombre}. Nuevo saldo: {self.cliente_autenticado.saldo}")

    def retirar_efectivo(self, cantidad):
        if self.cliente_autenticado.saldo >= cantidad:
            self.cliente_autenticado.saldo -= cantidad
            print(f"Se retiraron {cantidad} de la cuenta de {self.cliente_autenticado.nombre}. Saldo restante: {self.cliente_autenticado.saldo}")
        else:
            print("Saldo insuficiente.")

    def pagar_factura(self, info_factura):
        print(f"Se pagó la factura {info_factura} desde la cuenta {self.cliente_autenticado.numero_cuenta}.")

    def transferir_fondos(self, info_cuenta_destino, cantidad):
        # Lógica de transferencia de fondos
        print(f"Se transfirieron {cantidad} desde la cuenta {self.cliente_autenticado.numero_cuenta} a {info_cuenta_destino}.")

    def ver_saldo(self):
        print(f"Saldo actual de la cuenta de {self.cliente_autenticado.nombre}: {self.cliente_autenticado.saldo}")

# Creación de instancias con contraseñas
cliente1 = Cliente("Ana Rodríguez", "Calle Estrella", "12345", 10000, "4321")
cliente2 = Cliente("Carlos Pérez", "Avenida Central", "98765", 150000, "5678")
cliente3 = Cliente("Laura Gómez", "Calle Principal", "65432", 200000, "8765")

# Creación de instancia de CajeroAutomatico
banco = Banco("Banco Principal")
clientes = [cliente1, cliente2, cliente3]
cajero_automatico = CajeroAutomatico(banco, clientes)

# Solicitud
numero_cuenta = input("Ingrese el número de cuenta: ")
contrasena = input("Ingrese la contraseña: ")

# Validar
if cajero_automatico.validar_usuario(numero_cuenta, contrasena):
    print(f"Usuario autenticado como {cajero_automatico.cliente_autenticado.nombre}.")

    while True:
        cajero_automatico.mostrar_menu()

        opcion = input("Ingrese el número de la operación que desea realizar (0 para salir): ")

        if opcion == '0':
            print("Sesión terminada. Gracias por usar el cajero automático.")
            break

        if opcion.isdigit() and 1 <= int(opcion) <= 5:  # Actualizado para incluir la opción de ver saldo
            opcion = int(opcion)
            if opcion == 3:
                print("Seleccione el tipo de factura:")
                print("a. Pago de préstamo")
                print("b. Factura de tarjeta de crédito")
                subopcion = input("Ingrese la letra correspondiente: ")
                cajero_automatico.pagar_factura(info_factura=subopcion)
            elif opcion == 4:
                info_cuenta_destino = input("Ingrese la información de la cuenta destino: ")
                cantidad = float(input("Ingrese la cantidad que desea transferir: "))
                cajero_automatico.transferir_fondos(info_cuenta_destino, cantidad)
            elif opcion == 5:  # Nueva opción para ver saldo
                cajero_automatico.ver_saldo()
            else:
                cantidad = float(input("Ingrese la cantidad: "))
                if opcion == 1:
                    cajero_automatico.retirar_efectivo(cantidad)
                elif opcion == 2:
                    cajero_automatico.ingresar_efectivo(cantidad)
        else:
            print("Opción no válida. Ingrese un número del 1 al 5 o 0 para salir.")
else:
    print("Usuario o contraseña incorrectos.")
