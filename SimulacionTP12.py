import random
from tkinter import ROUND

# VARIABLES DE CONTROL
PORCENTAJE_TIERRA_ZANAHORIA = .4
PORCENTAJE_TIERRA_ESPINACA = .4
PORCENTAJE_TIERRA_MORRON = .2
M2 = 100000
# una hectarea son 10.000 m2, max 150.000m2

# VARIABLE DE ESTADO
BENEFICIO = 0
GASTO = 0

# VARIABLES GENERALES
PRECIO_KILO_ZANAHORIA = 104
PRECIO_KILO_ESPINACA = 440
PRECIO_KILO_MORRON = 360
PRECIO_M2_FERTILIZANTE_ZANAHORIA = 600
PRECIO_M2_FERTILIZANTE_ESPINACA = 600
PRECIO_M2_FERTILIZANTE_MORRON = 600
PRECIO_M2_INSECTICIDA_ZANAHORIA = 500
PRECIO_M2_INSECTICIDA_ESPINACA = 500
PRECIO_M2_INSECTICIDA_MORRON = 500
PRECIO_M2_SEMILLAS_ZANAHORIA = 5
PRECIO_M2_SEMILLAS_ESPINACA = 5
PRECIO_M2_SEMILLAS_MORRON = 5
CANTIDAD_ZANAHORIAS_X_M2 = 144
CANTIDAD_ESPINACAS_X_M2 = 90
CANTIDAD_MORRONES_X_M2 = 6

# por hectarea con 50mm de agua (simula lluvia)
PRECIO_X_HECTAREA_DE_RIEGO_DIARIO = 36270
GASTOS_POR_MAQUINA_POR_HECTAREA = 15000

# CONDICIONES INICIALES
TIEMPO = 0
TIEMPO_FINAL = 5

def cantidad_de_morrones_por_planta() :
    return random.randint(3,15)

def fdp_kilos_zanahoria() :
    return random.uniform(0.1,0.25)

def fdp_kilos_espinaca() :
    return random.uniform(0.02,0.05)

def fdp_kilos_morron() :
    return random.uniform(0.15,0.50)

def contratar_cosechadora(metros) :
    global GASTO 
    GASTO += (metros / 10000) * GASTOS_POR_MAQUINA_POR_HECTAREA

def tasa_de_exito_zanahoria() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.9,1.0) 
    elif(t==1) :
        return random.uniform(0.55,0.75)
    elif(t==2) :
        return random.uniform(0.3,0.7)
    elif(t==3) :
        return random.uniform(0.66,1.0)

def tasa_de_exito_espinaca() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.9,1.0)
    elif(t==1) :
        return random.uniform(0.55,0.75)
    elif(t==2) :
        return random.uniform(0.3,0.7)
    elif(t==3) :
        return random.uniform(0.66,1.0)

def tasa_de_exito_morron() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.9,1.0)
    elif(t==1) :
        return random.uniform(0.5,0.7)
    elif(t==2) :
        return random.uniform(0.0,0.15)
    elif(t==3) :
        return random.uniform(0.66,1.0)

def cantidad_de_morrones_por_planta() :
    return random.randint(3,15)

# devuelven la cantidad de veces que se tuvo que fertilizar
def fdp_fertilizante_zanahoria() :
    return 5

def fdp_fertilizante_espinaca() :
    return 5

def fdp_fertilizante_morron() :
    return 5

def fdp_insecticida_zanahoria() :
    return 5

def fdp_insecticida_espinaca() :
    return 5

def fdp_insecticida_morron() :
    return 5

###################################################### ZANAHORIA ########################################################
DIA_PROXIMA_COSECHA_ZANAHORIA = 0
ZANAHORIAS_CRECIENDO = False
PORCENTAJE_ZANAHORIAS_VIVAS = 0
PROXIMO_RIEGO_ZANAHORIA = 0

