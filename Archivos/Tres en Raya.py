def ComienzaElJuego():

    # Esta función presenta el juego. Es un mensaje de bienvenida.

    print("""
###############################################       
Bienvenidos! Hoy vamos a jugar al Tres en Raya!
Conoces las reglas o vives en un tupper?
Si conoces las reglas elige la opción '1'.
De lo contrario escriba el número '2'.
En caso de que quieras salir escriba "S".       
###############################################""")
    
    while (True):
        try:
            eleccion = input("\nOpción elegida: ")

            if eleccion == "S" or eleccion == "s":
                print("\nOk, si no quieres seguir jugando no hay problema. Hasta luego!")
                break
            elif eleccion != "1" and eleccion != "2":
                raise ValueError
            else:
                if eleccion == "1":
                    print("""
###############################################                          
                  Comencemos!                                       
###############################################""")

                    return ""
                else:
                    print("""\nNo conoces las reglas? Busca en google, no voy a
perder tiempo en explicarte un juego tan simple.
                          
###############################################                          
                  Comencemos!
###############################################""")
                    return ""
        except ValueError:
            print(f"\nDe verdad has escrito \"{eleccion}\"? Tenías que escribir '1', '2' ó 'S'. \
No es tan difícil. Vuelve a intentarlo.")

def DibujarTablero(tablero):

    # Esta función escribe el tablero en pantalla.
    # Toma como parámetro una lista de 3 listas que representan 
    # cada casillero y serán reemplazadas por los valores del
    # juego (una "X" o una "O") según el valor que introduzcan
    # los jugadores.

    for filas in range(3):
        print("+------------" * 3, end="+\n")
        print("|            " * 4)
        print("")
        for columnas in range(3):
            print(f"|      {tablero[filas][columnas]}     ", end="")                                        # Cuando los jugadores elijen un valor esta función recupera 
        print("|")                                                                                          # la lista "tablero" modificada y se imprime la opción elegida
        print("")                                                                                           # en el campo que corresponda.
        print("|            " * 4)                                  
    print("+------------" * 3, end="+\n")
    return ""

def Movimiento(tablero, contador=0):

    # Esta función define los movimientos introducidos por
    # los jugadores. Toma 2 argumentos. Por un lado, toma el
    # tablero con las 3 listas que representan cada casillero
    # y serán utilizadas como índices para determinar los 
    # movimientos de cada jugador. Cualquier valor fuera del
    # 1, el 9 o que esté ocupado devuelve una cadena indicando
    # que se reintente. Por el otro, toma un contador el cual
    # si es par representará al jugador 1 o al 2 si es impar.
    # Una vez indicado un valor correcto modifica el tablero
    # con una "X" u "O" según sea el turno del jugador 1 o 2.
    
    while (True):
        try:
            if contador % 2 == 0:                                                                           # Se establece un contador que representa el jugador
                valor_introducido = input(f"\n{jugador1} es tu turno! Introduzca un valor del 1 al 9: ")    # 1 si es par o el 2 si es impar
            else:
                valor_introducido = input(f"\n{jugador2} es tu turno! Introduzca un valor del 1 al 9: ")
            valor_introducido = int(valor_introducido)
            celda = valor_introducido - 1                                                                   # Se establecen cálculos sobre las variables celda, filas
            filas = celda // 3                                                                              # y columnas para que cada valor introducido (del 1 al 9)
            columna = celda % 3                                                                             # se corresponda con el índice correcto en el tablero. 
            opcion_elegida = tablero[filas][columna]                                                        # La variable "opción_elegida" si no detecta ningún error                                                                                              
            espacios_ocupados = ("O", "X")                                                                  # se actuliza de acuerdo al valor introducido. 
        
            if valor_introducido < 1 or valor_introducido > 9 or valor_introducido == None:
                raise IndexError
            elif opcion_elegida in espacios_ocupados: 
                print("\nError, el espacio seleccionado ya está ocupado. Elija un campo libre dentro del tablero.")
            else:
                if contador % 2 == 0:
                    opcion_elegida = tablero[filas][columna] = "X"
                    break                    
                else:
                    opcion_elegida = tablero[filas][columna] = "O"
                    break
                
        except ValueError:
            print(f"\nTe he pedido un número y escribes \"{valor_introducido}\"! No es tan difícil. Vuelva a intentarlo.")        
        except IndexError:
            print(f"\nDe verdad has escrito \"{valor_introducido}\"? Tenías que escribir un número entre \
el 1 y el 9. No es tan difícil. Vuelva a intentarlo.")

