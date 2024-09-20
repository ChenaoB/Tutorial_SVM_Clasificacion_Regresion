import numpy as np
import pandas as pd
from funciones import dividir_datos_entrenamiento_validacionR, kernel, quadprog, metricasRegresion, graficos

# Entrada
lengthScale = 5/3
C = 10
phi = 0.05
X = pd.read_csv('/content/DataSVMREGRESION.csv') # Se carga la base de datos

# Definición datos de entrenamiento y validación
x,t,z,y = dividir_datos_entrenamiento_validacionR(X)
Nx = x.shape[0]

# Cálculo de matrices kernel  K
Kxx = kernel(x,x,lengthScale)
Kzx = kernel(z,x,lengthScale)
S =  np.block([[Kxx, Kxx],[Kxx, Kxx]])

# Construcción del modelo de programación Cuadrático convexo
Uno = np.ones((Nx,1))
Unos = np.block([[Uno], [-Uno]])
P = np.dot(Unos,Unos.T)*S
Theta1 = t - phi
Theta2 = t + phi
qt = np.concatenate((-Theta1.T, Theta2.T))
qt = qt.reshape(-1)
lb = np.zeros(2*Nx)
ub = C*np.ones(2*Nx)
A = Unos.T
B = np.zeros(1)
apuntos = quadprog(P, qt, None, None, lb, ub, A, B)
print(np.size(np.where(np.squeeze(apuntos)!=0)))

# Cálculo de la predicción en datos de validación
at = apuntos*Unos
b = (1/Nx)*np.dot((Theta1.T - np.dot(at.T, np.block([[Kxx],[Kxx]]))), np.block([[Uno]]))
b = np.squeeze(b)
K = np.block([[Kzx, Kzx]])
yz = np.dot(at.T, K.T) + b

#Cálculo métricas de rendimiento
ERMS, ro = metricasRegresion(yz.T, y)
print('ro',ro)
print('ERMS',ERMS)
# Elaboración de gráficos
graficos(x,t,z,y,yz,apuntos)