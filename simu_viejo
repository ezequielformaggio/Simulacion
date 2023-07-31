import random
from tkinter import ROUND

# VARIABLES DE CONTROL
PORCENTAJE_TIERRA_ZANAHORIA = 15
PORCENTAJE_TIERRA_ESPINACA = 55
PORCENTAJE_TIERRA_MORRON = 30
M2 = 1000
# una hectarea son 10.000 m2

# VARIABLE DE ESTADO
BENEFICIO = 0
GASTO = 0

# VARIABLES GENERALES
PRECIO_KILO_ZANAHORIA = 15
PRECIO_KILO_ESPINACA = 10
PRECIO_KILO_MORRON = 40
PRECIO_M2_FERTILIZANTE_ZANAHORIA = 600
PRECIO_M2_FERTILIZANTE_ESPINACA = 600
PRECIO_M2_FERTILIZANTE_MORRON = 600
PRECIO_M2_INSECTICIDA_ZANAHORIA = 500
PRECIO_M2_INSECTICIDA_ESPINACA = 500
PRECIO_M2_INSECTICIDA_MORRON = 500
PRECIO_M2_DE_RIEGO_DIARIO = 800
CANTIDAD_ZANAHORIAS_X_M2 = 144
CANTIDAD_ESPINACAS_X_M2 = 90
CANTIDAD_MORRONES_X_M2 = 6
GASTOS_POR_MAQUINA_POR_HECTAREA = 10000
INTERVALO_DE_RIEGO = 2

# CONDICIONES INICIALES
TIEMPO = 1
TIEMPO_FINAL = 10

# devuelven la cantidad de plantas cosechadas en el trimestre actual, hasta aca todo muy lindo pero, hay que tener en cuenta
# que no se cosecha cada trimestre y eso, mas bien habria que tener un vector y ahi se vuelve aspera la cosa

def cosecha_zanahoria() :
    i = 0
    plantas = round(M2 * PORCENTAJE_TIERRA_ZANAHORIA * CANTIDAD_ZANAHORIAS_X_M2 * tasa_de_exito_zanahoria())
    cosecha = 0   
    while (i < plantas) :
        cosecha += fdp_kilos_zanahoria()
        i+=1
    return cosecha

def cosecha_espinaca() :
    i = 0
    intervalo_de_cosecha = 50
    plantas = round(M2 * PORCENTAJE_TIERRA_ESPINACA * CANTIDAD_ESPINACAS_X_M2 * tasa_de_exito_espinaca())
    cosecha = 0
    ultima_cosecha = 0
    
    while ((TIEMPO * 90) > (ultima_cosecha + intervalo_de_cosecha)) :
        while (i < plantas) :
            cosecha += fdp_kilos_espinaca()  
            i+=1      
        ultima_cosecha += intervalo_de_cosecha

    return cosecha

def cosecha_morron() :
    i = 0
    j = 0
    intervalo_de_cosecha = 140
    plantas = round(M2 * PORCENTAJE_TIERRA_MORRON * CANTIDAD_MORRONES_X_M2)
    cosecha = 0
    morrones_totales = 0
    ultima_cosecha = 0

    while(i < plantas) :
        morrones_totales += fdp_cantidad_de_morrones_por_planta()
        i+=1

    while ((TIEMPO * 90) > (ultima_cosecha + intervalo_de_cosecha)) :
        while (j < morrones_totales) :
            cosecha += fdp_kilos_morron()  
            j+=1      
        ultima_cosecha += intervalo_de_cosecha

    return cosecha

def fdp_cantidad_de_morrones_por_planta() :
    return random.randint(3,15)

# cosecha_de_###### devuelve la cantidad de kilos cosechados
def fdp_kilos_zanahoria() :
    return random.uniform(0.1,0.25)

def fdp_kilos_espinaca() :
    return random.uniform(0.02,0.05)

def fdp_kilos_morron() :
    return random.uniform(0.15,0.50)

# devuelve el porcentaje de taza de exito de crecimiento de todas las semillas en un metro cuadrado
def tasa_de_exito_zanahoria() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.9,1.0)
    elif(t==1) :
        return random.uniform(0.9,1.0)
    elif(t==2) :
        return random.uniform(0.7,1.0)
    elif(t==3) :
        return random.uniform(0.7,1.0)

def tasa_de_exito_espinaca() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.9,1.0)
    elif(t==1) :
        return random.uniform(0.9,1.0)
    elif(t==2) :
        return random.uniform(0.7,1.0)
    elif(t==3) :
        return random.uniform(0.7,1.0)

def tasa_de_exito_morron() :
    t = TIEMPO % 4
    if(t==0) :
        return random.uniform(0.9,1.0)
    elif(t==1) :
        return random.uniform(0.7,1.0)
    elif(t==2) :
        return random.uniform(0.0,0.15)
    elif(t==3) :
        return random.uniform(0.0,0.05)

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

def gastos_por_riego() :
    contador = 0
    dias = 0
    j = 0
    llueve = False

    while (dias < 90) :
        while (j < INTERVALO_DE_RIEGO) :
            if(hoy_llueve()) :
                llueve = True
            j+=1
        if(llueve == False) :
            contador += 1
        llueve = False
        j = 0
        dias += INTERVALO_DE_RIEGO
    return dias * PRECIO_M2_DE_RIEGO_DIARIO * M2
            
def hoy_llueve() :
    if (random.random() < probabilidad_lluvia()) :
        return True
    else : 
        return False

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
    
def gasto_por_cosechadora() :
    return 500 * M2
    
#---------------------------- Programa Principal -------------------------------------------

while TIEMPO < TIEMPO_FINAL :
    
    BENEFICIO += round(cosecha_zanahoria() * PRECIO_KILO_ZANAHORIA 
    + cosecha_espinaca() * PRECIO_KILO_ESPINACA 
    + cosecha_morron() * PRECIO_KILO_MORRON)

    GASTO -= ((gastos_por_riego() 
                  + fdp_fertilizante_zanahoria() * PRECIO_M2_FERTILIZANTE_ZANAHORIA
                  + fdp_fertilizante_espinaca() * PRECIO_M2_FERTILIZANTE_ESPINACA
                  + fdp_fertilizante_morron() * PRECIO_M2_FERTILIZANTE_MORRON
                  + fdp_insecticida_zanahoria() * PRECIO_M2_INSECTICIDA_ZANAHORIA
                  + fdp_insecticida_espinaca() * PRECIO_M2_INSECTICIDA_ESPINACA
                  + fdp_insecticida_morron() * PRECIO_M2_INSECTICIDA_MORRON) * M2) 
    + gasto_por_cosechadora()

    TIEMPO += 1

print("Beneficio anual: %d", (BENEFICIO-GASTO)/TIEMPO/4)