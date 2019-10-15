"""
	Clase 2
	@SantiagoDGarcia
"""
# Datos a usar
datos = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]
# Se describe la funcion a usar
def reversibles(x):
	# Se escribe una variable para estraer el reverso de las palabras
	datos2 = "".join(reversed(x)) 
	# Un condicional para evaluar las palabras
	if x==datos2 in datos:
		return True
	else:
		return False
# Se imprime el resultado
resultado = filter(reversibles, datos)
print (list(resultado))