#Calculadora

#input
#2 numeros y operaicon


def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    assert (b != 0), "No se puede divir por 0, melón."
    return (a/b)


def pow(a, b):
    return a**b


op = 0
print("\n\n")

operacion = {1: suma,
             2: resta,
             3: mult,
             4: div,
             5: pow
             }

while True:
    print("Operacion {1: suma | 2: resta | 3: multiplicaicon | 4: division | 5: potencia | 6: salir}")
    op = int(input("-> "))
    if (op == 6):
        break;
    a = float(input("Primer numero:\t"))
    b = float(input("Segundo numero:\t"))
    print(operacion[op](a, b), "\n\n")