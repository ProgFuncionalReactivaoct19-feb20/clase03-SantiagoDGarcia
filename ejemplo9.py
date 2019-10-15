"""
	Clase 2
	@SantiagoDGarcia
"""
# Se ingresan los datos
datos = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala",  "Portoviejo", "Macas"]
# Se imprime el resultado
resultado = filter(lambda x: len(x)%2 == 0, datos)
print (list(resultado))