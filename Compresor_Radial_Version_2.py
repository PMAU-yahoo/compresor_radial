"""
Programa: Método 1D para el prediseño de compresores centrífugos de 1 
escalonamiento y con difusor sin álabes.

Autor: David Bravo Berrocal.
"""

#Se importa el módulo "os", el cual permite usar funcionalidades dependientes del
#sistema operativo, como leer o escribir archivos, manipular rutas, etc. En este
#programa se utilizará principalmente para crear los archivos de entrada y salida
#de datos
import os

#Se importa "MaxNLocator", que se utilizará para establecer el número de 
#subdivisiones de los ejes de las figuras que se mostrarán al final del prediseño
from matplotlib.ticker import MaxNLocator

#Se importa el paquete "CoolProp", que se utilizará para calcular propiedades
#termodinámicas
import CoolProp.CoolProp as CP

#Se importa la función "quad", que permitirá calcular integrales definidas
from scipy.integrate import quad

#Se importa el módulo "sys", que se utilizará para borrar los textos visualizados
#a través de las funciones "print()"
import sys

#Se importa "mp", ya que contiene funciones matemáticas que serán de utilidad
from mpmath import mp

#Se importa "matplotlib.pyplot", que se utilizará para la creación de gráficos
import matplotlib.pyplot as pl

#Se importa una función creada para convertir números y otros caracteres en 
#subíndices
from Funcion_conversion_subindices import convertir_a_subindice


#Se guarda el valor de pi en una variable usando mp de mpmath, ya que será 
#necesario en muchas ocasiones a lo largo del código
pi = float(mp.pi)


print("")

print("                               ", end='') #Con este print se centra el
                                                 #siguiente cuando aparezca en
                                                 #la consola

print("Datos de entrada:") 
                          
print("")


"""
A continuación, antes de solicitar los datos de entrada, se van a crear sus 
símbolos.
"""

#Creación de la variable alfa1 poniendo con códigos Unicode el símbolo de 
#alfa y 1 como subíndice
alfa_simbolo = '\u03B1'
alfa1_texto = f"{alfa_simbolo}1"
alfa1_con_subindice = alfa1_texto.replace("1", convertir_a_subindice("1"))

#Creación de la variable beta2 poniendo con códigos Unicode el símbolo de 
#beta y 2 como subíndice
beta_simbolo = '\u03B2'
beta2_texto = f"{beta_simbolo}2"
beta2_con_subindice = beta2_texto.replace("2", convertir_a_subindice("2"))

#Creación de la variable p01 con 0 y 1 como subíndices
p01_texto = "p01"
p01_con_subindice = p01_texto.replace("01", convertir_a_subindice("01"))

#Creación de la variable T01 con 0 y 1 como subíndices
T01_texto = "T01"
T01_con_subindice = T01_texto.replace("01", convertir_a_subindice("01"))

#Creación de la variable cp con p como subíndice
cp_texto = "cp"
cp_con_subindice = cp_texto.replace("p", convertir_a_subindice("p"))

#Creación del símbolo gamma mediante su código Unicode
gamma_simbolo = '\u03B3'

#Creación del símbolo epsilon mediante su código Unicode
epsilon_simbolo = '\u03B5'

#Creación de la variable epsilonj con j como subíndice
epsilonj_texto = f"{epsilon_simbolo}j"
epsilonj_con_subindice = epsilonj_texto.replace("j", convertir_a_subindice("j"))

#Creación del símbolo tau mediante su código Unicode
tau_simbolo = '\u03C4'

#Creación del símbolo de grados usando Unicode
simbolo_grados = '\u00B0'

#Creación de la variable p03 con 0 y 3 como subíndices (p_03 no es un dato de
#entrada, pero se mostrará en el archivo de texto para definir la relación de
#presiones totales)
p03_texto = "p03"
p03_con_subindice = p03_texto.replace("03", convertir_a_subindice("03"))


######################## INICIO ARCHIVO DATOS DE ENTRADA ######################

#Se almacena en una variable el nombre del archivo de texto donde el usuario 
#tendrá que introducir los datos de entrada
nombre_archivo = 'Datos_entrada.txt'

#Con el siguiente condicional, haciendo uso del módulo os, se comprueba si 
#el archivo ya existe o no
if not os.path.exists(nombre_archivo):
    #Si no existe (primera compilación del código), entonces se crea a continuación
    #un archivo mediante la función "open()", en modo 'w' (solo escritura), 
    #donde se escribe todo lo que verá el usuario en el archivo (la solicitud de
    #todos los datos de entrada). Una vez que este archivo se cree, ya no se 
    #volverá a entrar en este condicional porque ya existirá el archivo con el 
    #nombre 'Datos_entrada.txt', por lo que no habrá problemas de que se 
    #sobreescriba o que surjan errores por coincidencia de nombres de archivos.
    #Además, con el archivo creado en la primera compilación, el usuario podrá 
    #probar diferentes datos de entrada tantas veces como quiera, solo tendrá 
    #que compilar de nuevo, modificar el archivo de texto y guardar los cambios    
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        
        archivo.write("Por favor, introduzca los siguientes datos de entrada:\n\n")
        
        archivo.write(f"·Ángulo de la velocidad absoluta a la entrada del rodete ({alfa1_con_subindice}) en ({simbolo_grados}). Tenga en cuenta que en este programa se van a analizar los casos para los que {alfa1_con_subindice}\u22650{simbolo_grados}: \n\n")

        archivo.write(f"·Ángulo geométrico de salida del rodete ({beta2_con_subindice}') en ({simbolo_grados}). Tenga en cuenta que en este programa se van a analizar los casos para los que 0{simbolo_grados}\u2264{beta2_con_subindice}'\u226445{simbolo_grados}: \n\n")
        
        archivo.write(f"·Presión de remanso a la entrada del rodete ({p01_con_subindice}) en (kPa): \n\n")
        
        archivo.write(f"·Temperatura de remanso a la entrada del rodete ({T01_con_subindice}) en (K): \n\n")
        
        archivo.write(f"·Calor específico a presión constante del aire ({cp_con_subindice}) en (kJ/(kg·K)): \n\n")
        
        archivo.write(f"·Índice adiabático del aire ({gamma_simbolo}): \n\n")
        
        archivo.write("·Gasto másico (G) en (kg/s): \n\n")
        
        archivo.write(f"·Relación de presiones totales (r={p03_con_subindice}/{p01_con_subindice}): \n\n")
        
        archivo.write(f"·Esfuerzo de torsión máximo admisible del eje ({tau_simbolo}) en (N/mm\u00B2): \n\n")
                
        archivo.write(f"·Valor del juego entre la cubierta estática y los bordes de los álabes del rodete abierto ({epsilonj_con_subindice}) en (mm): \n\n")
                
    
    print(f"Se ha creado el archivo de texto '{nombre_archivo}'.\n")

#Se pone un input para que la compilación se detenga mientras el usuario introduce
#los datos de entrada, ya que la compilación solo continúa después de un input
#cuando se pulsa la tecla Enter
input(f"Por favor, introduzca en el archivo de texto '{nombre_archivo}' los datos de entrada y guarde los cambios. Después, pulse la tecla Enter (con el cursor situado en la línea siguiente a donde acabe este mensaje) para comenzar con la secuencia de cálculo.\n")

#Se abre el archivo de texto mediante la función "open()", pero en este caso 
#en modo 'r' (solo lectura)
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    #Se usa "readlines()" para leer todas las líneas del archivo de texto,
    #almacenándolas en la variable "lineas"
    lineas = archivo.readlines()

#El siguiente paso es procesar todas las líneas leídas para extraer los datos de
#entrada

#Se crea el diccionario "datos" donde se almacenarán los datos de entrada 
#extraídos del archivo de texto
datos = {}

#Se inicializa la variable "j" que será de utilidad en el próximo bucle for
j=1

#El siguiente bucle for irá recorriendo las líneas del archivo y extrayendo los
#datos de entrada

#En la condición del bucle for, se asigna a la variable "linea" la línea de 
#"lineas[1:]" que corresponda en cada iteración. Por otro lado, como la primera
#línea de la lista "lineas" (donde están guardadas todas las líneas del archivo
#de texto) no contiene un dato de entrada, se comenzará a procesar por la segunda
#línea, que corresponderá al número "1"; de ahí el poner "1" en "lineas[1:]". 
for linea in lineas[1:]:  
    
    #Con el siguiente condicional, solo extraerá el dato de entrada de una línea
    #si en esa línea encuentra ":". En todas las líneas en las que se solicitan
    #datos hay ":", por lo que en esas se extraerán datos. En las líneas vacías,
    #sin embargo, como no se encontrará ":", no se entrará en el "if" y en esa 
    #iteración del bucle for no se hará nada. Además, solo se sumará 1 a j cuando
    #se entre en el "if", para que así solo se sume 1 a j cuando se extraigan 
    #datos de entrada y estén guardados correctamente como: dato1, dato2, etc, 
    #que es lo que se hará dentro del for con "datos[f'dato{j}'] = valor"
    if ':' in linea:
        
        #Con la función "split('delimitador')", se puede dividir una cadena de 
        #caracteres en dos subcadenas a partir de especificar un delimitador 
        #entre ambas subcadenas. En este caso, se asignará a la variable "_" lo
        #que haya antes de los ':' (no se utilizará) en cada línea del archivo 
        #de texto y a "valor" el dato de entrada introducido en cada línea
        _, valor = linea.split(':') 
        
        #Con la función "strip()" se eliminan los espacios en blanco al principio
        #y al final de la variable "valor"
        valor = valor.strip()
        
        #Se guarda en el diccionario "datos" el dato de entrada extraído del
        #archivo de texto en cada iteración. Entre [] se pondrá el nombre con
        #el que se guardará el dato de entrada en el diccionario
        datos[f'dato{j}'] = valor
        
        #Se suma 1 al valor de j, que será el valor utilizado en la siguiente
        #iteración
        j += 1

#Por último, se asignan a unas variables los valores guardados en el diccionario
#"datos". Para ello, se ha de tener en cuenta el orden en el que se solicitaron
#los datos de entrada en el archivo de texto, de forma que dato1 será el primero,
#dato2 el segundo, etc
alfa_1_grados = float(datos.get('dato1'))

#En este código "beta_2" será la variable en la que se guardará el ángulo del 
#álabe a la salida del rodete, ya que no se puede usar una comilla en una 
#variable (al usuario se le presenta el ángulo del álabe con comilla). Para hacer
#referencia al ángulo teniendo en cuenta el deslizamiento, esto se especificará
#y se llamará a dicha variable "beta_2_desl"
beta_2_grados = float(datos.get('dato2'))

#Se multiplica por 1000 la presión introducida por el usuario en (kPa) para 
#realizar los cálculos con (Pa) 
p_01 = float(datos.get('dato3'))*1000
        
T_01 = float(datos.get('dato4'))
      
#Se multiplica por 1000 el valor introducido por el usuario para trabajar con 
#(J/(kg·K)) en lugar de (kJ/(kg·K))
c_p = float(datos.get('dato5'))*1000

gamma = float(datos.get('dato6'))
        
G = float(datos.get('dato7'))

r = float(datos.get('dato8'))

#Se multiplica por 10**6 el valor introducido por el usuario para trabajar con 
#(N/m**2) en lugar de (N/mm**2)
tau = float(datos.get('dato9'))*(10**6)
                
#Se divide por 1000 el valor introducido por el usuario para trabajar con 
#(m) en lugar de (mm)
epsilon_j = float(datos.get('dato10'))/1000

            
######################## FIN ARCHIVO DATOS DE ENTRADA #########################

"""
1. Rangos de validez de alfa_1 y beta'_2 (ángulo del álabe), cálculo del número
 de álabes del rodete y consideraciones
"""

#Mensaje de error por si se introduce un alfa_1<0
if alfa_1_grados < 0:
        print(f"Valor de {alfa1_con_subindice} no válido. Por favor, compile de nuevo e introduzca un valor que cumpla {alfa1_con_subindice}\u22650{simbolo_grados}.\n")

#Mensaje de error por si se introduce un beta'_2 < 0º o beta'_2 > 45º
if beta_2_grados < 0 or beta_2_grados > 45:
        print(f"Valor de {beta2_con_subindice}' no válido. Por favor, compile de nuevo e introduzca un valor que cumpla 0{simbolo_grados}\u2264{beta2_con_subindice}'\u226445{simbolo_grados}.\n")

"""
A continuación se va a calcular el número de álabes del rodete a partir del ángulo
beta'_2 introducido por el usuario. 

En caso de que se obtenga un número de álabes no entero, se redondeará al entero
más cercano y se recalculará beta'_2 para dicho número de álabes. Por tanto, en 
ese caso el valor de beta'_2 introducido por el usuario será ligeramente corregido.
"""

#Cálculo del número de álabes del rotor
Z_r=(90-beta_2_grados)/3

#En el siguiente condicional lo que se hará es mantener el valor obtenido
#de Z_r si sale entero, y si no, se redondeará al más cercano
if (Z_r-int(Z_r)) == 0: #Esta condición se cumple solo si Z_r es un número entero
    Z_r_final=int(Z_r)
    
