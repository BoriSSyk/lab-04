import math
x = float(input('Введіть Х: '))
y = float(input('Введіть Y: '))
z = float(input('Введіть Z: '))
R = 12 / math.pow(x, 2)+math.sin(y)+(math.sqrt(z) /
                                     math.pow(z, 2))/math.log(3)/z+0.07
print(R)
