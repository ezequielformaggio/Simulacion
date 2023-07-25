import random
from tkinter import ROUND

# VARIABLES DE CONTROL
PORCENTAJE_TIERRA_ZANAHORIA = 15
PORCENTAJE_TIERRA_ESPINACA = 55
PORCENTAJE_TIERRA_MORRON = 30
M2 = 4

# VARIABLES DE ESTADO
BENEFICIO = 0

# VARIABLES GENERALES
PRECIO_KILO_ZANAHORIA = 0
PRECIO_KILO_ESPINACA = 0
PRECIO_KILO_MORRON = 0
PRECIO_M2_FERTILIZANTE_ZANAHORIA = 0
PRECIO_M2_FERTILIZANTE_ESPINACA = 0
PRECIO_M2_FERTILIZANTE_MORRON = 0
PRECIO_M2_INSECTICIDA_ZANAHORIA = 0
PRECIO_M2_INSECTICIDA_ESPINACA = 0
PRECIO_M2_INSECTICIDA_MORRON = 0
PRECIO_M2_DE_RIEGO_DIARIO = 0
CANTIDAD_ZANAHORIAS_X_M2 = 144
CANTIDAD_ESPINACAS_X_M2 = 90
CANTIDAD_MORRONES_X_M2 = 6
GASTOS_EMPLEADO = 450000
M2_POR_EMPLEADO = 1000
COSECHA_REMANENTE_ZANAHORIA = 0
COSECHA_REMANENTE_ESPINACA = 0
COSECHA_REMANENTE_MORRON = 0

# CONDICIONES INICIALES
TIEMPO = 0
TIEMPO_FINAL = 1000

# LAS DEJE PARA VER LA SINTAXIS DE PHYTON NOMAS #################
def generarIA() :
    R = random.random()
    if(R < 0.0203) :
        return 0
    elif(R < 0.0996) :
        return 1
    elif(R < 0.254) :
        return 2
    elif(R < 0.4544) :
        return 3
    elif(R < 0.6495) :
        return 4
    elif(R < 0.8014) :
        return 5
    elif(R < 0.9) :
        return 6
    elif(R < 0.9549) :
        return 7
    elif(R < 0.9816) :
        return 8
    elif(R < 0.9932) :
        return 9
    elif(R < 0.9977) :
        return 10
    elif(R < 0.9993) :
        return 11
    elif(R < 0.9998) :
        return 12
    else :
        return 13

#################################################################

# devuelve la cantidad de dias que tarda en crecer UNA semilla
def fdp_tiempo_crecimiento_zanahoria() :
    return round(random.randint(55,90))

def fdp_tiempo_crecimiento_espinaca() :
    return round(random.randint(40,50))

def fdp_tiempo_crecimiento_morron() :
    return round(random.randint(98,140))

# devuelven la cantidad de plantas cosechadas en el trimestre actual, hasta aca todo muy lindo pero, hay que tener en cuenta
# que no se cosecha cada trimestre y eso, mas bien habria que tener un vector y ahi se vuelve aspera la cosa

def cosecha_zanahoria() :
    v = 0
    cosecha = 0   
    while (v < M2 * PORCENTAJE_TIERRA_ZANAHORIA * CANTIDAD_ZANAHORIAS_X_M2) :
        if(fdp_tiempo_crecimiento_zanahoria > 90) :
            COSECHA_REMANENTE_ZANAHORIA += fdp_kilos_zanahoria()
        else : 
            cosecha += fdp_kilos_zanahoria()
    cosecha += COSECHA_REMANENTE_ZANAHORIA
    COSECHA_REMANENTE_ZANAHORIA = 0
    return cosecha

def cosecha_espinaca() :
    v = 0
    cosecha = 0
    tiempo_restante_temporada = 0
    tiempo_actual = 0
    
    while (v < M2 * PORCENTAJE_TIERRA_ESPINACA * CANTIDAD_ESPINACAS_X_M2) :
        tc = fdp_tiempo_crecimiento_espinaca()
        
        if(tc > tiempo_restante_temporada) :
            COSECHA_REMANENTE_ESPINACA += fdp_kilos_espinaca()
        else : 
            cosecha += fdp_kilos_espinaca()
        
    cosecha += COSECHA_REMANENTE_ESPINACA
    COSECHA_REMANENTE_ESPINACA = 0
    return cosecha

