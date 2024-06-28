# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:59:11 2024

@author: david
"""

#Se importa el paquete coolprop que se utilizará para calcular propiedades
#termodinámicas
import CoolProp.CoolProp as CP

#Se importa la función quad de la librería scipy.integrate, que permitirá
#calcular integrales definidas
from scipy.integrate import quad

#Se importa el módulo sys que se utilizará para borrar los textos visualizados
#a través de las funciones print()
import sys

#Se importa mp de la librería mpmath, ya que contiene funciones matemáticas que
#serán de utilidad
from mpmath import mp

#A continuación se va a programar una función que será de utilidad en numerosas
#ocasiones a lo largo del código

#Función para convertir caracteres (números o letras) en subíndices
def convertir_a_subindice(texto):
    #Relaciones de los caracteres con sus subíndices Unicode correspondientes
    subindices = {
        '0': '\u2080',
        '1': '\u2081',
        '2': '\u2082',
        '3': '\u2083',
        '4': '\u2084',
        '5': '\u2085',
        '6': '\u2086',
        '7': '\u2087',
        '8': '\u2088',
        '9': '\u2089',
        'e': '\u2091',
        'i': '\u1D62',
        'j': '\u2C7C',
        'm': '\u2098',
        'p': '\u209A',
        'r': '\u1D63',
        's': '\u209B',
        't': '\u209C'
        
    }
    #Se genera una nueva cadena reemplazando cada carácter por su subíndice 
    return ''.join(subindices.get(c, c) for c in texto)
    

#Se guarda el valor de pi en una variable usando mp de mpmath, ya que será 
#necesario en muchas ocasiones a lo largo del código
pi = float(mp.pi)


print("")

print("                               ", end='') #Con este print se centra el
                                                 #siguiente cuando aparezca en
                                                 #la consola

print("Datos de entrada:") #Nota: se visualiza solo el texto "Datos de entrada",
                           #pero bajo esa denominación se solicitarán los datos 
                           #de los próximos dos apartados ("Bases del diseño" y
                           #"Datos de entrada"), pues realmente ambos apartados
                           #solicitan datos de entrada, aunque el de "Bases
                           #del diseño" se haya denominado diferente simplemente
                           #por especificar qué tipo de datos de entrada se 
                           #solicitan en ese apartado
                          
print("")


"1. Bases del diseño"

#Creación de la variable alfa1 poniendo con códigos Unicode el símbolo de 
#alfa y 1 como subíndice
alfa_simbolo = '\u03B1'
alfa1_texto = f"{alfa_simbolo}1"
alfa1_con_subindice = alfa1_texto.replace("1", convertir_a_subindice("1"))

#Definición del símbolo de grados usando Unicode
simbolo_grados = '\u00B0'

#Se guarda en alfa_1_grados el valor introducido por el usuario
alfa_1_grados = float(input(f"·Introduzca el ángulo de la velocidad absoluta a la entrada del rotor ({alfa1_con_subindice}) en ({simbolo_grados}). Tenga en cuenta que en este programa se van a analizar los casos para los que {alfa1_con_subindice}\u22650: "))

#Bucle de mensaje de error por si se introduce un alfa_1<0
while alfa_1_grados < 0:
        print(f"Valor de {alfa1_con_subindice} no válido. Introduce un valor que cumpla {alfa1_con_subindice}\u22650")
        alfa_1_grados = float(input(f"·Introduzca el valor de {alfa1_con_subindice}: "))

print("")

#Creación de la variable beta2 poniendo con códigos Unicode el símbolo de 
#beta y 2 como subíndice
beta_simbolo = '\u03B2'
beta2_texto = f"{beta_simbolo}2"
beta2_con_subindice = beta2_texto.replace("2", convertir_a_subindice("2"))

#Se guarda en beta_2_grados el valor introducido por el usuario
beta_2_grados = float(input(f"·Introduzca el ángulo de la velocidad relativa a la salida del rotor ({beta2_con_subindice}) en ({simbolo_grados}). Tenga en cuenta que en este programa se van a analizar los casos para los que {beta2_con_subindice}>0: "))

#Bucle de mensaje de error por si introduce un beta_2<=0
while beta_2_grados <= 0:
        print(f"Valor de {beta2_con_subindice} no válido. Introduce un valor que cumpla {beta2_con_subindice}>0")
        beta_2_grados = float(input(f"·Introduzca el valor de {beta2_con_subindice}: "))

print("")

#Creación de la variable cm1 poniendo m y 1 como subíndices
cm1_texto = "cm1"
cm1_con_subindice = cm1_texto.replace("m1", convertir_a_subindice("m1"))

#Creación de la variable cm2 poniendo m y 2 como subíndices
cm2_texto = "cm2"
cm2_con_subindice = cm2_texto.replace("m2", convertir_a_subindice("m2"))

print(f"·Se considera que la velocidad meridiana en el rotor se conserva: {cm1_con_subindice}={cm2_con_subindice}")

print("")

#Creación de la variable b2 poniendo 2 como subíndice
b2_texto = "b2"
b2_con_subindice = b2_texto.replace("2", convertir_a_subindice("2"))

#Creación de la variable b3 poniendo 3 como subíndice
b3_texto = "b3"
b3_con_subindice = b3_texto.replace("3", convertir_a_subindice("3"))

print(f"·Se considera que los anchos axiales de entrada y salida del difusor son iguales: {b2_con_subindice}={b3_con_subindice}")

print("")


"2. Datos de entrada"

#Creación de la variable p01 con 0 y 1 como subíndices
p01_texto = "p01"
p01_con_subindice = p01_texto.replace("01", convertir_a_subindice("01"))

#Se guarda en p_01 el valor introducido por el usuario
p_01 = float(input(f"·Introduzca la presión de remanso a la entrada del rotor ({p01_con_subindice}) en (Pa): "))

print("")

# Creación de la variable T01 con 0 y 1 como subíndices
T01_texto = "T01"
T01_con_subindice = T01_texto.replace("01", convertir_a_subindice("01"))

#Se guarda en T_01 el valor introducido por el usuario
T_01 = float(input(f"·Introduzca la temperatura de remanso a la entrada del rotor ({T01_con_subindice}) en (K): "))

print("")

#Creación de la variable cp con p como subíndice
cp_texto = "cp"
cp_con_subindice = cp_texto.replace("p", convertir_a_subindice("p"))

#Se guarda en c_p el valor introducido por el usuario
c_p = float(input(f"·Introduzca el calor específico a presión constante del aire ({cp_con_subindice}) en (J/(kg·K)): "))

print("")

#Creación del símbolo gamma mediante su código Unicode
gamma_simbolo = '\u03B3'

#Se guarda en gamma el valor introducido por el usuario
gamma = float(input(f"·Introduzca el índice adiabático del aire ({gamma_simbolo}): "))

"""
c_p y gamma solo se utilizarán para calcular la constante R del aire (que a
su vez será necesaria para calcular los números de Mach) y para estimar un 
valor inicial del salto isentrópico total a total (Delta_h_stt), cuyo valor 
definitivo será determinado al final a partir de las propiedades termodinámicas
calculadas a lo largo de la secuencia de cálculo. Para calcular dichas propiedades,
en lugar de utilizar ecuaciones que impliqen el uso de c_p y gamma, se utilizará
el paquete coolprop. De esta forma se eliminan los errores que pudieran
cometerse al suponer un valor de c_p y gamma constantes para todo el proceso
que tiene lugar en el compresor.
"""

print("")

#c_v del aire
c_v=c_p/gamma #c_v será necesario para calcular R

#R del aire
R=c_p-c_v #R será necesaria para calcular los números de Mach

#Se guarda en G el valor introducido por el usuario
G = float(input("·Introduzca el gasto másico (G) en (kg/s): "))

print("")

#Se guarda en r el valor introducido por el usuario 
r = float(input("·Introduzca la relación de compresión total a total (r): "))

print("")

#Además, se debe solicitar al usuario el valor del coeficiente de rugosidad del
#material 

#Creación del símbolo epsilon mediante su código Unicode
epsilon_simbolo = '\u03B5'

#Se guarda en epsilon el valor introducido por el usuario 
epsilon = float(input(f"·Introduzca el coeficiente de rugosidad del material del conducto del rotor ({epsilon_simbolo}) en (m): "))

print("")

#También tendrá que ser introducido por el usuario el juego entre rotor y estator
#(epsilon_j)

#Creación de la variable epsilonj con j como subíndice
epsilonj_texto = f"{epsilon_simbolo}j"
epsilonj_con_subindice = epsilonj_texto.replace("j", convertir_a_subindice("j"))

#Se guarda en epsilon_j el valor introducido por el usuario 
epsilon_j = float(input(f"·Introduzca el valor del juego entre rotor y estator ({epsilonj_con_subindice}) en (m): "))

print("")


"""
Por otro lado, para determinar el radio interior de entrada r_1i (lo cual se 
realizará en el bucle de ns (ns es el número específico de revoluciones)), antes
se ha de calcular el diámetro del eje, para lo que, a su vez, se han de determinar:
el esfuerzo de torsión máximo admisible del eje, la potencia y la velocidad angular.
De esos 3 términos, la potencia se calculará antes de entrar en el bucle de ns,
para no calcular el mismo valor en cada iteración. En cuanto al esfuerzo de torsión
máximo admisible del eje, se solicitará al usuario, y la velocidad angular sí se
calculará dentro del bucle ns, ya que depende de ns.
"""

#Creación del símbolo tau mediante su código Unicode
tau_simbolo = '\u03C4'

#Se guarda en tau el valor introducido por el usuario para el esfuerzo de torsión
#máximo admisible del eje
tau = float(input(f"·Introduzca el esfuerzo de torsión máximo admisible del eje ({tau_simbolo}) en (N/m\u00B2): "))

print("")


"""
Cálculo de la potencia:

    Potencia=trabajo_esp*G 

Donde trabajo_esp es el trabajo específico, el cual depende del rendimiento total
a total eta_tt, para el cual se considerará inicialmente un valor intermedio en
práctica de 0.85. 

