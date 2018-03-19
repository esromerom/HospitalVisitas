import MySQLdb

class consulta:
	
	identificacion = 0
	cedula=0
	fechahorainicio = ""
	fechahorafin = ""
	tipo = ""
	idcama = 0
#	db=MySQLdb.connect(host="servidorcedulas",user="root",passwd="acceso",db="usuarios")
	def _init_(self,identificacion,dispositivo,cedula,fechahorainicio,fechahorafin,tipo,idcama,db):
		self.identificacion=identificacion
		self.fechahorainicio=fechahorainicio
		self.fechahorafin = fechahorafin
		self.tipo = tipo
		self.idcama = idcama		
	def insertar(self,identificacion,dispositivo,fechahorainicio,idcama):
		db=MySQLdb.connect(host="localhost",user="hospital",passwd="Acceso2018*",db="hospital")
        	cursor=db.cursor()
	        notificacion="Insercion"
		try:
        	        cursor.execute("INSERT INTO asistencia (identificacion,dispositivo,idcama,fechahorainicio) VALUES (%s,%s,%s,%s)",(identificacion,dispositivo,idcama,fechahorainicio))
                	db.commit()
                	print "exito"
       		except:
			print "fallo"
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






