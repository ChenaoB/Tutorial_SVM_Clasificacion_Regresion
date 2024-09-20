clc
clear
close all

%% Empieza el programa

%% SVM para clasificación utilizando una función de base radial como Kernel

%% Entradas
lengthScale = 5/3;
C = 10;
phi = 0.05;

%% Definición datos de entrenamiento y validación
X1 = xlsread('TrainR.xlsx');
X2 = xlsread('TestR.xlsx');
[x, t, z, y] = dividir_datos_entrenamiento_validacion(X1,X2);
Nx = length(x);

%% Función que determina la matriz Kernel
Kxx = kernel(x,x,lengthScale);
Kzx = kernel(z,x,lengthScale);
S = [Kxx Kxx; Kxx Kxx];

%% Construcción del modelo de programación Cuadrático convexo
Uno = ones(Nx,1);
Unos = [Uno; -Uno];
P = (Unos*Unos').*S;
Theta1 = t - phi;
Theta2 = t + phi;
qt = [-Theta1' Theta2'];
lb = zeros(2*Nx,1);
ub = C*ones(2*Nx,1);
g = [];
h = [];
A = Unos';
B = zeros(1,1);
apuntos = progquad(P, qt, g, h, A, B, lb, ub);
length(find(apuntos~=0))
%% Cálculo de la predicción en datos de validación
at = apuntos.*Unos;
b = (1/Nx)*(Theta1' - at'*[ Kxx ;Kxx])*Uno;
K = [Kzx, Kzx];
yz = at'*[Kzx Kzx]' + b;

%%Cálculo métricas de rendimiento

[ro, ERMS ] = metricasRegresion(yz', y)

%%Elaboración de gráficos
SPARS = graficosR(x,t,z,y,yz,apuntos);
