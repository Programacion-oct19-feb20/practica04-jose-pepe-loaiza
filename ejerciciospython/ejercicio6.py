"""
	@autor: jose-pepe-loaiza
	nombre: ejercicio6.py
	descripcion: ...

	Jose loaiza -- 19
	Su suma de notas es: 30
	Su promedio es: 15

"""  


nombre = input("ingrese su nombre: \n")
edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese el valor de su nota 1: \n")
nota2 = input("Ingrese el valor de su nota 2: \n")


suma = int(nota1) + int(nota2);
promedio = suma / 2;

print("%s -- %s\nSu suma de nota es %s\nSu promedio es %s\n" %
	(nombre, edad, suma, promedio))