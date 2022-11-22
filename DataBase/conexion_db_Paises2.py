"""
	Tutorial de CRUD con MySQL y Python 3
	parzibyte.me/blog
"""
import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db_paises')
	try:
		with conexion.cursor() as cursor:
			#Filtramos los paises que en 2021 aumentaron un 10% las emisiones per cápita de CO2 con respecto al año anterior.
			consulta = "SELECT Paises, Var FROM Paisest_co2 WHERE Var > %s ORDER BY Var DESC;"
			cursor.execute(consulta, (10.00))
            
			# Con fetchall traemos todas las filas
			db_paises = cursor.fetchall()
			#db_paises = cursor.fetchone()
            
			# Recorrer e imprimir
			for db_paises in db_paises:
				print(db_paises)
	    
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)