def cosecha_zanahoria() :
    i = 0
    global DIA_PROXIMA_COSECHA_ZANAHORIA

    while(i < 90):
        if(ZANAHORIAS_CRECIENDO == False or PORCENTAJE_ZANAHORIAS_VIVAS < 0.65) :
            plantar_zanahoria(i)
        
        if(i == DIA_PROXIMA_COSECHA_ZANAHORIA) :
            cosechar_zanahoria()
            plantar_zanahoria(i)

        if(ZANAHORIAS_CRECIENDO == True and PORCENTAJE_ZANAHORIAS_VIVAS > 0.65) :
            gastos_por_riego(M2 * PORCENTAJE_TIERRA_ZANAHORIA, i, "Z")
        
        i+=1

def plantar_zanahoria(i) :
    global DIA_PROXIMA_COSECHA_ZANAHORIA, GASTO, ZANAHORIAS_CRECIENDO, PORCENTAJE_ZANAHORIAS_VIVAS
    tasa_exito = tasa_de_exito_zanahoria()
    if(tasa_exito > 0.65) :
        DIA_PROXIMA_COSECHA_ZANAHORIA = 89 - i
        ZANAHORIAS_CRECIENDO = True
        PORCENTAJE_ZANAHORIAS_VIVAS = tasa_exito
        GASTO += PRECIO_M2_SEMILLAS_ZANAHORIA * M2 * PORCENTAJE_TIERRA_ZANAHORIA
    else :
        ZANAHORIAS_CRECIENDO = False
        DIA_PROXIMA_COSECHA_ZANAHORIA = 9999

def cosechar_zanahoria() :
    global BENEFICIO
    hectareas = round(M2 * PORCENTAJE_TIERRA_ZANAHORIA * PORCENTAJE_ZANAHORIAS_VIVAS / 10000)
    cosecha = 0
    i = 0
    while (i < hectareas) :
        cosecha += fdp_kilos_zanahoria() * CANTIDAD_ZANAHORIAS_X_M2 * 10000
        i+=1
    contratar_cosechadora(M2 * PORCENTAJE_TIERRA_ZANAHORIA / 10000)
    BENEFICIO += cosecha * PRECIO_KILO_ZANAHORIA 

###################################################### ESPINACA ########################################################
DIA_PROXIMA_COSECHA_ESPINACA = 0
ESPINACAS_CRECIENDO = False
PORCENTAJE_ESPINACAS_VIVAS = 0
PROXIMO_RIEGO_ESPINACA = 0

def cosecha_espinaca() :
    i = 0
    global DIA_PROXIMA_COSECHA_ESPINACA

    while(i < 90):
        if(ESPINACAS_CRECIENDO == False or PORCENTAJE_ESPINACAS_VIVAS < 0.65) :
            plantar_espinaca(i)
        
        if(i == DIA_PROXIMA_COSECHA_ESPINACA) :
            cosechar_espinaca()
            plantar_espinaca(i)

        if(ESPINACAS_CRECIENDO == True and PORCENTAJE_ESPINACAS_VIVAS > 0.65) :
            gastos_por_riego(M2 * PORCENTAJE_TIERRA_ESPINACA, i, "E")
        
        i+=1

def plantar_espinaca(i) :
    global DIA_PROXIMA_COSECHA_ESPINACA, GASTO, ESPINACAS_CRECIENDO, PORCENTAJE_ESPINACAS_VIVAS
    tasa_exito = tasa_de_exito_espinaca()
    if(tasa_exito > 0.65) :

        if(i + 50 > 90) :
            DIA_PROXIMA_COSECHA_ESPINACA = i + 50 - 90
        else:
            DIA_PROXIMA_COSECHA_ESPINACA += 50

        ESPINACAS_CRECIENDO = True
        PORCENTAJE_ESPINACAS_VIVAS = tasa_exito
        GASTO += PRECIO_M2_SEMILLAS_ESPINACA * M2 * PORCENTAJE_TIERRA_ESPINACA
    else :
        ESPINACAS_CRECIENDO = False
        DIA_PROXIMA_COSECHA_ESPINACA = 9999