def Victoria(tablero):

    # Esta función define las distintas posibilidades que   
    # determinan la victoria. Toma como argumento el tablero 
    # actualizado, lo evalúa y retorna las variables jugador
    # 1 o 2 si encuentra alguna combinación ganadora.   
    
    for f in range(3):
        if tablero[f][0] == tablero[f][1] == tablero[f][2] == "X":        # Verifica las filas 1, 2 y 3 para el jugador 1    
            return jugador1
        elif tablero[f][0] == tablero[f][1] == tablero[f][2] == "O":      # Verifica las filas 1, 2 y 3 para el jugador 2 
            return jugador2              
        elif tablero[0][f] == tablero[1][f] == tablero[2][f] == "X":      # Verifica las columnas 1, 2 y 3 para el jugador 1    
            return jugador1
        elif tablero[0][f] == tablero[1][f] == tablero[2][f] == "O":      # Verifica las columnas 1, 2 y 3 para el jugador 2    
            return jugador2
        
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == "X":            # Verifica la diagonal de los casilleros 1, 5 y 9
        return jugador1                                                   # para el jugador 1.
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] == "O":          # Verifica la diagonal de los casilleros 1, 5 y 9
        return jugador2                                                   # para el jugador 2.
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] == "X":          # Verifica la diagonal de los casilleros 3, 5 y 7
        return jugador1                                                   # para el jugador 1.
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] == "O":          # Verifica la diagonal de los casilleros 3, 5 y 7
        return jugador2                                                   # para el jugador 2.


#################################
#### AQUÍ SE DEFINE EL JUEGO ####
#################################

try:

    while(True):

        if ComienzaElJuego() == None:                                                               # Primer bucle que determina si el juego comienza o no.
            break
        else:

            tablero = [[1,2,3], [4,5,6], [7,8,9]]                                                   # Tablero que representa los valores iniciales de cada fila y columna.
            contador = 0                                                                            # Variable que cuenta los movimientos correctos y finaliza el juego al superar el valor 8.
            reinciar = False                                                                        # Variable cambia de False a True cuando de desee volver a jugar.
                                                                                                    
            print("\nEscribe el nombre del jugador nº 1 y a continuación el del jugador nº 2.\n")
            jugador1 = input("Nombre del jugador 1: ")
            jugador2 = input("Nombre del jugador 2: ")
            print(f"\nBienvenidos {jugador1} y {jugador2}. Comencemos con el juego!\n")

            while(True):                                                                            # Segundo bucle que consta de 2 partes. Un bucle que que sólo finaliza cuando la variable                      
                                                                                                    # reinicar se establezca como "True" y un bloque "else" que evalúa si se desea comenzar
                while reinciar == False:  
                                                                                                    # una nueva partida.
                    DibujarTablero(tablero)
                    Movimiento(tablero, contador)
                    contador +=1

                    if Victoria(tablero) == jugador1:                                               # Evalúa la victoria del jugador 1.
                        DibujarTablero(tablero)
                        print(f"\nFelicitaciones {jugador1}, has ganado!! Lo siento {jugador2}, \
tendrás que practicar más.")
                        reinciar = True                                                             # Reinciar cambia de estado para salir del bucle.

                    elif Victoria(tablero) == jugador2:                                             # Evalúa la victoria del jugador 1.
                        DibujarTablero(tablero)
                        print(f"\nFelicitaciones {jugador2}, has ganado!! Lo siento {jugador1}, \
tendrás que practicar más.")
                        reinciar = True                                                             # Reinciar cambia de estado para salir del bucle.
                        
                    elif contador > 8:                                                              # Cuando el contador supera el 8 significa que ya no hay movimientos posibles.
                        DibujarTablero(tablero)                                                     # Si llegado a este punto no hay un ganador entonces hay un empate.
                        print(f"\nPffff, qué aburrido, han empatado.")
                        reinciar = True                                                             # Reinciar cambia de estado para salir del bucle.

                else:                                                                               # Este bloque "else" se ocupa de reiniciar el juego o no.
                    opciones_validas = ["S", "s", "N", "n"]
                    reinciar = input("\nQuieren volver a jugar? Si es así, elijan 'S'. En caso \
contrario elijan 'N'. ")
                    if reinciar not in opciones_validas:
                        print(f"\nTe he pedido que escribas 'S' o 'N' y escribes \"{reinciar}\"! \
No es tan difícil. Vuelva a intentarlo.")
                    elif reinciar in opciones_validas[:2]:                                          # Continuar jugando. Se restablece todo como al inicio sin salir del segundo bucle.
                        reinciar = False
                        contador = 0
                        tablero = [[1,2,3], [4,5,6], [7,8,9]]
                    elif reinciar in opciones_validas[2:]:                                          # No continuar. Se sale del segundo bucle.
                        print(f"\nHasta la próxima {jugador1} y {jugador2}")
                        break
                    
        break                                                                                       # Finaliza el primer bucle y termina el juego.
except KeyboardInterrupt:
    print("\n\nOk, no era necesario ser tan directo! Si no quiere seguir jugando no hay problema. Hasta luego.")
