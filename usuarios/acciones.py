import usuarios.usuario as modelo
import notas.acciones

class Acciones: 

    def registro (self):
        print (" \n Ok!! VAmos a registrarte en el sistema...")

        nombre= input("\n Cual es tu nombre?  ")
        apellidos= input("\n Cuales son tus apellidos?  ")
        email= input("\n Introduce tu email: ")
        password= input(" \n introduce tu passwword o contraseña:  ")

                                                
                                                 #OBJETO CREADO 

        usuario = modelo.Usuario(nombre, apellidos, email,password)
        registro = usuario.registrar()

        if registro[0]>=1:
            print (f"\n Perfecto {registro[1].nombre} te has registrado con el email:  {registro[1].email}")
        else:
            print ("""\n No tea has registrado correctamente!!!!
            Puede que tu email ya este registrado""")




                                            #login

    def login (self):
        print (" \n Correcto!!  identificate en el sistema...")

        try:
            email = input (" Introduce tu email:")
            password = input("introduce tu passwword o contraseña:")

            usuario = modelo.Usuario( '', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\n Bienvenido {login[1]},te has logiado correctamente y te registraste el{login[5]}")
            
            
                self.proximasAcciones(login)

        except Exception as e:
            print("\n ")
            print (type (e))
            print (type (e).__name__)  #poder sacar el error emn concreto
            print (f"Login incorrecto!!! Intentalo de nuevo.")
        
    def proximasAcciones(self, usuario):

        print("""
            acciones disponibles:

            -Crear nota (crear)
            -Mostrar tus notas (Mostrar)
            -Eliminar notas (Eliminar)
            -Salir (Salir)
        """)

        accion = input ("¿Que deseas hacer?; ")
        hazEl= notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "salir":
            print (f"Hasta pronto {usuario[1]}!!!")
            exit()

        