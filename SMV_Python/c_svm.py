import numpy as np
import pandas as pd
from funciones import dividir_datos_entrenamiento_validacion, kernel, quadprog, metricas, curva_decision, grafico

# Entrada
lengthScale = 5/3
C = 10
X = pd.read_csv('/content/DataSVMToClass.csv') # Se carga la base de datos

# Definición datos de entrenamiento y validación
x,t,z,y = dividir_datos_entrenamiento_validacion(X)
Nx = x.shape[0]
# Cálculo de zmatrices kernel  K
Kxx = kernel(x,x,lengthScale)
Kzx = kernel(z,x,lengthScale)

# Construcción del modelo de programación Cuadrático convexo
P = np.dot(t,t.T)*Kxx
q = -np.ones(Nx)
lb = np.zeros(Nx)
ub = C*np.ones(Nx)
A = np.squeeze(t.T)
B = np.zeros(1)
a = quadprog(P,q,None,None,lb,ub,A,B)

## Cálculo de la predicción en datos de validación
Uno = np.ones((Nx,1))
at = a*t
b = (1/Nx)*np.dot((t.T - np.dot(at.T,Kxx)),Uno)
b = np.squeeze(b)
yz = np.dot(at.T,Kzx.T) + b
yzclass1 = np.where(yz>0.1)
yzclass2 = np.where(yz<=-0.1)
yz[yzclass1] = 1
yz[yzclass2] = -1

#Cálculo métricas de rendimiento
TRN,TPR,PVV,Acc = metricas(yz.T, y)
print('TRN:',TRN)
print('TPR:',TPR)
print('PVV:',PVV)
print('Acc:',Acc)

# Determinación curva de decisión
Xcurva, Ycurva, Nivelcurva = curva_decision(a, b, x, t)

# Elaboración de gráficos
grafico(Xcurva, Ycurva, Nivelcurva, X, x, a)