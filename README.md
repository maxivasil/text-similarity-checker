<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2621/2621040.png" alt="Logo Detector" width="100px" style="margin-bottom: 20px;">

  <h1>🕵️‍♂️ Text Similarity Checker</h1>

  <p>
    <strong>Fundamentos de Programación</strong><br>
    Herramienta de análisis forense de documentos utilizando comparaciones algorítmicas.
  </p>

  <img src="https://img.shields.io/badge/Language-Python_3-blue?style=flat-square&logo=python" alt="Python 3">
  <img src="https://img.shields.io/badge/Algorithm-Jaccard_Index-orange?style=flat-square" alt="Jaccard">
  <img src="https://img.shields.io/badge/Technique-N--Grams-green?style=flat-square" alt="N-Grams">
  <img src="https://img.shields.io/badge/Export-CSV_Report-lightgrey?style=flat-square&logo=microsoft-excel" alt="CSV">

  <br><br>
</div>

---

## 📋 Descripción

Este proyecto es una herramienta de línea de comandos (CLI) diseñada para **detectar similitudes entre múltiples documentos de texto**. Es ideal para auditar trabajos prácticos, informes o cualquier conjunto de archivos `.txt`.

El sistema procesa un directorio completo, comparando "todos contra todos" y generando alertas automáticas cuando el porcentaje de coincidencia supera un umbral sospechoso.

### ✨ Características Principales
* **Zero Dependencies:** Funciona con Python puro, sin librerías externas.
* **Análisis configurable:** Permite ajustar el tamaño de los *N-gramas* (2 a 9 palabras) para afinar la sensibilidad.
* **Reportes Automáticos:** Exporta los casos relevantes a un archivo `.csv` para su posterior revisión.
* **Normalización:** Limpia signos de puntuación y mayúsculas para evitar falsos negativos.

---

## 🧠 ¿Cómo funciona?

El núcleo del detector se basa en dos conceptos fundamentales de la lingüística computacional y la teoría de conjuntos:

### 1. N-Gramas
El texto no se analiza palabra por palabra, sino en secuencias.
> *Ejemplo (N=3):* "El perro corre" -> `("el", "perro", "corre")`

Esto permite detectar frases copiadas incluso si se cambia el orden de las oraciones.

### 2. Índice de Jaccard
Para calcular el porcentaje de similitud entre dos textos ($A$ y $B$), utilizamos la siguiente fórmula:

$$J(A,B) = \frac{|A \cap B|}{|A \cup B|}$$

Donde:
* $A \cap B$: Es la intersección (N-gramas compartidos).
* $A \cup B$: Es la unión (Total de N-gramas únicos en ambos textos).

---

## ⚙️ Requerimientos

Solo necesitas tener **Python 3** instalado.

```bash
python --version
# Debería mostrar Python 3.x.x
```

---

## 🚀 Instalación y Uso

### 1. Preparar los datos

Crea una carpeta (ej: textos_analisis) y coloca dentro todos los archivos .txt que desees comparar.

### 2. Ejecutar el programa

```bash
python3 main.py
```

### 3. Flujo de Interacción

El programa te guiará paso a paso:

- Ingresar Directorio: Escribe el nombre de la carpeta con los textos.

- Definir N-gramas: Elige la precisión (Recomendado: 3 o 4).

- Resultados: Verás en pantalla las parejas con similitud > 15%.

- Exportación: Si se detectan coincidencias > 1%, podrás guardar un reporte .csv.

---

## 📂 Estructura del Proyecto

- main.py: Controlador principal. Maneja la interacción con el usuario, la validación de entradas y el flujo de archivos.

- detector_de_plagios.py: Lógica del negocio. Contiene las funciones matemáticas (jaccard), el procesamiento de strings (limpiar_palabra) y la generación de diccionarios de N-gramas.

---

## 👥 Autor

| Integrante | Padrón | Contacto |
| :--- | :---: | :---: |
| **Calderón Vasil, Máximo Augusto** | 111810 | [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/maxivasil) [![Email](https://img.shields.io/badge/Email-red?style=flat-square&logo=gmail&logoColor=white)](mailto:mcalderonv@fi.uba.ar) |