import MySQLdb

class consulta:
	dispositivo=0
	cedula=0
#	db=MySQLdb.connect(host="servidorcedulas",user="root",passwd="acceso",db="usuarios")
	def _init_(self,dispositivo,cedula,db):
		self.dispositivo=dispositivo
		self.cedula=cedula
	def insertar(self,dispositivo,cedula):
		db=MySQLdb.connect(host="localhost",user="cedula",passwd="acceso",db="usuarios")
        	cursor=db.cursor()
	        notificacion="INsercion"
		try:
        	        cursor.execute("INSERT INTO autenticacioncc (id_dispositivo,cc) VALUES (%s,%s)",(dispositivo,cedula))
                	db.commit()
                	return notificacion
       		except:
                	db.rollback()
       		db.close()
	def buscar(self,cedula):
	        db = MySQLdb.connect(host="localhost",user="cedula",passwd="acceso",db="usuarios" )
		cursor = db.cursor()
       		try:
			disp = 0
			cursor.execute("select id_dispositivo from autenticacioncc where cc=%s",(cedula,))
               		results = cursor.fetchall()
			if not results:
				return int(disp)
			for row in results:
				disp=row[0]
				#disp = numpy.ravel(d)
				return int(disp)
		except:
		        print("Error en consulta")
       		db.close()
	def delete(self,cedula):
		notificacion="Eliminacion realizada con exito"
		db=MySQLdb.connect(host="localhost",user="cedula",passwd="acceso",db="usuarios")
	        cursor=db.cursor()
	        try:
        	        cursor.execute("delete from  autenticacion where cc=%s",(cedula,))
                	db.commit()
                	return notificacion
        	except:
                	db.rollback()
        	db.close()
	def actualizar(self,dispositivo,cedula):
                notificacion="Actualizacion realizada con exito"
                db = MySQLdb.connect(host="localhost",user="cedula",passwd="acceso",db="usuarios" )
                cursor = db.cursor()
                try:
                        cursor.execute("update autenticacioncc set id_dispositivo=%s where cc=%s",(dispositivo,cedula))
                        db.commit()
                        return notificacion
                except:
                        db.rollback()
                        print "Error: unable to fecth data"
                db.close()






