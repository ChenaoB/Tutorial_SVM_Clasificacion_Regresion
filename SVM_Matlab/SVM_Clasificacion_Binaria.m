clc
clear
close all

%% Empieza el programa

%% SVM para clasificaci�n utilizando una funci�n de base radial como Kernel

%% Entradas
lengthScale = 5/3;
C = 10;

%% Definici�n datos de entrenamiento y validaci�n
X1 = xlsread('Train2.xlsx');
X2 = xlsread('Test2.xlsx');
[x, t, z, y] = dividir_datos_entrenamiento_validacion(X1,X2);
Nx = length(x);

%% Funci�n que determina la matriz Kernel
Kxx = kernel(x,x,lengthScale);
Kzx = kernel(z,x,lengthScale);


%% Construcci�n del modelo de programaci�n Cuadr�tico convexo

P = (t*t').*Kxx;
qt = -ones(Nx,1);
lb = zeros(Nx,1);
ub = C*ones(Nx,1);
A = t';
B = zeros(1,1);
a = progquad(P,qt,[],[], A, B, lb, ub);
%% C�lculo de la predicci�n en datos de validaci�n

Uno = ones(Nx,1);
b = (1/Nx)*(t' - (a.*t)'*Kxx)*Uno;
yz = (a.*t)'*Kzx';
yzclass1 = find(yz>0);
yzclass2 = find(yz<-0);
yz(yzclass1) = 1;
yz(yzclass2) = -1;

%% C�lculo m�tricas de rendimiento
[TRN,TPR,PVV,Acc] = metricas(yz', y)

%% Determinaci�n curva de decisi�n
[Xcurva, Ycurva, Nivelcurva] = curva_decision(a, b, x, t, lengthScale);

%% Elaboraci�n de gr�ficos
grafico(Xcurva, Ycurva, Nivelcurva, x, t, z, y, a)