def cosechar_espinaca() :
    global BENEFICIO
    hectareas = round(M2 * PORCENTAJE_TIERRA_ESPINACA * PORCENTAJE_ESPINACAS_VIVAS / 10000)
    cosecha = 0
    i = 0
    while (i < hectareas) :
        cosecha += fdp_kilos_espinaca() * CANTIDAD_ESPINACAS_X_M2 * 10000
        i+=1
    contratar_cosechadora(M2 * PORCENTAJE_TIERRA_ESPINACA / 10000)
    BENEFICIO += cosecha * PRECIO_KILO_ESPINACA

###################################################### MORRON ########################################################

DIA_PROXIMA_COSECHA_MORRON = 0
MORRONES_CRECIENDO = False
PORCENTAJE_MORRONES_VIVOS = 0
PROXIMO_RIEGO_MORRON = 0

def cosecha_morron() :
    i = 0
    global DIA_PROXIMA_COSECHA_MORRON

    while(i < 90):
        if(MORRONES_CRECIENDO == False or PORCENTAJE_MORRONES_VIVOS < 0.65) :
            plantar_morron(i)
        
        if(i == DIA_PROXIMA_COSECHA_MORRON) :
            cosechar_morron()
            plantar_morron(i)

        if(MORRONES_CRECIENDO == True and PORCENTAJE_MORRONES_VIVOS > 0.65) :
            gastos_por_riego(M2 * PORCENTAJE_TIERRA_MORRON, i, "M")
        
        i+=1

def plantar_morron(i) :
    global DIA_PROXIMA_COSECHA_MORRON, GASTO, MORRONES_CRECIENDO, PORCENTAJE_MORRONES_VIVOS
    tasa_exito = tasa_de_exito_morron()
    if(tasa_exito > 0.65) :
        DIA_PROXIMA_COSECHA_MORRON = i + 140 - 90 # i muy grande se pasa de trimestre
        MORRONES_CRECIENDO = True
        PORCENTAJE_MORRONES_VIVOS = tasa_exito
        GASTO += PRECIO_M2_SEMILLAS_MORRON * M2 * PORCENTAJE_TIERRA_MORRON
    else :
        MORRONES_CRECIENDO = False
        DIA_PROXIMA_COSECHA_MORRON = 9999

def cosechar_morron() :
    global BENEFICIO
    hectareas = round(M2 * PORCENTAJE_TIERRA_MORRON * PORCENTAJE_MORRONES_VIVOS / 10000)
    cosecha = 0
    i = 0
    while (i < hectareas) :
        cosecha += fdp_kilos_morron() * CANTIDAD_MORRONES_X_M2 * 10000
        i+=1
    contratar_cosechadora(M2 * PORCENTAJE_TIERRA_MORRON / 10000)
    BENEFICIO += cosecha * PRECIO_KILO_MORRON

########################################### RIEGO, LLUVIAS Y GRANIZO ############################################

def gastos_por_riego(m2_tipo_cultivo, hoy, tipo_cultivo) :

    global GASTO
    proximo_riego = asignar(tipo_cultivo)

    if(LLUVIAS_Y_GRANIZO[hoy] == 1) :
        iterar_dia_de_riego(tipo_cultivo)
    
    if(LLUVIAS_Y_GRANIZO[hoy] > 1) :
        afectar_plantaciones_por_granizo(tipo_cultivo, hoy)
        
    if(hoy == proximo_riego) :
        iterar_dia_de_riego(tipo_cultivo)
        GASTO += PRECIO_X_HECTAREA_DE_RIEGO_DIARIO * m2_tipo_cultivo / 10000

def asignar(tipo_cultivo) :
    if(tipo_cultivo == "Z") :
        return PROXIMO_RIEGO_ZANAHORIA
    elif(tipo_cultivo == "E") :
        return PROXIMO_RIEGO_ESPINACA
    elif(tipo_cultivo == "M") :
        return PROXIMO_RIEGO_MORRON

