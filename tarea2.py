import random

# Funcion para la tirada del dado
def lanzar_dado():
   # devuelve un valor entre 1 y 6
   return random.randint(1,6)


# Funcion para calcular el puntaje
def puntaje(dado1, dado2):
   # dado1 corresponde al valor de la tirada del primer dado
   # dado2 corresponde al valor de la tirada del segundo dado
   # devuelve el puntaje obtenido

   if (dado1 == 4 and dado2 == 1) or (dado1==1 and dado2 == 4):
      return 1
   elif (dado1 == 4 and dado2 == 2) or (dado1==2 and dado2 == 4):
      return 2
   elif (dado1 == 4 and dado2 == 3) or (dado1==3 and dado2 == 4):
      return 3
   elif (dado1 == 4 and dado2 == 4):
      return 4
   elif (dado1 == 4 and dado2 == 5) or (dado1==5 and dado2 == 4):
      return 5
   elif (dado1 == 4 and dado2 == 6) or (dado1==6 and dado2 == 4):
      return 6
   else:
      return 0
  

# Estrategia elegida por Juan
def juan():
    # Se lanzan los dos dados y se obtiene un puntaje
    dado1=lanzar_dado()
    dado2=lanzar_dado()
    puntos=puntaje(dado1, dado2)
    
    if puntos == 0:
       # Obtuvo 0 puntos, jugar denuevo
        dado1=lanzar_dado()
        dado2=lanzar_dado()
        puntos=puntaje(dado1, dado2)

    elif puntos <= 3:
       # Si obtiene 1,2 o 3 puntos usa la segunda tirada para mejorar el puntaje. Si obtiene mas de 3, se planta y no tira denuevo
       # Tira de nuevo el dado que no obtuvo 4 o cualquiera de los dos si obtuvo en ambos 4
        if dado2 != 4:
           # El segundo dado es distinto a 4, tirarlo denuevo
           dado2=lanzar_dado()
        else:
           # El primer dado es distinto a 4 o ambos son igual a 4, tirar dado1 denuevo
            dado1=lanzar_dado()
        puntos=puntaje(dado1, dado2)

    return puntos

# Estrategia elegida por Maria
def maria(puntaje_juan):
   # puntaje_juan corresponde al puntaje obtenido por Juan
   # La estrategia de maria es ganarle a Juan, es decir, si empatan Maria deberia tirar de nuevo los dados.
   
   # Se lanzan los dos dados y se obtiene un puntaje
    dado1=lanzar_dado()
    dado2=lanzar_dado()
    puntos=puntaje(dado1, dado2)
    
    if puntos == 0:
       # Obtuvo 0 puntos, jugar denuevo
        dado1=lanzar_dado()
        dado2=lanzar_dado()
        puntos=puntaje(dado1, dado2)

    elif puntos <= puntaje_juan:
       # Obtuvo menos o el mismo puntaje que Juan, lanzar los dados de nuevo
       # Tira de nuevo el dado que no obtuvo 4 o cualquiera de los dos si obtuvo en ambos 4
        if dado2 != 4:
           # El segundo dado es distinto a 4, tirarlo denuevo
           dado2=lanzar_dado()
        else:
           # El primer dado es distinto a 4 o ambos son igual a 4, tirar dado1 denuevo
            dado1=lanzar_dado()
        puntos=puntaje(dado1, dado2)

    return puntos

# Funcion para correr el juego una vez
def jugar(imprimir):
    
   # imprimir corresponde a si se quiere ver los resultados. Toma valor de True o False
   # devuelve -1 si gana Juan, 0 si empatan y 1 si gana Maria

   puntaje_juan=juan()
   puntaje_maria=maria(puntaje_juan)

   if puntaje_juan == puntaje_maria:
      # Juan y Maria empatan
      if imprimir:
         print(f"Empataron. Puntaje Juan: {puntaje_juan} , Puntaje Maria: {puntaje_maria}")
      return 0
   elif puntaje_juan > puntaje_maria:
      # Juan obtiene mayor puntaje que Maria. Juan gana.
      if imprimir:
         print(f"Juan Gano. Puntaje Juan: {puntaje_juan} , Puntaje Maria: {puntaje_maria}")
      return -1
   else:
      # Maria obtiene mayor puntaje que Juan. Maria gana.
      if imprimir:
         print(f"Maria Gano. Puntaje Juan: {puntaje_juan} , Puntaje Maria: {puntaje_maria}")
      return 1

def repetir_juego(cantidad, imprimir):
   # cantidad corresponde a las veces que se repite el juego
   # imprimir corresponde a si se quiere que se impriman los resultados de los juegos individuales

    # Contadores para el conteo de victorias de cada uno, y los empates
    juan=0
    maria=0
    empate=0

    for i in range(0, cantidad):
        res = jugar(imprimir)

        if res == -1:
            # Gano Juan
            juan+=1    
        elif res == 1:
            # Gano Maria
            maria+=1
        else:
           # Empataron
           empate+=1
    
    print(f"En {cantidad} juegos: Juan gana {juan} veces, Maria gana {maria} veces y empatan {empate} veces.")

# Correr el juego 1000 veces
repetir_juego(1000, False)

# Correr el juego 10.000 veces
repetir_juego(10000, False)

# Correr el juego 100.000 veces
repetir_juego(100000, False)


