from tkinter import *
import os

def ventana_inicio():
    global ventana_principal
    vcolor = "DarkGrey"
    ventana_principal = Tk()
    ventana_principal.geometry("300x500")
    ventana_principal.title("Login con tkinter")
    Label(text="Escoja su opcion",bg="LightGreen", width="300", height="2", font=("Calibri",13)).pack()
    Button(text="Acceder", height="2", width="30",bg=vcolor,command=login).pack()
    Button(text="Registrar", height="2", width="30",bg=vcolor,command=registro).pack()
    ventana_principal.mainloop()

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca el nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()

    global verifica_usuario
    global verifica_clave

    verifica_usuario = StringVar()
    verifica_clave = StringVar()

    global entrada_login_usuario
    global entrada_login_clave

    Label(ventana_login, text="Nombre de usuario (*)").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()

    Label(ventana_login, text="");

    Label(ventana_login, text="Contraseña (*):").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show="*")
    entrada_login_clave.pack()

    Label(ventana_login, text="");

    Button(ventana_login, text="Acceder", width="10", height="1", command=verifica_login).pack()

def verifica_login():

    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()

    entrada_login_usuario.delete(0, END)
    entrada_login_clave.delete(0, END)

    lista_archivos = os.listdir()

    if(usuario1 in lista_archivos):
        archivo1 = open(usuario1, "r")
        verifica = archivo1.read().splitlines()

        if clave1 in verifica:
            exito_login()
        else:
            no_clave()
    else:
        no_usuario()
            

def exito_login():
    global ventana_exito 
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="Ok", command=borrar_exito_login).pack()
    

def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")

    global nombre_usuario
    global clave

    global entrada_nombre
    global entrada_clave

    nombre_usuario = StringVar()
    clave = StringVar()

    Label(ventana_registro, text="Introduzca sus datos", bg="LightGreen").pack()

    Label(ventana_registro, text="");

    Label(ventana_registro,text="Nombre de usuario (*):").pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario)
    entrada_nombre.pack()

    Label(ventana_registro,text="");

    Label(ventana_registro,text="Contraseña (*):").pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave)
    entrada_clave.pack()

    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command=registro_usuario).pack()



def registro_usuario():
    usuario_info = nombre_usuario.get();
    clave_info = clave.get()

    file = open(usuario_info, "w" )
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()

    entrada_nombre.delete(0, END);
    entrada_clave.delete(0, END);

    Label(ventana_registro, text="Registro completado con exito", bg="green", font=("calibri", 11)).pack()

def borrar_exito_login(): 
    ventana_exito.destroy()

def borrar_no_clave():
    ventana_no_clave.destroy()

def borrar_no_usuario():
    ventana_no_usuario.destroy()

def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta").pack()
    Button(ventana_no_clave,text="Ok", command=borrar_no_clave).pack()

def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario,text="Ok", command=borrar_no_usuario).pack()












    
