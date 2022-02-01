# ESAI
import math
# Maria Sofia Alvarez Lopez - 201729031
# Mariana Dueñas Rodriguez - 202021016

# Ejercicio 1
precio_con_iva = 1499000
# Asumimos que el IVA es el 19% (Colombia)
IVA = 0.19
# De acuerdo con este video: https://www.youtube.com/watch?v=-h_-mlq3uns la forma de calcular el precio sin IVA es:
# valor_sin_iva = valor_con_iva/(1 + IVA)
# Tiene mucho sentido porque el precio con IVA es el 119% del valor del producto (100%).
print(' ---- Ejercicio 1 ----')
precio_sin_iva = precio_con_iva / (1 + IVA)
print('El precio sin IVA que debe pagar Juan por la tablet es: $', precio_sin_iva)

# Ejercicio 2
try:
    precio_con_iva = float(input('Ingrese el valor con IVA de la tablet: '))
    precio_sin_iva = precio_con_iva / (1 + IVA)
    print(' ---- Ejercicio 2 ----')
    print('El precio sin IVA de la tablet es: $', precio_sin_iva)
except:
    print('No se ha ingresado un valor numérico')

# Ejercicio 3
print(' ---- Ejercicio 3 ----')
# Cuadrado
l = 3
area_cuadrado = l**2
print('El área del cuadrado es: {} cm^2'.format(area_cuadrado))

# Círculo
d = 8
area_circulo = math.pi * (d/2)**2
print('El área del círculo es: {} mm^2'.format(area_circulo))

# Triángulo
x, y = 5, 6
area_triangulo = x*y/2
print('El área del triángulo es: {} m^2'.format(area_triangulo))

# Pacman
r = 7
# Multiplicamos por 3/4 porque estamos quitando 1/4 del circulo.
area_pacman = 3* math.pi * (r**2)/4
print('El área del pacman es: {} cm^2'.format(area_pacman))

# Hexágono
a = 5
area_hexagono = 3*(math.sqrt(3))*(a**2)/2
print('El área del hexágono es: {} cm^2'.format(area_hexagono))

# Ejercicio 4
print('---- Ejercicio 4 ----')
# Cuadrado
l = float(input('Escriba la longitud del lado del cuadrado en cm: '))
area_cuadrado = l**2
print('El área del cuadrado es: {} cm^2'.format(area_cuadrado))

# Círculo
d = float(input('Escriba el diámetro del círculo en mm: '))
area_circulo = math.pi * (d/2)**2
print('El área del círculo es: {} mm^2'.format(area_circulo))

# Triángulo
x = float(input('Escriba el valor de la base del triángulo en m: '))
y= float(input('Escriba el valor de la altura del triángulo en m: '))
area_triangulo = x*y/2
print('El área del triángulo es: {} m^2'.format(area_triangulo))

# Pacman
r = float(input('Escriba el valor del radio del pacman en cm: '))
# Multiplicamos por 3/4 porque estamos quitando 1/4 del circulo.
area_pacman = 3* math.pi * (r**2)/4
print('El área del pacman es: {} cm^2'.format(area_pacman))

# Hexágono
a = float(input('Escriba el valor de un lado del hexágono en cm: '))
area_hexagono = 3*(math.sqrt(3))*(a**2)/2
print('El área del hexágono es: {} cm^2'.format(area_hexagono))

#Ejercicio 5:
print('---- Ejercicio 5 ----')

# Volumen esfera
r = float(input("Indique el radio de la esfera: "))
volumen_esfera = (4/3)*math.pi*(r**3)
print("El volumen de la esfera es (en unidades de longitud cubicas): ", volumen_esfera)

#Volumen octaedro
l = float(input("Digite la longitud de un lado del octaedro: "))
volumen_octaedro = (l**3)*math.sqrt(2)/3
print("El volumen del octaedro es (en unidades de longitud cubicas): ", volumen_octaedro)








