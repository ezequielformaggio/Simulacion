import random, math
from tkinter import ROUND

# VARIABLES DE CONTROL
PORCENTAJE_TIERRA_ZANAHORIA = 0
PORCENTAJE_TIERRA_ESPINACA = 0
PORCENTAJE_TIERRA_MORRON = 0
M2 = 150000
# una hectarea son 10.000 m2, max 150.000m2

# VARIABLE DE ESTADO
BENEFICIO = 0
GASTO = 0

# CONDICIONES INICIALES
TIEMPO = 0
TIEMPO_FINAL = 250

def contratar_cosechadora(metros, tipo_cultivo) :
    global GASTO 
    sumar_gasto_cosechadora(tipo_cultivo, metros)
    GASTO += (metros / 10000) * GASTOS_POR_MAQUINA_POR_HECTAREA

def sumar_gasto_cosechadora(tipo_cultivo, metros) :
    global GASTO_ZANAHORIA, GASTO_ESPINACA, GASTO_MORRON
    if(tipo_cultivo == "Z") :
        GASTO_ZANAHORIA += (metros / 10000) * GASTOS_POR_MAQUINA_POR_HECTAREA
    elif(tipo_cultivo == "E") :
        GASTO_ESPINACA += (metros / 10000) * GASTOS_POR_MAQUINA_POR_HECTAREA
    elif(tipo_cultivo == "M") :
        GASTO_MORRON += (metros / 10000) * GASTOS_POR_MAQUINA_POR_HECTAREA

###################################################### ZANAHORIA ########################################################
PRECIO_M2_FERTILIZANTE_ZANAHORIA = 70
PRECIO_M2_INSECTICIDA_ZANAHORIA = 70
DIA_PROXIMA_COSECHA_ZANAHORIA = 0
PRECIO_M2_SEMILLAS_ZANAHORIA = 5
INTERVALO_COSECHA_ZANAHORIA = 89
PORCENTAJE_ZANAHORIAS_VIVAS = 0
T_PROXIMA_COSECHA_ZANAHORIA = 0
CANTIDAD_ZANAHORIAS_X_M2 = 144
PROXIMO_RIEGO_ZANAHORIA = 0
PRECIO_KILO_ZANAHORIA = 104
BENEFICIO_ZANAHORIA = 0
GASTO_ZANAHORIA = 0
ZANAHORIAS_CRECIENDO = False

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
    global DIA_PROXIMA_COSECHA_ZANAHORIA, GASTO, ZANAHORIAS_CRECIENDO, PORCENTAJE_ZANAHORIAS_VIVAS, T_PROXIMA_COSECHA_ZANAHORIA, GASTO_ZANAHORIA
    tasa_exito = tasa_de_exito_zanahoria()
    if(tasa_exito > 0.65) :
        T_PROXIMA_COSECHA_ZANAHORIA = math.trunc(i + INTERVALO_COSECHA_ZANAHORIA/90)
        DIA_PROXIMA_COSECHA_ZANAHORIA = (i + INTERVALO_COSECHA_ZANAHORIA) % 90 
        ZANAHORIAS_CRECIENDO = True
        PORCENTAJE_ZANAHORIAS_VIVAS = tasa_exito
        GASTO += PRECIO_M2_SEMILLAS_ZANAHORIA * M2 * PORCENTAJE_TIERRA_ZANAHORIA
        GASTO_ZANAHORIA += PRECIO_M2_SEMILLAS_ZANAHORIA * M2 * PORCENTAJE_TIERRA_ZANAHORIA
    else :
        ZANAHORIAS_CRECIENDO = False
        DIA_PROXIMA_COSECHA_ZANAHORIA = 9999

def cosechar_zanahoria() :
    global BENEFICIO, BENEFICIO_ZANAHORIA
    hectareas = round(M2 * PORCENTAJE_TIERRA_ZANAHORIA * PORCENTAJE_ZANAHORIAS_VIVAS / 10000)
    cosecha = 0
    i = 0
    while (i < hectareas) :
        cosecha += fdp_kilos_zanahoria() * CANTIDAD_ZANAHORIAS_X_M2 * 10000
        i+=1
    contratar_cosechadora(M2 * PORCENTAJE_TIERRA_ZANAHORIA / 10000, "Z")
    BENEFICIO += cosecha * PRECIO_KILO_ZANAHORIA 
    BENEFICIO_ZANAHORIA += cosecha * PRECIO_KILO_ZANAHORIA 

