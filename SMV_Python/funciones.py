import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.lines import Line2D
from qpsolvers import solve_qp
from qpsolvers import Problem, solve_problem

# Función para graficar resultados caso regresión

def graficos(x,t,z,y,yz,apuntos):
  Nx = x.shape[0]
  fig, axs = plt.subplots(1, 2, figsize=(14, 7))
  plt.rcParams['mathtext.fontset'] = 'cm'  # 'cm' fuente estándar Latex
  plt.rcParams['mathtext.rm'] = 'serif'    # Fuente  matemáticas
  an = apuntos[0:Nx]
  am = apuntos[-Nx:]
  SPARS = np.where(an-am!=0)
  SPARS = np.concatenate(SPARS)
  plt.subplot(1,2,1)
  plt.plot(z, yz.T, '.g', label = r'$y(\mathbf{z})$')
  plt.plot(z, y, '.b', label =r'$\mathbf{y}$')
  #plt.scatter(x[SPARS,0], t[SPARS,0], marker = 'o', facecolor='none', edgecolor='black', label= 'Vectores de soporte')
  plt.xlabel(r'$\mathbf{z}$', fontsize = 20)
  plt.ylabel(r'$\mathbf{y}$', fontsize = 20)
  plt.legend(fontsize = 11)
  plt.subplot(1,2,2)
  plt.plot(y,y, 'b', label = r'$\mathbf{y}$ vs $\mathbf{y}$')
  plt.plot(y,yz.T, '.k', label = r'$\mathbf{y}$ vs $y(\mathbf{z})$')
  plt.xlabel(r'$\mathbf{y}$', fontsize = 20)
  plt.ylabel(r'$y(\mathbf{z})$', fontsize = 20)
  plt.legend(fontsize = 12)
  plt.show()

# Función para graficar resultados caso clasificación

def grafico(Xcurva, Ycurva, Nivelcurva, X, x, a):
  fig, axs = plt.subplots(1, 1, figsize=(10, 7))
  plt.rcParams['mathtext.fontset'] = 'cm'  # 'cm' fuente estándar Latex
  plt.rcParams['mathtext.rm'] = 'serif'    # Fuente  matemáticas

  contorno = plt.contour(Xcurva, Ycurva , Nivelcurva, levels=[0], colors='r')
  legendcurvaDecision = Line2D([0], [0], color='r', label=r'$y(z)=0$')

  IndexClass1 = np.where(X['Y'] == 1)
  IndexClass2 = np.where(X['Y'] == -1)
  Xclass1 = X[['X1', 'X2']].iloc[IndexClass1]
  Xclass2 = X[['X1', 'X2']].iloc[IndexClass2]

  # Se gráfica el plano de decisión y los datos de las respectivas clases
  a = np.squeeze(a)
  SPARS = np.where(a!=0)
  SPARS = np.concatenate(SPARS)
  clase1, = plt.plot(Xclass1['X1'], Xclass1['X2'], '.g', label=r'$t_n=1$')
  clase2, = plt.plot(Xclass2['X1'], Xclass2['X2'], '.y', label=r'$t_n=-1$')
  Vectores_Soporte = plt.scatter(x[SPARS,0], x[SPARS,1], marker = 'o', facecolor='none', edgecolor='black', label= 'Vectores de soporte')
  plt.ylabel(r'$x_2$', fontsize=20)
  plt.xlabel(r'$x_1$', fontsize=20)
  plt.legend()
  plt.legend(handles=[clase1, clase2, Vectores_Soporte, legendcurvaDecision], fontsize = 11)
  plt.show()