Ese 0.85 naturalmente no será el valor final, pero no hay problema en suponer
inicialmente ese valor para calcular trabajo_esp, ya que en la bibliografía se
argumenta que se ha de suponer un valor inicial aproximado para eta_tt para 
calcular el trabajo específico, señalando además que si se diera el caso de que
el rendimiento estimado resultase diferente del real, esto no afectaría esencialmente
a las dimensiones del compresor.
"""

#Creación del símbolo eta mediante su código Unicode
eta_simbolo = '\u03B7'

#Creación de la variable etatt con las t como subíndices
eta_tt_texto = f"{eta_simbolo}tt"
eta_tt_con_subindice = eta_tt_texto.replace("tt", convertir_a_subindice("tt"))

#Se asigna al rendimiento un valor intermedio en la práctica de 0.85
eta_tt=0.85

#Para calcular trabajo_esp, antes será necesario calcular el salto isentrópico 
#total y total (Delta_h_stt), el cual se puede estimar a partir de la siguiente
#ecuación
Delta_h_stt=c_p*T_01*(r**((gamma-1)/gamma)-1)

#El trabajo específico se puede poner en función de Deltah_s_tt gracias a la
#definición del rendimiento total a total
trabajo_esp=Delta_h_stt/eta_tt

#Por tanto, la potencia será
Potencia=trabajo_esp*G

"""
El cálculo de la velocidad angular omega (rad/s) se realizará dentro del bucle
de ns a partir de la siguiente ecuación:
    
    omega=2*pi*n

Donde n (rev/s) a su vez está dado por la siguiente ecuación:
    
    n=(ns*(Delta_h_stt**(3/4)))/(2*pi*(Q**(1/2)))
    
Se puede que observar que n depende de ns, razón por la que tiene que calcularse
dentro del bucle de ns; sin embargo, Q puede calcularse antes del bucle, 
para que no se calcule en repetidas ocasiones innecesariamente.

Q es el caudal volumétrico, que se puede calcular a partir de la siguiente 
ecuación:

    Q=G/densidad_01

"""

#Cálculo de densidad_01 (densidad de remanso a la entrada del rotor) con coolprop
fluido = 'Air'  
densidad_01 = CP.PropsSI('D', 'T', T_01, 'P', p_01, fluido)

#Cálculo de Q
Q=G/densidad_01


"""
Por otro lado, a continuación se van a calcular algunos términos que serán 
necesarios más adelante dentro del bucle de ns (al calcularlos antes se evita 
que se calculen reiteradamente dentro del bucle de forma innecesaria)
"""

#Conversión de alfa_1 de grados a radianes
alfa_1_radianes = float(mp.radians(alfa_1_grados))

# Cálculo de tg_alfa_1
tg_alfa_1 = float(mp.tan(alfa_1_radianes))

#Cálculo de cos_alfa_1
cos_alfa_1 = float(mp.cos(alfa_1_radianes))


"""
Por último, antes de comenzar con el bucle de ns, que abarcará hasta el final
de la secuencia de cálculo, se va a visualizar un mensaje de espera para que 
dure mientras se estén realizando iteraciones del bucle ns, de forma que el 
usuario sepa que se están realizando cálculos. Para que dicho mensaje desaparezca
justo cuando acabe el bucle ns, simplemente se tendrá que borrar después del
bucle ns. Por tanto, a continuación se va a visualizar lo siguiente:
"""
print("Calculando... Por favor, espere", end='')

"""
Para borrar el mensaje anterior cuando acabe el bucle ns, habrá que poner al 
final del mismo lo siguiente:
    
sys.stdout.write('\r' + ' ' * len("Calculando... Por favor, espere") + '\r')

Lo que hace ese código es mover el cursor al inicio de la línea, borrarla y
mover el cursor de nuevo al inicio.
"""

########################### INICIO BUCLE ns ###################################

"""
El bucle de ns se extenderá hasta que se muestren los resultados finales, es 
decir, toda la secuencia de cálculo estará dentro de dicho bucle porque 
toda la secuencia tendrá que repetirse si el valor probado de ns provoca que
ciertos parámetros básicos no estén dentro de los márgenes recomendados.
    
En cuanto a los valores que se podrán probar de ns, tendrán que estar dentro del
rango [0.5, 0.8], tomando como primer valor 0.65, el cual es el óptimo, y probando
tras ese valor (si ciertos parámetros básicos no estén dentro de los márgenes 
recomendados) valores por encima y debajo de ese óptimo alternativamente.
"""

#Valor inicial de ns (óptimo)
ns=0.65

"""
Se especifican los siguientes valores iniciales de 4 parámetros que serán de 
utilidad en el bucle de ns:
"""

t=1 #t es una variable que dentro del bucle ns se actualizará a 1 si es necesario
    #realizar otra iteración (lo cual es necesario si ciertos parámetros están
    #fuera de los márgenes recomendados) o a 0 si no es necesario realizar
    #otra iteración. Su valor inicial es 1 básicamente para que se cumpla la 
    #condición del bucle while y este pueda comenzar

paridad_iteracion=0 #Esta variable controlará si el número de la iteración es 
                    #par o impar, de forma que en las iteraciones pares se 
                    #probará un valor de ns por debajo del ns de la anterior
                    #iteración par y en las iteraciones impares se probará un 
                    #valor de ns por encima del ns de la anterior iteración impar

ns_impar=ns #ns_impar será el valor de ns para las iteraciones impares. Su valor
            #inicial es igual al de ns (0.65) porque para asignar un nuevo valor
            #para ns_impar se usa la expresión "ns_impar=ns_impar+0.01"; por 
            #tanto, el primer valor de ns_impar (al que se le suma 0.01) deberá
            #ser 0.65, para que se pruebe 0.66 en la siguiente iteración y se 
            #cumpla lo que se ha comentado de que se pretenden probar valores 
            #por encima y debajo de 0.65 alternativamente, pero partiendo de 0.65

ns_par=ns #ns_par será el valor de ns para las iteraciones pares. Su valor
          #inicial tiene la misma explicación que el de ns_impar, pero en este 
          #caso la asignación del nuevo valor de ns_par será "ns_par=ns_par-0.01",
          #logrando de esta forma que en las iteraciones pares se prueben 
          #valores por debajo de 0.65

"""
Para entender un poco mejor el funcionamiento del bucle ns, se recomienda
consultar la estructura condicional que se encuentra al final del mismo y a 
partir de la cual se asignan los nuevos valores que tomará ns en las sucesivas
iteraciones, en función de la paridad de la iteración. 

