import tornado.httpserver, tornado.websocket, tornado.ioloop, tornado.web
from tornado.options import define, options
#from querys import consulta
#from querys_cod import consulta_cod

encabezado = ""
dispositivo = ""
td = ""
identificacion = ""
nid = ""
fintrama = ""
#miclase = consulta()
#miclasecod = consulta_cod()


class WSHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is your response")
        print 'get message'
        self.finish()


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self, *args):
        print 'User is connected \n'

    def on_message(self, message):
        print 'recieved message %s\n' % message
        cadena = message.split("/")
        encabezado = cadena[0]
        dispositivo = cadena[1]
        td = cadena[2]
        identificacion = cadena[3]
        nid = cadena[4]
        fintrama = cadena[5]
        if ((encabezado == "I" or encabezado == "B" or encabezado == "C" or encabezado == "D") and fintrama == "X" and int(nid) == len(identificacion)):
            self.write_message('ACK')
            print 'Encabezado de trama: %s' % encabezado
            print 'El dispositivo que llega es: %s' % dispositivo
            print 'el tipo de documento de identificacion: %s' % td
            print 'El numero de identificacion: %s' % identificacion
            print 'El numero de caracteres: %s' % nid
            print 'El fin de trama es: %s ' % fintrama
            print  "La longitud de la trama es: ", len(identificacion)
            if (encabezado == "I"):
				print("llego dato")
 #               miclase.insertar(dispositivo, identificacion)
            if (encabezado == "B"):
                print("llego dato")
  #              miclase.delete(identificacion)
            if (encabezado == "C"):
                print("llego dato")
   #             miclasecod.insertar(dispositivo, identificacion)
            if (encabezado == "D"):
                print("llego dato")
                #miclasecod.delete(identificacion)
        else:
            self.write_message('NACK')
            print("NACK")

    def on_close(self):
        print 'connection closed\n'


if __name__ == "__main__":
    app = tornado.web.Application(handlers=[(r'/', WebSocketHandler), ])
    app.listen(8080)
    print "Server Start"
    tornado.ioloop.IOLoop.instance().start()
