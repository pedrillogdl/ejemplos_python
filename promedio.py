num1=int(input("Podrias proporcionar el primer numero: "))
num2=int(input("Podrias proporcionar el Segundo numero: "))
num3=int(input("Podrias proporcionar el tercer numero: "))

def promedio(n1, n2, n3):
	prom=(n1+n2+n3)/3
	return prom

resultado=str(promedio(num1, num2, num3))
print("El promedio de los tres numeros es: " + resultado)