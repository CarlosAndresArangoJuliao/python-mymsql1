import notas.nota as modelo

class Acciones:
    
    def crear (seft, usuario):
        print(f"OK {usuario[1]} !! Vamos a crear una nueva nota..")

        titulo = input ("Introduce el titulo de tu nota: ")
        descripcion = input ("Ingresa el contenido de la nota: ")
        
        nota = modelo.Nota (usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar [0]>= 1:
            print (f" \n Perfecto has guardado la nota {nota.titulo}")


        else:
            print (f"No se ha guardado la nota {usuario[1]}")

    def mostrar (self, usuario):
        print (f" \n Listo {usuario[1]}!! Aqui tienes tus notas: ")
        nota = modelo.Nota (usuario[0])
        notas = nota.listar()

        for nota in notas:
            print ("\n******************************************************")
            print(f"Titulo: {nota[2]}")
            print(f"Descripcion: {nota[3]}")
            print ("******************************************************")



    def borrar (self, usuario):
        print (f"\ Okey {usuario[1]} !! Vamos a borrar notas")

        titulo = input ( "Introduce el titulo sw la NOTA A BORRAR: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar [0] >=1:
            print (f" Hemos borrado la nota: {nota.titulo}")

        else:
            print (" No se ha borrado la nota, prueba de nuevo.")