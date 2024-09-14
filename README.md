# La Máquina de Soporte Vectorial como Problema de Programación Cuadrática Convexa: Análisis y un tutorial

Se estudian las operaciones vectoriales necesarias para transformar el problema de optimización en su forma dual a su notación matricial, 
determinado así la analogía entre la SVM y un QP (problema de programación cuadrático convexo ). Se examinan los algoritmos C-SVM y R-SVM desarrollando el componente matemático completo. 
Finalmente, se implementa un caso de estudio para validar el desarrollo propuesto.

# La SVM para clasificación C-SVM y para Regresión R-SVM

Este repositorio contiene un ejemplo de los algoritmos **C-SVM** (Máquina de Soporte Vectorial para Clasificación binaria) 
y **R-SVM** (Máquina de Soporte Vectorial para regresión con única salida), estos están basados en la referencias [1,2]. 
La implementación se encuentra disponible para **Python** y **Matlab**.

# Diagrama de flujo de los algoritmo C-SVM Y R-SVM

![Descripción de la imagen](https://github.com/ChenaoB/Tutorial_SVM_Clasificacion_Regresion/blob/main/Algoritmos_SVM.png)

# Bases de datos

En este repositorio encontrará los siguientes dataset

**Clasificación**

- DataSVMToClass.csv (dos entradas y salida binaria)
- DataSVMToClassCase2.csv (dos entradas y salida binaria)
- Train.xlsx (Matlab)
- Train2.xlsx (Matlab)
- Test.xlsx (Matlab)
- Test2.xlsx (Matlab)

**Regresión**

- DataSVMREGRESION.csv (única entrada con única salida)
- TrainR.xlsx (Matlab)
- TestR.xlsx (Matlab)


# Requerimientos

Los códigos ejecutadados fueron probados en las siguientes versiones

- Python 3.10.12
- Numpy 1.26.4
- Matplotlib 3.7.1
- Pandas 2.1.4
- Qpsolvers 4.3.3
- Matlab 2016a

Se sugiere realizan la siguinte instalación del paquete de optimización qpsolvers: pip install qpsolvers[open_source_solvers]

# Créditos

Si encuentra útil este trabajo en su investigación, puede citarlo como:


# Referencias

[1] Cortes, C., & Vapnik, V. (1995). Support-vector networks. Machine learning, 20, 273-297. https://doi.org/10.1007/BF00994018

[2] Bishop, C. M., & Nasrabadi, N. M. (2006). Pattern recognition and machine learning (Vol. 4, No. 4, p. 738). New York: springer.  https://doi.org/10.1117/1.2819119