Nota: el final del bucle está claramente señalado de igual manera que el comentario 
de inicio que se encuentra antes de la definición de estos valores iniciales.
"""

#Bucle de ns
while ns >= 0.5 and ns <= 0.8 and t==1:
    
    "3. Cálculo del radio interior de entrada r_1i"
    
    #El régimen de giro n (rev/s) está dado por la siguiente ecuación
    n=(ns*(Delta_h_stt**(3/4)))/(2*pi*(Q**(1/2)))

    #La velocidad angular omega (rad/s) será
    omega=2*pi*n
    
    #Cálculo del diámetro del eje
    d_e=((16*Potencia)/(omega*pi*tau))**(1/3)

    #Finalmente ya se puede determinar d_1i y con ello r_1i (m)
    d_1i=d_e+0.025

    r_1i=d_1i/2
    
    "4. Cálculo del ángulo de la velocidad relativa a la entrada del rotor en el radio exterior (beta_1e)"

    """
    En este apartado se va a realizar el cálculo de beta_1e, ya que este será 
    necesario para el bucle 1, que se verá más adelante. Se van a analizar 2 
    casos: entrada axial (alfa_1=0) y en prerrotación (alfa_1>0).                                            
    """

    #Se establece una estructura condicional para determinar beta_1e en cada caso de
    #alfa_1
    if alfa_1_grados == 0:
            beta_1e_grados = 60 #Valor según la bibliografía
            
    elif alfa_1_grados > 0:
        
            """   
            El procedimiento que se va a programar a continuación para el cálculo
            beta_1e para el caso de alfa_1>0 se resume en lo siguiente: se trata
            de encontrar el máximo de una función F que se definirá más adelante
            en el rango 0° <= beta_1e <= 90°; de forma que beta_1e será la abscisa
            de dicho máximo. 
            
            Se comenzará dando un valor al único parámetro de la expresión de F
            que es desconocido hasta el momento: el número de Mach de la velocidad
            relativa en el radio exterior de entrada al rotor (M_w1e). Se le dará
            un valor de 0.9 (podría haberse escogido otro menor que 1, ya que 
            el máximo de F no varía con el valor de M_w1e). Es importante
            recalcar que este valor de 0.9 no será de ninguna manera el final 
            para M_w1e, el cual se calculará más adelante, solo se le da ese valor
            en este momento para calcular beta_1e.
            """
            M_w1e_calculo_beta_1e=0.9
            
            """
            Como lo que se prentende es calcular el máximo de una función F en 
            el rango 0° <= beta_1e <= 90°, a continuación se va a programar
            un bucle que calcule cada 0.1° el valor de F en ese rango de 
            beta_1e, de forma que se vaya guardando el valor de beta_1e al final
            de cada iteración del bucle solo si el valor de F es mayor al 
            calculado en la anterior iteración. De esta forma, al finalizar el 
            bucle se habrá guardado el valor de beta_1e correspondiente al 
            máximo de F.
            """
            #Valor inicial de beta_1e para la 1ª iteración del bucle
            beta_1e_bucle_grados=0
            
            """
            Se inicializa el valor de F_ant_iteracion (F en la anterior iteración 
            del bucle) con un valor tal que el primer valor de F que se calculará 
            en el bucle (para beta_1e=0) sea sí o sí mayor que este valor inicial 
            de F_ant_iteracion, que realmente solo se aporta porque es necesario
            que esta variable tenga un valor inicial fuera del bucle, ya que el
            valor que se le asigna dentro del bucle es una vez se compara su valor
            con el de F calculado en cada iteración. 
            
            Como se ha comprobado que en el rango 0° <= beta_1e <= 90°, F no toma
            valores negativos, el valor inicial que se le dará a F_ant_iteracion
            será precisamente negativo, asegurando así que en la 1ª iteración el 
            valor de F será mayor a F_ant_iteracion y por tanto se guardará beta_1e=0
            como el primer valor de beta_1e correspondiente al mayor valor de F 
            evaluado.
            """
            F_ant_iteracion=-1
            
            #Bucle para el cálculo de beta_1e correspondiente al máximo de F en
            #el rango 0° <= beta_1e <= 90°
            while beta_1e_bucle_grados >= 0 and beta_1e_bucle_grados <= 90:
                #Se define la función F
                #Numerador de F
                #N=(M_w1e_calculo_beta_1e**3)*(cos_beta_1e**3)*(tg_beta_1e+tg_alfa_1)**2
                
                #Donde se han de calcular: cos_beta_1e y tg_beta_1e
                
                #Conversión de beta_1e de grados a radianes
                beta_1e_bucle_radianes = float(mp.radians(beta_1e_bucle_grados))

                #Cálculo de cos_beta_1e
                cos_beta_1e = float(mp.cos(beta_1e_bucle_radianes))
                
                #Cálculo de tg_beta_1e
                tg_beta_1e = float(mp.tan(beta_1e_bucle_radianes))
                
                #Por tanto, ya se puede calcular N
                N=(M_w1e_calculo_beta_1e**3)*(cos_beta_1e**3)*((tg_beta_1e+tg_alfa_1)**2)
                     
                #Denominador de F
                D=(1+(0.5*(gamma-1)*(M_w1e_calculo_beta_1e**2)*(cos_beta_1e**2)*(1/(cos_alfa_1**2))))**((1/(gamma-1))+(3/2))
                
                #Luego el valor de F en cada iteración (para cada beta_1e) estará 
                #dado por
                F=N/D
                
                """
                Condicional para asignar a beta_1e el valor correspondiente a 
                esta iteración si F es mayor que en la anterior iteración o 
                mantener el valor de beta_1e correspondiente a la anterior 
                iteración si F es menor o igual que en la anterior iteración:
                """
                if F > F_ant_iteracion:
                    beta_1e_grados=round(beta_1e_bucle_grados, 1)
                    """
                    Donde se ha usado round para redondear al primer decimal el
                    valor de beta_1e_grados, ya que al probar el funcionamiento
                    del bucle se observó que los valores de beta_1e que arrojaba
                    contenían decimales residuales de órdenes de magnitud mucho 
                    menores a las milésimas. Redondeando al primer decimal (lo 
                    adecuado ya que en cada iteración se está sumando 0.1°), se
                    asegura que el valor guardado en beta_1e_grados no contiene
                    dichos residuos.
                    """                  
                """
                Una vez comparada la F calculada en esta iteración con la de la 
                anterior, se asigna F a F_ant_iteracion, de forma que cuando se 
                llegue en la siguiente iteración al anterior condicional, F habrá
                tomado un nuevo valor correspondiente a esa iteración mientra que 
                F_ant_iteracion será el valor de F calculado en la anterior 
                iteración
                """
                F_ant_iteracion=F
                
                #Fin bucle aumentando el valor de beta_1e en 0.1° para la 
                #siguiente iteración
                beta_1e_bucle_grados+=0.1
                
    #Fin del condicional "elif alfa_1_grados > 0:" y con ello fin de la estructura 
    #condicional para determinar beta_1e en cada caso de alfa_1


    "5. Bucle 1: Optimización de la sección de entrada"

    #Antes de comenzar con el bucle 1, se van a calcular algunos valores que serán 
    #necesarios para el mismo

    #En primer lugar, se convierte beta_1e (calculado en el apartado 4) de grados
    #a radianes
    beta_1e_radianes = float(mp.radians(beta_1e_grados))

    #Cálculo de tg_beta_1e
    tg_beta_1e = float(mp.tan(beta_1e_radianes))

    #Cálculo de cos_beta_1e
    cos_beta_1e = float(mp.cos(beta_1e_radianes))

    #Cálculo de beta_1e-alfa_1
    beta_1e_menos_alfa_1 = beta_1e_grados-alfa_1_grados

    #Conversión a radianes
    beta_1e_menos_alfa_1_radianes = float(mp.radians(beta_1e_menos_alfa_1))

    #Cálculo de sin(beta_1e-alfa_1)
    sin_beta_1e_menos_alfa_1 = float(mp.sin(beta_1e_menos_alfa_1_radianes))

    #Cálculo con coolprop de la entalpía total a la entrada del rotor (h_01)
    h_01=CP.PropsSI('H', 'T', T_01, 'P', p_01, fluido)

    #Cálculo con coolprop de la entropía específica de remanso a la entrada del 
    #rotor (s_01)
    s_01=CP.PropsSI('S', 'T', T_01, 'P', p_01, fluido)

    #La entropía específica estática s_1 será igual a la de remanso s_01
    s_1=s_01
    

    """
    Para iniciar el bucle 1, se ha de suponer un valor inicial para r_1e, que 
    será el que se use en la 1ª iteración. 
    
    Como es lógico, se cogerá uno ligeramente mayor que el radio interior de 
    entrada (r_1i).
    """
    #Valor inicial de r_1e_bucle
    r_1e_bucle = r_1i+0.01
    
    """
    Nota: en el bucle habrá 2 variables para el radio exterior de entrada: 
    r_1e_bucle y r_1e, ya que si solo se usara una el valor final que se 
    guardaría sería el de la iteración siguiente a la de convergencia del bucle.
    Es decir, en r_1e se guarda el valor de r_1e_bucle correspondiente a la
    iteración en la que el bucle converge.
    """
    
    """
    Por otro lado, se tiene que dar también un valor inicial a la variable G_bucle
    (gasto másico que se calculará dentro del bucle y que formará parte de la 
    condición de dicho bucle comparándose con el gasto G introducido por el 
    usuario). 
    
    La razón de dar un valor inicial a G_bucle es simplemente porque si no existe
    un valor para esta variable el bucle no puede comenzar. Por tanto, como la 
    condición de comienzo del bucle es que G_bucle sea distinto del gasto 
    introducido por el usuario (G), se dará a G_bucle un valor que en ningún 
    caso podrá ser igual a G; por ejemplo, un valor negativo.
    """
    G_bucle=-1

    """
    A continuación, se establece un condicional para adaptar el bucle 1 a cada
    uno de los dos casos de alfa_1 que se están analizando:
    """
    
    if alfa_1_grados == 0:
        #Bucle 1 para alfa_1=0
        while G_bucle < G-0.001 or G_bucle > G+0.001:
            """
            Como se puede observar en la condición del while, no se ha puesto
            que G_bucle sea distinto a G, sino que esté fuera de un pequeño 
            rango alrededor de G.
            
            La razón de lo anterior es simple: el hecho de que tengan que ser
            exactamente iguales para que el bucle converja es muy complicado no 
            solo porque pueden no llegar a ser exactamente iguales por decimales
            de muy poco orden que no tienen importancia, sino porque sumado a 
            eso en los cálculos se pueden generar decimales residuales que pongan
            más difícil aún que el bucle converja. Por tanto, para evitar que 
            esos decimales impidan la convergencia del bucle, se aceptarán valores
            de G_bucle que estén en un rango muy pequeño alrededor de G.
            """
            
            """
            Comenzando ya con el bucle 1, la ecuación para calcular el gasto 
            másico G_bucle es la siguiente:
                
                G_bucle=pi*((r_1e**2)-(r_1i**2))*densidad_1*c_1
        
            Donde se desconocen: densidad_1 (densidad a la entrada del rotor)
            y c_1 (velocidad absoluta a la entrada del rotor).
            
            c_1 se puede calcular con la siguiente ecuación:
                
                c_1=u_1e/tg_beta_1e
            
            Donde se desconoce la velocidad periférica en r_1e (u_1e).
            """
            
            #Cálculo de u_1e
            u_1e=omega*r_1e_bucle
            
            #Por tanto, ya se puede calcular c_1
            c_1=u_1e/tg_beta_1e
            
            #Para entrada axial se cumple lo siguiente
            c_m1=c_1 #Esto será de utilidad más adelante, no en este bucle, pero 
                     #ya queda definido al igual que el resto de magnitudes del
                     #triángulo de velocidades a la entrada del rotor
        
            """
            Por otro lado, densidad_1 se puede calcular con coolprop, pero para
            ello antes será necesario determinar la temperatura estática T_1 y 
            la presión estática p_1.
            """
            #Cálculo de la entalpía estática a la entrada del rotor (h_1)
            h_1=h_01-(c_1**2)/2
        
            #Cálculo con coolprop de T_1
            T_1=CP.PropsSI('T', 'H', h_1, 'S', s_1, fluido)
            
            #Cálculo con coolprop de p_1 
            p_1=CP.PropsSI('P', 'H', h_1, 'S', s_1, fluido)
            
            #Por tanto, ya se puede calcular densidad_1 con coolprop
            densidad_1 = CP.PropsSI('D', 'T', T_1, 'P', p_1, fluido)
            
            #Ecuación para calcular el gasto másico G_bucle:
            G_bucle=pi*((r_1e_bucle**2)-(r_1i**2))*densidad_1*c_1
        
            #Asignación a r_1e del valor de r_1e_bucle probado en cada iteración
            #(de esa forma el valor de r_1e_bucle para el que converja el bucle
            #se quedará guardado en r_1e, mientras que en r_1e_bucle se quedará
            #guardado el valor de convergencia+0.00001, que es lo que se le suma
            #a r_1e_bucle al final de cada iteración)
            r_1e=r_1e_bucle
        
            #Se suma 0.00001 al valor de r_1e_bucle obteniendo así el valor que
            #se probará en la siguiente iteración
            r_1e_bucle += 0.00001

    elif alfa_1_grados > 0:
        #Bucle 1 para alfa_1>0
        while G_bucle < G-0.001 or G_bucle > G+0.001:
            """
            Ecuación para calcular el gasto másico G_bucle:
            
                G_bucle=pi*((r_1e**2)-(r_1i**2))*densidad_1*c_m1
            
            De donde se desconocen: densidad_1 y c_m1.
            
            c_m1 se puede calcular con la siguiente ecuación:
                
                c_m1=c_1*cos_alfa_1
                
            Donde c_1, en este caso, puede calcularse mediante la siguiente 
            ecuación:
                
            c_1=((cos_beta_1e*sin_beta_1e_menos_alfa_1)/((cos_alfa_1**2)-(cos_beta_1e**2)))*u_1e 
            """
            
            #Cálculo de u_1e
            u_1e=omega*r_1e_bucle
            
            #Por tanto, ya se puede calcular c_1
            c_1=((cos_beta_1e*sin_beta_1e_menos_alfa_1)/((cos_alfa_1**2)-(cos_beta_1e**2)))*u_1e
            
            #Cálculo de c_m1
            c_m1=c_1*cos_alfa_1
            
            """
            Al igual que en el caso anterior de alfa_1=0, densidad_1 se puede 
            calcular con coolprop, pero para ello antes será necesario determinar
            T_1 y p_1.
            """
            #Cálculo de la entalpía estática a la entrada del rotor (h_1)
            h_1=h_01-(c_1**2)/2
       
            #Cálculo con coolprop de T_1
            T_1=CP.PropsSI('T', 'H', h_1, 'S', s_1, fluido)
           
            #Cálculo con coolprop de p_1 
            p_1=CP.PropsSI('P', 'H', h_1, 'S', s_1, fluido)
           
            #Por tanto, ya se puede calcular densidad_1 con coolprop
            densidad_1 = CP.PropsSI('D', 'T', T_1, 'P', p_1, fluido)
            
            #Ecuación para calcular el gasto másico G_bucle:
            G_bucle=pi*((r_1e_bucle**2)-(r_1i**2))*densidad_1*c_m1
            
            #Asignación a r_1e del valor de r_1e_bucle probado en cada iteración
            r_1e=r_1e_bucle
        
            #Se suma 0.00001 al valor de r_1e_bucle obteniendo así el valor que
            #se probará en la siguiente iteración
            r_1e_bucle += 0.00001


    "6. Cálculo de: w_1e y M_w1e"
    
    #Cálculo de sin_beta_1e
    sin_beta_1e = float(mp.sin(beta_1e_radianes))

    if alfa_1_grados == 0:
        #Cálculo de w_1e
        w_1e=u_1e/sin_beta_1e
        
        #Cálculo de M_w1e
        M_w1e=w_1e/((gamma*R*T_1)**(1/2))
        
    elif alfa_1_grados > 0:
        #Cálculo de w_1e
        w_1e=c_m1/cos_beta_1e
        
        #Cálculo de M_w1e
        M_w1e=w_1e/((gamma*R*T_1)**(1/2))
        
        
    "7. Cálculo de: Z_r y sigma"

    #Cálculo del número de álabes 
    Z_r=(90-beta_2_grados)/3
    
    #En el siguiente condicional lo que se hará es mantener el valor obtenido
    #de Z_r si sale exacto (p.ej: 20), y si no, se tomará el valor superior 
    #(p.ej: si sale 20.33, se cogería 21)
    if (Z_r-int(Z_r)) == 0:
        Z_r_final=int(Z_r)
    else:
        Z_r_final=int(Z_r)+1

    #Antes de calcular el factor de deslizamiento (sigma), se va a determinar el 
    #coseno de beta_2, ya que será necesario para el cálculo de sigma

    #Conversión de beta_2 de grados a radianes
    beta_2_radianes = float(mp.radians(beta_2_grados))

    #Cálculo de cos_beta_2
    cos_beta_2 = float(mp.cos(beta_2_radianes))

    #Cálculo del factor de deslizamiento 
    if beta_2_grados > 0 and beta_2_grados < 45:
        #Ecuación de Stanitz:
        sigma=1-((0.63*pi)/Z_r)
    elif beta_2_grados > 60:
        #Ecuación de Stodola:
        sigma=1-((pi*cos_beta_2)/Z_r)

    #DUDA: en el Torralbo no viene una ecuación para calcular sigma para valores
    #de beta_2 entre 45° y 60°.
    

    "8. Bucle 2"

    #Antes de comenzar con el bucle 2, se van a calcular algunos términos que serán
    #necesarios para el mismo

    #Cálculo de tg_beta_2
    tg_beta_2 = float(mp.tan(beta_2_radianes))

    #Cálculo de sin_beta_2
    sin_beta_2 = float(mp.sin(beta_2_radianes)) 

    #Cálculo de r_1 (radio medio de entrada al rotor)
    r_1=(0.5*((r_1e**2)+(r_1i**2)))**(1/2)

    #Cálculo de u_1 (velocidad tangencial del rotor en r_1)
    u_1=omega*r_1

    #Cálculo de c_u1 (componente tangencial de c_1)
    c_u1=c_m1*tg_alfa_1 #Esta expresión es la correspondiente al caso de alfa_1>0;
                        #sin embargo, es válida también para el caso de alfa_1=0,
                        #ya que tg_alfa_1=0, por lo que saldrá c_u1=0.

    #Cálculo w_1 (velocidad relativa en r_1)
    w_1=(((u_1-c_u1)**2)+(c_m1**2))**(1/2) #Esta expresión también vale para los
                                           #2 casos: alfa_1>0 y alfa_1=0
                   
    #Cálculo de u_1i (velocidad tangencial del rotor en r_1i)
    u_1i=omega*r_1i                                     
                    
    #Cálculo w_1i (velocidad relativa en r_1i)   
    w_1i=(((u_1i-c_u1)**2)+(c_m1**2))**(1/2) #Esta expresión también vale para los
                                             #2 casos: alfa_1>0 y alfa_1=0
                                           
    #Por otro lado, como se señaló en el apartado 1 (bases del diseño), la velocidad
    #meridiana en el rotor se conserva
    c_m2=c_m1
    
    #Cálculo de la componente tangencial de la velocidad relativa a la salida del 
    #rotor w_u2
    w_u2=c_m2*tg_beta_2

    #Cálculo de la velocidad relativa a la salida del rotor w_2
    w_2=w_u2/sin_beta_2 

    """
    Para que pueda comenzar el bucle 2, antes se han de inicializar las variables
    que intervienen en el mismo. 
    """
    #El valor mínimo aceptable para el rendimiento de un compresor es un 70%
    eta_c_minimo=0.7

    """
    El valor inicial del rendimiento será el mínimo aceptable, de forma que se
    probarán valores cada vez mayores del rendimiento a partir de ese mínimo. 
    De esta forma, se asegura que el rendimiento final que se obtenga será 
    aceptable porque será sí o sí mayor que el mínimo que se considera correcto.
    """
    eta_c_bucle = eta_c_minimo

    """
    También se debe inicializar la relación de compresión r_bucle, ya que 
    interviene en la condición del bucle while. Así, r_bucle deberá tomar un 
    valor inicial tal que se cumpla la condición del bucle while y este pueda 
    comenzar. Un valor que siempre cumplirá la condición será uno negativo, ya 
    que r-0.001 (donde r es la relación de compresión introducida por el usuario)
    no podrá ser nunca negativo.
    """
    r_bucle=-1
    
    #Bucle 2
    while r_bucle < r-0.001 or r_bucle > r+0.001:
        #Cálculo del trabajo específico W_i (no confundir con trabajo_esp, que 
        #fue la variable que se usó para calcular la potencia en el apartado 
        #2 (datos de entrada))
        W_i=Delta_h_stt/eta_c_bucle
        
        #Para seguir con la secuencia de cálculo, de nuevo se tienen que 
        #diferenciar los 2 casos de alfa_1
        if alfa_1_grados == 0:
            #Cálculo de la velocidad tangencial a la salida del rotor
            u_2=((sigma*c_m1*tg_beta_2)+((((sigma*c_m1*tg_beta_2)**2)+4*sigma*W_i)**(1/2)))/(2*sigma)

        elif alfa_1_grados > 0:
            #Cálculo de la velocidad tangencial a la salida del rotor
            u_2=((sigma*c_m1*tg_beta_2)+((((sigma*c_m1*tg_beta_2)**2)+4*sigma*(u_1*c_u1+W_i))**(1/2)))/(2*sigma)
            
        """
        En cuanto al ángulo de la velocidad absoluta a la salida del rotor 
        alfa_2, este se puede calcular a partir de la siguiente ecuación:
            
            alfa_2=arctan(c_u2/c_m2)
        
        Donde c_u2 (componente tangencial de c_2) es desconocida.
        """
        #Cálculo de c_u2 
        c_u2=u_2-w_u2
        
        #Al conocer c_u2, ya se puede calcular alfa_2
        alfa_2_radianes = float(mp.atan(c_u2/c_m2))
        
        #Conversión de alfa_2 de radianes a grados
        alfa_2_grados = float(mp.degrees(alfa_2_radianes))
        
        """
        Para calcular la velocidad absoluta a la salida del rotor, se tiene la
        siguiente ecuación:
        
            c_2=c_u2/sin_alfa_2
        """
        #Cálculo de sin_alfa_2
        sin_alfa_2 = float(mp.sin(alfa_2_radianes)) 
        
        #Por tanto, ya se puede calcular c_2
        c_2=c_u2/sin_alfa_2
        
        #Cálculo del radio de salida del rotor
        r_2=u_2/omega
        
        
        #Bucle 3
        """
        Este bucle 3, el cual se encuentra dentro del bucle 2, consiste en un 
        procedimiento iterativo donde la variable que controlará la repetición
        o validez de las iteraciones realizadas será el coeficiente de pérdidas
        en el rotor (zeta_R). 
        
        En el bucle habrá dos variables para el coeficiente de pérdidas:
            
            -zeta_R: valor que se prueba en cada iteración.
            
            -zeta_R_prima: valor que se obtiene al final de cada iteración y que
            se comparará en la condición del bucle con el zeta_R que se estableció
            al principio de la iteración.
        """

        """
        Se da como valor inicial a zeta_R_prima el valor que tomará zeta_R en 
        la primera iteración del bucle 3, ya que lo primero que se hace en 
        dicho bucle es asignar a zeta_R el valor de zeta_R_prima de la anterior
        iteración.
        """
        zeta_R_prima=0.2

        """
        Se da un valor inicial a zeta_R que asegure que se entrará en el bucle 
        debido a que se cumplirá la primera de las 2 condiciones del while:
            
            zeta_R_prima=0.2 < zeta_R-0.0001
        """
        zeta_R=1

        """
        Funcionamiento del bucle 3 (explicación de la primera y segunda iteración):
            
            1) Gracias al valor inicial asignado a zeta_R, el bucle podrá comenzar. 
            
            2) Una vez se entra en el bucle, se le asigna a zeta_R el valor 
               inicial de 0.2 (guardado en zeta_R_prima), ya que zeta_R suele 
               valer en torno a ese valor por regla general.
            
            3) Se realizan una serie de cálculos durante la primera iteración 
               que finalmente permiten calcular a partir de las pérdidas un 
               nuevo valor del coeficiente de pérdidas en el rotor (zeta_R_prima).
            
            4) Una vez determinado zeta_R_prima, se vuelven a comprobar las 
               condiciones del bucle while, de forma que:
                   
                4.1) Si zeta_R_prima es suficientemente similar a zeta_R (valor 
                     "supuesto" o "probado en la última iteración") el bucle se 
                      termina y queda guardado en zeta_R (o zeta_R_prima, en la 
                      la última iteración serán prácticamente iguales debido a la 
                      condición del bucle while: "zeta_R_prima < zeta_R-0.0001 or 
                      zeta_R_prima > zeta_R+0.0001:") el valor definitivo del 
                      coeficiente de pérdidas en el rotor.
                      
                      Nota: no se ha puesto como condición del while que 
                      "zeta_R_prima!=zeta_R" porque esto podría dar problemas de
                      convergencia debido a los decimales de pequeño orden y a 
                      los residuos, como ya se explicó anteriormente para otros
                      bucles. Por ello, se ha establecido un rango de valores
                      válidos en torno a zeta_R del orden 0.0001, lo cual se 
                      considera lo suficientemente preciso. 
                        
                4.2) Si zeta_R_prima no es suficientemente similar a zeta_R, se 
                     realiza una nueva iteración donde el nuevo valor que se 
                     probará de zeta_R será el valor de zeta_R_prima calculado 
                     en la anterior iteración.
        """

        while zeta_R_prima < zeta_R-0.0001 or zeta_R_prima > zeta_R+0.0001:
            #Se asigna a zeta_R el valor de zeta_R_prima de la anterior iteración,
            #o el valor inicial en el caso de la primera iteración
            zeta_R = zeta_R_prima
            
            #1) Cálculo de: p_2, T_2, densidad_2, M_2, b_2 y p_02
            
            #1.1) Cálculo de p_2
            
            #Cálculo de la entalpía de remanso específica a la salida del rotor
            #(punto 2 del diagrama h-s)
            h_02=W_i+h_01
            
            #Cálculo de la entalpía estática específica en 2
            h_2=h_02-(c_2**2)/2
            
            #Cálculo de la entalpía estática específica  en el punto 2s (punto 
            #2 isentrópico del diagrama h-s)
            h_2s=h_2-zeta_R*(w_1e**2)/2
            
            #La entropía estática específica en el punto 2s será igual a la del
            #punto 1
            s_2s=s_1
            
            #Cálculo con coolprop de la presión estática en el punto 2s a partir
            #de h_2s y s_2s
            p_2s=CP.PropsSI('P', 'H', h_2s, 'S', s_2s, fluido)
            
            #La presión de un punto real y su isentrópico correspondiente es la 
            #misma, luego
            p_2=p_2s
            
            #1.2) Cálculo de T_2
            
            #La temperatura estática en 2 puede calcularse con coolprop a partir
            #de h_2 y p_2
            T_2=CP.PropsSI('T', 'H', h_2, 'P', p_2, fluido)
            
            #1.3) Cálculo de densidad_2
            
            #La densidad estática en 2 puede calcularse con coolprop a partir de
            #T_2 y p_2
            densidad_2=CP.PropsSI('D', 'T', T_2, 'P', p_2, fluido)
            
            #1.4) Cálculo de M_2 
            
            #El número de Mach en 2 se puede calcular a partir de su definición
            M_2=c_2/((gamma*R*T_2)**(1/2))
            
            #1.5) Cálculo de b_2
            
            #El ancho axial a la salida del rotor se puede obtener de la ecuación
            #de continuidad
            b_2=G/(2*pi*r_2*densidad_2*c_m2)
            
            #1.6) Cálculo de p_02
            
            #Cálculo de la entropía estática específica en 2 con coolprop a 
            #partir de T_2 y p_2
            s_2=CP.PropsSI('S', 'T', T_2, 'P', p_2, fluido)
            
            #La entropía de un punto y su punto de remanso correspondiente son
            #iguales, luego
            s_02=s_2
            
            #Cálculo con coolprop de la presión de remanso a la salida del rotor
            #a partir de h_02 y s_02
            p_02=CP.PropsSI('P', 'H', h_02, 'S', s_02, fluido)
            
            #2) Cálculo de las pérdidas en el rotor
            
            #2.1) Cálculo de las pérdidas por fricción viscosa en la superficie
            #del conducto (Deltah_f)
            
            #Para poder determinar Deltah_f, antes se han de calcular una serie
            #de términos
            
            #Cálculo del diámetro hidráulico 
            D=0.5*(((4*((r_1e**2)-(r_1i**2)))/(r_1e-r_1i))+((4*pi*b_2*r_2)/(b_2+2*pi*r_2)))
            
            #Cálculo de la rugosidad relativa  
            epsilon_r=epsilon/D

            #Cálculo del logaritmo en base 10 de (epsilon_r/3.7)
            log_10_f = float(mp.log((epsilon_r/3.7), 10))
            
            #Cálculo del factor de fricción de Darcy (correlación de Nikuradse)
            f=(-1/(2*log_10_f))**2
            
            #Cálculo del coeficiente de fricción 
            zeta_f=4*f
            
            #Cálculo de la longitud media del conducto
            l=1.2*r_2
            
            #Cálculo de la velocidad media del flujo
            w_media=(w_1+w_2)/2
            
            #Finalmente, ya se pueden calcular las pérdidas por fricción viscosa
            Deltah_f=4*zeta_f*(l/D)*(w_media**2)/2
            
            #2.2) Cálculo de las pérdidas por engrosamiento de la capa límite,
            #desprendimiento y flujo secundario (Deltah_d)
            
            #Para poder determinar Deltah_d, antes se han de calcular una serie
            #de términos
            
            #Cálculo de la longitud media de la línea de corriente
            l_m=l
            
            #Cálculo del parámetro b
            b=(r_1e-r_1i+b_2)/2
            
            #Cálculo del parámetro r_s
            r_s=r_2-r_1e
            
            #Cálculo de la velocidad media cuadrática de entrada
            w_1mc=(((w_1e**2)+(w_1i**2))/2)**(1/2)
            
            #Cálculo del coeficiente de difusión
            D_f=1-(w_2/w_1mc)+((pi*r_2*u_2)/(Z_r*l_m*w_1mc))*((c_u2*u_2-c_u1*u_1)/(u_2**2))
            
            #Conocidos los anteriores términos, ya se puede determinar el 
            #incremento de entalpía debido a las pérdidas por difusión 
            Deltah_d=0.05*(D_f**2)*(u_2**2)
            
            #2.3) Cálculo de las pérdidas intersticiales internas (Deltah_ii)
            Deltah_ii=((0.6*epsilon_j*c_u2)/(b_2*u_2))*((((4*pi)/(b_2*Z_r))*(((r_1e**2)-(r_1i**2))/((r_2-r_1i)*(1+(densidad_2/densidad_1))*c_u2*c_m1/(u_2**2))))**(1/2))
            
            #2.4) Cálculo de las pérdidas por rozamiento del disco (Deltah_disco)
            Deltah_disco=(1/G)*0.0095*densidad_2*(n**3)*((r_2-r_1i)**5)
            
            #3) Cálculo de las pérdidas totales (Deltah_pérdidas) y del coeficiente
            #de pérdidas (zeta_R_prima)
            
            #Para calcular las pérdidas totales, simplemente se suman los distintos
            #tipos calculados
            Deltah_pérdidas=Deltah_f+Deltah_d+Deltah_ii+Deltah_disco
            
            #Otra forma de denominar a estas pérdidas en el rotor es Y_R
            Y_R=Deltah_pérdidas
            
            #Cálculo del nuevo coeficiente de pérdidas en el rotor
            zeta_R_prima=(Y_R)/((w_1e**2)/2)
            
            #Fin del bucle 3
            
        """
        El siguiente paso del bucle 2 es el cálculo del difusor sin álabes.
        
        En primer lugar, se va a programar un bucle para determinar el valor
        de x=r_3/r_2 (r_3 es el radio a la salida del rotor) correspondiente
        al punto donde la pendiente de la función C_p=f(x=r_3/r_2) (C_p es el 
        coeficiente de aumento de presión. Nota: no confundir con el calor 
        específico a presión constante (c_p)) disminuye considerablemente, lo 
        cual implica que un aumento del tamaño del difusor no produce un aumento
        significativo de presión. 
        
        El valor de la pendiente en ese momento en el que disminuye 
        considerablemente se ha estimado en 0.4444 (ese valor no se ha calculado
        en este código sino a parte (y de hecho manualmente), porque ese valor 
        siempre se considerará igual en cualquier caso e incorporar en el código
        el procedimiento para su cálculo es una pérdida de velocidad de cálculo
        innecesaria), y el punto donde la pendiente alcanza ese valor se va a 
        denominar como punto "A". 
        
        Así, el bucle que se va a programar calculará el valor de x en el punto
        A, que se denominará como x_A.
        
        El funcionamiento del bucle será el siguiente:
            
            1) Se define la ecuación de la derivada de la función C_p con respecto 
               a x, que será una nueva función de x.
               
            2) En cada iteración, se irán probando valores de x desde 1 hasta 
               que la derivada alcance el valor límite de la pendiente (0.4444).
               Ese valor de x con el que se alcance ese 0.4444 será x_A. 
               
               Nota: se probarán valores de x a partir de 1 porque C_p=f(x=r_3/r_2)
               toma valores positivos a partir de x=1.
        """
        
        #Antes de comenzar con el bucle, se va a definir la tangente de alfa_2,
        #ya será necesaria dentro del mismo
        tg_alfa_2=float(mp.tan(alfa_2_radianes))
        
        """
        En cuanto al valor inicial de la derivada de la función C_p=f(x=r_3/r_2),
        tendrá que ser tal que permita comenzar el bucle. Por ejemplo, 0 valdría
        ya que una de las condiciones del while es:
            
            derivada_Cp < 0.4444-0.0001
        """
        derivada_Cp=0
        
        #Valor inicial de x
        x=1
        
        #Bucle para el cálculo de x_A
        while derivada_Cp < 0.4444-0.0001 or derivada_Cp > 0.4444+0.0001:
            
            #Cálculo del parámetro Gamma, el cual será necesario para calcular 
            #derivada_Cp. Nota: no confundir con el índice adiabático del gas 
            #(gamma)
            Gamma=1/(1+(tg_alfa_2*0.18*(x-1)))
            
            #Cálculo de la derivada de la función C_p=f(x=r_3/r_2)
            derivada_Cp=(2/((x**3)*((tg_alfa_2**2)+1)))*((Gamma**2)*(tg_alfa_2**2)+1-(x*0.18*(((Gamma**2)*(tg_alfa_2**2)+1)**(1/2))))
            
            #Asignación a x_A del valor de x probado en esta iteración (al final
            #del bucle quedará guardado en x_A el valor de x de la última 
            #iteración, evitando que se sume 0.00001 a dicho valor debido a que
            #el bucle finaliza con: "x += 0.00001")
            x_A=x
            
            #Se suma 0.00001 al valor de x para obtener el valor que se usará en 
            #la siguiente iteración
            x += 0.00001
        
        
        """
        Una vez determinado x_A, el siguiente paso es calcular el coeficiente de 
        aumento de presión correspondiente a x_A. Para ello, habrá que sustituir
        x_A en la expresión C_p=f(x=r_3/r_2), quedando lo siguiente:
        
            C_pA=(2/((tg_alfa_2**2)+1))*I(x=x_A)
        
        Donde "I" es una integral que, dada su complejidad, debe resolverse
        numéricamente.
        
        """
        
        #Resolución numérica de la integral "I"
        
        #1) Se define el integrando de "I" (se va a usar una nueva variable "y",
        #ya que x ya tiene un valor debido al último bucle)
        def integrando_I(y):
            return ((((tg_alfa_2**2)/((1+tg_alfa_2*0.18*(y-1))**2))+1)/(y**3))-((0.18/(y**2))*((((tg_alfa_2**2)/((1+tg_alfa_2*0.18*(y-1))**2))+1)**(1/2)))

        #2) Se definen los límites inferior y superior de la integral
        x_i=1
        x_s=x_A

        #3) Resolución de la integral usando la función "quad"
        I, error = quad(integrando_I, x_i, x_s)
        #En la variable error se guarda el error cometido al calcular la integral 
        #mediante el algoritmo que utiliza la función "quad"
        
        #Una vez resuelta "I", ya se puede determinar el coeficiente de aumento
        #de presión para x_A
        C_pA=(2/((tg_alfa_2**2)+1))*I
        
        """
        De esta manera, ya se han determinado x_A y C_pA.
        
        El siguiente paso para proseguir con el cálculo del difusor sin álabes 
        es determinar el coeficiente de pérdidas en el difusor (Y_p), lo cual se
        puede realizar gracias a la siguiente ecuación:
            
            Y_p=1-C_pA-(c_3/c_2)**2
            
        Donde son conocidos todos los términos excepto la velocidad absoluta a 
        la salida del rotor (c_3).
        """
        
        #Antes de calcular c_3, se hace efectiva la consideración que se comentó
        #en el apartado 1 (bases del diseño) de que los anchos de entrada y 
        #salida del difusor son iguales
        b_3=b_2
        
        #Cálculo de c_3
        c_3=(c_2/x_A)*(((((Gamma*tg_alfa_2)**2)+((b_2/b_3)**2))/((tg_alfa_2**2)+1))**(1/2))
        
        #Cálculo de Y_p
        Y_p=1-C_pA-((c_3/c_2)**2)
        
        """
        Una vez determinados x_A, C_pA y Y_p, ya se pueden determinar las 
        condiciones del fluido a la salida del difusor, el triángulo de velocidades
        y el radio de salida, que es lo que se va a realizar a continuación.
        """
        
        #Cálculo del radio de salida del difusor
        r_3=x_A*r_2
        
        #Cálculo de la presión estática a la salida del difusor a partir de la 
        #definición de C_p
        p_3=C_pA*(p_02-p_2)+p_2
        
        #Cálculo de la presión de remanso a la salida del difusor a partir de la
        #definición de Y_p
        p_03=p_02-Y_p*(p_02-p_2)
        
        #La entalpía de remanso en el difusor se conserva, luego
        h_03=h_02
        
        #La temperatura de remanso a la salida del difusor puede calcularse con
        #coolprop a partir de h_03 y p_03
        T_03=CP.PropsSI('T', 'H', h_03, 'P', p_03, fluido)
        
        #Cálculo con coolprop de la entropía específica de remanso a la salida 
        #del difusor (ya que será necesaria, junto con p_3, para hallar la 
        #temperatura estática)
        s_03=CP.PropsSI('S', 'H', h_03, 'P', p_03, fluido)
        
        #La entropía del punto 03 es igual a la del 3, luego
        s_3=s_03
        
        #De esta forma, la temperatura estática a la salida del difusor puede 
        #calcularse con coolprop a partir de p_3 y s_3
        T_3=CP.PropsSI('T', 'S', s_3, 'P', p_3, fluido)
        
        #Cálculo con coolprop de la densidad estática a la salida del difusor a
        #partir de p_3 y T_3
        densidad_3 = CP.PropsSI('D', 'T', T_3, 'P', p_3, fluido)
        
        #Cálculo de la componente radial de c_3 a partir de la ecuación de 
        #continuidad aplicada a la salida del difusor
        c_r3=(G)/(2*pi*r_3*b_3*densidad_3)
        
        #Cálculo del ángulo de c_3 
        alfa_3_radianes = float(mp.acos(c_r3/c_3))
         
        #Conversión de alfa_3 de radianes a grados
        alfa_3_grados = float(mp.degrees(alfa_3_radianes))
         
        """
        Las pérdidas en el difusor se pueden calcular a partir de la siguiente
        ecuación:
            
            Y_E=h_3-h_3s
            
        Donde se desconocen h_3 y h_3s, que se van a calcular a continuación.
        """
        
        #Cálculo de la entalpía específica estática a la salida del difusor
        #con coolprop a partir de T_3 y p_3
        h_3=CP.PropsSI('H', 'T', T_3, 'P', p_3, fluido)
        
        #La entropía específica estática en el punto 3s (isentrópico correspondiente
        #a la salida del difusor) será igual a la del punto 2 (entrada al difusor)
        s_3s=s_2
        
        #La presión estática en 3s será igual a la de 3
        p_3s=p_3
        
        #Cálculo de h_3s con coolprop a partir de s_3s y p_3s
        h_3s=CP.PropsSI('H', 'S', s_3s, 'P', p_3s, fluido)
        
        #Por tanto, ya se pueden calcular las pérdidas en el difusor
        Y_E=h_3-h_3s
        
        #Cálculo del coeficiente de pérdidas en el difusor
        zeta_E=(2*Y_E)/(c_2**2)
        
        """
        Finalmente, para acabar con el bucle 2 y con la secuencia de cálculo, los 
        últimos términos que se van a calcular son los siguientes:
    
            1) Delta_h_stt_prima: valor final del salto isentrópico total a total. 
               Este término ya se etimó al inicio de la secuencia de cálculo 
               (apartado 2) a partir de los datos de entrada (incluyendo el uso
               de c_p y gamma), pero a continuación se va a calcular el valor 
               final a partir de los términos calculados en la secuencia de 
               cálculo (ya sin usar c_p y gamma, sino solo a partir de las 
               propiedades calculadas con coolprop).
               
            2) W_i_prima: valor final del trabajo específico; ya que el W_i que 
               se obtuvo a partir del bucle 2 dependía de Delta_h_stt.
        """
        
        #1) Para calcular Delta_h_stt_prima, antes hay que calcular h_03ss. Para
        #ello, se puede usar la presión p_03ss y la entropía s_03ss
        
        #La presión p_03ss es igual a la de los puntos 03s y 03
        p_03ss=p_03
        
        #La entropía s_03ss es igual a la del punto 1
        s_03ss=s_1
        
        #Cálculo de h_03ss a partir de p_03ss y s_03ss usando coolprop
        h_03ss=CP.PropsSI('H', 'S', s_03ss, 'P', p_03ss, fluido)
        
        #Cálculo de Delta_h_stt_prima
        Delta_h_stt_prima=h_03ss-h_01
        
        #2) Cálculo de W_i_prima
        W_i_prima=Delta_h_stt_prima+Y_R+Y_E
        
        #Cálculo de r_bucle (su valor determinará si se realiza otra iteración 
        #o no, debido a que r_bucle es comparado con r en la condición del bucle
        #2)
        r_bucle=p_03/p_01 
        
        """
        Asignación a eta_c_final del valor de eta_c_bucle probado en cada 
        iteración (al final del bucle quedará guardado en eta_c_final el valor 
        final del rendimiento (el de la última iteración), evitando que se sume
        0.0001 a dicho valor debido a que el bucle finaliza con: 
        "eta_c_bucle += 0.0001").
        """
        eta_c_final=eta_c_bucle
        
        #Se suma 0.0001 al valor de eta_c_bucle para obtener el valor que se 
        #usará en la siguiente iteración
        eta_c_bucle += 0.0001

        #Fin del bucle 2    
    
    """    
    A continuación se van a calcular una serie de parámetros que tienen que 
    estar dentro de ciertos márgenes recomendados.
    """
    
    #1) Relación de radios (RR)
    RR=r_2/r_1e

    #2) Relación de difusión (RD)
    RD=w_1e/w_2

    #3) b_2/D_2 (BD)
    #BD=b_2/D_2

    #Cálculo del diámetro a la salida del rotor
    D_2=2*r_2

    BD=b_2/D_2
    

    """
    Lo siguiente será una estructura condicional "if-else" que asignará
    t=1 si alguno o varios de los parámetros básicos están fuera de los márgenes
    recomendados y t=0 si todos están dentro de los márgenes; además de asignar,
    en el caso de t=0, a ns_final el valor de ns en la iteración en la que se 
    cumpla que todos los parámetros estén dentro de los márgenes. 
    
    Por tanto, como la condición del bucle ns es "while ns >= 0.5 and ns <= 0.8 and t==1:",
    el funcionamiento de la próxima estructura condicional en relación con el 
    bucle ns será el siguiente:
        
        -Si t=1 (algún/os parámetros fuera de márgenes recomendados) y ns está 
        dentro del margen [0.5, 0.8], se seguirán probando valores de ns porque
        se cumplirán las 2 condiciones del bucle while. Si ns pasa a tener un
        valor fuera del rango [0.5, 0.8] (finaliza el bucle porque no se cumple
        1 de las 2 condiciones del while) y en todas las iteraciones se ha dado
        el caso de t=1, entonces no habrá ningún valor de ns para el que todos
        los parámetros estén dentro de los márgenes recomendados y será necesario
        replantearse las características básicas del diseño.
        
        -Si en una cierta iteración t=0 (todos los parámetros están dentro de 
        los márgenes recomendados), entonces no se cumplirá 1 de las 2 condiciones
        del while y el bucle finaliza, guardándose en ns_final el valor de ns
        de la iteración para la que todos los parámetros hayan estado dentro de 
        los márgenes recomendados.
    """
    
    if eta_c_bucle >= 1 or alfa_2_grados < 64 or alfa_2_grados > 71 or RR < 1.2 or RR > 2.2 or RD < 1.5 or RD > 1.8 or BD < 0.02 or BD > 0.12:
        t=1
    else:
        t=0
        ns_final=ns
       
    """
    A continuación se tiene una estructura condicional que comprobrá la paridad
    de la iteración y asignará en función de dicha paridad un nuevo valor a ns,
    que será el que se usará en la siguiente iteración.
    
    Nota: todo el tema de la paridad es simplemente porque no se trata de probar
    valores de ns que aumenten o disminuyan en una cantidad constante en cada
    iteración, si no que se pretende probar alternativamente valores por encima
    y debajo del óptimo (ns=0.65).
    """
    
    #Estructura condional para la asignación del nuevo valor que tomará ns en 
    #la próxima iteración
    if paridad_iteracion % 2 == 0: #LA ITERACIÓN EN LA QUE SE ESTÁ ES PAR
        #Se suma 0.01 al ns que se probó en la última iteración impar (la anterior
        #a la par en la que se está)
        ns_impar=ns_impar+0.01
        
        #Se asigna a ns el valor que tomará en la siguiente iteración, la cual
        #será impar
        ns=round(ns_impar, 2) 
        
        """
        Se ha usado round para redondear a 2 decimales porque aparecen decimales
        residuales de orden extremadamente pequeño que no influyen en los cálculos,
        pero sí en la condición del bucle, ya que cuando se llegue a ns=0.80,
        si en realidad es 0.8000000000000001 por ejemplo, el bucle finalizará
        sin probar 0.50, que sería el último valor del bucle porque el siguiente
        ya sería 0.81.
        """
        
    else: #LA ITERACIÓN EN LA QUE SE ESTÁ ES IMPAR
        #Se resta 0.01 al ns que se probó en la última iteración par
        ns_par=ns_par-0.01
        
        #Se asigna a ns el valor que tomará en la siguiente iteración, la cual
        #será par
        ns=round(ns_par, 2)
        
    paridad_iteracion += 1
    
  
####################### FIN BUCLE ns #######################################  

#Como ya ha finalizado el bucle ns, se borra el print("Calculando... Por favor, espere", end='')
#que se puso justo antes de comenzar el bucle
sys.stdout.write('\r' + ' ' * len("Calculando... Por favor, espere") + '\r')


"""
Para finalizar, se tiene una estructura condicional que visualizará en la consola
los resultados solo si se ha logrado que todos los parámetros básicos estén 
dentro de los márgenes recomendados para algún valor de ns en el rango [0.5, 0.8].