def iterar_dia_de_riego(tipo_cultivo) :
    global PROXIMO_RIEGO_ZANAHORIA, PROXIMO_RIEGO_ESPINACA, PROXIMO_RIEGO_MORRON
    if(tipo_cultivo == "Z") :
        PROXIMO_RIEGO_ZANAHORIA += 3
    elif(tipo_cultivo == "E") :
        PROXIMO_RIEGO_ESPINACA += 3
    elif(tipo_cultivo == "M") :
        PROXIMO_RIEGO_MORRON += 3

def afectar_plantaciones_por_granizo(tipo_cultivo, hoy) :
    global PORCENTAJE_ZANAHORIAS_VIVAS, PORCENTAJE_ESPINACAS_VIVAS, PORCENTAJE_MORRONES_VIVOS
    if(tipo_cultivo == "Z") :
        PORCENTAJE_ZANAHORIAS_VIVAS -= PORCENTAJE_ZANAHORIAS_VIVAS * (LLUVIAS_Y_GRANIZO[hoy] - 1)
    elif(tipo_cultivo == "E") :
        PORCENTAJE_ESPINACAS_VIVAS -= PORCENTAJE_ESPINACAS_VIVAS * (LLUVIAS_Y_GRANIZO[hoy] - 1)
    elif(tipo_cultivo == "M") :
        PORCENTAJE_MORRONES_VIVOS -= PORCENTAJE_MORRONES_VIVOS * (LLUVIAS_Y_GRANIZO[hoy] - 1)
    
LLUVIAS_Y_GRANIZO = [0] * 90

def generador_de_lluvias() :
    i = 0
    global LLUVIAS_Y_GRANIZO

    while(i < 90) :
        if (random.random() < probabilidad_lluvia()) :
            LLUVIAS_Y_GRANIZO[i] = 1
            
            if(random.random() < 0.01) :
                LLUVIAS_Y_GRANIZO[i] = 1 + porcentaje_plantas_muertas_granizo()
        i += 1

def porcentaje_plantas_muertas_granizo() :
    return random.random()

def probabilidad_lluvia() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.0,0.35)
    elif(t==1) :
        return random.uniform(0.0,0.24)
    elif(t==2) :
        return random.uniform(0.0,0.17)
    elif(t==3) :
        return random.uniform(0.0,0.29)


########################################### PROGRAMA PRINCIPAL ############################################

while TIEMPO < TIEMPO_FINAL :

    generador_de_lluvias()

    cosecha_zanahoria() 
    cosecha_espinaca()
    cosecha_morron() 

    # + fdp_fertilizante_zanahoria() * PRECIO_M2_FERTILIZANTE_ZANAHORIA
    # + fdp_fertilizante_espinaca() * PRECIO_M2_FERTILIZANTE_ESPINACA
    # + fdp_fertilizante_morron() * PRECIO_M2_FERTILIZANTE_MORRON
    # + fdp_insecticida_zanahoria() * PRECIO_M2_INSECTICIDA_ZANAHORIA
    # + fdp_insecticida_espinaca() * PRECIO_M2_INSECTICIDA_ESPINACA
    # + fdp_insecticida_morron() * PRECIO_M2_INSECTICIDA_MORRON) * M2) 
    
    TIEMPO += 1

print("############## BENEFICIO       :", BENEFICIO)
print("############## GASTO           :", GASTO)
print("############## BENEFICIO ANUAL :", round(BENEFICIO/TIEMPO*4))
print("############## GASTO ANUAL     :", (GASTO/TIEMPO)*4)
print("############## NETO ANUAL      :", round((BENEFICIO-GASTO)/TIEMPO*4))
print("Promedio de costo de funcionamiento anual:", GASTO/TIEMPO*4)
print("Beneficio total promedio anual:", (BENEFICIO-GASTO)/TIEMPO*4)
print("Menor ganancia obtenida en un trimestre y su temporada", )