else:
    Z_r_final=int(round(Z_r, 0))
    
    #Cálculo del valor corregido de beta'_2 a partir de Z_r_final
    beta_2_grados=90-3*Z_r_final
    
    print(f"Aviso: El ángulo {beta2_con_subindice}' introducido ha sido corregido a {beta_2_grados}{simbolo_grados} para poder obtener un valor entero para el número de álabes del rodete.\n")

    
print("Consideraciones:\n")

#Creación de la variable cm1 poniendo m y 1 como subíndices
cm1_texto = "cm1"
cm1_con_subindice = cm1_texto.replace("m1", convertir_a_subindice("m1"))

#Creación de la variable cm2 poniendo m y 2 como subíndices
cm2_texto = "cm2"
cm2_con_subindice = cm2_texto.replace("m2", convertir_a_subindice("m2"))

#Se muestra un mensaje con la consideración de c_m1=c_m2
print(f"·Se considera que la velocidad meridiana en el rodete se conserva: {cm1_con_subindice}={cm2_con_subindice}.\n")

#Creación de la variable b2 poniendo 2 como subíndice
b2_texto = "b2"
b2_con_subindice = b2_texto.replace("2", convertir_a_subindice("2"))

#Creación de la variable b3 poniendo 3 como subíndice
b3_texto = "b3"
b3_con_subindice = b3_texto.replace("3", convertir_a_subindice("3"))

#Se muestra un mensaje con la consideración de b_2=b_3
print(f"·Se considera que los anchos axiales de entrada y salida del difusor son iguales: {b2_con_subindice}={b3_con_subindice}.\n")


"2. Estimación de la potencia y cálculo de Q (caudal volumétrico)"


"""
En principio, siempre que sea posible se calcularán todas las propiedades del 
aire mediante la librería "CoolProp". Sin embargo, en ciertos puntos de la 
secuencia será necesario adoptar la hipótesis de gas perfecto; como por ejemplo
para la estimación de valores iniciales de ciertas variables. Por esta razón se
piden como datos de entrada el calor específico a presión constante y el 
coeficiente de expansión adiabática del aire.

"""

#c_v del aire
c_v=c_p/gamma 

#R del aire
R_aire=c_p-c_v 


"""
Por otro lado, para determinar el radio interior de entrada r_1i (lo cual se 
realizará en el bucle de ns (ns es el número específico de revoluciones)), antes
se ha de calcular el diámetro del eje, para lo que, a su vez, se han de determinar: 
la potencia y la velocidad angular. De esos 2 términos, la potencia se calculará
antes de entrar en el bucle de ns, para no calcular el mismo valor en cada 
iteración. En cuanto a la velocidad angular, esta sí se calculará dentro del 
bucle ns, ya que depende de ns.

A continuación, se va a estimar la potencia.
"""

"""
Estimación de la potencia:

    Potencia=trabajo_esp*G 

Donde trabajo_esp es el trabajo específico, el cual depende del rendimiento total
a total eta_tt, para el cual se considerará inicialmente un valor intermedio en
la práctica de 0.775.  

El anterior valor de 0.775 se puede considerar como intermedio debido a que, 
según la empresa "Atlas Copco", el rango normal para el rendimiento de un 
compresor centrífugo es de entre un 70% y un 85%.

Ese 0.775 naturalmente no será el valor final del rendimiento, pero no hay problema
en suponer inicialmente ese valor para estimar trabajo_esp y con ello
la potencia para determinar r_1i, ya que en la bibliografía se argumenta que se
ha de suponer un valor inicial aproximado para eta_tt para estimar el trabajo 
específico, señalando además que si se diera el caso de que el rendimiento 
estimado resultase diferente del real, esto no afectaría esencialmente a las 
dimensiones del compresor.

Al igual que se ha comentado para el rendimiento, los valores finales del trabajo
específico y la potencia no serán los estimados para determinar r_1i, sino que se
calcularán más adelante a partir de las propiedades termodinámicas calculadas
a lo largo de la secuencia de cálculo.
"""

#Creación del símbolo eta mediante su código Unicode
eta_simbolo = '\u03B7'

#Creación de la variable etatt con las t como subíndices
eta_tt_texto = f"{eta_simbolo}tt"
eta_tt_con_subindice = eta_tt_texto.replace("tt", convertir_a_subindice("tt"))

#Se asigna al rendimiento un valor intermedio en la práctica de 0.775
eta_tt=0.775

#Para calcular trabajo_esp, antes será necesario calcular el salto isentrópico 
#total y total, el cual se puede estimar a partir de la siguiente ecuación
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
#Se guarda en una variable que el fluido será aire, para indicarlo cuando se 
#utilice CoolProp
fluido = 'Air'  

#Cálculo de la densidad de remanso a la entrada del rodete con CoolProp
densidad_01 = CP.PropsSI('D', 'T', T_01, 'P', p_01, fluido)

#Cálculo de Q
Q=G/densidad_01


"""
Por otro lado, a continuación se van a calcular algunos términos que serán 
necesarios más adelante dentro del bucle de ns.
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

"3. Bucle de ns"

"""
El bucle de ns se extenderá hasta que se muestren los resultados finales, es 
decir, prácticamente toda la secuencia de cálculo estará dentro de dicho bucle porque
la misma tendrá que repetirse si el valor probado de ns provoca que
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

