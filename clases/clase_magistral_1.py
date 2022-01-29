## Ejemplo tipos de variables
a = 2.3
b = 3 + 5j
c = "Programación científica"
d = True
print(a, b, c, d)

# Saber el tipo de variable
print(type(a), type(b), type(c), type(d))

A = 5
B = 4
C = A + B
print(C)

D = A ** 2
print(D)

F = A / B
G = A // B  # ?
H = A % B  # ?
print(F, G, H)  # ¿Qué diferencia hay entre F, G y H?
I = 2.4
J = 5.4
K = I* J
print(K)

hello = 'Programación'  # Un String con comillas sencillas
world = "Científica"  # Un String con comillas dobles
print(hello)
print(len(hello))  # ¿Qué longitud tiene la variable hello?
hw = hello + ' ' + world  # Ejemplo de concatenación de Strings
print(hw)

s = "Uniandes"
print(s.capitalize())  # Es un nombre, debe iniciar en Mayúscula!
print(s.upper())  # Colocar todo el texto en mayúscula
print(s.rjust(10))  # "Right-justify". Mueve un String a la derecha
print(s.center(14))  # Centra un String
print(s.replace('n', 's'))  # Reemplaza todas las letras 'n' por 's'
print('Uni\nandes')  # Demos un espacio. La instrucción '\n' hace un enter
print(r'Uni\nandes')  # Anulamos la instrucción del enter '\n'
print(3 * 'Uni' + 'andes')  # ¿Podemos hacer operaciones matemáticas con Strings?
print(s[3])  # ¿Que hay en la posición 3 de la variable 's'?
print(s[0:3])  # Imprimimos la variable s entre los espacios de memoria 0 a 3 (sin incluir el 3)
