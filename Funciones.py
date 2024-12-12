def saludo(nombre, edad):
    print("Hola " + nombre + " y tienes " + str(edad) + " años" )

saludo("Carlos", 20)
saludo("Liceth", 18)



def fuerza(peso):
    print(peso * g)
g = 9.81
fuerza(69)
print(g)

def velocidad(peso):
    if peso >= 80:
        print("eres lento")
    else:
        print("eres rapido")

velocidad(79)

def altura(estatura):
    if estatura >= 1.80:
        print("Eres alto")
    elif estatura >1.60 <= 1.75:
        print("tu estarura es promedio")
    else:
        print("eres pequeño")
        altura(1.80)




