class CajeroAutomatico:
    def __init__(self):
        self.saldo = 1000  

    def realizarRetiro(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes.")


cajero = CajeroAutomatico()
monto_retiro = float(input("Ingrese el monto que desea retirar: "))
cajero.realizarRetiro(monto_retiro)
