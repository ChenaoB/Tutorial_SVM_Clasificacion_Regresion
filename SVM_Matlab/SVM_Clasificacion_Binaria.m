clc
clear
close all

%% Empieza el programa

%% SVM para clasificación utilizando una función de base radial como Kernel

%% Entradas
lengthScale = 5/3;
C = 10;

%% Definición datos de entrenamiento y validación
X1 = xlsread('Train2.xlsx');
X2 = xlsread('Test2.xlsx');
[x, t, z, y] = dividir_datos_entrenamiento_validacion(X1,X2);
Nx = length(x);

%% Función que determina la matriz Kernel
Kxx = kernel(x,x,lengthScale);
Kzx = kernel(z,x,lengthScale);


%% Construcción del modelo de programación Cuadrático convexo

P = (t*t').*Kxx;
qt = -ones(Nx,1);
lb = zeros(Nx,1);
ub = C*ones(Nx,1);
A = t';
B = zeros(1,1);
a = progquad(P,qt,[],[], A, B, lb, ub);
%% Cálculo de la predicción en datos de validación

Uno = ones(Nx,1);
b = (1/Nx)*(t' - (a.*t)'*Kxx)*Uno;
yz = (a.*t)'*Kzx';
yzclass1 = find(yz>0);
yzclass2 = find(yz<-0);
yz(yzclass1) = 1;
yz(yzclass2) = -1;

%% Cálculo métricas de rendimiento
[TRN,TPR,PVV,Acc] = metricas(yz', y)

%% Determinación curva de decisión
[Xcurva, Ycurva, Nivelcurva] = curva_decision(a, b, x, t, lengthScale);

%% Elaboración de gráficos
grafico(Xcurva, Ycurva, Nivelcurva, x, t, z, y, a)




