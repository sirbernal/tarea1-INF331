from datetime import datetime

def log(error, tipo, arg):
    archivo = open('logs.txt', 'a')
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    if not error:
        if tipo == 1:
            archivo.write("[%s] Valor erroneo ingresado en menú: %s \n" % (current_time, arg))
        elif tipo == 2:
            archivo.write("[%s] Formato invalido al comparar caracteres: %s \n" % (current_time, arg))
        elif tipo == 3:
            archivo.write("[%s] Se ingresaron opciones no existentes al comparar caracteres: %s \n" % (current_time, arg))
        elif tipo == 4:
            archivo.write("[%s] Se ingresa a la opción de comparar caracteres, pero no hay al menos 2 para comparar \n" % (current_time))
    else:
        if tipo == 1:
            archivo.write("[%s] Se agrega el caracter: %s a la pila \n" % (current_time, arg))
        if tipo == 2:
            archivo.write("[%s] Se compara %s y %s, resultando que son %s \n" % (current_time, arg[0], arg[1], arg[2]))
    archivo.close()
    
    
def comparar_elementos_pila():
    print("Caracteres disponibles para comparar")
    for i in range(len(pila)):
        print("[" + str(i) + "] " + pila[i])
    print("Anotar las 2 opciones a comparar, separados por una coma")
    print("Ejemplo: 1,2  para comparar el elemento 1 y 2")
    comparar = input()
    try:
        index1, index2 = comparar.split(",")
        if pila[int(index1)] == pila[int(index2)]:
            log(True, 2, (pila[int(index1)], pila[int(index2)], "iguales"))
            print("Son iguales")
        else:
            log(True, 2, (pila[int(index1)], pila[int(index2)], "distintos"))
            print("Son distintos")   
    except ValueError:
        log(False, 2, comparar)
        print("Formato ingresado invalido, volviendo al menú")
    except IndexError:
        log(False, 3, comparar)
        print("Valores ingresados no estan dentro de las opciones")
#    finally:
#        pass
        

pila = []
while(True): 
    print("---MENU----")
    print("Opciones disponibles \n")
    print("[1] Guardar cadena de caracteres")
    print("[2] Comparar caracteres disponibles")
    print("[3] Cerrar programa")
    option = input("Escribir número de la opción a realizar: ")
    print("\n")
    try:
        if (int(option) == 1):
            cadena = input("Escribir cadena a guardar:  ")
            pila.append(cadena)
            log(True,1,cadena)
        elif (int(option) == 2):
            if len(pila) < 2:
                log(False,4,cadena)
                print("Para comparar elementos es necesario tener por lo menos 2 elementos almacenados \n")
            else:
                comparar_elementos_pila()
        elif (int(option) == 3):
            break
        
        else:
            raise ValueError
    
    except ValueError:
        log(False, 1, option)
        print("Se ha ingresado una opción no válida, por favor volver a intentar")
   