# Función que determina la curva de decisión
def curva_decision(a, b, x, t):
  at = a*t
  xlevel = np.linspace(np.min(x[:,0]), np.max(x[:,0]), 100)  # Valores de x
  ylevel = np.linspace(np.min(x[:,1]), np.max(x[:,1]), 100)  # Valores de y
  k = x.shape[1]
  Xc, Yc = np.meshgrid(xlevel, ylevel)
  Ycontorno = np.zeros((x.shape[0],100))
  Curva = np.zeros((len(xlevel), len(ylevel)))
  Kcontour = np.zeros((x.shape[0], Xc.shape[0]))
  for zz in range(len(xlevel)):
    Xcountor = np.column_stack((Xc[:, zz], Yc[:, zz]))
    for i in range(Xcountor.shape[0]):
      for j in range(x.shape[0]):
        k1contour = np.exp(-5/3*(np.dot(x[j,:]-Xcountor[i,:], np.transpose(x[j,:]-Xcountor[i,:]))))
        Kcontour[j,i] = k1contour
    Curva[:,zz] = np.dot(at.T,Kcontour) + b
  return Xc, Yc, Curva


# Función que calcula las métricas de desempeño clasificación

def metricas(y,yz):
  VP = 0
  VN = 0
  FP = 0
  FN = 0
  for j,i in enumerate(y):
    if(i==1):
      if(i==yz[j]):
        VP += 1
      else:
        FN += 1
    else:
      if(i==yz[j]):
        VN += 1
      else:
        FP += 1
  TRN = VN/(VN+FP)
  TPR = VP/(VP+FN)
  PVV = VP/(VP+FP)
  Acc = (VP+VN)/(VP+VN+FP+FN)
  TRN, TPR, PVV, Acc
  return  TRN, TPR, PVV, Acc

# Función que calcula las métricas de desempeño regresión

def metricasRegresion(yz, y):
  ro = (1/(yz.shape[0]))*np.dot((yz-np.mean(yz)).T, y - np.mean(y))/np.sqrt(np.var(yz)*np.var(y))
  ERMS = np.sqrt(np.dot((yz-y).T, yz - y)/yz.shape[0])
  return ERMS, ro


# Función que resuelve el problema de programación cuadrática convexa

def quadprog(P, q, G, u, lb, ub, A, B):
  problem = Problem(P, q, G, u, A, B, lb,  ub)
  solution = solve_problem(problem, solver="cvxopt")
  a = np.transpose(solution.x.reshape(1, -1))
  for v,h in enumerate(a):
    if(np.abs(h)< 0.0000001):
      a[v,0] = 0
  return a

# Función que determina la matriz Kernel

def kernel(X, XT,lengthScale):
  KERNEL = np.zeros((X.shape[0], XT.shape[0]))
  for d in range(X.shape[0]):
    for e in range(XT.shape[0]):
      KERNEL[d, e] = np.exp(-lengthScale*(np.dot(XT[e,:]-X[d,:],np.transpose(XT[e,:]-X[d,:]))))
  return KERNEL

# Función de selección de los datos de entrenamiento y validación

def dividir_datos_entrenamiento_validacion(X):
  X1 = X.sample(frac=0.70, random_state=42)
  X2 = X.drop(X1.index)
  salidas = 1             # Número de salidas
  j = X.shape[1] - salidas
  x = np.zeros((X1.shape[0], j))
  t = np.zeros((X1.shape[0], salidas))
  z = np.zeros((X2.shape[0], j))
  y = np.zeros((X2.shape[0], salidas))
  t[:,0] = X1['Y']
  y[:,0] = X2['Y']
  x = X1[['X1','X2']].values
  z = X2[['X1','X2']].values
  return x,t,z,y

def dividir_datos_entrenamiento_validacionR(X):
  X1 = X.sample(frac=0.70, random_state=42)
  X2 = X.drop(X1.index)
  salidas = 1             # Número de salidas
  j = X.shape[1] - salidas
  x = np.zeros((X1.shape[0], j))
  t = np.zeros((X1.shape[0], salidas))
  z = np.zeros((X2.shape[0], j))
  y = np.zeros((X2.shape[0], salidas))
  t[:,0] = X1['Y']
  y[:,0] = X2['Y']
  x = X1[['X']].values
  z = X2[['X']].values
  return x,t,z,y