def fdp_kilos_zanahoria() :
    return random.uniform(0.1,0.25)

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

def fdp_fertilizante_zanahoria() :
    return 5

def fdp_insecticida_zanahoria() :
    return 5

###################################################### ESPINACA ########################################################
PRECIO_M2_FERTILIZANTE_ESPINACA = 70
PRECIO_M2_INSECTICIDA_ESPINACA = 70
DIA_PROXIMA_COSECHA_ESPINACA = 0
PRECIO_M2_SEMILLAS_ESPINACA = 5
INTERVALO_COSECHA_ESPINACA = 50
PORCENTAJE_ESPINACAS_VIVAS = 0
T_PROXIMA_COSECHA_ESPINACA = 0
CANTIDAD_ESPINACAS_X_M2 = 90
PROXIMO_RIEGO_ESPINACA = 0
PRECIO_KILO_ESPINACA = 440
BENEFICIO_ESPINACA = 0
GASTO_ESPINACA = 0
ESPINACAS_CRECIENDO = False

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
    global DIA_PROXIMA_COSECHA_ESPINACA, GASTO, ESPINACAS_CRECIENDO, PORCENTAJE_ESPINACAS_VIVAS, T_PROXIMA_COSECHA_ESPINACA, GASTO_ESPINACA 
    tasa_exito = tasa_de_exito_espinaca()
    if(tasa_exito > 0.65) :
        T_PROXIMA_COSECHA_ESPINACA = math.trunc(i + INTERVALO_COSECHA_ESPINACA/90)
        DIA_PROXIMA_COSECHA_ESPINACA = (i + INTERVALO_COSECHA_ESPINACA) % 90 
        ESPINACAS_CRECIENDO = True
        PORCENTAJE_ESPINACAS_VIVAS = tasa_exito
        GASTO += PRECIO_M2_SEMILLAS_ESPINACA * M2 * PORCENTAJE_TIERRA_ESPINACA
        GASTO_ESPINACA += PRECIO_M2_SEMILLAS_ESPINACA * M2 * PORCENTAJE_TIERRA_ESPINACA
    else :
        ESPINACAS_CRECIENDO = False
        DIA_PROXIMA_COSECHA_ESPINACA = 9999

def cosechar_espinaca() :
    global BENEFICIO, BENEFICIO_ESPINACA
    hectareas = round(M2 * PORCENTAJE_TIERRA_ESPINACA * PORCENTAJE_ESPINACAS_VIVAS / 10000)
    cosecha = 0
    i = 0
    while (i < hectareas) :
        cosecha += fdp_kilos_espinaca() * CANTIDAD_ESPINACAS_X_M2 * 10000
        i+=1
    contratar_cosechadora(M2 * PORCENTAJE_TIERRA_ESPINACA / 10000, "E")
    BENEFICIO += cosecha * PRECIO_KILO_ESPINACA
    BENEFICIO_ESPINACA += cosecha * PRECIO_KILO_ESPINACA
    
def fdp_kilos_espinaca() :
    return random.uniform(0.02,0.05)

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

def fdp_fertilizante_espinaca() :
    return 5

def fdp_insecticida_espinaca() :
    return 5

###################################################### MORRON ########################################################
PRECIO_M2_FERTILIZANTE_MORRON = 70
PRECIO_M2_INSECTICIDA_MORRON = 70
INTERVALO_COSECHA_MORRON = 140
DIA_PROXIMA_COSECHA_MORRON = 0
PRECIO_M2_SEMILLAS_MORRON = 5
PORCENTAJE_MORRONES_VIVOS = 0
T_PROXIMA_COSECHA_MORRON = 0
CANTIDAD_MORRONES_X_M2 = 6
PRECIO_KILO_MORRON = 360
PROXIMO_RIEGO_MORRON = 0
BENEFICIO_MORRON = 0
GASTO_MORRON = 0
MORRONES_CRECIENDO = False

def cosecha_morron() :
    i = 0
    global T_PROXIMA_COSECHA_MORRON, GASTO, BENEFICIO_MORRON

    while(i < 90):
        if(MORRONES_CRECIENDO == False or PORCENTAJE_MORRONES_VIVOS < 0.65) :
            plantar_morron(i)
        
        if(i == DIA_PROXIMA_COSECHA_MORRON and TIEMPO == T_PROXIMA_COSECHA_MORRON) :
            cosechar_morron()
            plantar_morron(i)

        if(MORRONES_CRECIENDO == True and PORCENTAJE_MORRONES_VIVOS > 0.65) :
            gastos_por_riego(M2 * PORCENTAJE_TIERRA_MORRON, i, "M")
        
        i+=1

