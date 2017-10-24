contrasena=input("Por favor, introduce tu contrasena: ")

valida=True

for i in contrasena:
	if i==" ":
		valida=False


if len(contrasena)>8 and valida==True:
	print("La contrasena es Correcta")
else:
	print("La contrasena es Incorrecta")

