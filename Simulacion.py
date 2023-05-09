import random

# VARIABLES DE CONTROL
CANTIDAD_DE_TAREAS_ASIGNABLES = 15
CANTIDAD_DE_TESTERS = 4

# VARIABLES DE ESTADO
BP = 0
MP = 0 
AP = 0

# CONDICIONES INICIALES
TIEMPO = 0
TIEMPO_FINAL = 500000
HV = 2147483646
TPLL = 0
TPS = [HV] * CANTIDAD_DE_TESTERS
TOCIO = [] 
SUMATORIA_TPLL = 0
SUMATORIA_TPS = [0] * CANTIDAD_DE_TESTERS
SUMATORIA_TIEMPO_OSCIOSO = [0] * CANTIDAD_DE_TESTERS
INICIO_TIEMPO_OSCIOSO = [0] * CANTIDAD_DE_TESTERS
VECTOR_PRIORIDADES = [0] * CANTIDAD_DE_TESTERS
ARREPENTIDOS = 0 
CONTADOR_DE_TAREAS = 0
CONTADOR_DE_TAREAS_TOTALES = 0

PUESTO = [0] * CANTIDAD_DE_TESTERS 
DIAST = [0] * CANTIDAD_DE_TESTERS

def generarIATA() :
    R = random.random()
    if(R < 0.3826) :
        return 0
    elif(R < 0.8545) :
        return 1
    else :
        return 2

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

def generarTAAP() :
    R = random.random()
    if(R < 0.001) :
        return 1
    elif(R < 0.0102) :
        return 2
    elif(R < 0.0596) :
        return 3
    elif(R < 0.2181) :
        return 4
    elif(R < 0.5234) :
        return 5
    elif(R < 0.8501) :
        return 6
    else :
        return 7

def generarTAMP() :
    R = random.random()
    if(R < 0.0055) :
        return 1
    elif(R < 0.0505) :
        return 2
    elif(R < 0.2424) :
        return 3
    elif(R < 0.6513) :
        return 4
    else :
        return 5

def generarTABP() :
    R = random.random()
    if(R < 0.87) :
        return 1
    else :
        return 2
           
def buscarMenorTPS() :
    minimo_TPS = min(TPS)
    posicion_minimo_TPS = TPS.index(minimo_TPS)
    return posicion_minimo_TPS
    
def buscarHV() :
    posicion_TPS_HV = TPS.index(HV)
    return posicion_TPS_HV

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

def salida(menorTPS) :
    global AP,MP,BP, PUESTO, P2
    TIEMPO = TPS[menorTPS]
    SUMATORIA_TPS[menorTPS] += TPS[menorTPS]

    if VECTOR_PRIORIDADES[menorTPS] == "AP" :
        AP -=1
    elif VECTOR_PRIORIDADES[menorTPS] == "MP" :
        MP -=1
    elif VECTOR_PRIORIDADES[menorTPS] == "BP" :
        BP -=1
            
    if AP+MP+BP>= CANTIDAD_DE_TESTERS :
        if AP > 0 and AP > VECTOR_PRIORIDADES.count("AP"):
            VECTOR_PRIORIDADES[menorTPS] = "AP"
            DIAS = generarTAAP()
            TPS[menorTPS] = TIEMPO + DIAS
            PUESTO[menorTPS] += 1
            DIAST[menorTPS] += DIAS
        elif MP > 0 and MP > VECTOR_PRIORIDADES.count("MP"):
            VECTOR_PRIORIDADES[menorTPS] = "MP"
            DIAS = generarTAMP()
            TPS[menorTPS] = TIEMPO + DIAS
            PUESTO[menorTPS] += 1
            DIAST[menorTPS] += DIAS
        elif BP > 0 and BP > VECTOR_PRIORIDADES.count("BP"):
            VECTOR_PRIORIDADES[menorTPS] = "BP" 
            DIAS = generarTABP()
            TPS[menorTPS] = TIEMPO + DIAS
            PUESTO[menorTPS] += 1
            DIAST[menorTPS] += DIAS
    else :
        TPS[menorTPS] = HV
        VECTOR_PRIORIDADES[menorTPS] = "0"
        INICIO_TIEMPO_OSCIOSO[menorTPS] = TIEMPO
        
#---------------------------- Programa Principal -------------------------------------------

while TIEMPO < TIEMPO_FINAL :
    menorTPS = buscarMenorTPS()
    if TPLL <= TPS[menorTPS]:
        llegada()
    else :
        salida(menorTPS)

TPLL = HV
while AP+MP+BP>0 :
    menorTPS = buscarMenorTPS()
    if TPLL <= TPS[menorTPS]:
        llegada()
    else :
        salida(menorTPS)

# CALCULO DE RESULTADOS

PTO = [0] * CANTIDAD_DE_TESTERS

for i in range(CANTIDAD_DE_TESTERS):
    if(PUESTO[i] == 0) :
        PTO[i] = 100
    else :
        PTO[i] = round(SUMATORIA_TIEMPO_OSCIOSO[i]*100/TIEMPO)

PPS = round((sum(SUMATORIA_TPS) - SUMATORIA_TPLL)/CONTADOR_DE_TAREAS)

PTA = round(ARREPENTIDOS *100 / CONTADOR_DE_TAREAS_TOTALES)

print("-------------------------------------------------------------------------------------------")
print("Cantidad de tareas: %s" %CANTIDAD_DE_TAREAS_ASIGNABLES)
print("En un lapso de %s días llegaron %s tareas, se rechazaron %s \n" % (TIEMPO_FINAL, CONTADOR_DE_TAREAS, ARREPENTIDOS))

for i in range(CANTIDAD_DE_TESTERS) :
    print("Puesto %s, atendio %s tareas, y trabajo %s dias" %(i ,PUESTO[i], DIAST[i]))

for i in range(CANTIDAD_DE_TESTERS):
    print("Porcentaje de tiempo ocioso del integrante %s por mes es del %s" % (i, PTO[i]))

print("\nPromedio de permanencia en el sistema en dias: %s" %PPS)
print("Porcentaje de tareas asignadas a otros equipos: %s" %PTA)
print("Tiempo: %s" %TIEMPO)
print("-------------------------------------------------------------------------------------------")
