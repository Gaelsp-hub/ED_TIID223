#Declarando un arreglo
numeros=[10,20,30,40,50]

#imprime la posicion 2
print(numeros[2])

#cambio el valor de la 3ra posicion 
numeros[3]=15
print(numeros)

#Agregamos un valor nuevo al fial del arreglo
numeros.append(60)
print(numeros)

#eliminamos un valor del arreglo de la posicon 1
numeros.pop(1)
print(numeros)

#eliminamos un valor por el contenido de la posicion 
numeros.remove(30)
print(numeros)


frutas=["Mango","Manzana","Uva","Pera","Maracuya"]
frutas.remove("Uva")
print(frutas)

frutas.pop(3)
print(frutas)

frutas.append("Kiwi")
print(frutas)

frutas["Pera"]="Fresa"
print(frutas)

arreglo=[]
n = int (input("Ingresa el tamaño del arreglo"))

arreglo.append(n)