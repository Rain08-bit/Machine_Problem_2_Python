from math import sqrt 

x1 = int(input('Enter a value for x1:'));
y1 = int(input('Enter a value for y1:'));
x2 = int(input('Enter a value for x2:'));
y2 = int(input('Enter a value for y2:'));
x3 = int(input('Enter a value for x3:'));
y3 = int(input('Enter a value for y3:'));

D = ((pow(x2,2)-pow(x1,2))*(y3-y1)+(pow(y2,2)-pow(y1,2))*(y3-y1)+(pow(x1,2)-pow(x3,2))*(y2-y1)+(pow(y1,2)-pow(y3,2))*(y2-y1)) / ((y3-y1)*(x1-x2)-(x1-x3)*(y2-y1));
E = ((pow(x1,2)-pow(x3,2))*(x1-x2)+(pow(y1,2)-pow(y3,2))*(x1-x2)+(pow(x2,2)-pow(x1,2))*(x1-x3)+(pow(y2,2)-pow(y1,2))*(x1-x3)) / ((x1-x2)*(y3-y1)-(y2-y1)*(x1-x3));
F = - pow(x1,2) - pow(y1,2) - (D)*(x1) - (E)*(y1);
print('Vector = (',D,',',E,',',F,')')

h = D / -2;
k = E / -2;
print('Center = (', h, ', ', k, ')')

r = sqrt((h* h) + (k* k) - (F));
print('Radius = ', r)