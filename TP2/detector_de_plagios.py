'''
Lógica del programa detector de plagios.
'''

def limpiar_palabra(palabra:str) -> str:
    '''
    Procesa una cadena eliminando los signos de puntuación, y pasando 
    las mayúsculas a minúsculas.

    PRECONDICIONES:
        - Palabra es un string.
    
    POSTCONDICIONES: 
        - La función devuelve la cadena palabra procesada.
    '''
    palabras_prohibidas=",.!¡¿?;:()[]}{%#$/&=+-*-_<>"
    palabra_nueva=""
    for caracter in palabra:
        if caracter in palabras_prohibidas:
            continue
        palabra_nueva+=caracter
    return palabra_nueva.lower()

def cargar_n_gramas(palabras_linea:list[str], n:int, n_gramas:dict[tuple[str, ...], int], n_grama:list[str]):
    '''
    Recopila y carga las apariciones de todos los n_grama, formados por las 
    palabras de palabras_linea, de longitud n, en el diccionario n_gramas.
    Si el diccionario carga con valores previos, suma nuevos o los actualiza.

    PRECONDICIONES: 
        -Recibe una lista de strings que representa un renglón de un archivo; un entero 
        mayor o igual a dos y menor a diez; un diccionario (vacío o no) con tuplas de 
        extensión n como claves y enteros como valores asociados; y una lista de extensión 
        menor o igual a n.
    
    POSTCONDICIONES: 
        -La función no devuelve nada, actualiza los valores de la lista y diccionario.
    '''
    faltantes=n-len(n_grama)
    for i in range(min(faltantes, len(palabras_linea))):
        palabra_limpia=limpiar_palabra(palabras_linea[i])
        if palabra_limpia:
            n_grama.append(palabra_limpia)
    if len(n_grama)==n:
        n_gramas[tuple(n_grama)]=n_gramas.get(tuple(n_grama), 0)+1
    for palabra in palabras_linea[faltantes:]:
        palabra_limpia=limpiar_palabra(palabra)
        if palabra_limpia:
            n_grama.pop(0)
            n_grama.append(palabra_limpia)
            n_gramas[tuple(n_grama)]=n_gramas.get(tuple(n_grama), 0)+1

def inicializar_archivo(ruta:str, n:int) -> dict[tuple[str, ...], int]:
    '''
    Abre los archivos y sirve de base para el diccionario n_gramas y la lista 
    n_grama que serán actualizados luego de cada iteración del bucle 'for' que 
    llama a la función cargar_n_gramas.
    
    PRECONDICIONES:
        -Recibe la ruta absoluta del archivo que se quiere procesar y un entero que
    es el que define el tamaño de los n_gramas con los que se quiere comparar las 
    similitudes.
    
    POSTCONDICIONES:
        -Devuelve el diccionario completo de n_gramas para el archivo dado.
    '''
    with open(ruta, 'r') as archivo:
        n_gramas={}
        n_grama=[]
        for linea in archivo:
            palabras_linea=linea.strip().split()
            cargar_n_gramas(palabras_linea, n, n_gramas, n_grama)
    return n_gramas

def jaccard(A: dict[tuple[str, ...], int], B: dict[tuple[str, ...], int]) -> float:
    """
    Devuelve el índice de Jaccard que representa la similitud entre dos
    textos mediante el procesado a través de n_gramas de longitud n de cada
    uno de los textos a analizar.

    PRECONDICIONES:
        -Recibe dos diccionarios cuyas claves son n-gramas y sus valores
    asociados, las apariciones totales en un texto.
    
    POSTCONDICIONES:
        -Devuelve el índice de Jaccard como tipo de dato float.
    """
    interseccion=0
    suma=sum(A.values())+sum(B.values())
    claves_comunes= set(A.keys()).intersection(set(B.keys()))
    for clave in claves_comunes:
        interseccion+=A[clave]+B[clave]  
    indice=interseccion/suma
    return indice