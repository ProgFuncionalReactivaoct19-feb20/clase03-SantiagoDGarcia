"""
	Clase 2
	@SantiagoDGarcia
"""
datos = ["lba-001", "gma-002", "azx-003", "ess-004",  "oro-100", "mab-001", "iaj-002"]
# Se describe la funcion a usar
def provincias_placa(x):
	# Se define las iniciales de las provincias para mayor facilidad
	provincias = ["l", "p", "e", "a", "i"]
	# Un ciclo repititivo para evaluar las placas de la matriz
	if x[0] in provincias:
		return True
	else:
		return False
# Se escriben las 2 funciones
resultado = filter(provincias_placa, datos)
print (list(resultado))