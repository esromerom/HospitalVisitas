import MySQLdb

class consulta_cod:
        dispositivo=0
        codigo=0
        #db=MySQLdb.connect("localhost","root","acceso","usuarios")
        def _init_(self,dispositivo,codigo,db):
                self.dispositivo=dispositivo
                self.cedula=codigo
        def insertar(self,dispositivo,codigo):
	        db=MySQLdb.connect(host="localhost",user="cedula",passwd="acceso",db="usuarios")
        	cursor=db.cursor()
		notificacion="Codigo insertado con exito"
        	try:
                	cursor.execute("INSERT INTO autenticacion (id_dispositivo,codigo) VALUES (%s,%s)",(dispositivo,codigo))
                	db.commit()
              		return(notificacion)
       		except:
                	db.rollback()
       		db.close()
	def buscar(self,codigo):
        	db = MySQLdb.connect(host="localhost",user="cedula",passwd="acceso",db="usuarios" )
        	cursor = db.cursor()
        	notificacion="La busqueda del codigo fue realizada con exito"
		try:
			cursor.execute("select id_dispositivo from autenticacioncod where codigo=%s",(codigo,))
                	results = cursor.fetchall()
                	if not results:
				return 0
			for row in results:
                        	disp=row[0]
               			return disp
		except:
                		print("Error en busqueda de codigo")
        	db.close()

	def delete(self,codigo):
		notificacion="Eliminacion del codigo realizada con exito"
        	db=MySQLdb.connect(host="localhost",user="cedula",passwd="acceso",db="usuarios")
       		cursor=db.cursor()
	        try:
        	        cursor.execute("delete from  autenticacion where codigo=%s",(codigo,))
                	db.commit()
                	return(notificacion)
        	except:
               		db.rollback()
        	db.close()
	def actualizar(self,dispositivo,codigo):
                notificacion="Actualizacion realizada con exito"
                db = MySQLdb.connect(host="localhost",user="cedula",passwd="acceso",db="usuarios")
                cursor = db.cursor()
                try:
                        cursor.execute("update autenticacion set id_dispositivo=%s where codigo=%s",(dispositivo,codigo))
                        db.commit()
                        return notificacion
                except:
                        db.rollback()
                        print "Error: unable to fecth data"
                db.close()