En el caso de que lo anterior no se haya dado, se mostrará un mensaje que 
informará de ello y de que, en consecuencia, será necesario replantearse las 
características básicas del diseño (datos de entrada y bases del diseño).
"""

if t==1: #Si se da este caso es porque no hay ningún valor de ns en el rango 
         #[0.5, 0.8] para el que todos los parámetros estuvieran dentro de los 
         #márgenes recomendados, por lo que será necesario replantearse las 
         #características básicas del diseño
    print("Para los datos de entrada introducidos se obtienen uno o varios parámetros básicos fuera de los márgenes recomendados, por lo que será necesario replantearse las características básicas del diseño. Cambios no importantes como por ejemplo variar ligeramente {beta2_con_subindice} u otros parámetros podrían solucionar el problema.")
    
else: #Si se da este caso es porque en el bucle ns se ha llegado a t=0 (todos 
      #los parámetros están dentro de los márgenes recomendados), por lo que
      #el siguiente paso será visualizar en la consola todos los resultados de 
      #la secuencia de cálculo, finalizando de esta manera el prediseño
         
    print("                               ", end='') #Con este print se centra 
    #el siguiente print cuando aparezca en la consola
    
    print("Resultados:") 
    
    print("")
    
    #Creación de la variable ns poniendo s como subíndice
    ns_texto = "ns"
    ns_con_subindice = ns_texto.replace("s", convertir_a_subindice("s"))
    
    #El ns de la última iteración del bucle de ns (para el que se ha conseguido
    #la convergencia con todos los parámetros básicos dentro de los márgenes
    #recomendados) estará guardado en ns_final
    print(f"·Número específico de revoluciones: {ns_con_subindice}={ns_final}")
    
    print("")
    
    #Creación del símbolo omega mediante su código Unicode
    omega_simbolo = '\u03A9'
    
    print(f"·Velocidad angular del compresor: {omega_simbolo}={round(omega, 4)} (rad/s)")
    
    print("")
    
    #Creación de la variable r1i poniendo i y 1 como subíndices
    r1i_texto = "r1i"
    r1i_con_subindice = r1i_texto.replace("1i", convertir_a_subindice("1i"))
    
    print(f"·Radio interior de entrada: {r1i_con_subindice}={round(r_1i, 4)} (m)")
    
    print("")
    
    #Creación de la variable beta1e poniendo 1 y e como subíndices
    beta1e_texto = f"{beta_simbolo}1e"
    beta1e_con_subindice = beta1e_texto.replace("1e", convertir_a_subindice("1e"))
      
    print(f"·Ángulo de la velocidad relativa a la entrada del rotor en el radio exterior: {beta1e_con_subindice}={round(beta_1e_grados, 4)}{simbolo_grados}")
    
    print("")
        
    #Creación de la variable r1e con 1 y e como subíndices
    r1e_texto = "r1e"
    r1e_con_subindice = r1e_texto.replace("1e", convertir_a_subindice("1e"))
    
    print(f"·Radio exterior de entrada al rotor: {r1e_con_subindice}={round(r_1e, 4)} (m)")
    
    print("")
    
    #Creación de la variable u1e con 1 y e como subíndices
    u1e_texto = "u1e"
    u1e_con_subindice = u1e_texto.replace("1e", convertir_a_subindice("1e"))
        
    print(f"·Velocidad periférica en el radio exterior de entrada al rotor: {u1e_con_subindice}={round(u_1e, 4)} (m/s)")
    
    print("")
    
    #Creación de la variable c1 con 1 como subíndice
    c1_texto = "c1"
    c1_con_subindice = c1_texto.replace("1", convertir_a_subindice("1"))
        
    print(f"·Velocidad absoluta a la entrada del rotor: {c1_con_subindice}={round(c_1, 4)} (m/s)")
    
    print("")
    
    #Creación de la variable p1 con 1 como subíndice
    p1_texto = "p1"
    p1_con_subindice = p1_texto.replace("1", convertir_a_subindice("1"))
        
    print(f"·Presión a la entrada del rotor: {p1_con_subindice}={round(p_1, 4)} (Pa)")
    
    print("")
    
    #Creación de la variable T1 con 1 como subíndice
    T1_texto = "T1"
    T1_con_subindice = T1_texto.replace("1", convertir_a_subindice("1"))
        
    print(f"·Temperatura a la entrada del rotor: {T1_con_subindice}={round(T_1, 4)} (K)")
    
    print("")
    
    #Creación del símbolo rho mediante su código Unicode
    rho_simbolo = '\u03C1'

    #Creación de la variable rho1 con 1 como subíndice
    rho1_texto = f"{rho_simbolo}1"
    rho1_con_subindice = rho1_texto.replace("1", convertir_a_subindice("1"))
        
    print(f"·Densidad a la entrada del rotor: {rho1_con_subindice}={round(densidad_1, 4)} (kg/m\u00B3)")
    
    print("")
    
    #Creación de la variable w1e con 1 y e como subíndices
    w1e_texto = "w1e"
    w1e_con_subindice = w1e_texto.replace("1e", convertir_a_subindice("1e"))
    
    print(f"·Velocidad relativa en {r1e_con_subindice}: {w1e_con_subindice}={round(w_1e, 4)} (m/s)")
    
    print("")
    
    #Creación de la variable Mw1e con w, 1 y e como subíndices
    Mw1e_texto = "Mw1e"
    Mw1e_con_subindice = Mw1e_texto.replace("w1e", convertir_a_subindice("w1e"))

    print(f"·Mach correspondiente a {w1e_con_subindice}: {Mw1e_con_subindice}={round(M_w1e, 4)}")
    
    print("")
    
    #Creación de la variable Zr con r como subíndice
    Zr_texto = "Zr"
    Zr_con_subindice = Zr_texto.replace("r", convertir_a_subindice("r"))

    print(f"·Número de álabes del rotor: {Zr_con_subindice}={Z_r_final}") 
    
    print("")
    
    #Creación del símbolo sigma mediante su código Unicode
    sigma_simbolo = '\u03C3'

    print(f"·Factor de deslizamiento: {sigma_simbolo}={round(sigma, 4)}")
    
    print("")
    
    #Creación de la variable Wi con i como subíndice
    Wi_texto = "Wi"
    Wi_con_subindice = Wi_texto.replace("i", convertir_a_subindice("i"))
    
    print(f"·Trabajo específico en el rotor: {Wi_con_subindice}={round(W_i_prima, 4)} (J/kg)")
    
    print("")
    
    #Creación de la variable u2 con 2 como subíndice
    u2_texto = "u2"
    u2_con_subindice = u2_texto.replace("2", convertir_a_subindice("2"))

    print(f"·Velocidad periférica a la salida del rotor: {u2_con_subindice}={round(u_2, 4)} (m/s)")
    
    print("")
    
    #Creación de la variable w2 con 2 como subíndice
    w2_texto = "w2"
    w2_con_subindice = w2_texto.replace("2", convertir_a_subindice("2"))
      
    print(f"·Velocidad relativa a la salida del rotor: {w2_con_subindice}={round(w_2, 4)} (m/s)")
    
    print("")
    
    #Creación de la variable c2 con 2 como subíndice
    c2_texto = "c2"
    c2_con_subindice = c2_texto.replace("2", convertir_a_subindice("2"))

    print(f"·Velocidad absoluta a la salida del rotor: {c2_con_subindice}={round(c_2, 4)} (m/s)")
    
    print("")
    
    #Creación de la variable alfa2 con 2 como subíndice
    alfa2_texto = f"{alfa_simbolo}2"
    alfa2_con_subindice = alfa2_texto.replace("2", convertir_a_subindice("2"))
    
    print(f"·Ángulo de la velocidad absoluta a la salida del rotor: {alfa2_con_subindice}={round(alfa_2_grados, 4)}{simbolo_grados}")
    
    print("")
    
    #Creación de la variable r2 con 2 como subíndice
    r2_texto = "r2"
    r2_con_subindice = r2_texto.replace("2", convertir_a_subindice("2"))
    
    print(f"·Radio de salida del rotor: {r2_con_subindice}={round(r_2, 4)} (m)")
    
    print("")
    
    #Creación de la variable T2 con 2 como subíndice
    T2_texto = "T2"
    T2_con_subindice = T2_texto.replace("2", convertir_a_subindice("2"))

    print(f"·Temperatura a la salida del rotor: {T2_con_subindice}={round(T_2, 4)} (K)")
    
    print("")
    
    #Creación de la variable p2 con 2 como subíndice
    p2_texto = "p2"
    p2_con_subindice = p2_texto.replace("2", convertir_a_subindice("2"))

    print(f"·Presión a la salida del rotor: {p2_con_subindice}={round(p_2, 4)} (Pa)")
    
    print("")
    
    #Creación de la variable rho2 con 2 como subíndice
    rho2_texto = f"{rho_simbolo}2"
    rho2_con_subindice = rho2_texto.replace("2", convertir_a_subindice("2"))
        
    print(f"·Densidad a la salida del rotor: {rho2_con_subindice}={round(densidad_2, 4)} (kg/m\u00B3)")
    
    print("")
    
    #Creación de la variable M2 con 2 como subíndice
    M2_texto = "M2"
    M2_con_subindice = M2_texto.replace("2", convertir_a_subindice("2"))

    print(f"·Número de Mach a la salida del rotor: {M2_con_subindice}={round(M_2, 4)}")
    
    print("")
    
    print(f"·Ancho axial a la salida del rotor: {b2_con_subindice}={round(b_2, 4)} (m)")

    print("")

    #Creación del símbolo Delta mediante su código Unicode
    Delta_simbolo = '\u0394'
    
    print(f"·Pérdidas en el rotor por fricción viscosa: {Delta_simbolo}h={round(Deltah_f, 4)} (J/kg)")
    
    print("")
    
    print(f"·Pérdidas en el rotor por engrosamiento de la capa límite, desprendimiento y flujo secundario: {Delta_simbolo}h={round(Deltah_d, 4)} (J/kg)")
    
    print("")
    
    print(f"·Pérdidas intersticiales internas en el rotor: {Delta_simbolo}h={round(Deltah_ii, 4)} (J/kg)")
    
    print("")
    
    print(f"·Pérdidas en el rotor por rozamiento del disco: {Delta_simbolo}h={round(Deltah_disco, 4)} (J/kg)")
    
    print("")
    
    #Creación de la variable Deltahtr con t y r como subíndices
    Deltahtr_texto = f"{Delta_simbolo}htr"
    Deltahtr_con_subindice = Deltahtr_texto.replace("tr", convertir_a_subindice("tr"))
    
    #Creación de la variable Yr con r como subíndice
    Yr_texto = "Yr"
    Yr_con_subindice = Yr_texto.replace("r", convertir_a_subindice("r"))
    
    print(f"·Pérdidas totales en el rotor: {Deltahtr_con_subindice}={Yr_con_subindice}={round(Deltah_pérdidas, 4)} (J/kg)")
    
    print("")
    
    #Creación del símbolo zeta mediante su código Unicode
    zeta_simbolo = '\u03B6'
    
    #Creación de la variable zetar con r como subíndice
    zetar_texto = f"{zeta_simbolo}r"
    zetar_con_subindice = zetar_texto.replace("r", convertir_a_subindice("r"))
    
    print(f"·Coeficiente de pérdidas en el rotor: {zetar_con_subindice}={round(zeta_R, 4)}")
    
    print("")
    
    #Creación de la variable r3 con 3 como subíndice
    r3_texto = "r3"
    r3_con_subindice = r3_texto.replace("3", convertir_a_subindice("3"))

    print(f"·Radio de salida del difusor: {r3_con_subindice}={round(r_3, 4)} (m)")
    
    print("")
    
    #Creación de la variable T3 con 3 como subíndice
    T3_texto = "T3"
    T3_con_subindice = T3_texto.replace("3", convertir_a_subindice("3"))

    print(f"·Temperatura a la salida del difusor: {T3_con_subindice}={round(T_3, 4)} (K)")
    
    print("")
    
    #Creación de la variable p3 con 3 como subíndice
    p3_texto = "p3"
    p3_con_subindice = p3_texto.replace("3", convertir_a_subindice("3"))

    print(f"·Presión a la salida del difusor: {p3_con_subindice}={round(p_3, 4)} (Pa)")
    
    print("")
    
    #Creación de la variable rho3 con 3 como subíndice
    rho3_texto = f"{rho_simbolo}3"
    rho3_con_subindice = rho3_texto.replace("3", convertir_a_subindice("3"))
        
    print(f"·Densidad a la salida del difusor: {rho3_con_subindice}={round(densidad_3, 4)} (kg/m\u00B3)")
    
    print("")
    
    #Creación de la variable c3 con 3 como subíndice
    c3_texto = "c3"
    c3_con_subindice = c3_texto.replace("3", convertir_a_subindice("3"))

    print(f"·Velocidad absoluta a la salida del difusor: {c3_con_subindice}={round(c_3, 4)} (m/s)")
    
    print("")
    
    #Creación de la variable cr3 con r y 3 como subíndices
    cr3_texto = "cr3"
    cr3_con_subindice = cr3_texto.replace("r3", convertir_a_subindice("r3"))

    print(f"·Componente radial de la velocidad absoluta a la salida del difusor: {cr3_con_subindice}={round(c_r3, 4)} (m/s)")
    
    print("")
    
    #Creación de la variable alfa3 con 3 como subíndice
    alfa3_texto = f"{alfa_simbolo}3"
    alfa3_con_subindice = alfa3_texto.replace("3", convertir_a_subindice("3"))
    
    print(f"·Ángulo de la velocidad absoluta a la salida del difusor: {alfa3_con_subindice}={round(alfa_3_grados, 4)}{simbolo_grados}")
    
    print("")
    
    #Creación de la variable Ye con e como subíndice
    Ye_texto = "Ye"
    Ye_con_subindice = Ye_texto.replace("e", convertir_a_subindice("e"))
    
    print(f"·Pérdidas en el difusor: {Ye_con_subindice}={round(Y_E, 4)} (J/kg)")
    
    print("")
    
    #Creación de la variable zetae con e como subíndice
    zetae_texto = f"{zeta_simbolo}e"
    zetae_con_subindice = zetae_texto.replace("e", convertir_a_subindice("e"))
    
    print(f"·Coeficiente de pérdidas en el difusor: {zetae_con_subindice}={round(zeta_E, 4)}")
    
    print("")
    
    #Creación de la variable Cp con p como subíndice
    C_p_texto = "Cp"
    C_p_con_subindice = C_p_texto.replace("p", convertir_a_subindice("p"))
    
    print(f"·Coeficiente de aumento de presión en el difusor: {C_p_con_subindice}={round(C_pA, 4)}")
    
    print("")
    
    print(f"·Rendimiento total a total del compresor centrífugo: {eta_tt_con_subindice}={round(eta_c_final, 4)}", end=" ")
    
    print("\n")
    
    
print("Fin del prediseño")