def plantar_morron(i) :
    global DIA_PROXIMA_COSECHA_MORRON, GASTO, MORRONES_CRECIENDO, PORCENTAJE_MORRONES_VIVOS, T_PROXIMA_COSECHA_MORRON, GASTO_MORRON
    tasa_exito = tasa_de_exito_morron()
    if(tasa_exito > 0.65) :
        T_PROXIMA_COSECHA_MORRON = math.trunc(i + INTERVALO_COSECHA_MORRON/90)
        DIA_PROXIMA_COSECHA_MORRON = (i + INTERVALO_COSECHA_MORRON) % 90 
        MORRONES_CRECIENDO = True
        PORCENTAJE_MORRONES_VIVOS = tasa_exito
        GASTO += PRECIO_M2_SEMILLAS_MORRON * M2 * PORCENTAJE_TIERRA_MORRON
        GASTO_MORRON += PRECIO_M2_SEMILLAS_MORRON * M2 * PORCENTAJE_TIERRA_MORRON
    else :
        MORRONES_CRECIENDO = False
        T_PROXIMA_COSECHA_MORRON = 9999
        DIA_PROXIMA_COSECHA_MORRON = 9999

def cosechar_morron() :
    global BENEFICIO, BENEFICIO_MORRON
    hectareas = round(M2 * PORCENTAJE_TIERRA_MORRON * PORCENTAJE_MORRONES_VIVOS / 10000)
    cosecha = 0
    i = 0
    while (i < hectareas) :
        cosecha += fdp_kilos_morron() * CANTIDAD_MORRONES_X_M2 * 10000
        i+=1
    contratar_cosechadora(M2 * PORCENTAJE_TIERRA_MORRON / 10000, "M")
    BENEFICIO += cosecha * PRECIO_KILO_MORRON
    BENEFICIO_MORRON += cosecha * PRECIO_KILO_MORRON

def fdp_kilos_morron() :
    return random.uniform(0.15,0.50)

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

def fdp_fertilizante_morron() :
    return 5

def fdp_insecticida_morron() :
    return 5

########################################### RIEGO, LLUVIAS Y GRANIZO ############################################

# por hectarea con 50mm de agua (simula lluvia)
PRECIO_X_HECTAREA_DE_RIEGO_DIARIO = 36270
GASTOS_POR_MAQUINA_POR_HECTAREA = 15000

def gastos_por_riego(m2_tipo_cultivo, hoy, tipo_cultivo) :

    global GASTO
    proximo_riego = asignar(tipo_cultivo)

    if(LLUVIAS_Y_GRANIZO[hoy] == 1) :
        iterar_dia_de_riego(tipo_cultivo)
    
    if(LLUVIAS_Y_GRANIZO[hoy] > 1) :
        afectar_plantaciones_por_granizo(tipo_cultivo, hoy)
        
    if(hoy == proximo_riego) :
        iterar_dia_de_riego(tipo_cultivo)
        sumar_gasto_riego(tipo_cultivo, m2_tipo_cultivo)
        GASTO += PRECIO_X_HECTAREA_DE_RIEGO_DIARIO * m2_tipo_cultivo / 10000

def sumar_gasto_riego(tipo_cultivo, m2_tipo_cultivo) :
    global GASTO_ZANAHORIA, GASTO_ESPINACA, GASTO_MORRON
    if(tipo_cultivo == "Z") :
        GASTO_ZANAHORIA += PRECIO_X_HECTAREA_DE_RIEGO_DIARIO * m2_tipo_cultivo / 10000
    elif(tipo_cultivo == "E") :
        GASTO_ESPINACA += PRECIO_X_HECTAREA_DE_RIEGO_DIARIO * m2_tipo_cultivo / 10000
    elif(tipo_cultivo == "M") :
        GASTO_MORRON += PRECIO_X_HECTAREA_DE_RIEGO_DIARIO * m2_tipo_cultivo / 10000
    
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
    
def generador_de_lluvias() :
    i = 0
    global LLUVIAS_Y_GRANIZO, CONTADOR_DE_GRANIZO

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
LLUVIAS_Y_GRANIZO = [0] * 90
MAYOR_GANANCIA = [0,0]
MENOR_GANANCIA = [9999999999999999999999999,0]
ESCENARIO = 0

