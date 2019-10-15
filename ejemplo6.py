"""
	Clase 2
	@SantiagoDGarcia
"""

def es_vocales(x):
	vocales = ["a", "e", "i","o", "u"]
	if x in vocales:
		return True
	else:
		return False

datos = ["e", "c", "u", "a", "d", "o", "r"]
resultado = filter(es_vocales, datos)

print (list(resultado))