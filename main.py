"""
Proyecto
-abrir asistente
-Login o Registro
-si elegimops registro, creara un usuario y una contraseña en la BBDD
-si elegimos Login, se identifica usuario y nos preguntara
-crear nota, mostrar nota, borrar nota.
"""
from usuarios import acciones

print("""
Acciones disponibles:
-registro 
-login
""")

hazEl=acciones.Acciones()
accion = input ("¿Que quieres hacer: ")

if accion == "registro":
    hazEl.registro()
   

elif accion == "login":
    hazEl.login()
    