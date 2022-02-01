# ESAI
# Maria Sofia Alvarez Lopez - 201729031
# Mariana Dueñas Rodriguez - 202021016
import math

print()
print('----- Maria Sofia Alvarez - Mariana Dueñas -----'.center(50))
print('Programacion Cientifica: Laboratorio 0'.center(50))


# Hacemos una funcion porque tanto en el ejercicio 1 como en el 2 haremos el mismo calculo
def calcular_precio_sin_iva(precio_con_iva):
    # Asumimos un IVA del 19%
    IVA = 0.19
    # De acuerdo con este video: https://www.youtube.com/watch?v=-h_-mlq3uns la forma de calcular el precio sin IVA es:
    # valor_sin_iva = valor_con_iva/(1 + IVA)
    # Tiene mucho sentido porque el precio con IVA es el 119% del valor del producto (100%).
    return precio_con_iva / (1 + IVA)


# Ejercicio 1
print('--- Ejercicio 1 ---')
# Este es el precio sugerido para el ejercicio
precio_con_iva = 1499000
precio_sin_iva = calcular_precio_sin_iva(precio_con_iva)
print('El precio sin IVA que Juan debe pagar por su tablet es: ${}'.format(precio_sin_iva))

# Ejercicio 2
print('--- Ejercicio 2 ---')
try:
    # Solicitamos al usuario que ingrese el valor por consola
    precio_con_iva = float(input('Ingrese el valor con IVA de la tablet: '))
    precio_sin_iva = calcular_precio_sin_iva(precio_con_iva)
    print('El precio sin IVA que Juan debe pagar por su tablet es: ${}'.format(precio_sin_iva))
except:
    print('No se ha ingresado un valor numérico')

# Ejercicio 3
# Primero definimos algunas funciones para las areas, porque las usaremos en el 4to ejercicio tambien.
print('--- Ejercicio 3 ---')


# Area del cuadrado = lado**2
def area_cuadrado(lado):
    return lado ** 2


# Area del circulo = pi * radio**2
def area_circulo(diametro):
    return math.pi * (diametro / 2) ** 2


# En este caso, x es la base e y es la altura del triangulo
# Area del triangulo = base*altura/2
def area_triangulo(x, y):
    return x * y / 2


# Area del hexagono regular = 3*sqrt(3)*(lado**2) / 2
def area_hexagono(lado):
    return 3 * (math.sqrt(3)) * (lado ** 2) / 2


# Cuadrado
lado = 3
print('El area del cuadrado es: {} cm^2'.format(area_cuadrado(lado)))

# Círculo
diametro = 8
print('El area del círculo es: {} mm^2'.format(area_circulo(diametro)))

# Triángulo
x, y = 5, 6
print('El area del triángulo es: {} m^2'.format(area_triangulo(x, y)))

# Pacman
# Note que en este caso nos basta con la formula del circulo.
# Primero calculamos el diametro (los datos que recibimos son del radio)
radio = 7
diametro_pacman = radio*2
# Notamos que el pacman corresponde a 3/4 partes de un circulo, entonces el area es la de un circulo a la que le
# hemos quitado 1/4 parte de el. Es decir:
area_pacman = (3/4)*area_circulo(diametro_pacman)
print('El area del pacman es: {} cm^2'.format(area_pacman))

# Hexagono
lado_hex = 5
print('El area del hexágono es: {} cm^2'.format(area_hexagono(lado_hex)))

# Ejercicio 4
# NOTA: Aqui ya no usamos try-catch porque el profe dijo que no era necesario
print('--- Ejercicio 4 ---')
# Cuadrado
lado = float(input('Escriba la longitud del lado del cuadrado en cm: '))
print('El área del cuadrado es: {} cm^2'.format(area_cuadrado(lado)))

# Círculo
diametro = float(input('Escriba el diametro del círculo en mm: '))
print('El área del círculo es: {} mm^2'.format(area_circulo(diametro)))

# Triángulo
x = float(input('Escriba el valor de la base del triángulo en m: '))
y= float(input('Escriba el valor de la altura del triángulo en m: '))
print('El área del triángulo es: {} m^2'.format(area_triangulo(x,y)))

# Pacman
radio = float(input('Escriba el valor del radio del pacman en cm: '))
# Primero calculamos el diametro (los datos que recibimos son del radio)
diametro_pacman = radio*2
# Notamos que el pacman corresponde a 3/4 partes de un circulo, entonces el area es la de un circulo a la que le
# hemos quitado 1/4 parte de el. Es decir:
area_pacman = (3/4)*area_circulo(diametro_pacman)
print('El area del pacman es: {} cm^2'.format(area_pacman))

# Hexagono
lado_hex = float(input('Escriba el valor de un lado del hexagono en cm: '))
print('El área del hexágono es: {} cm^2'.format(area_hexagono(lado_hex)))

# Ejercicio 5
print('--- Ejercicio 5 ---')
# En este caso no necesitamos hacer funciones porque los volumenes no los reutilizamos despues

# Volumen esfera
r = float(input("Indique el radio de la esfera: "))
volumen_esfera = (4/3)*math.pi*(r**3)
print("El volumen de la esfera es (en unidades de longitud cubicas): ", volumen_esfera)

#Volumen octaedro
l = float(input("Digite la longitud de un lado del octaedro: "))
volumen_octaedro = (l**3)*math.sqrt(2)/3
print("El volumen del octaedro es (en unidades de longitud cubicas): ", volumen_octaedro)
