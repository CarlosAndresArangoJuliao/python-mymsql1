
import datetime
import hashlib
import usuarios.conexion as conexion  #importar modulo conexion que esta paquiete usuarios  y lo llamaremos conexion

connect = conexion.conectar()    # variable connect llamar metodo conectar que esta dentro de coexion
database = connect[0]            #indice cero donde eeta la base de datos
cursor = connect[1]              #indice uno  donde esta el cursor



class Usuario:

    def __init__(self, nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
                                #METODO REGISTRAR
    def registrar(self):

        fecha = datetime.datetime.now()

                                #CIFRAR CONTRASEÑA

        cifrado = hashlib.sha256()    # metodo de cifrado sha256()
        cifrado.update(self.password.encode('utf8')) #se utiliza el metodo de cifrado .encode('utf8')
        sql =  "INSERT INTO usuarios VALUES (null ,%s,%s,%s,%s,%s)"
        usuario=(self.nombre,self.apellidos,self.email,cifrado.hexdigest(),fecha)  #tupla que remplaza los %

        
        try:
            cursor.execute (sql,usuario)
            database.commit()
            result= [cursor.rowcount, self ]
        except:
            result= [0,self]

        return result


                                #CONSULTA COMPROBAR SI EXISTE USUARIO 

    def identificar (self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        cifrado = hashlib.sha256()    # metodo de cifrado sha256()
        cifrado.update(self.password.encode('utf8')) #se utiliza el metodo de cifrado .encode('utf8')
        
        #DATOS PARA CONSULTA
        usuario = (self.email, cifrado.hexdigest())

        #CONSULTA
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result