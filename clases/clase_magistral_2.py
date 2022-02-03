print("Hay {:d} planetas en el sistema solar".format(8))  # Formato entero - decimal
print("{:f} (m/s2) es el valor de la aceleración gravitacional en la tierra".format(9.80665))  # Formato flotante
print("bin: {0:b}, oct: {0:o}, hex: {0:X}".format(15))  # Otros formatos

print("{:4}".format(18))  # El número es de 2 dígitos,
# pero como el padding =4, se mueve 2
# espacios a la derecha
print("{:2d}".format(2290))  # Si el ancho del número es mayor que el padding,
# no hay ningún desplazamiento
print("{:8.3f}".format(12.2729))  # El número 8 especifica el 'padding',
# mientras que el .3 específica un
# redondeo a 3 posiciones.
print("{:05d}".format(24))  # Si en cambio de un desplazamiento,
# se quiere rellenar el padding (ancho) con 0s
print("{:08.3f}".format(12.2817))

print("{:8.2f}".format(-8.349))  # Sin alineanción
print("{:^8.2f}".format(-8.349))  # Centrado
print("{:<8.2f}".format(-8.349))  # Alineación a la izquierda
print("{:>8.2f}".format(-8.349))  # Alineación a la derecha
print("{:=8.2f}".format(-8.349))  # "Signo forzado"

lista = ['UniAndes', 12, 3, 5, 8]  # Creamos una lista
print(lista[0])  # Posición 0
print(lista[-2])  # Posición -2 (Izquierda a derecha)
print(lista[2:], '\n')  # Desde la posición 2 en adelante
lista.append('Programación')  # Añadimos otro elemento al final de la lista
print(lista)

del lista[3]  # Eliminamos el elemento # 3
print(lista)

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # Nueva lista
letras[2:5] = ['C', 'D', 'E']  # Sobrescribimos
print(letras)

letras[2:5] = []  # "Quitamos" lo que hay en ese intervalo
New_list = [lista, letras]  # Una lista de 2 listas!
print(New_list)

New_list1 = lista + letras  # Concatenamos las 2 listas
print(New_list1)


tupla1 = ('peras', 'manzanas', '145') # Se crea la tupla
print(tupla1)

print(tupla1[0]) # Se imprime el primer elemento
print(tupla1[-1]) # Se imprime el último elemento
print(len(tupla1)) # Se imprime la longitud de la tupla
tuplaunelem = ('peras',) # Tupla con 1 elemento debe contener la ","!!
print(type(tuplaunelem))

notupla = ("apple") # NO es una tupla si no tiene la "," !!
print(type(notupla))

Vertebrados = {'Mamifero': ['vaca', 'perro', 'mono'], 'Aves': ['águila', 'colibrí'],
               'Peces': ['tiburón', 'salmón'], 'Reptiles': ['tortuga', 'cocodrilo']}

print(Vertebrados['Peces'])  # ¿Qué peces tenemos en nuestro diccionario?
print('Aves' in Vertebrados)  # ¿Hay Aves en nuestro diccionario?
Vertebrados['Mamifero']  # Obtenemos los valores de Mamífero (Forma A)
Vertebrados.get('Mamifero')  # Obtenemos los valores de Mamífero (Forma B)
del Vertebrados['Peces']  # Eliminamos los datos de 'Peces'
Vertebrados['Anfibios'] = 'Sapo, Tritón'  # Agregamos una nueva clave al diccionario
print(Vertebrados)

estudiante = {'nombre': 'Juan', 'apellido': 'Peña', 'edad': 20, 'carrera': 'Ing Biomédica'}
# a)
print("{p[nombre]} {p[apellido]}, estudiante de {p[carrera]} tiene {p[edad]} años".format(p=estudiante))
# b)
print("{nombre} {apellido}, estudiante de {carrera} tiene {edad} años".format(**estudiante))

## Estructuras de control
# if
a = 5
b = 10
c = 15
d = 20
e = 25
if b > a and c > b and d > c and e > d:
    print("Entra al if 1")
if b > a and c > b or d > c and e < d:
    print("Entra al if 2")
if b > a and (c > b or d > c) and e < d:
    print("Entra al if 3")

anios = int(input('¿Cuántos años tienes?'))  # Recordar que por defecto, lo
# que recibe input es tipo 'str'
if anios >= 18:
    print('Puedes entrar al bar!')
else:
    print('Lo siento, eres menor de edad y no puedes entrar')