Nota: el final del bucle de ns está claramente señalado.
"""

#Bucle de ns
while ns >= 0.5 and ns <= 0.8 and t==1:

    "3.1 Cálculo del radio interior de entrada r_1i"
    
    #El régimen de giro n (rev/s) está dado por la siguiente ecuación
    n=(ns*(Delta_h_stt**(3/4)))/(2*pi*(Q**(1/2)))

    #La velocidad angular omega (rad/s) será
    omega=2*pi*n

    #Cálculo del diámetro del eje
    d_e=((16*Potencia)/(omega*pi*tau))**(1/3)

    #Finalmente ya se puede determinar d_1i y con ello r_1i
    d_1i=d_e+0.025

    r_1i=d_1i/2
    
    
    "3.2 Cálculo del ángulo de la velocidad relativa a la entrada del rodete en el radio exterior (beta_1e)"

    """
    En este apartado se va a realizar el cálculo de beta_1e, ya que este será 
    necesario para el bucle 1, que se verá más adelante.                                       
    """
        
    """   
    El procedimiento que se va a programar a continuación para el cálculo
    beta_1e se resume en lo siguiente: se trata de encontrar el máximo de una 
    función F que se definirá más adelante en el rango 0° <= beta_1e <= 90°; de
    forma que beta_1e será la abscisa de dicho máximo. 
            
    Se comenzará dando un valor al único parámetro de la expresión de F
    que es desconocido hasta el momento: el número de Mach de la velocidad
    relativa en el radio exterior de entrada al rodete (M_w1e). Se le dará
    un valor de 0.85 (podría haberse escogido otro menor que 1, ya que 
    el máximo de F no varía con el valor de M_w1e). Es importante
    recalcar que este valor de 0.85 no será de ninguna manera el final 
    para M_w1e, el cual se calculará más adelante, solo se le da ese valor
    en este momento para calcular beta_1e.
    """
    M_w1e_calculo_beta_1e=0.85
            
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
            
    Como se ha comprobado (no en este código sino en el TFG asociado) que en el
    rango 0° <= beta_1e <= 90°, F no toma valores negativos, el valor inicial 
    que se le dará a F_ant_iteracion será precisamente negativo, asegurando así
    que en la 1ª iteración el valor de F será mayor a F_ant_iteracion y por tanto
    se guardará beta_1e=0 como el primer valor de beta_1e correspondiente al mayor
    valor de F evaluado.
    """
    F_ant_iteracion=-1
            
    #Bucle para el cálculo de beta_1e correspondiente al máximo de F en
    #el rango 0° <= beta_1e <= 90°
    while beta_1e_bucle_grados >= 0 and beta_1e_bucle_grados <= 90:
        #Numerador de F
        #Num=(M_w1e_calculo_beta_1e**3)*(cos_beta_1e**3)*(tg_beta_1e+tg_alfa_1)**2
        
        #Donde se han de calcular: cos_beta_1e y tg_beta_1e
        
        #Conversión de beta_1e de grados a radianes
        beta_1e_bucle_radianes = float(mp.radians(beta_1e_bucle_grados))

        #Cálculo de cos_beta_1e
        cos_beta_1e = float(mp.cos(beta_1e_bucle_radianes))
                
        #Cálculo de tg_beta_1e
        tg_beta_1e = float(mp.tan(beta_1e_bucle_radianes))
                
        #Por tanto, ya se puede calcular Num
        Num=(M_w1e_calculo_beta_1e**3)*(cos_beta_1e**3)*((tg_beta_1e+tg_alfa_1)**2)
                     
        #Denominador de F
        Den=(1+(0.5*(gamma-1)*(M_w1e_calculo_beta_1e**2)*(cos_beta_1e**2)*(1/(cos_alfa_1**2))))**((1/(gamma-1))+(3/2))
                
        #Luego el valor de F en cada iteración (para cada beta_1e) estará 
        #dado por
        F=Num/Den
                
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
        iteración.
        """
        F_ant_iteracion=F
        
        #Fin del bucle aumentando el valor de beta_1e en 0.1° para la 
        #siguiente iteración
        beta_1e_bucle_grados += 0.1
                
        
    "3.3 Bucle 1: Optimización de la sección de entrada"

    #Antes de comenzar con el bucle 1, se van a calcular algunos valores que serán 
    #necesarios para el mismo

    #En primer lugar, se convierte beta_1e (calculado en el anterior apartado) 
    #de grados a radianes
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

    #Cálculo con CoolProp de la entropía específica de remanso a la entrada del 
    #rodete
    s_01=CP.PropsSI('S', 'T', T_01, 'P', p_01, fluido)

    #La entropía específica estática en 1 será igual a la de remanso 
    s_1=s_01
    

    """
    Para iniciar el bucle 1, se debe asginar un valor inicial a r_1e, que 
    será el que se use en la 1ª iteración. Se cogerá el valor del radio interior
    de entrada (r_1i), ya que r_1e tendrá que ser mayor, lógicamente, por lo que 
    ese será el punto de partida del bucle a partir del cual se irán probando 
    valores cada vez mayores hasta que se alcance la convergencia.
    """
    #Valor inicial de r_1e_bucle
    r_1e_bucle = r_1i
    
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

    #Bucle 1 (para alfa_1>=0)
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
        de G_bucle que estén en un pequeño rango alrededor de G.
        """
            
        """
        Comenzando ya con el bucle 1, la ecuación para calcular el gasto 
        másico G_bucle es la siguiente:
            
            G_bucle=pi*((r_1e**2)-(r_1i**2))*densidad_1*c_m1
            
        De donde se desconocen: densidad_1 y c_m1.
            
        c_m1 se puede calcular con la siguiente ecuación:
                
            c_m1=c_1*cos_alfa_1
                
        Donde c_1 puede calcularse mediante la siguiente ecuación:
                
        c_1=((cos_beta_1e*sin_beta_1e_menos_alfa_1)/((cos_alfa_1**2)-(cos_beta_1e**2)))*u_1e 
        """
            
        #Cálculo de u_1e
        u_1e=omega*r_1e_bucle
            
        #Por tanto, ya se puede calcular c_1
        c_1=((cos_beta_1e*sin_beta_1e_menos_alfa_1)/((cos_alfa_1**2)-(cos_beta_1e**2)))*u_1e
            
        #Cálculo de c_m1
        c_m1=c_1*cos_alfa_1
            
        """
        Por otro lado, densidad_1 se puede calcular con CoolProp. También se
        calcularán la temperatura estática T_1 y la presión estática p_1.
        """
        
        #Cálculo con CoolProp de la entalpía específica de remanso a la entrada del
        #rodete
        h_01=CP.PropsSI('H', 'T', T_01, 'P', p_01, fluido)
        
        #Cálculo de la entalpía específica estática a la entrada del rodete
        h_1=h_01-(c_1**2)/2
       
        #Cálculo con CoolProp de T_1
        T_1=CP.PropsSI('T', 'H', h_1, 'S', s_1, fluido)
          
        #Cálculo con CoolProp de p_1 
        p_1=CP.PropsSI('P', 'H', h_1, 'S', s_1, fluido)
           
        #Por tanto, ya se puede calcular densidad_1 con CoolProp
        densidad_1 = CP.PropsSI('D', 'T', T_1, 'P', p_1, fluido)
            
        #Ecuación para calcular el gasto másico G_bucle
        G_bucle=pi*((r_1e_bucle**2)-(r_1i**2))*densidad_1*c_m1
            
        #Asignación a r_1e del valor de r_1e_bucle probado en cada iteración
        r_1e=r_1e_bucle
        
        #Se suma 0.00001 al valor de r_1e_bucle obteniendo así el valor que
        #se probará en la siguiente iteración
        r_1e_bucle += 0.00001 
        #El valor 0.00001 implica que el resultado se obtendrá con una 
        #precisión de una centésima de milímetro. Quizás con una décima 
        #sería suficiente; sin embargo, en ese caso el bucle no converge
        #en algunos casos porque no se han probado suficientes valores 
        #de r_1e_bucle. Al poner 0.00001 en lugar de 0.0001, se prueban más
        #valores de r_1e_bucle y por tanto la convergencia es más probable


    "3.4 Cálculo de: w_1e y M_w1e"
    
    #Cálculo de w_1e
    w_1e=c_m1/cos_beta_1e
        
    #Cálculo de M_w1e
    M_w1e=w_1e/((gamma*R_aire*T_1)**(1/2))
        
        
    "3.5 Cálculo del factor de deslizamiento"

    #El factor de deslizamiento se calculará mediante la ecuación de Stanitz,
    #la cual es válida para el rango de beta'_2 entre 0 y 45 grados, que es el
    #rango permitido por el programa del cual se informa en el archivo de los 
    #datos de entrada
    sigma=1-((0.63*pi)/Z_r_final)
    

    "3.6 Bucle 2"

    #Antes de comenzar con el bucle 2, se van a calcular algunos términos que 
    #serán necesarios para el mismo
    
    #Conversión de beta'_2 de grados a radianes
    beta_2_radianes = float(mp.radians(beta_2_grados))

    #Cálculo de tangente de beta'_2
    tg_beta_2 = float(mp.tan(beta_2_radianes))

    #Cálculo del radio medio de entrada al rodete
    r_1=(0.5*((r_1e**2)+(r_1i**2)))**(1/2)

    #Cálculo de la velocidad tangencial del rodete en r_1
    u_1=omega*r_1

    #Cálculo de la componente tangencial de c_1
    c_u1=c_m1*tg_alfa_1 #Esta expresión es la correspondiente al caso de alfa_1>0;
                        #sin embargo, es válida también para el caso de alfa_1=0,
                        #ya que tg_alfa_1=0, por lo que saldrá c_u1=0

    #Cálculo de la velocidad relativa en r_1
    w_1=(((u_1-c_u1)**2)+(c_m1**2))**(1/2) #Esta expresión también vale para los
                                           #2 casos: alfa_1>0 y alfa_1=0
                   
    #Cálculo de la velocidad tangencial del rodete en r_1i
    u_1i=omega*r_1i                                     
                    
    #Cálculo de la velocidad relativa en r_1i 
    w_1i=(((u_1i-c_u1)**2)+(c_m1**2))**(1/2) #Esta expresión también vale para los
                                             #2 casos: alfa_1>0 y alfa_1=0
                                           
    #Por otro lado, haciendo efectiva una de las consideraciones que se señaló 
    #en el apartado 1, la velocidad meridiana en el rodete se conserva
    c_m2=c_m1

    """
    Para que pueda comenzar el bucle 2, antes se han de inicializar las variables
    que intervienen en el mismo. 
    """
    #El valor mínimo aceptable para el rendimiento de un compresor centrífugo es
    #un 70%, ya que el rango normal, según la empresa "Atlas Copco", es de 
    #entre un 70% y un 85%
    eta_c_minimo=0.7

    """
    El valor inicial del rendimiento será el mínimo aceptable, de forma que se
    probarán valores cada vez mayores del rendimiento a partir de ese mínimo. 
    De esta forma, se asegura que el rendimiento final que se obtenga será 
    aceptable porque será sí o sí mayor que el mínimo que se considera correcto.
    """
    eta_c_bucle = eta_c_minimo

    """
    También se debe inicializar la relación de presiones totales r_prima, ya que 
    interviene en la condición del bucle while. Así, r_prima deberá tomar un 
    valor inicial tal que se cumpla una de la condición "(r_prima < r-0.02 or r_prima > r+0.02)" 
    del bucle while y este pueda comenzar. Un valor que siempre cumplirá la 
    condición será uno negativo, ya que r-0.02 (donde r es la relación de 
    presiones introducida por el usuario) siempre será mayor que un número 
    negativo.
    """
    r_prima=-1
    
    """
    La siguiente condición del bucle es "(eta_c_prima < eta_c_it-0.01 or eta_c_prima > eta_c_it+0.01)",
    que obliga a que el rendimiento obtenido al final del bucle sea prácticamente
    igual (no exactamente igual por lo que se explicó anteriormente de la 
    casi imposibilidad de convergencia por los decimales de muy poco orden) 
    al fijado al comienzo del mismo, lo que le da validez a la iteración para
    la que se produzca la convergencia.
    
    Con la misma explicación que para r_prima, se inicializan las variables para
    este caso (aunque realmente la condición a la que pertenecen estas variables
    daría igual que no se cumpliese en un inicio para entrar en el bucle ya que 
    es una condición que está ligada a la anterior de r_prima con un "or", lo 
    que significa que con que una de las dos se cumpla es suficiente para entrar
    en el bucle).
    """
    
    eta_c_it=1
    
    eta_c_prima=0
    
     
    """
    Por último, se inicializa la variable t_1, que será la que controlará que
    el bucle no siga realizando iteraciones para valores del rendimiento iguales 
    o superiores a 1. Este valor de t_1 tomará en principio un valor de 1, aunque
    podría ser cualquiera, y solo variará si se alcanza un valor del rendimiento
    igual a 1, momento en el que t_1 tomará el valor 0 y ya no se realizarán más 
    iteraciones del bucle 2 porque no se cumplirá la condición t_1 == 1. Esto
    ocurrirá cuando el bucle 2 no converja para valores del rendimiento en el
    rango adecuado de entre 0.7 y 1, y en ese caso habrá que probar otro valor
    para ns (nueva iteración del bucle ns).
    """
    t_1=1
    
    
    #Bucle 2
    while ((r_prima < r-0.02 or r_prima > r+0.02) or (eta_c_prima < eta_c_it-0.01 or eta_c_prima > eta_c_it+0.01)) and t_1 == 1:
        #Cálculo del trabajo específico W_i (no confundir con trabajo_esp, que 
        #fue la variable que se usó para estimar la potencia en el apartado 2)
        W_i=Delta_h_stt/eta_c_bucle
        
        #Cálculo de la velocidad tangencial a la salida del rodete
        u_2=((sigma*c_m1*tg_beta_2)+((((sigma*c_m1*tg_beta_2)**2)+4*sigma*(u_1*c_u1+W_i))**(1/2)))/(2*sigma)
            
        #Cálculo de la componente tangencial de la velocidad absoluta a la 
        #salida del rodete (teniendo en cuenta el deslizamiento)
        c_u2=(W_i+u_1*c_u1)/u_2
            
        #Recordatorio: la variable "beta_2" ya se comentó que realmente haría 
        #referencia a "beta'_2" (áng. del álabe = sin deslizamiento), lo cual no
        #puede usarse como nombre de una variable en Python por la comilla. No 
        #debe asociarse este ángulo a las componentes de velocidad del triángulo
        #a la salida del rodete considerando deslizamiento, para las que no 
        #se usan comillas. Cuando se calcule el ángulo de la velocidad relativa
        #a la salida del rodete con deslizamiento, se señalizará como 
        #"beta_2_desl" para distinguirlo del ángulo del álabe ("beta_2").
            
        """
        En cuanto al ángulo de la velocidad absoluta a la salida del rodete
        alfa_2, este se puede calcular a partir de la siguiente ecuación:
            
            alfa_2=arctan(c_u2/c_m2)
            
        """
    
        #Cálculo alfa_2
        alfa_2_radianes = float(mp.atan(c_u2/c_m2))
        
        #Conversión de alfa_2 de radianes a grados
        alfa_2_grados = float(mp.degrees(alfa_2_radianes))
        
        #Cálculo de la componente tangencial de la velocidad relativa a la salida
        #del rodete
        w_u2=u_2-c_u2

        #Cálculo de la velocidad relativa a la salida del rodete
        w_2=((w_u2**2)+(c_m2**2))**(1/2)
             
        #Cálculo de la velocidad absoluta a la salida del rodete
        c_2=((c_u2**2)+(c_m2**2))**(1/2)
        
        #Cálculo del radio de salida del rodete
        r_2=u_2/omega
        
        
        #Bucle 3
        """
        Este bucle 3, el cual se encuentra dentro del bucle 2, consiste en un 
        procedimiento iterativo donde la variable que controlará la repetición
        o validez de las iteraciones realizadas será el coeficiente de pérdidas
        en el rodete (zeta_R). 
        
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
        zeta_R_prima=0.2 #Se ha tomado como punto de partida 0.2 porque es un 
                         #valor intermedio en la práctica según la bibliografía
                         

        """
        Se da un valor inicial a zeta_R que asegure que se entrará en el bucle 
        debido a que se cumplirá la primera de las 2 condiciones del while:
            
            zeta_R_prima=0.2 < zeta_R-0.001
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
               nuevo valor del coeficiente de pérdidas en el rodete (zeta_R_prima).
            
            4) Una vez determinado zeta_R_prima, se vuelven a comprobar las 
               condiciones del bucle while, de forma que:
                   
                4.1) Si zeta_R_prima es suficientemente similar a zeta_R (valor 
                      probado en la última iteración) el bucle se termina y queda
                      guardado en zeta_R_prima el valor definitivo del coeficiente
                      de pérdidas en el rodete.
                      
                      Nota: no se ha puesto como condición del while que 
                      "zeta_R_prima!=zeta_R" porque esto podría dar problemas de
                      convergencia debido a los decimales de pequeño orden y a 
                      los residuos, como ya se explicó anteriormente para otros
                      bucles. Por ello, se ha establecido un pequeño rango de 
                      valores válidos en torno a zeta_R.
                        
                4.2) Si zeta_R_prima no es suficientemente similar a zeta_R, se 
                     realiza una nueva iteración donde el nuevo valor que se 
                     probará de zeta_R será el valor de zeta_R_prima calculado 
                     en la anterior iteración.
        """

        while zeta_R_prima < zeta_R-0.001 or zeta_R_prima > zeta_R+0.001:
            #Se asigna a zeta_R el valor de zeta_R_prima de la anterior iteración,
            #o el valor inicial en el caso de la primera iteración
            zeta_R = zeta_R_prima
            
            #1) Cálculo de: p_2, T_2, densidad_2, M_2, b_2 y p_02
            
            #1.1) Cálculo de p_2
            
            #Cálculo de la entalpía específica de remanso a la salida del rodete
            h_02=W_i+h_01
            
            #Cálculo de la entalpía específica estática a la salida del rodete
            h_2=h_02-(c_2**2)/2
            
            #Cálculo de la entalpía específica estática en el punto 2s (punto 
            #2 isentrópico del diagrama h-s)
            h_2s=h_2-zeta_R*(w_1e**2)/2
            
            #La entropía específica estática en el punto 2s será igual a la del
            #punto 1
            s_2s=s_1
            
            #Cálculo con CoolProp de la presión estática en el punto 2s a partir
            #de h_2s y s_2s
            p_2s=CP.PropsSI('P', 'H', h_2s, 'S', s_2s, fluido)
            
            #La presión de un punto real y su isentrópico correspondiente es la 
            #misma
            p_2=p_2s
            
            #1.2) Cálculo de T_2
            
            #La temperatura estática en 2 puede calcularse con CoolProp a partir
            #de h_2 y p_2
            T_2=CP.PropsSI('T', 'H', h_2, 'P', p_2, fluido)
            
            #1.3) Cálculo de densidad_2
    
            #La densidad en 2 puede calcularse con CoolProp a partir de T_2 y p_2
            densidad_2=CP.PropsSI('D', 'T', T_2, 'P', p_2, fluido)
            
            #1.4) Cálculo de M_2 
            
            #El número de Mach en 2 se puede calcular a partir de su definición
            M_2=c_2/((gamma*R_aire*T_2)**(1/2))
            
            #1.5) Cálculo de b_2
            
            #El ancho axial a la salida del rodete se puede obtener de la ecuación
            #de continuidad
            b_2=G/(2*pi*r_2*densidad_2*c_m2)
            
            #1.6) Cálculo de p_02
            
            #Cálculo de la entropía específica estática en 2 con CoolProp a 
            #partir de T_2 y p_2
            s_2=CP.PropsSI('S', 'T', T_2, 'P', p_2, fluido)
            
            #La entropía de un punto y su punto de remanso correspondiente es
            #la misma
            s_02=s_2
            
            #Cálculo con CoolProp de la presión de remanso a la salida del rodete
            #a partir de h_02 y s_02
            p_02=CP.PropsSI('P', 'H', h_02, 'S', s_02, fluido)
            
            #Además, se van a calcular s_02s y h_02s, para así poder representar
            #el punto 02s en el diagrama h-s que se realizará al final de la 
            #secuencia de cálculo
            
            #La entropía específica de remanso en el punto 02s será igual a la
            #del punto 1 
            s_02s=s_1
            
            #La presión en 02s será igual a la de 02
            p_02s=p_02
            
            #Cálculo de h_02s con CoolProp a partir de s_02s y p_02s
            h_02s=CP.PropsSI('H', 'S', s_02s, 'P', p_02s, fluido)
            
            
            #2) Cálculo de las pérdidas en el rodete
            
            #2.1) Cálculo de las pérdidas por fricción viscosa en la superficie
            #del conducto (Deltah_sf) (skin friction)
            
            """
            Para poder determinar Deltah_sf, antes se han de calcular una serie
            de términos.
            
            En primer lugar el diámetro hidráulico se calculará como una media
            entre el de entrada y el de salida:
                
            D_h=(D_h1/2)+(D_h2/2)
            
            """
            
            #Cálculo del ángulo de la velocidad relativa en r_1i
            beta_1i_radianes = float(mp.acos(c_m1/w_1i))
            
            #Cálculo de cos_beta_1i
            cos_beta_1i = float(mp.cos(beta_1i_radianes))
        
            cos_beta_1ie = (cos_beta_1e+cos_beta_1i)/2
            
            #Cálculo del diámetro hidráulico a la entrada del rodete 
            D_h1=2*pi*((r_1e**2)-(r_1i**2))/((Z_r_final*(r_1e-r_1i)/(cos_beta_1ie))+(pi*r_1i))
            
            #Cálculo de cos_beta_2
            cos_beta_2 = float(mp.cos(beta_2_radianes))
            
            #Cálculo del diámetro hidráulico a la salida del rodete 
            D_h2=4*(pi*2*r_2*b_2)/(2*(b_2*Z_r_final/cos_beta_2)+(pi*2*r_2))
            
            #Cálculo del diámetro hidráulico medio 
            D_h=(D_h1+D_h2)/2
            
            #Rugosidad relativa del conducto (valor normal en la práctica)
            epsilon_r=0.01
    
            #Cálculo del coeficiente de flujo 
            phi=Q/(pi*(r_2**2)*u_2)
            
            #Cálculo de la longitud axial del rodete
            l_axial=2*r_2*(0.014+(0.023*r_2/r_1i)+1.58*phi)
            
            #Cálculo de la longitud media del conducto
            l=(pi/8)*(2*r_2-r_1e-r_1i-b_2+2*l_axial)*(2/(cos_beta_1ie+cos_beta_2))
            
            #Cálculo de la velocidad media del flujo
            w_media=(2*w_2+w_1e+w_1i)/4
            
            #Cálculo con CoolProp de la viscosidad dinámica en 01
            viscosidad_din_01=CP.PropsSI('V', 'T', T_01, 'P', p_01, fluido)
            
            #Cálculo de la viscosidad cinemática en 01
            viscosidad_cin_01=viscosidad_din_01/densidad_01
            
            #Cálculo del número de Reynolds
            Re_sf=u_2*b_2/viscosidad_cin_01
            
            #Cálculo del logaritmo en base 10
            log_10_f = float(mp.log(((epsilon_r/3.7)**1.1)+(6.9/Re_sf), 10))
            
            #Factor de fricción
            f_sf=1/((-1.8*log_10_f)**2)
            
            #Coeficiente de fricción
            C_sf=f_sf/4
            
            #Finalmente, ya se pueden calcular las pérdidas por fricción viscosa
            Deltah_sf=2*C_sf*(l/D_h)*(w_media**2)
            
            
            #2.2) Cálculo de las pérdidas por engrosamiento y desprendimiento 
            #de la capa límite (Deltah_bl) (blade loading)
            
            """
            Para poder determinar Deltah_bl, antes es necesario calcular el 
            coeficiente de difusión.
            """
            
            #Cálculo del coeficiente de difusión
            D_f=1-(w_2/w_1e)+((0.75*(c_u2*u_2-c_u1*u_1)/(u_2**2))/((w_1e/w_2)*((Z_r_final/pi)*(1-(r_1e/r_2))+2*(r_1e/r_2))))
            
            #Conocido el coeficiente de difusión, ya se pueden calcular estas 
            #pérdidas
            Deltah_bl=0.05*(D_f**2)*(u_2**2)
            
            
            #2.3) Cálculo de las pérdidas intersticiales internas (Deltah_cl) (clearance) 
            Deltah_cl=2*(epsilon_j/b_2)*(((r_1i+r_1e)/(2*r_2))-0.275)*(u_2**2)
            
            
            #2.4) Cálculo de las pérdidas por rozamiento del disco (Deltah_df) (disk friction)
            
            #Diámetro a la salida del rodete
            D_2=2*r_2
            
            #Cálculo del número de Reynolds
            Re_df=u_2*D_2/viscosidad_cin_01 
 
            #Pérdidas por el rozamiento del disco
            Deltah_df=(0.01356*densidad_2*(u_2**3)*(D_2**2))/(G_bucle*(Re_df**0.2))
            
            
            #2.5) Cálculo de las pérdidas por recirculación (Deltah_rc) (recirculation)
            
            sin_h=float(mp.sinh(3.5*(alfa_2_radianes**3)))
            
            #Cálculo de las pérdidas por recirculación
            Deltah_rc=(8*(10**(-5)))*sin_h*((D_f*u_2)**2)
            
            
            #2.6) Cálculo de las pérdidas por fuga (Deltah_lk) (leakage)
            
            #Ancho radial a la entrada del rodete
            b_1=r_1e-r_1i
            
            b_med=(b_1+b_2)/2
            
            r_med=(r_1+r_2)/2
            
            #Pérdidas por fuga
            Deltah_lk=(densidad_2*epsilon_j*u_2*1.332*(r_2*c_u2-r_1*c_u1))/(2*r_med*b_med)
            
            
            #3) Cálculo de las pérdidas totales en el rodete (Y_R) y del coeficiente
            #de pérdidas (zeta_R_prima)
            
            #Para calcular las pérdidas totales, simplemente se suman los distintos
            #tipos calculados
            Y_R=Deltah_sf+Deltah_bl+Deltah_cl+Deltah_df+Deltah_rc+Deltah_lk
            
            #Cálculo del nuevo coeficiente de pérdidas en el rodete
            zeta_R_prima=(Y_R)/((w_1e**2)/2)
            
            #Fin del bucle 3
            

        """
        El siguiente paso del bucle 2 es el cálculo del difusor sin álabes.
        
        En primer lugar, se va a programar un bucle para determinar el valor
        de x=r_3/r_2 (r_3 es el radio a la salida del difusor) correspondiente
        al punto donde la pendiente de la función C_p=f(x=r_3/r_2) (C_p es el 
        coeficiente de aumento de presión. Nota: no confundir con el calor 
        específico a presión constante (c_p)) disminuye considerablemente, lo 
        cual implica que un aumento del tamaño del difusor no produce un aumento
        significativo de presión. 
        
        Ese punto en el que la pendiente disminuye considerablemente se denominará
        punto "A", y se considerará que la pendiente vale 0.11 en dicho punto
        (valor calculado en el TFG asociado).
        
        Así, el bucle que se va a programar calculará el valor de x en el punto
        A, que se denominará x_A.
        
        El funcionamiento del bucle será el siguiente:
            
            1) Se define la ecuación de la derivada de la función C_p con respecto 
               a x, que será una nueva función de x.
               
            2) En cada iteración, se irán probando valores de x desde 1 hasta 
               que la derivada alcance el valor límite de la pendiente (0.11).
               Ese valor de x con el que se alcance el 0.37 será x_A. 
               
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
            
            derivada_Cp < 0.11-0.01
        """
        derivada_Cp=0
        
        #Valor inicial de x
        x=1

        #Bucle para el cálculo de x_A
        while derivada_Cp < 0.11-0.01 or derivada_Cp > 0.11+0.01:
            
            #Cálculo del parámetro Gamma, el cual será necesario para calcular 
            #derivada_Cp. Nota: no confundir con el índice adiabático del gas 
            #(gamma)
            Gamma=1/(1+(tg_alfa_2*0.18*(x-1)))
            
            #Cálculo de la derivada de la función C_p=f(x=r_3/r_2)
            derivada_Cp=(2/((x**3)*((tg_alfa_2**2)+1)))*(((Gamma*tg_alfa_2)**2)+1-(x*0.18*((((Gamma*tg_alfa_2)**2)+1)**(1/2))))
            
            #Asignación a x_A del valor de x probado en cada iteración (al final
            #del bucle quedará guardado en x_A el valor de x de la última 
            #iteración, evitando que se sume 0.001 a dicho valor debido a que
            #el bucle finaliza con: "x += 0.001")
            x_A=x
            
            #Se suma 0.001 al valor de x para obtener el valor que se usará en 
            #la siguiente iteración
            x += 0.001 
            
        
        """
        Una vez determinada x_A, el siguiente paso es calcular el coeficiente de 
        aumento de presión correspondiente a x_A. Para ello, habrá que sustituir
        x_A en la expresión C_p=f(x=r_3/r_2), quedando lo siguiente:
        
            C_pA=(2/((tg_alfa_2**2)+1))*I(x=x_A)
        
        Donde "I" es una integral que, dada su complejidad, debe resolverse
        numéricamente.
        
        """
        
        #Resolución numérica de la integral "I"
        
        #1)Se define el integrando de "I" (se va a usar una nueva variable "y",
        #para no usar de nuevo "x")
        def integrando_I(y):
            return ((((tg_alfa_2**2)/((1+tg_alfa_2*0.18*(y-1))**2))+1)/(y**3))-((0.18/(y**2))*((((tg_alfa_2**2)/((1+tg_alfa_2*0.18*(y-1))**2))+1)**(1/2)))

        #2)Se definen los límites inferior y superior de la integral
        x_i=1
        x_s=x_A
        
        #3)Resolución de la integral usando la función "quad"
        I, error = quad(integrando_I, x_i, x_s)
        #En la variable "error" se guarda el error cometido al calcular la  
        #integral mediante el algoritmo que utiliza la función "quad"
        
        #Una vez resuelta "I", ya se puede determinar el coeficiente de aumento
        #de presión para x_A
        C_pA=(2/((tg_alfa_2**2)+1))*I
        
        """
        De esta manera, ya se han determinado x_A y C_pA.
        
        El siguiente paso para proseguir con el cálculo del difusor sin álabes 
        es determinar el coeficiente de pérdida de presión de remanso Y_p, lo 
        cual se puede realizar mediante la siguiente ecuación:
            
            Y_p=1-C_pA-(c_3/c_2)**2
            
        Donde son conocidos todos los términos excepto la velocidad absoluta a 
        la salida del rodete (c_3).
        """
        
        #Se hace efectiva la consideración que se comentó al comienzo de la
        #secuencia de que los anchos de entrada y salida del difusor serán iguales
        b_3=b_2
        
        #Cálculo de c_3
        c_3=(c_2/x_A)*(((((Gamma*tg_alfa_2)**2)+1)/((tg_alfa_2**2)+1))**(1/2))
        
        #Cálculo de Y_p
        Y_p=1-C_pA-((c_3/c_2)**2)
        
        """
        Una vez determinados x_A, C_pA e Y_p, ya se pueden determinar las 
        condiciones del fluido a la salida del difusor, el triángulo de velocidades
        y el radio de salida.
        """
        
        #Cálculo del radio de salida del difusor
        r_3=x_A*r_2
        
        #Cálculo de la presión estática a la salida del difusor a partir de la 
        #definición de C_p
        p_3=C_pA*(p_02-p_2)+p_2
        
        #Cálculo de la presión de remanso a la salida del difusor a partir de la
        #definición de Y_p
        p_03=p_02-Y_p*(p_02-p_2)
        
        #La entalpía de remanso en el difusor se conserva
        h_03=h_02
        
        #La temperatura de remanso a la salida del difusor puede calcularse con
        #CoolProp a partir de h_03 y p_03
        T_03=CP.PropsSI('T', 'H', h_03, 'P', p_03, fluido)
        
        #Cálculo con CoolProp de la entropía específica de remanso a la salida 
        #del difusor (ya que será necesaria, junto con p_3, para hallar la 
        #temperatura estática)
        s_03=CP.PropsSI('S', 'H', h_03, 'P', p_03, fluido)
        
        #La entropía del punto 3 es igual a la del 03
        s_3=s_03
        
        #De esta forma, la temperatura estática a la salida del difusor puede 
        #calcularse con CoolProp a partir de p_3 y s_3
        T_3=CP.PropsSI('T', 'S', s_3, 'P', p_3, fluido)
        
        #Cálculo con CoolProp de la densidad a la salida del difusor a partir 
        #de p_3 y T_3
        densidad_3 = CP.PropsSI('D', 'T', T_3, 'P', p_3, fluido)
        
        #Cálculo de la componente radial de c_3 a partir de la ecuación de 
        #continuidad aplicada a la salida del difusor
        c_r3=(G_bucle)/(2*pi*r_3*b_3*densidad_3)
        
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
        #con CoolProp a partir de T_3 y p_3
        h_3=CP.PropsSI('H', 'T', T_3, 'P', p_3, fluido)
        
        #La entropía específica estática en el punto 3s será igual a la del 2
        s_3s=s_2
        
        #La presión estática en 3s será igual a la de 3
        p_3s=p_3
        
        #Cálculo de h_3s con CoolProp a partir de s_3s y p_3s
        h_3s=CP.PropsSI('H', 'S', s_3s, 'P', p_3s, fluido)
        
        #Por tanto, ya se pueden calcular las pérdidas en el difusor
        Y_E=h_3-h_3s
  
        #Cálculo del coeficiente de pérdida de energía mecánica en el difusor
        zeta_E=(2*Y_E)/(c_2**2)
        
        #Además, se van a calcular s_3ss, h_3ss, h_03s y s_03s, para así poder 
        #representar los puntos 3ss y 03s en el diagrama h-s que se realizará 
        #al final de la secuencia de cálculo
        
        #La entropía específica estática en el punto 3ss será igual a la del 
        #punto 1 
        s_3ss=s_1
        
        #La presión estática en 3ss será igual a la de 3s 
        p_3ss=p_3s
        
        #Cálculo de h_3ss con CoolProp a partir de s_3ss y p_3ss
        h_3ss=CP.PropsSI('H', 'S', s_3ss, 'P', p_3ss, fluido)
        
        #La entropía específica en el punto 03s será igual a la del punto 2 
        s_03s=s_2
        
        #La presión en 03s será igual a la de 03
        p_03s=p_03
        
        #Cálculo de h_03s con CoolProp a partir de s_03s y p_03s
        h_03s=CP.PropsSI('H', 'S', s_03s, 'P', p_03s, fluido)
        
        
        """
        Finalmente, para acabar con el bucle 2 se van a calcular los siguientes
        términos:
    
            1) Delta_h_stt_prima: valor final del salto isentrópico total a total. 
               Este término ya se estimó al inicio de la secuencia de cálculo 
               a partir de los datos de entrada (incluyendo el uso de gamma), 
               pero a continuación se va a calcular el valor final a partir de 
               los términos calculados en la secuencia de cálculo (ya sin usar 
               c_p y gamma, sino solo a partir de las propiedades calculadas con
               CoolProp).
               
            2) W_i_prima: valor final del trabajo específico; ya que el W_i que 
               se obtuvo al inicio del bucle 2 dependía de Delta_h_stt.
               
            3) Potencia_prima: valor final de la potencia. Este término se estimó
               al inicio de la secuencia de cálculo para calcular
               r_1i, pero a continuación se va a calcular su valor final a partir
               del valor final del trabajo W_i_prima.
               
            4) eta_c_prima: valor final del rendimiento total a total del 
               compresor. Para que el bucle 2 converja, este rendimiento calculado
               al final del bucle 2 debe ser igual que el rendimiento probado 
               al inicio del mismo. Nota: como ya se ha explicado en varias
               ocasiones, no será exactamente igual debido al tema de los decimales
               de poco orden, pero será lo suficientemente similar al estar dentro
               de un pequeño rango alrededor del valor probado al comienzo del
               bucle.
                                                                          
            5) r_prima: valor final de la relación de presiones totales.
               Para que el bucle 2 converja, esta relación de presiones calculada
               al final del bucle 2 debe ser igual al valor introducido como dato
               de entrada por el usuario (no exactamente igual como ya se ha
               explicado, pero lo suficiente).
               
        """
        
        #1) Para calcular Delta_h_stt_prima, antes hay que calcular h_03ss. Para
        #ello, se puede usar la presión p_03ss y la entropía s_03ss
        
        #La presión p_03ss es igual a la del punto 03
        p_03ss=p_03
        
        #La entropía s_03ss es igual a la del punto 01
        s_03ss=s_01
        
        #Cálculo de h_03ss a partir de p_03ss y s_03ss usando CoolProp
        h_03ss=CP.PropsSI('H', 'S', s_03ss, 'P', p_03ss, fluido)
        
        #Cálculo de Delta_h_stt_prima
        Delta_h_stt_prima=h_03ss-h_01
        
        #2) Cálculo de W_i_prima
        W_i_prima=Delta_h_stt_prima+Y_R+Y_E
        
        #3) Cálculo de Potencia_prima
        Potencia_prima=W_i_prima*G_bucle
        
        #Cálculo del rendimiento a partir de Delta_h_stt_prima y W_i_prima
        eta_c_prima=Delta_h_stt_prima/W_i_prima
        
        #Cálculo de r_prima 
        r_prima=p_03/p_01 
        
        """
        A continuación, se va a asignar a eta_c_it el valor de eta_c_bucle 
        probado en cada iteración, de forma que se pueda comprobar si este es 
        suficientemente similar a eta_c_prima (dicha comprobación se realiza en
        la condición de entrada al bucle 2). 
        
        Nota: no se puede comparar eta_c_prima con eta_c_bucle porque el bucle
        finaliza con "eta_c_bucle += 0.001", es decir, cuando se realice la 
        comprobación, en eta_c_bucle ya no estará guardado el valor que se probó
        en la misma iteración en la que se obtuvo eta_c_prima.
        """
        eta_c_it=eta_c_bucle
        
        #Se suma 0.001 al valor de eta_c_bucle para obtener el valor que se 
        #usará en la siguiente iteración
        eta_c_bucle += 0.001 
        
        """
        Se asigna un valor de 0 a t_1 si se llega a un rendimiento de 1, de 
        forma que el bucle no seguirá iterando para valores del rendimiento 
        superiores a 1 (ya que una de las condiciones que tenía que cumplirse
        para entrar de nuevo en el bucle era que t_1=1), por lo que tendrá que 
        realizarse una nueva iteración del bucle ns.
        """
        if eta_c_bucle >= 1: #Se pone >= y no solo == porque por el tema de los
                             #decimales residuales de muy poco orden es poco
                             #probable que se dé un valor exacto de 1.
            t_1=0

        #Fin del bucle 2    
        
    
    """    
    A continuación se van a calcular una serie de parámetros que tienen que 
    estar dentro de ciertos márgenes recomendados.
    """
    
    #1) Relación de radios del rodete (RR)
    RR=r_2/r_1e

    #2) Relación de difusión (RD)
    RD=w_1e/w_2

    #3) 
    BD=b_2/D_2

    
    """    
    Por otro lado, se van a calcular los siguientes parámetros: grado de reacción,
    coeficiente de flujo (velocidades evaluadas a la salida del rodete) y 
    coeficiente de carga.
    """
    
    #1) Grado de reacción (R)
    R=(h_2-h_1)/W_i_prima
    
    #2) Coeficiente de flujo (velocidades evaluadas a la salida del rodete) 
    #phi_2=c_r2/u_2
    
    #La componente radial de c_2 será igual a la velocidad meridiana en 2
    c_r2=c_m2
    
    phi_2=c_r2/u_2
    
    #3) Coeficiente de carga (velocidad evaluada a la salida del rodete)
    psi_2=W_i_prima/(u_2**2)   
    
    
    
    """
    Lo siguiente será una estructura condicional "if-else" que asignará
    t=1 si uno o varios de los parámetros básicos están fuera de los márgenes
    recomendados y t=0 si todos están dentro de los márgenes; además de asignar,
    en el caso de t=0, a ns_final el valor de ns de la iteración en la que se 
    cumpla que todos los parámetros estén dentro de los márgenes. 
    
    Por tanto, como la condición del bucle de ns es "while ns >= 0.5 and ns <= 0.8 and t==1:",
    el funcionamiento de la próxima estructura condicional en relación con el 
    bucle de ns será el siguiente:
        
        -Si t=1 (uno o varios parámetros fuera de márgenes recomendados) y ns 
        está dentro del margen [0.5, 0.8], se seguirán probando valores de ns 
        porque se cumplirán las 2 condiciones del bucle while. Si ns pasa a tener
        un valor fuera del rango [0.5, 0.8] (finaliza el bucle porque no se cumple
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
    
    
    #Nota: si t_1=0 es porque no se ha conseguido la convergencia del bucle 2
    #para valores del rendimiento entre 0.7 y 1, por lo que será necesaria otra
    #iteración del bucle de ns
    if t_1 == 0 or alfa_2_grados < 60 or alfa_2_grados > 70 or RR < 1.2 or RR > 2.2 or RD < 1.25 or RD > 1.65 or BD < 0.02 or BD > 0.12 or M_2 > 1.2 or M_w1e > 1.2:
        t=1
    else:
        t=0
        ns_final=ns
    
    """
    A continuación se tiene una estructura condicional que comprobará la paridad
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
        Se ha usado "round" para redondear a 2 decimales porque pueden aparecer
        decimales residuales de orden muy pequeño que no influyen en los cálculos,
        pero sí podrían hacerlo en la condición del bucle de ns 
        "while ns >= 0.5 and ns <= 0.8 and t==1:", en concreto, en los extremos
        del intervalo de ns.
        """
        
    else: #LA ITERACIÓN EN LA QUE SE ESTÁ ES IMPAR
        #Se resta 0.01 al ns que se probó en la última iteración par
        ns_par=ns_par-0.01
        
        #Se asigna a ns el valor que tomará en la siguiente iteración, la cual
        #será par
        ns=round(ns_par, 2)
        
    paridad_iteracion += 1
    
    
####################### FIN BUCLE ns ####################################### 

#Como ya ha finalizado el bucle ns, se borra el "print("Calculando... Por favor, espere", end='')"
#que se puso justo antes de comenzar el bucle
sys.stdout.write('\r' + ' ' * len("Calculando... Por favor, espere") + '\r')


"""
Para finalizar, se tiene una estructura condicional que creará un archivo de 
texto con los resultados solo si se ha logrado que todos los parámetros básicos
estén dentro de los márgenes recomendados para algún valor de ns en el rango
[0.5, 0.8].

En el caso de que lo anterior no se haya dado, se mostrará un mensaje que 
informará de ello y de que, en consecuencia, será necesario replantearse las 
características básicas del diseño (datos de entrada).
"""

if t==1: #Si se da este caso es porque no hay ningún valor de ns en el rango 
         #[0.5, 0.8] para el que todos los parámetros básicos hayan estado 
         #dentro de los márgenes recomendados, por lo que será necesario 
         #replantearse las características básicas del diseño
    print(f"Para los datos de entrada introducidos se obtienen uno o varios parámetros básicos fuera de los márgenes recomendados, por lo que será necesario replantearse las características básicas del diseño. Cambios no importantes como por ejemplo variar ligeramente {beta2_con_subindice}' u otros parámetros podrían solucionar el problema.")
    
else: #Si se da este caso es porque en el bucle de ns se ha llegado a t=0 (todos 
      #los parámetros están dentro de los márgenes recomendados), por lo que
      #el siguiente paso será crear un archivo de texto con todos los resultados
      #de la secuencia de cálculo, finalizando de esta manera el prediseño
         
    print("                               ", end='') #Con este print se centra 
                                                     #el siguiente cuando
                                                     #aparezca en la consola
    
    print("Resultados:") 
    
    print("")
    
    
    """
    A continuación, antes de mostrar los datos de salida, se van a crear sus 
    símbolos.
    """
    
    #Creación de la variable ns poniendo s como subíndice
    ns_texto = "ns"
    ns_con_subindice = ns_texto.replace("s", convertir_a_subindice("s"))
    
    #Creación del símbolo omega mediante su código Unicode
    omega_simbolo = '\u03A9'
    
    #Creación de la variable r1i poniendo 1 e i como subíndices
    r1i_texto = "r1i"
    r1i_con_subindice = r1i_texto.replace("1i", convertir_a_subindice("1i"))
    
    #Creación de la variable beta1e poniendo 1 y e como subíndices
    beta1e_texto = f"{beta_simbolo}1e"
    beta1e_con_subindice = beta1e_texto.replace("1e", convertir_a_subindice("1e"))
    
    #Creación de la variable r1e con 1 y e como subíndices
    r1e_texto = "r1e"
    r1e_con_subindice = r1e_texto.replace("1e", convertir_a_subindice("1e"))
    
    #Creación de la variable u1e con 1 y e como subíndices
    u1e_texto = "u1e"
    u1e_con_subindice = u1e_texto.replace("1e", convertir_a_subindice("1e"))
    
    #Creación de la variable c1 con 1 como subíndice
    c1_texto = "c1"
    c1_con_subindice = c1_texto.replace("1", convertir_a_subindice("1"))
    
    #Creación de la variable ca1 con a y 1 como subíndices
    ca1_texto = "ca1"
    ca1_con_subindice = ca1_texto.replace("a1", convertir_a_subindice("a1"))
    
    #Creación de la variable cu1 con u y 1 como subíndices
    cu1_texto = "cu1"
    cu1_con_subindice = cu1_texto.replace("u1", convertir_a_subindice("u1"))
    
    #Creación de la variable p1 con 1 como subíndice
    p1_texto = "p1"
    p1_con_subindice = p1_texto.replace("1", convertir_a_subindice("1"))
    
    #Creación de la variable T1 con 1 como subíndice
    T1_texto = "T1"
    T1_con_subindice = T1_texto.replace("1", convertir_a_subindice("1"))
    
    #Creación de la variable h1 con 1 como subíndice
    h1_texto = "h1"
    h1_con_subindice = h1_texto.replace("1", convertir_a_subindice("1"))
    
    #Creación del símbolo rho mediante su código Unicode
    rho_simbolo = '\u03C1'

    #Creación de la variable rho1 con 1 como subíndice
    rho1_texto = f"{rho_simbolo}1"
    rho1_con_subindice = rho1_texto.replace("1", convertir_a_subindice("1"))
    
    #Creación de la variable w1e con 1 y e como subíndices
    w1e_texto = "w1e"
    w1e_con_subindice = w1e_texto.replace("1e", convertir_a_subindice("1e"))
    
    #Creación de la variable wa1e con a, 1 y e como subíndices
    wa1e_texto = "wa1e"
    wa1e_con_subindice = wa1e_texto.replace("a1e", convertir_a_subindice("a1e"))
    
    #Creación de la variable wu1e con u, 1 y e como subíndices
    wu1e_texto = "wu1e"
    wu1e_con_subindice = wu1e_texto.replace("u1e", convertir_a_subindice("u1e"))
    
    #Creación de la variable Mw1e con w, 1 y e como subíndices
    Mw1e_texto = "Mw1e"
    Mw1e_con_subindice = Mw1e_texto.replace("w1e", convertir_a_subindice("w1e"))
    
    #Creación de la variable Zr con r como subíndice
    Zr_texto = "Zr"
    Zr_con_subindice = Zr_texto.replace("r", convertir_a_subindice("r"))
    
    #Creación del símbolo sigma mediante su código Unicode
    sigma_simbolo = '\u03C3'
    
    #Creación de la variable Wi con i como subíndice
    Wi_texto = "Wi"
    Wi_con_subindice = Wi_texto.replace("i", convertir_a_subindice("i"))
    
    #Creación de la variable u2 con 2 como subíndice
    u2_texto = "u2"
    u2_con_subindice = u2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación de la variable w2 con 2 como subíndice
    w2_texto = "w2"
    w2_con_subindice = w2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación de la variable wr2 con r y 2 como subíndices
    wr2_texto = "wr2"
    wr2_con_subindice = wr2_texto.replace("r2", convertir_a_subindice("r2"))
    
    #Creación de la variable wu2 con u y 2 como subíndices
    wu2_texto = "wu2"
    wu2_con_subindice = wu2_texto.replace("u2", convertir_a_subindice("u2"))
    
    #Creación de la variable c2 con 2 como subíndice
    c2_texto = "c2"
    c2_con_subindice = c2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación de la variable cr2 con r y 2 como subíndices
    cr2_texto = "cr2"
    cr2_con_subindice = cr2_texto.replace("r2", convertir_a_subindice("r2"))
    
    #Creación de la variable cu2 con u y 2 como subíndices
    cu2_texto = "cu2"
    cu2_con_subindice = cu2_texto.replace("u2", convertir_a_subindice("u2"))
    
    #Creación de la variable alfa2 con 2 como subíndice
    alfa2_texto = f"{alfa_simbolo}2"
    alfa2_con_subindice = alfa2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación de la variable r2 con 2 como subíndice
    r2_texto = "r2"
    r2_con_subindice = r2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación de la variable T2 con 2 como subíndice
    T2_texto = "T2"
    T2_con_subindice = T2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación de la variable h2 con 2 como subíndice
    h2_texto = "h2"
    h2_con_subindice = h2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación de la variable p2 con 2 como subíndice
    p2_texto = "p2"
    p2_con_subindice = p2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación de la variable rho2 con 2 como subíndice
    rho2_texto = f"{rho_simbolo}2"
    rho2_con_subindice = rho2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación de la variable M2 con 2 como subíndice
    M2_texto = "M2"
    M2_con_subindice = M2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación del símbolo Delta mediante su código Unicode
    Delta_simbolo = '\u0394'
    
    #Creación de la variable Deltahtr con t y r como subíndices
    Deltahtr_texto = f"{Delta_simbolo}htr"
    Deltahtr_con_subindice = Deltahtr_texto.replace("tr", convertir_a_subindice("tr"))
    
    #Creación de la variable Yr con r como subíndice
    Yr_texto = "Yr"
    Yr_con_subindice = Yr_texto.replace("r", convertir_a_subindice("r"))
    
    #Creación del símbolo zeta mediante su código Unicode
    zeta_simbolo = '\u03B6'
    
    #Creación de la variable zetar con r como subíndice
    zetar_texto = f"{zeta_simbolo}r"
    zetar_con_subindice = zetar_texto.replace("r", convertir_a_subindice("r"))
    
    #Creación de la variable r3 con 3 como subíndice
    r3_texto = "r3"
    r3_con_subindice = r3_texto.replace("3", convertir_a_subindice("3"))
    
    #Creación de la variable T3 con 3 como subíndice
    T3_texto = "T3"
    T3_con_subindice = T3_texto.replace("3", convertir_a_subindice("3"))
    
    #Creación de la variable h3 con 3 como subíndice
    h3_texto = "h3"
    h3_con_subindice = h3_texto.replace("3", convertir_a_subindice("3"))
    
    #Creación de la variable p3 con 3 como subíndice
    p3_texto = "p3"
    p3_con_subindice = p3_texto.replace("3", convertir_a_subindice("3"))
    
    #Creación de la variable rho3 con 3 como subíndice
    rho3_texto = f"{rho_simbolo}3"
    rho3_con_subindice = rho3_texto.replace("3", convertir_a_subindice("3"))
    
    #Creación de la variable c3 con 3 como subíndice
    c3_texto = "c3"
    c3_con_subindice = c3_texto.replace("3", convertir_a_subindice("3"))
    
    #Creación de la variable cr3 con r y 3 como subíndices
    cr3_texto = "cr3"
    cr3_con_subindice = cr3_texto.replace("r3", convertir_a_subindice("r3"))
    
    #Creación de la variable cu3 con u y 3 como subíndices
    cu3_texto = "cu3"
    cu3_con_subindice = cu3_texto.replace("u3", convertir_a_subindice("u3"))
    
    #Creación de la variable alfa3 con 3 como subíndice
    alfa3_texto = f"{alfa_simbolo}3"
    alfa3_con_subindice = alfa3_texto.replace("3", convertir_a_subindice("3"))
    
    #Creación de la variable Ye con e como subíndice
    Ye_texto = "Ye"
    Ye_con_subindice = Ye_texto.replace("e", convertir_a_subindice("e"))
    
    #Creación de la variable zetae con e como subíndice
    zetae_texto = f"{zeta_simbolo}e"
    zetae_con_subindice = zetae_texto.replace("e", convertir_a_subindice("e"))
    
    #Creación de la variable Cp con p como subíndice
    C_p_texto = "Cp"
    C_p_con_subindice = C_p_texto.replace("p", convertir_a_subindice("p"))
    
    #Creación de la variable Yp con p como subíndice
    Y_p_texto = "Yp"
    Y_p_con_subindice = Y_p_texto.replace("p", convertir_a_subindice("p"))
    
    #Creación de la variable r1 con 1 como subíndice
    r1_texto = "r1"
    r1_con_subindice = r1_texto.replace("1", convertir_a_subindice("1"))

    #Creación del símbolo phi mediante su código Unicode
    phi_simbolo = '\u03A6'
    
    #Creación de la variable phi2 con 2 como subíndice
    phi2_texto = f"{phi_simbolo}2"
    phi2_con_subindice = phi2_texto.replace("2", convertir_a_subindice("2"))
    
    #Creación del símbolo psi mediante su código Unicode
    psi_simbolo = '\u03C8'
    
    #Creación de la variable psi2 con 2 como subíndice
    psi2_texto = f"{psi_simbolo}2"
    psi2_con_subindice = psi2_texto.replace("2", convertir_a_subindice("2"))

    """
    Además, puesto que todas las variables calculadas durante la secuencia de
    cálculo están en el Sistema Internacional y, como para mostrar los resultados
    puede ser necesario realizar cambios de unidades, estos se van a realizar
    a continuación, antes de crear el archivo de los datos de salida.
    """
    
    #Cambio de Potencia_prima: (W) a (kW)
    Potencia_kW=Potencia_prima/1000
    
    #Cambio de W_i_prima: (J/kg) a (kJ/kg)
    W_i_kJ_kg=W_i_prima/1000
    
    #Cambio de r_1i: (m) a (mm)
    r_1i_mm=r_1i*1000
    
    #Cambio de r_1: (m) a (mm) 
    r_1_mm=r_1*1000
    
    #Cambio de r_1e: (m) a (mm) 
    r_1e_mm=r_1e*1000
    
    #Cambio de p_1: (Pa) a (kPa) 
    p_1_kPa=p_1/1000

    #Cambio de h_1: (J/kg) a (kJ/kg)
    h_1_kJ_kg=h_1/1000
    
    #Cambio de r_2: (m) a (mm) 
    r_2_mm=r_2*1000
    
    #Cambio de p_2: (Pa) a (kPa) 
    p_2_kPa=p_2/1000
    
    #Cambio de h_2: (J/kg) a (kJ/kg)
    h_2_kJ_kg=h_2/1000

    #Cambio de b_2: (m) a (mm) 
    b_2_mm=b_2*1000
    
    #Cambio de b_3: (m) a (mm) 
    b_3_mm=b_3*1000
    
    #Cambio de Deltah_sf: (J/kg) a (kJ/kg)
    Deltah_sf_kJ_kg=Deltah_sf/1000
    
    #Cambio de Deltah_bl: (J/kg) a (kJ/kg)
    Deltah_bl_kJ_kg=Deltah_bl/1000
    
    #Cambio de Deltah_cl: (J/kg) a (kJ/kg)
    Deltah_cl_kJ_kg=Deltah_cl/1000
    
    #Cambio de Deltah_df: (J/kg) a (kJ/kg)
    Deltah_df_kJ_kg=Deltah_df/1000
    
    #Cambio de Deltah_rc: (J/kg) a (kJ/kg)
    Deltah_rc_kJ_kg=Deltah_rc/1000
    
    #Cambio de Deltah_lk: (J/kg) a (kJ/kg)
    Deltah_lk_kJ_kg=Deltah_lk/1000
    
    #Cambio de Y_R: (J/kg) a (kJ/kg)
    Y_R_kJ_kg=Y_R/1000
    
    #Cambio de r_3: (m) a (mm) 
    r_3_mm=r_3*1000
   
    #Cambio de p_3: (Pa) a (kPa) 
    p_3_kPa=p_3/1000
    
    #Cambio de h_3: (J/kg) a (kJ/kg)
    h_3_kJ_kg=h_3/1000
    
    #Cambio de Y_E: (J/kg) a (kJ/kg)
    Y_E_kJ_kg=Y_E/1000
    
    
    """
    A continuación, se van a calcular algunas variables que no han sido de 
    utilidad durante la secuencia de cálculo pero que se mostrarán como datos
    de salida.
    """
    
    #Cálculo de la componente tangencial de w_1e
    w_u1e=u_1e-c_u1
    
    #Cálculo de la componente tangencial de c_3
    c_u3=((c_3**2)-(c_r3**2))**(1/2)
    
    #Cálculo del ángulo de w_2. Nota: es importante no confundir este ángulo,
    #que es teniendo en cuenta el deslizamiento, con el ángulo geométrico de 
    #salida del rodete, el cual está guardado en la variable "beta_2_grados". Al
    #ángulo de w_2 se le denominará "beta_2_desl_grados"
      
    #Cálculo beta_2_desl_radianes
    beta_2_desl_radianes = float(mp.atan(w_u2/c_m2))
    
    #Conversión de beta_2_desl_radianes de radianes a grados
    beta_2_desl_grados = float(mp.degrees(beta_2_desl_radianes))
    
    
    ######################## INICIO ARCHIVO DATOS DE SALIDA ###################
    
    #Se almacena en una variable el nombre del archivo de texto donde se mostrarán
    #los datos de salida
    nombre_archivo_salida = 'Datos_salida.txt'
    
    print(f"A continuación, se creará un archivo de texto denominado '{nombre_archivo_salida}' donde se mostrarán todos los datos de salida del prediseño.\n")
   
    #El por qué del siguiente mensaje informativo se justifica más adelante;
    #concretamente, cuando se cree el archivo con los datos de salida mediante
    #la función "open()" con el modo 'w'. Se ha utilizado "input()" en lugar
    #de "print()" para que al usuario le dé tiempo a realizar la acción que se
    #le solicita en caso de que se cumplan las condiciones del aviso
    input("Aviso: si no es la primera vez que utiliza este programa y quiere conservar el archivo con los datos de salida de un prediseño anterior, deberá modificar su nombre de forma que sea distinto a 'Datos_salida.txt'. De lo contrario, se sobrescribirá. Después, pulse la tecla Enter (con el cursor situado en la línea siguiente a donde acabe este mensaje) para obtener el archivo de texto con los datos de salida del prediseño.\n")
    
    #Se crea un archivo de texto con todos los datos de salida con el modo 'w' 
    #(solo escritura). Nota importante: si se encuentra un archivo existente con
    #el mismo nombre de 'Datos_salida.txt', se sobrescribirá. Para avisar de ello,
    #se puso el anterior "input()"
    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
        
        archivo_salida.write("Datos de salida:\n\n")
        
        archivo_salida.write(f"·Potencia del compresor: P={round(Potencia_kW, 3)} (kW)\n\n")
        
        archivo_salida.write(f"·Trabajo específico en el rodete: {Wi_con_subindice}={round(W_i_kJ_kg, 3)} (kJ/kg)\n\n")

        archivo_salida.write(f"·Rendimiento total a total del compresor centrífugo: {eta_tt_con_subindice}={round(eta_c_prima, 3)}\n\n")
        
        archivo_salida.write(f"·Gasto másico: G={round(G_bucle, 3)} (kg/s)\n\n")
        
        archivo_salida.write(f"·Relación de presiones totales: r={round(r_prima, 2)} \n\n")
        
        archivo_salida.write(f"·Grado de reacción: R={round(R, 2)}\n\n")
        
        archivo_salida.write(f"·Coeficiente de flujo (velocidades evaluadas a la salida del rodete): {phi2_con_subindice}={round(phi_2, 2)}\n\n")
        
        archivo_salida.write(f"·Coeficiente de carga (velocidad evaluada a la salida del rodete): {psi2_con_subindice}={round(psi_2, 2)}\n\n")
        
        archivo_salida.write(f"·Número específico de revoluciones: {ns_con_subindice}={ns_final}\n\n")

        archivo_salida.write(f"·Velocidad angular del compresor: {omega_simbolo}={round(omega, 2)} (rad/s)\n\n")
        
        archivo_salida.write(f"·Radio interior de entrada al rodete: {r1i_con_subindice}={round(r_1i_mm, 1)} (mm)\n\n") 
        
        archivo_salida.write(f"·Radio medio de entrada al rodete: {r1_con_subindice}={round(r_1_mm, 1)} (mm)\n\n") 
        
        archivo_salida.write(f"·Radio exterior de entrada al rodete: {r1e_con_subindice}={round(r_1e_mm, 1)} (mm)\n\n")
        
        archivo_salida.write(f"·Velocidad tangencial en el radio exterior de entrada al rodete: {u1e_con_subindice}={round(u_1e, 2)} (m/s)\n\n")
        
        archivo_salida.write(f"·Velocidad meridiana a la entrada del rodete: {cm1_con_subindice}={round(c_m1, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Velocidad absoluta a la entrada del rodete: {c1_con_subindice}={round(c_1, 2)} (m/s)\n\n")
        
        archivo_salida.write(f"·Ángulo de {c1_con_subindice}: {alfa1_con_subindice}={round(alfa_1_grados, 1)}{simbolo_grados}\n\n")

        #c_a1=c_m1
        archivo_salida.write(f"·Componente axial de {c1_con_subindice}: {ca1_con_subindice}={round(c_m1, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Componente tangencial de {c1_con_subindice}: {cu1_con_subindice}={round(c_u1, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Velocidad relativa en {r1e_con_subindice}: {w1e_con_subindice}={round(w_1e, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Ángulo de {w1e_con_subindice}: {beta1e_con_subindice}={round(beta_1e_grados, 1)}{simbolo_grados}\n\n")

        archivo_salida.write(f"·Mach correspondiente a {w1e_con_subindice}: {Mw1e_con_subindice}={round(M_w1e, 3)}\n\n")

        #w_a1e=c_m1
        archivo_salida.write(f"·Componente axial de {w1e_con_subindice}: {wa1e_con_subindice}={round(c_m1, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Componente tangencial de {w1e_con_subindice}: {wu1e_con_subindice}={round(w_u1e, 2)} (m/s)\n\n")
        
        archivo_salida.write(f"·Temperatura a la entrada del rodete: {T1_con_subindice}={round(T_1, 1)} (K)\n\n")
        
        archivo_salida.write(f"·Presión a la entrada del rodete: {p1_con_subindice}={round(p_1_kPa, 3)} (kPa)\n\n")
        
        archivo_salida.write(f"·Densidad a la entrada del rodete: {rho1_con_subindice}={round(densidad_1, 3)} (kg/m\u00B3)\n\n")

        archivo_salida.write(f"·Entalpía específica estática a la entrada del rodete: {h1_con_subindice}={round(h_1_kJ_kg, 3)} (kJ/kg)\n\n")
    
        archivo_salida.write(f"·Número de álabes del rodete: {Zr_con_subindice}={Z_r_final}\n\n")
        
        archivo_salida.write(f"·Factor de deslizamiento: {sigma_simbolo}={round(sigma, 3)}\n\n")
        
        archivo_salida.write(f"·Radio de salida del rodete: {r2_con_subindice}={round(r_2_mm, 1)} (mm)\n\n")
        
        archivo_salida.write(f"·Ancho axial a la salida del rodete: {b2_con_subindice}={round(b_2_mm, 1)} (mm)\n\n")
        
        archivo_salida.write(f"·Velocidad tangencial a la salida del rodete: {u2_con_subindice}={round(u_2, 2)} (m/s)\n\n")
        
        archivo_salida.write(f"·Velocidad meridiana a la salida del rodete: {cm2_con_subindice}={round(c_m2, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Velocidad absoluta a la salida del rodete: {c2_con_subindice}={round(c_2, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Ángulo de {c2_con_subindice}: {alfa2_con_subindice}={round(alfa_2_grados, 1)}{simbolo_grados}\n\n")

        archivo_salida.write(f"·Componente radial de {c2_con_subindice}: {cr2_con_subindice}={round(c_r2, 2)} (m/s)\n\n")
        
        archivo_salida.write(f"·Componente tangencial de {c2_con_subindice}: {cu2_con_subindice}={round(c_u2, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Velocidad relativa a la salida del rodete: {w2_con_subindice}={round(w_2, 2)} (m/s)\n\n")
        
        archivo_salida.write(f"·Ángulo de {w2_con_subindice}: {beta2_con_subindice}={round(beta_2_desl_grados, 1)}{simbolo_grados}. Nota: no confundir este ángulo, que es teniendo en cuenta el deslizamiento, con el ángulo geométrico de salida del rodete {beta2_con_subindice}').\n\n")

        archivo_salida.write(f"·Ángulo geométrico de salida del rodete: {beta2_con_subindice}'={round(beta_2_grados, 1)}{simbolo_grados}\n\n")

        archivo_salida.write(f"·Número de Mach a la salida del rodete: {M2_con_subindice}={round(M_2, 3)}\n\n")

        #w_r2=c_m2
        archivo_salida.write(f"·Componente radial de {w2_con_subindice}: {wr2_con_subindice}={round(c_m2, 2)} (m/s)\n\n")
        
        archivo_salida.write(f"·Componente tangencial de {w2_con_subindice}: {wu2_con_subindice}={round(w_u2, 2)} (m/s)\n\n")
        
        archivo_salida.write(f"·Temperatura a la salida del rodete: {T2_con_subindice}={round(T_2, 1)} (K)\n\n")
        
        archivo_salida.write(f"·Presión a la salida del rodete: {p2_con_subindice}={round(p_2_kPa, 3)} (kPa)\n\n")
        
        archivo_salida.write(f"·Densidad a la salida del rodete: {rho2_con_subindice}={round(densidad_2, 3)} (kg/m\u00B3)\n\n")
        
        archivo_salida.write(f"·Entalpía específica estática a la salida del rodete: {h2_con_subindice}={round(h_2_kJ_kg, 3)} (kJ/kg)\n\n")

        archivo_salida.write(f"·Pérdidas en el rodete por fricción viscosa en la superficie del conducto (skin friction losses): {Delta_simbolo}h={round(Deltah_sf_kJ_kg, 3)} (kJ/kg)\n\n")
        
        archivo_salida.write(f"·Pérdidas en el rodete por engrosamiento y desprendimiento de la capa límite (blade loading losses): {Delta_simbolo}h={round(Deltah_bl_kJ_kg, 3)} (kJ/kg)\n\n")
        
        archivo_salida.write(f"·Pérdidas intersticiales internas en el rodete (clearance losses): {Delta_simbolo}h={round(Deltah_cl_kJ_kg, 3)} (kJ/kg)\n\n")

        archivo_salida.write(f"·Pérdidas en el rodete por rozamiento del disco (disk friction losses): {Delta_simbolo}h={round(Deltah_df_kJ_kg, 3)} (kJ/kg)\n\n")
        
        archivo_salida.write(f"·Pérdidas en el rodete por recirculación (recirculation losses): {Delta_simbolo}h={round(Deltah_rc_kJ_kg, 3)} (kJ/kg)\n\n")

        archivo_salida.write(f"·Pérdidas en el rodete por fuga (leakage losses): {Delta_simbolo}h={round(Deltah_lk_kJ_kg, 3)} (kJ/kg)\n\n")
        
        archivo_salida.write(f"·Pérdidas totales en el rodete: {Deltahtr_con_subindice}={Yr_con_subindice}={round(Y_R_kJ_kg, 3)} (kJ/kg)\n\n")
        
        archivo_salida.write(f"·Coeficiente de pérdidas en el rodete: {zetar_con_subindice}={round(zeta_R_prima, 3)}\n\n")
        
        archivo_salida.write(f"·Radio de salida del difusor: {r3_con_subindice}={round(r_3_mm, 1)} (mm)\n\n")
        
        archivo_salida.write(f"·Ancho axial a la salida del difusor: {b3_con_subindice}={round(b_3_mm, 1)} (mm)\n\n")

        archivo_salida.write(f"·Velocidad absoluta a la salida del difusor: {c3_con_subindice}={round(c_3, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Ángulo de {c3_con_subindice}: {alfa3_con_subindice}={round(alfa_3_grados, 1)}{simbolo_grados}\n\n")

        archivo_salida.write(f"·Componente radial de {c3_con_subindice}: {cr3_con_subindice}={round(c_r3, 2)} (m/s)\n\n")
        
        archivo_salida.write(f"·Componente tangencial de {c3_con_subindice}: {cu3_con_subindice}={round(c_u3, 2)} (m/s)\n\n")

        archivo_salida.write(f"·Temperatura a la salida del difusor: {T3_con_subindice}={round(T_3, 1)} (K)\n\n")
        
        archivo_salida.write(f"·Presión a la salida del difusor: {p3_con_subindice}={round(p_3_kPa, 3)} (kPa)\n\n")
        
        archivo_salida.write(f"·Densidad a la salida del difusor: {rho3_con_subindice}={round(densidad_3, 3)} (kg/m\u00B3)\n\n")

        archivo_salida.write(f"·Entalpía específica estática a la salida del difusor: {h3_con_subindice}={round(h_3_kJ_kg, 3)} (kJ/kg)\n\n")

        archivo_salida.write(f"·Pérdidas en el difusor: {Ye_con_subindice}={round(Y_E_kJ_kg, 3)} (kJ/kg)\n\n")
        
        archivo_salida.write(f"·Coeficiente de pérdidas en el difusor (pérdida de energía mecánica): {zetae_con_subindice}={round(zeta_E, 3)}\n\n")
        
        archivo_salida.write(f"·Coeficiente de pérdida de presión de remanso en el difusor: {Y_p_con_subindice}={round(Y_p, 2)}\n\n")

        archivo_salida.write(f"·Coeficiente de aumento de presión en el difusor: {C_p_con_subindice}={round(C_pA, 2)}\n\n")
     
        
    print(f"Se ha creado el archivo de texto '{nombre_archivo_salida}' con todos los datos de salida del prediseño.\n")
    
    ######################## FIN ARCHIVO DATOS DE SALIDA ######################

    """
    Para finalizar, se van a obtener los siguientes gráficos:
        
        1) Diagrama h-s.
                                                                          
        2) Triángulo de velocidades a la entrada del rodete en el radio exterior. 
           El eje horizontal será la dirección tangencial y el eje vertical la
           axial.
                                                                        
        3) Triángulo de velocidades a la salida del rodete. 
           El eje horizontal será la dirección tangencial y el eje vertical la 
           radial.                                   
                            
    """

    print("A continuación, se crearán tres archivos JPG: 'Diagrama_h-s.jpg', 'Triángulo_entrada.jpg' (triángulo de velocidades a la entrada del rodete en el radio exterior) y 'Triángulo_salida.jpg' (triángulo de velocidades a la salida del rodete).\n")
       
    input("Aviso: si no es la primera vez que utiliza este programa y quiere conservar los tres archivos JPG de un prediseño anterior, deberá modificar sus nombres de forma que sean distintos a los especificados. De lo contrario, se sobrescribirán. Después, pulse la tecla Enter (con el cursor situado en la línea siguiente a donde acabe este mensaje) para obtener los archivos JPG.\n")
    
    
    "1) Diagrama h-s."  
    
    #Antes de comenzar con la representación del diagrama, se van a cambiar las
    #unidades de las "h" de (J/kg) a (kJ/kg) y de las "s" de (J/kg·K) a (kJ/kg·K)
    
    s_1_kJ_kg_K=s_1/1000
    
    s_2_kJ_kg_K=s_2/1000
    
    s_3_kJ_kg_K=s_3/1000
    
    h_01_kJ_kg=h_01/1000
    
    s_01_kJ_kg_K=s_01/1000
    
    h_2s_kJ_kg=h_2s/1000
    
    s_2s_kJ_kg_K=s_2s/1000
    
    h_3ss_kJ_kg=h_3ss/1000
    
    s_3ss_kJ_kg_K=s_3ss/1000
    
    h_03ss_kJ_kg=h_03ss/1000
    
    s_03ss_kJ_kg_K=s_03ss/1000
    
    h_02s_kJ_kg=h_02s/1000
    
    s_02s_kJ_kg_K=s_02s/1000
    
    h_3s_kJ_kg=h_3s/1000
    
    s_3s_kJ_kg_K=s_3s/1000
    
    h_03s_kJ_kg=h_03s/1000
    
    s_03s_kJ_kg_K=s_03s/1000
    
    h_02_kJ_kg=h_02/1000
    
    s_02_kJ_kg_K=s_02/1000
    
    h_03_kJ_kg=h_03/1000
    
    s_03_kJ_kg_K=s_03/1000
    
    #A continuación, se van a crear arrays para almacenar los puntos que se 
    #visualizarán unidos por una línea en el diagrama

    #Puntos 1-2-3 
    h1_3 = [h_1_kJ_kg, h_2_kJ_kg, h_3_kJ_kg]
    s1_3 = [s_1_kJ_kg_K, s_2_kJ_kg_K, s_3_kJ_kg_K]
    etiquetas1_3 = ['1', '2', '3']

    #Puntos 1-01-2s-3ss-03ss-02s
    h1_02s = [h_1_kJ_kg, h_01_kJ_kg, h_2s_kJ_kg, h_3ss_kJ_kg, h_03ss_kJ_kg, h_02s_kJ_kg]
    s1_02s = [s_1_kJ_kg_K, s_01_kJ_kg_K, s_2s_kJ_kg_K, s_3ss_kJ_kg_K, s_03ss_kJ_kg_K, s_02s_kJ_kg_K]
    etiquetas1_02s = [None, '01', '2s', '3ss', '03ss', '02s']
    
    #Puntos 2-3s-03s-02
    h2_02 = [h_2_kJ_kg, h_3s_kJ_kg, h_03s_kJ_kg, h_02_kJ_kg]
    s2_02 = [s_2_kJ_kg_K, s_3s_kJ_kg_K, s_03s_kJ_kg_K, s_02_kJ_kg_K]
    etiquetas2_02 = [None, '3s', '03s', '02']
    
    #Puntos 3-03
    h3_03 = [h_3_kJ_kg, h_03_kJ_kg]
    s3_03 = [s_3_kJ_kg_K, s_03_kJ_kg_K]
    etiquetas3_03 = [None, '03']
    
    #Puntos 02-03
    h02_03 = [h_02_kJ_kg, h_03_kJ_kg]
    s02_03 = [s_02_kJ_kg_K, s_03_kJ_kg_K]

    #Se crea el gráfico especificando sus dimensiones
    pl.figure(figsize=(10, 6))

    #Se representan los arrays
    pl.plot(s1_3, h1_3, marker='o', linestyle='-', color='k')
    pl.plot(s1_02s, h1_02s, marker='o', linestyle='--', color='k')
    pl.plot(s2_02, h2_02, marker='o', linestyle='--', color='k')
    pl.plot(s3_03, h3_03, marker='o', linestyle='--', color='k')
    pl.plot(s02_03, h02_03, marker='o', linestyle='--', color='k')

    #Se añaden las etiquetas a los puntos
    for i, txt in enumerate(etiquetas1_3):
        pl.annotate(txt, (s1_3[i], h1_3[i]), textcoords="offset points", xytext=(7.5, -10), ha='left', fontsize=12)

    for i, txt in enumerate(etiquetas1_02s):
        pl.annotate(txt, (s1_02s[i], h1_02s[i]), textcoords="offset points", xytext=(6, 2.5), ha='left', fontsize=12)

    for i, txt in enumerate(etiquetas2_02):
        pl.annotate(txt, (s2_02[i], h2_02[i]), textcoords="offset points", xytext=(-7.5, -5), ha='right', fontsize=12)
        
    for i, txt in enumerate(etiquetas3_03):
        pl.annotate(txt, (s3_03[i], h3_03[i]), textcoords="offset points", xytext=(7.5, -5), ha='left', fontsize=12)

    #Se establece el título y las etiquetas de los ejes
    pl.title('Diagrama h-s', fontsize=14)
    pl.xlabel('s (kJ/kg·K)', fontsize=12) 
    pl.ylabel('h (kJ/kg)', fontsize=12) 
    pl.grid(True)
    
    #Se introduce el número de subdivisiones en los ejes
    pl.gca().xaxis.set_major_locator(MaxNLocator(nbins=15))
    pl.gca().yaxis.set_major_locator(MaxNLocator(nbins=10))

    #Se guarda el gráfico en formato JPG
    pl.savefig('Diagrama_h-s.jpg', format='jpg')
    
    
    "2) Triángulo de velocidades a la entrada del rodete en el radio exterior."
    
    """
    En este gráfico, el eje vertical representará la dirección axial, y por tanto
    medirá la magnitud de las componentes axiales de las velocidades, mientras 
    que el eje horizontal representará la dirección tangencial.
    """
    
    #Puntos que forman los lados w_1e y u_1e del triángulo (no se incluye aquí 
    #el lado c_1 por una cuestión de colocación de las etiquetas que identificarán
    #cada lado del triángulo)
    Axial_ent1 = [0, c_m1, c_m1]
    Tangencial_ent1 = [w_u1e, 0, u_1e] 
    etiquetas_ent1 = [f'{w1e_con_subindice}', f'{u1e_con_subindice}']
                    
    #Puntos que forman el lado c_1 del triángulo
    Axial_ent2 = [c_m1, 0]
    Tangencial_ent2 = [u_1e, w_u1e] 
    etiquetas_ent2 = [f'{c1_con_subindice}']
    
    #Puntos de la línea de la altura del triángulo
    Alt_Y_ent = [0, c_m1]
    Alt_X_ent = [w_u1e, w_u1e] 
    etiquetas_alt_ent = [f'{cm1_con_subindice}']
    
    #Se crea el gráfico especificando sus dimensiones
    pl.figure(figsize=(10, 6))

    #Se representan los arrays
    pl.plot(Tangencial_ent1, Axial_ent1, marker='o', linestyle='-', color='k')
    pl.plot(Tangencial_ent2, Axial_ent2, marker='o', linestyle='-', color='k')
    pl.plot(Alt_X_ent, Alt_Y_ent, marker='o', linestyle='--', color='k')
    
    #Se calcula el punto medio de cada línea del triángulo y se añaden las 
    #etiquetas de las velocidades en esos puntos
    for i in range(len(etiquetas_ent1)):
        Tangencial_ent1_mid = (Tangencial_ent1[i] + Tangencial_ent1[i + 1]) / 2
        Axial_ent1_mid = (Axial_ent1[i] + Axial_ent1[i + 1]) / 2
        pl.annotate(etiquetas_ent1[i], (Tangencial_ent1_mid, Axial_ent1_mid), textcoords="offset points", xytext=(-15, -15), ha='center', fontsize=16)
    
    for i in range(len(etiquetas_ent2)):
        Tangencial_ent2_mid = (Tangencial_ent2[i] + Tangencial_ent2[i + 1]) / 2
        Axial_ent2_mid = (Axial_ent2[i] + Axial_ent2[i + 1]) / 2
        pl.annotate(etiquetas_ent2[i], (Tangencial_ent2_mid, Axial_ent2_mid), textcoords="offset points", xytext=(15, -15), ha='center', fontsize=16)

    for i in range(len(etiquetas_alt_ent)):
        Alt_X_ent_mid = (Alt_X_ent[i] + Alt_X_ent[i + 1]) / 2
        Alt_Y_ent_mid = (Alt_Y_ent[i] + Alt_Y_ent[i + 1]) / 2
        pl.annotate(etiquetas_alt_ent[i], (Alt_X_ent_mid, Alt_Y_ent_mid), textcoords="offset points", xytext=(-20, 0), ha='center', fontsize=16)
    
    #Se establece el título y las etiquetas de los ejes
    pl.title('Triángulo de velocidades a la entrada del rodete en el radio exterior', fontsize=14)
    pl.xlabel('Velocidad tangencial (m/s)', fontsize=12) 
    pl.ylabel('Velocidad axial (m/s)', fontsize=12) 
    pl.grid(True)
    
    #Se introduce el número de subdivisiones en los ejes
    pl.gca().xaxis.set_major_locator(MaxNLocator(nbins=20))
    pl.gca().yaxis.set_major_locator(MaxNLocator(nbins=10))
    
    #Con el siguiente código se asegura que una unidad del eje x tenga la misma
    #longitud que una unidad del eje y. De esta forma, se evitan deformaciones
    #en el triángulo
    pl.gca().set_aspect('equal', adjustable='box')

    #Se guarda el gráfico en formato JPG
    pl.savefig('Triángulo_entrada.jpg', format='jpg')
    
    
    "3) Triángulo de velocidades a la salida del rodete."
    
    """
    En este gráfico, el eje vertical representará la dirección radial y el eje 
    horizontal la tangencial.
    """
    
    #Puntos que forman los lados w_2 y u_2 del triángulo
    Radial_sal1 = [0, c_m2, c_m2]
    Tangencial_sal1 = [w_u2, 0, u_2] 
    etiquetas_sal1 = [f'{w2_con_subindice}', f'{u2_con_subindice}']
    
    #Puntos que forman el lado c_2 del triángulo
    Radial_sal2 = [c_m2, 0]
    Tangencial_sal2 = [u_2, w_u2] 
    etiquetas_sal2 = [f'{c2_con_subindice}']
    
    #Puntos de la línea de la altura del triángulo
    Alt_Y_sal = [0, c_m2]
    Alt_X_sal = [w_u2, w_u2] 
    etiquetas_alt_sal = [f'{cm2_con_subindice}']
    
    #Se crea el gráfico especificando sus dimensiones
    pl.figure(figsize=(10, 6))

    #Se representan los arrays
    pl.plot(Tangencial_sal1, Radial_sal1, marker='o', linestyle='-', color='k')
    pl.plot(Tangencial_sal2, Radial_sal2, marker='o', linestyle='-', color='k')
    pl.plot(Alt_X_sal, Alt_Y_sal, marker='o', linestyle='--', color='k')
    
    #Se calcula el punto medio de cada línea del triángulo y se añaden las 
    #etiquetas de las velocidades en esos puntos
    for i in range(len(etiquetas_sal1)):
        Tangencial_sal1_mid = (Tangencial_sal1[i] + Tangencial_sal1[i + 1]) / 2
        Radial_sal1_mid = (Radial_sal1[i] + Radial_sal1[i + 1]) / 2
        pl.annotate(etiquetas_sal1[i], (Tangencial_sal1_mid, Radial_sal1_mid), textcoords="offset points", xytext=(-15, -15), ha='center', fontsize=16)
      
    for i in range(len(etiquetas_sal2)):
        Tangencial_sal2_mid = (Tangencial_sal2[i] + Tangencial_sal2[i + 1]) / 2
        Radial_sal2_mid = (Radial_sal2[i] + Radial_sal2[i + 1]) / 2
        pl.annotate(etiquetas_sal2[i], (Tangencial_sal2_mid, Radial_sal2_mid), textcoords="offset points", xytext=(15, -15), ha='center', fontsize=16)

    for i in range(len(etiquetas_alt_sal)):
        Alt_X_sal_mid = (Alt_X_sal[i] + Alt_X_sal[i + 1]) / 2
        Alt_Y_sal_mid = (Alt_Y_sal[i] + Alt_Y_sal[i + 1]) / 2
        pl.annotate(etiquetas_alt_sal[i], (Alt_X_sal_mid, Alt_Y_sal_mid), textcoords="offset points", xytext=(20, 0), ha='center', fontsize=16)

    #Se establece el título y las etiquetas de los ejes
    pl.title('Triángulo de velocidades a la salida del rodete', fontsize=14)
    pl.xlabel('Velocidad tangencial (m/s)', fontsize=12) 
    pl.ylabel('Velocidad radial (m/s)', fontsize=12) 
    pl.grid(True)
    
    #Se introduce el número de subdivisiones en los ejes
    pl.gca().xaxis.set_major_locator(MaxNLocator(nbins=20))
    pl.gca().yaxis.set_major_locator(MaxNLocator(nbins=10))
    
    #Con el siguiente código se asegura que una unidad del eje x tenga la misma
    #longitud que una unidad del eje y. De esta forma, se evitan deformaciones
    #en el triángulo
    pl.gca().set_aspect('equal', adjustable='box')
    
    #Se guarda el gráfico en formato JPG
    pl.savefig('Triángulo_salida.jpg', format='jpg')
    
    
    #Se muestran todos los gráficos en la pestaña "Plots"
    pl.show()
    
    print("Se ha creado el archivo JPG 'Diagrama_h-s.jpg', que contiene el diagrama h-s del prediseño realizado.\n")
    
    print("Se ha creado el archivo JPG 'Triángulo_entrada.jpg', que contiene el triángulo de velocidades a la entrada del rodete en el radio exterior del prediseño realizado.\n")
    
    print("Se ha creado el archivo JPG 'Triángulo_salida.jpg', que contiene el triángulo de velocidades a la salida del rodete del prediseño realizado.\n")
    
    print("\n")
    
    print("Para realizar un nuevo prediseño, compile de nuevo. IMPORTANTE: antes de recompilar, para asegurar que se ejecute desde cero y así evitar posibles problemas por memoria de anteriores ejecuciones, conviene realizar lo siguiente: Tools -> Preferences -> Run -> Execute in a dedicated console.")
     