def temporada(numero) :
    if(numero % 4 == 0) :
        return "verano"
    elif(numero % 4 == 1) :
        return "otoño"
    elif(numero % 4 == 2) :
        return "invierno"
    elif(numero % 4 == 3) :
        return "primavera"
    
def resetear_escenario() :
    global BENEFICIO, BENEFICIO_ZANAHORIA, BENEFICIO_ESPINACA, BENEFICIO_MORRON, TIEMPO
    global GASTO, GASTO_ZANAHORIA, GASTO_ESPINACA, GASTO_MORRON
    global MAYOR_GANANCIA, MENOR_GANANCIA
    TIEMPO = 0
    BENEFICIO = 0
    BENEFICIO_ZANAHORIA = 0
    BENEFICIO_ESPINACA = 0
    BENEFICIO_MORRON = 0
    GASTO = 0
    GASTO_ZANAHORIA = 0
    GASTO_ESPINACA = 0
    GASTO_MORRON = 0
    MAYOR_GANANCIA = [0,0]
    MENOR_GANANCIA = [9999999999999999999999999,0]

def main(z, e, m) :
    global TIEMPO, LLUVIAS_Y_GRANIZO,PORCENTAJE_TIERRA_ZANAHORIA, PORCENTAJE_TIERRA_ESPINACA, PORCENTAJE_TIERRA_MORRON, MAYOR_GANANCIA, MENOR_GANANCIA
    PORCENTAJE_TIERRA_ZANAHORIA = z
    PORCENTAJE_TIERRA_ESPINACA = e
    PORCENTAJE_TIERRA_MORRON = m

    print("ESCENARIO", ESCENARIO+1)
    print("ZANAHORIA: %", round(z*100))
    print("ESPINACA:  %", round(e*100))
    print("MORRON:    %", round(m*100))

    resetear_escenario()

    while TIEMPO < TIEMPO_FINAL :

        LLUVIAS_Y_GRANIZO = [0] * 90
        generador_de_lluvias()

        beneficio_trimestre_anterior = BENEFICIO
        gasto_trimestre_anterior = GASTO

        cosecha_zanahoria() 
        cosecha_espinaca()
        cosecha_morron()

        beneficio_trimestre_actual = BENEFICIO - beneficio_trimestre_anterior
        gasto_trimestre_actual = GASTO - gasto_trimestre_anterior

        if(MAYOR_GANANCIA[0] < (beneficio_trimestre_actual - gasto_trimestre_actual)) :
            MAYOR_GANANCIA[0] = (beneficio_trimestre_actual - gasto_trimestre_actual)
            MAYOR_GANANCIA[1] = TIEMPO

        if(MENOR_GANANCIA[0] > (beneficio_trimestre_actual - gasto_trimestre_actual)) :
            MENOR_GANANCIA[0] = (beneficio_trimestre_actual - gasto_trimestre_actual)
            MENOR_GANANCIA[1] = TIEMPO

        TIEMPO += 1

def escenarios() :
    global ESCENARIO
    i = 0
    while(i < 7) :
        if(i == 0) :
            main(1,0,0)
        elif(i == 1) :
            main(0,1,0)
        elif(i == 2) :
            main(0,0,1)
        elif(i == 3) :
            main(0.33,.33,0.33)
        elif(i == 4) :
            main(0.5,0.5,0)
        elif(i == 5) :
            main(0,0.5,0.5)
        elif(i == 6) :
            main(0.5,0,0.5)

        print("Promedio de costo de funcionamiento anual:..................$", round(GASTO/TIEMPO*4))
        print("Beneficio promedio anual:...................................$", round((BENEFICIO-GASTO)/TIEMPO*4))
        print("Beneficio por venta de zanahoria promedio anual:............$", round((BENEFICIO_ZANAHORIA-GASTO_ZANAHORIA)/TIEMPO*4))
        print("Beneficio por venta de espinaca promedio anual:.............$", round((BENEFICIO_ESPINACA-GASTO_ESPINACA)/TIEMPO*4))
        print("Beneficio por venta de morron promedio anual:...............$", round((BENEFICIO_MORRON-GASTO_MORRON)/TIEMPO*4))
        print("Mayor ganancia obtenida en un trimestre y su temporada:.....$", round(MAYOR_GANANCIA[0]), " ", temporada(MAYOR_GANANCIA[1]))
        print("Menor ganancia obtenida en un trimestre y su temporada:.....$", round(MENOR_GANANCIA[0]), " ", temporada(MENOR_GANANCIA[1]))
        print(" ")
        ESCENARIO += 1
        i += 1

escenarios()