def cosecha_morron() :
    v = 0
    h = 0
    cosecha = 0
    morrones_totales = 0

    while(v < M2 * PORCENTAJE_TIERRA_MORRON * CANTIDAD_MORRONES_X_M2) :
        morrones_totales += fdp_cantidad_de_morrones_por_planta
        v+=1

    while (morrones_totales) :
        if(fdp_tiempo_crecimiento_morron > 90) :
            COSECHA_REMANENTE_MORRON += fdp_kilos_morron()
        else : 
            cosecha += fdp_kilos_morron() 

    cosecha += COSECHA_REMANENTE_MORRON
    COSECHA_REMANENTE_MORRON = 0
    return cosecha


# cosecha_de_###### devuelve la cantidad de kilos cosechados
def fdp_kilos_zanahoria() :
    return round(random.uniform(0.1,0.25))

def fdp_kilos_espinaca() :
    return round(random.uniform(0.02,0.05))

def fdp_kilos_morron() :
    return round(random.uniform(0.15,0.50))

# devuelve el porcentaje de taza de exito de crecimiento de todas las semillas en un metro cuadrado
def fdp_tasa_de_exito_zanahoria() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.9,1.0)
    elif(t==1) :
        return random.uniform(0.9,1.0)
    elif(t==2) :
        return random.uniform(0.7,1.0)
    elif(t==3) :
        return random.uniform(0.7,1.0)

def fdp_tasa_de_exito_espinaca() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.9,1.0)
    elif(t==1) :
        return random.uniform(0.9,1.0)
    elif(t==2) :
        return random.uniform(0.7,1.0)
    elif(t==3) :
        return random.uniform(0.7,1.0)

def fdp_tasa_de_exito_morron() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.9,1.0)
    elif(t==1) :
        return random.uniform(0.7,1.0)
    elif(t==2) :
        return random.uniform(0.0,0.15)
    elif(t==3) :
        return random.uniform(0.0,0.05)

def fdp_cantidad_de_morrones_por_planta() :
    return random.randint(3,15)
 
# devuelve la cantidad de dias que se tuvo que regar ese trimestre
def fdp_riego() :
    ...

def fdp_lluvias() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.0,0.35)
    elif(t==1) :
        return random.uniform(0.0,0.24)
    elif(t==2) :
        return random.uniform(0.0,0.17)
    elif(t==3) :
        return random.uniform(0.0,0.29)

# devuelve el gasto de empleados segun metros cuadrados
def gasto_por_empleados() :
    return ROUND(M2 / M2_POR_EMPLEADO) * GASTOS_EMPLEADO

# devuelven la cantidad de veces que se tuvo que fertilizar
def fdp_fertilizante_zanahoria() :
    ...

def fdp_fertilizante_espinaca() :
    ...

def fdp_fertilizante_morron() :
    ...

def fdp_insecticida_zanahoria() :
    ...

def fdp_insecticida_espinaca() :
    ...

def fdp_insecticida_morron() :
    ...
    
#---------------------------- Programa Principal -------------------------------------------

while TIEMPO < TIEMPO_FINAL :
    
    BENEFICIO += cosecha_de_zanahoria() * PRECIO_KILO_ZANAHORIA 
    + cosecha_de_espinaca() * PRECIO_KILO_ESPINACA 
    + cosecha_de_morron() * PRECIO_KILO_MORRON

    BENEFICIO -= (fdp_riego * PRECIO_M2_DE_RIEGO_DIARIO 
                  + fdp_fertilizante_zanahoria() * PRECIO_M2_FERTILIZANTE_ZANAHORIA
                  + fdp_fertilizante_espinaca() * PRECIO_M2_FERTILIZANTE_ESPINACA
                  + fdp_fertilizante_morron() * PRECIO_M2_FERTILIZANTE_MORRON
                  + fdp_insecticida_zanahoria() * PRECIO_M2_INSECTICIDA_ZANAHORIA
                  + fdp_insecticida_espinaca() * PRECIO_M2_INSECTICIDA_ESPINACA
                  + fdp_insecticida_morron() * PRECIO_M2_INSECTICIDA_MORRON) * M2 + gasto_por_empleados()

    TIEMPO += TIEMPO

print("Beneficio anual: %d", BENEFICIO/TIEMPO/4)