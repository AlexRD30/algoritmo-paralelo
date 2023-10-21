op= int(input(" La calificacion: "))
match op:
    case _ if op >= 90:
        print("A")
    case _ if op >= 80:
        print("B")
    case _ if op >= 70:
        print("C")
    case _ if op >= 60:
        print("D")
    case _:
        print("Selecciona una opcion valida")