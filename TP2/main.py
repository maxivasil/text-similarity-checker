'''
Flujo del programa.
'''

import os
import detector_de_plagios

def validar_directorio():
    '''
    Valida la entrada del directorio por parte del usuario. El mismo se considera correcto
    cuando se pueda acceder a él desde donde se ejecuta el programa y tenga al menos un 
    archivo dentro.

    PRECONDICIONES:
        -No recibe ningún parámetro. Utiliza módulo os.

    POSTCONDICIONES:
        -Devuelve el nombre del directorio y una lista con los nombres de los archivos que 
    se encuentran dentro. Si el usuario quiere terminar con el flujo del programa, devuelve 
    0, 0 como enteros.
    '''
    while True:
        directorio=input('Ingrese el directorio a analizar (o deje vacío para finalizar): ')
        if directorio=="":
            return 0, 0
        try:
            nombres_archivos=os.listdir(directorio)
            return directorio, nombres_archivos
        except FileNotFoundError:
            print(f'No se encontró el directorio: {directorio}\nPor favor verifique que exista y haya sido bien referenciado')
        except NotADirectoryError:
            print(f'{directorio} no es un directorio')

def validar_n() -> int:
    '''
    Valida la entrada por parte del usuario del tamaño n de los n_gramas a procesar, 
    que sea un entero y que sea mayor o igual que dos y menor que diez. 

    PRECONDICIONES:
        -No recibe ningún parámetro.
    
    POSTCONDICIONES:
        -Devuelve el entero validado.
    '''
    while True:
        n=input('Ingrese el tamaño para procesar los n-gramas (debe ser entero mayor o igual que dos y menor que diez): ')
        if not n.isdigit():
            print('No ingresó un número entero')
            continue
        n=int(n)
        if not 2<=n<10:
            print('El número debe ser mayor o igual que dos y menor que diez')
            continue
        return n

def procesar(directorio:str, nombres_archivos:list[str], n:int) -> list[tuple[str, dict[tuple[str, ...], int]]]:
    '''
    
    Por cada archivo, si es de formato .txt, establece la ruta absoluta del mismo, 
    calcula el diccionario n_gramas y agrega al final de la lista procesados una tupla 
    donde el primer valor es la ruta relativa del archivo, y el segundo, el diccionario
    de los n_gramas que aparecen en el mismo.
    
    PRECONDICIONES:
        -Recibe un string (directorio), una lista de los archivos que se encuentran dentro 
    del directorio(nombres_archivos), y un entero (n) que es el tamaño de los n_grama a procesar.

    POSTCONDICIONES:
        -Devuelve la lista procesados.
    '''
    procesados=[]
    for archivo in nombres_archivos:
        if archivo[len(archivo)-4:]=='.txt':
            ruta=os.path.join(directorio, archivo)
            procesados.append((archivo, detector_de_plagios.inicializar_archivo(ruta, n)))
    return procesados

def analizar_procesados(procesados:list[tuple[str, dict[tuple[str, ...], int]]]) -> tuple[list[tuple[str, str]], list[str]]:
    '''
    Itera sobre procesados, comparando todos los archivos entre sí y agrega a la lista 
    resultados_sospechosos aquellos cuya similitud es mayor a 15%.
    En la misma iteración recopila aquellos cuyos resultados de similitud sean al menos
    del 1%, pero esta vez los agrega a la lista resultados_mayores_indice1.

    PRECONDICIONES:
        -Recibe una lista de tuplas, en donde cada una tiene como primer elemento la 
    ruta relativa del archivo, y como segundo elemento, un diccionario con las 
    apariciones de n_grama.

    POSTCONDICIONES:
        -Devuelve dos listas, resultados_sospechosos donde cada elemento es una tupla de una cadena
    que indica los nombres de los archivos comparados y un string que representa el porcentaje de 
    similitud entre ambos archivos; y resultados_mayores_indice1 donde cada elemento es una cadena
    en formato csv que contiene tres elementos: nombre del primer archivo, nombre del segundo, y porcentaje
    de similitud entre ambos.
    '''
    resultados_sospechosos=[]
    resultados_mayores_indice1=[]
    for i in range(len(procesados)):
        for j in range(i+1, len(procesados)):
            indice=detector_de_plagios.jaccard(procesados[i][1], procesados[j][1])
            if 0.01<=indice:
                resultados_mayores_indice1.append(f'{procesados[i][0]},{procesados[j][0]},{str(indice*100)[:5]}')
            if indice>0.15:
                resultados_sospechosos.append((f'{procesados[i][0]} vs {procesados[j][0]}',str(indice*100)[:5]))
    return resultados_sospechosos, resultados_mayores_indice1

def mostrar_por_pantalla(resultados_sospechosos:list):
    '''
    Muestra por pantalla uno debajo del otro cada resultado sospechoso.
    Si no hay resultados sospechosos lo muestra al usuario.

    PRECONDICIONES:
        -Recibe una lista de tuplas con cada uno de los resultados_sospechosos como cadena.

    POSTCONDICIONES:
        - No devuelve nada.
    '''
    if not resultados_sospechosos:
        print('No se encontraron resultados sospechosos')
        return
    print('RESULTADOS SOSPECHOSOS:')
    for i, resultado in enumerate(resultados_sospechosos):
        nombres, indice=resultado
        print(f'{i+1}: {nombres} {indice}%')

def guardar_reporte(resultados_mayores_indice1: list[str]):
    '''
    Solicita un nombre para escribir un archivo en formato .csv con encabezado, y escribe 
    por cada linea un resultado de la lista ingresada. No admite nombre vacío.
    
    PRECONDICIONES:
        -Recibe una lista de cadenas con los resultados cuyo indice de similitud es mayor a 1.
    POSTCONDICIONES:
        -No devuelve nada.
    '''
    while True:
        archivo=input("Ingrese el nombre de un archivo que se creará para guardar el reporte de similitudes mayores a 1%: ")
        if archivo!="":
            break
        print("Debe ingresar un nombre de archivo")
    archivo+='.csv'
    with open(archivo, 'w') as destino:
        encabezado='nombre_archivo1,nombre_archivo2,similaridad'
        destino.write(f'{encabezado}\n')
        for resultado in resultados_mayores_indice1:
            destino.write(f'{resultado}%\n')
    print(f'{archivo} fue creado y cargado exitosamente')

def main():
    while True:
        directorio, nombres_archivos=validar_directorio()
        if nombres_archivos==0:
            return
        n=validar_n()
        procesados=procesar(directorio, nombres_archivos, n)
        resultados_sospechosos, resultados_mayores_indice1=analizar_procesados(procesados)
        mostrar_por_pantalla(resultados_sospechosos)
        if len(resultados_mayores_indice1)>0:
            guardar_reporte(resultados_mayores_indice1)
        
main()