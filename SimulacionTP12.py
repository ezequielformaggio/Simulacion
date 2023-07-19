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


def llegada() :
    global AP,MP,BP, ARREPENTIDOS, TIEMPO, TPLL, CONTADOR_DE_TAREAS, SUMATORIA_TPLL, SUMATORIA_TIEMPO_OSCIOSO, INICIO_TIEMPO_OSCIOSO, PUESTO, DIAS, CONTADOR_DE_TAREAS_TOTALES
    TIEMPO = TPLL
    SUMATORIA_TPLL += TPLL
    TPLL = TIEMPO + generarIATA()
    CONTADOR_DE_TAREAS_TOTALES += 1

    if BP+MP+AP == CANTIDAD_DE_TAREAS_ASIGNABLES :
        ARREPENTIDOS += 1
        SUMATORIA_TPLL -= TPLL
    else:
        CONTADOR_DE_TAREAS += 1
        R = random.random()
        if R < 0.27 :
            AP += 1
            if BP+MP+AP <= CANTIDAD_DE_TESTERS :
                puestoLibre = buscarHV()
                SUMATORIA_TIEMPO_OSCIOSO[puestoLibre] += (TIEMPO - INICIO_TIEMPO_OSCIOSO[puestoLibre])
                DIAS = generarTAAP()
                TPS[puestoLibre] = TIEMPO + DIAS
                VECTOR_PRIORIDADES[puestoLibre] = "AP"
                DIAST[puestoLibre] += DIAS
                PUESTO[puestoLibre] += 1
        elif R < 0.58 :
            MP += 1
            if BP+MP+AP <= CANTIDAD_DE_TESTERS :
                puestoLibre = buscarHV()
                SUMATORIA_TIEMPO_OSCIOSO[puestoLibre] += (TIEMPO - INICIO_TIEMPO_OSCIOSO[puestoLibre])
                DIAS = generarTAMP()
                TPS[puestoLibre] = TIEMPO + DIAS
                VECTOR_PRIORIDADES[puestoLibre] = "MP"
                DIAST[puestoLibre] += DIAS
                PUESTO[puestoLibre] += 1
        else :
            BP += 1
            if BP+MP+AP <= CANTIDAD_DE_TESTERS :
                puestoLibre = buscarHV()
                SUMATORIA_TIEMPO_OSCIOSO[puestoLibre] += (TIEMPO - INICIO_TIEMPO_OSCIOSO[puestoLibre])
                DIAS = generarTABP()
                TPS[puestoLibre] = TIEMPO + DIAS
                VECTOR_PRIORIDADES[puestoLibre] = "BP"
                DIAST[puestoLibre] += DIAS
                PUESTO[puestoLibre] += 1
#################################################################

# devuelve la cantidad de dias que tarda en crecer UNA semilla
def fdp_tiempo_crecimiento_zanahoria() :
    ...

def fdp_tiempo_crecimiento_espinaca() :
    ...

def fdp_tiempo_crecimiento_morron() :
    ...

# devuelve el porcentaje de taza de exito de un metro cuadrado?
def fdp_tasa_de_exito_zanahoria_verano() :
    ...

def fdp_tasa_de_exito_zanahoria_otonio() :
    ...

def fdp_tasa_de_exito_zanahoria_invierno() :
    ...

def fdp_tasa_de_exito_zanahoria_primavera() :
    ...

def fdp_tasa_de_exito_espinaca_verano() :
    ...

def fdp_tasa_de_exito_espinaca_otonio() :
    ...

def fdp_tasa_de_exito_espinaca_invierno() :
    ...

def fdp_tasa_de_exito_espinaca_primavera() :
    ...

def fdp_tasa_de_exito_morron_verano() :
    ...

def fdp_tasa_de_exito_morron_otonio() :
    ...

def fdp_tasa_de_exito_morron_invierno() :
    ...

def fdp_tasa_de_exito_morron_primavera() :
    ...


# devuelve la cantidad de dias que se tuvo que regar ese trimestre
def fdp_riego() :
    ...

# cosecha_de_###### devuelve la cantidad de kilos cosechados
def cosecha_de_zanahoria() :
    ...

def cosecha_de_espinaca() :
    ...

def cosecha_de_morron() :
    ...

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