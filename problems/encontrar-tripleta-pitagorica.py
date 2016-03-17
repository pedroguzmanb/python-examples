# ---------------------------------------------------------
# UNIVERSIDAD LATINOAMERICANA DE CIENCIA Y TECNOLOGÍA
# FACULTAD DE INGENIERÍA
# ESCUELA DE INGENIERÍA INFORMÁTICA
# TUTOR: Pedro Guzmán (pguzmanb498@ulacit.ed.cr)
# ---------------------------------------------------------
# Definición de tripleta pitagórica:
# Una tripleta pitagórica son tres números que cumplen las
# siguientes condiciones:
# - a < b < c (a es menor que b y b es menor que c)
# - (a**2)+(b**2)==(c**2)
# ---------------------------------------------------------
# PROBLEMA:
# Hacer un programa que encuentre a,b,c tal que éstos sean
# una tripleta pitagórica y además: a + b + c = 1000
# ---------------------------------------------------------


# ---------------------------------------------------------
# FUNCIÓN CUMPLE ÓRDEN
# ---------------------------------------------------------
# HACE: Determina si a es menor que b y b es menor que c
# REQUIERE: tres valores enteros a, b, y c
def cumple_orden(a,b,c):
    return (a < b < c) is True

# ---------------------------------------------------------
# FUNCIÓN CUMPLE PITÁGORAS
# ---------------------------------------------------------
# HACE: Determina si "a" al cuadrado + "b" al cuadrado es
# 		igual a "c" al cuadrado
# REQUIERE: tres valores enteros a, b, y c
def cumple_pitagoras(a,b,c):
    return ((a**2)+(b**2) == (c**2)) is True

# ---------------------------------------------------------
# FUNCIÓN CUMPLE SUMA
# ---------------------------------------------------------
# HACE: Determina si a+b+c = x
# REQUIERE: cuatro valores enteros a, b, ,c y x donde a,b,c
# son los valores de una tripleta pitagórica y x es el valor
# con el cual se va a comparar la suma de a+b+c
def cumple_suma(a,b,c,x):
    return ((a+b+c) == x) is True


# ---------------------------------------------------------
# FUNCIÓN ENCONTRAR SOLUCIÓN
# ---------------------------------------------------------
# HACE: Encontrar (si existe) los valores a,b,c tal que se
# 		cumpla que a+b+c = x. Se hace por medio de una solución
#		iterativa por claridad de la solución. Existen maneras
#		más eficientes pero muy complejas para un curso de
#		introducción a la programación por lo que en este
#		caso no serán tomadas en cuenta.
#
# REQUIERE: un valor entero x para que se debe cumplir que
# 			una tripleta pitagórica de a, b, c, a+b+c == x
def encontrar_solucion_para(x):
    # DEFINICIÓN DE DOMINIO PARA: a, b, c
    # al especificarse x, se sabe que la solución se encuentra
    # en una combinación de a,b,c donde a=<x y b=<x y c=<x
    # puesto que si alguno fuera mayor a x entonces NO se puede
    # cumplir que a + b + c = x, por lo tanto lo valores posibles
    # para a, b, c se encuentra en el rango [0 hasta x].

    solucion_encontrada = False

    # Recorre todos los posibles valores de a [0 a X]
    # El rango de enteros que se recorre va desde 0 hasta
    # x por lo que se suma 1 para que el rango incluya x,
    # de lo contrario solo llegaría hasta (x-1)
    for a in range(0,x+1):
        # Se recorren todos lo posibles valores de "b"
        for b in range(0, x+1):
            # Se recorren todos los posibles valores de "c"
            for c in range(0, x+1):
                # Se valua que la permutación de a,b,c en éste
                # momento, cumpla las condiciones requeridas para
                # saber si se encontró la solución
                if cumple_orden(a,b,c) and cumple_pitagoras(a,b,c) and cumple_suma(a,b,c,x):
                    solucion_encontrada=True
                    print("La solucion es a:" + str(a) + ", b:" + str(b) + ", c:" + str(c))
                    print("Y cumple que: " + str(a)+ "+" + str(b) + "+" + str(c) + " = " + str(x))
                    # Como encontró la solución, entonces se sale del todos los ciclos
                    # y retorna verdadero porque la encontro
                    return solucion_encontrada

    # Si llegó hasta aquí es porque no encontró la solución,
    # por lo tanto indica que no encontró la solución y retorna
    # false
    print("No hay solucion de una tripleta pitagorica que la suma de a,b,c sea " + str(x))
    return solucion_encontrada

print(" ------------------------------------------------------------------- ")
print(str(encontrar_solucion_para(300)))
print(" ------------------------------------------------------------------- ")
print(str(encontrar_solucion_para(600)))
print(" ------------------------------------------------------------------- ")
print(str(encontrar_solucion_para(1000)))
print(" ------------------------------------------------------------------- ")
