import os

class Cliente(object):
    #Los atributos de cliente
    def __init__(self, name, date, curp, address, phone, first_deposit, account_type):
     self.name = name
     self.date = date
     self.curp = curp
     self.address = address
     self.phone =  phone
     self.first_deposit = first_deposit
     self.account_type = account_type

    #Función para ingresar clientes
    def IngresarCliente(self):
      archivocliente=open("Archivo.txt", "a")
      #se cambio el guardado para que se separado por | para posterior trabajar con posiciones
      archivocliente.write(self.name + "|")
      archivocliente.write(self.date + "|" )
      archivocliente.write(self.curp + "|")
      archivocliente.write(self.address + "|")
      archivocliente.write(self.phone + "|")
      archivocliente.write(self.first_deposit + "|")
      archivocliente.write(self.account_type + "\n")
      archivocliente.close()
    
    #Función para borrar clientes


class Menu():
    num=0
    cont = 0
    #FUNCIÓN PARA CREAR CLIENTE  
    def NewAccount():
     print("        ||||||||||CREA UNA NUEVA CUENTA||||||||||") 
     nombre = input("Ingrese el nombre del cliente: ")
     date=input("Ingrese la fecha de nacimiento dd/mm/yyyy: ")
     curp=input("Ingrese CURP de la persona: ")
     address=input("Ingrese la dirección: ")
     phone=input("Ingrese el número de teléfono: ")
     first_deposit=input("Ingrese el deposito: ")
     account_type=input("Seleccione el tipo de cuenta: \n1. Ahorro \n2. Actual \n3. Por un año. \n4. Por dos años \n5. Por tres años ")
     NUEVACUENTA=Cliente(nombre,date,curp,address,phone,first_deposit,account_type)
     Cliente.IngresarCliente(NUEVACUENTA)  
     op=int(input("Ingrese un número para continuar "))
    #Función para buscar clientes
    def BuscarCliente(self):
     cont=0
     num = input("Ingresa la CURP: ")
     archivocliente=open("Archivo.txt", "r")
     existe = 0
     for j in archivocliente:
      #print("Registro: "+j) # se parte la cadena con | y se trabaja con posiciones
      nueva = j.split('|')
      cont = cont+1
      if nueva[2] == num:
        '''linea = archivocliente.readline()'''
        '''print(linea)'''
        print('Nombre: '+ nueva[cont-2])
        print('Fecha: '+ nueva[cont-1])
        print('Curp: '+ nueva[cont])
        print('Dirección: '+ nueva[cont+1])
        print('Telefono: '+ nueva[cont+2])
        print('Deposito: '+ nueva[cont+3])
        print('Tipo: '+ nueva[cont+4])
        existe = 1
     archivocliente.close()
     if existe == 0:
       print("No se encontró al cliente")  


    def BorrarCliente(self):
      num = input("Ingrese la CURP del cliente: ")
      archivocliente = open("Archivo.txt", "r") #Abres archivo original
      archivocopia=open("Archivocopia.txt", "a") #Este es uno de copia para reemplazar
      eliminar = 0 #Para inicializar la posición correspondiente a la lista
      for j in archivocliente: #Aquí hace el for para guardar en el copia <- Marca el error aquí
        if num in j:
          eliminar = 7
        if j == 0:
          archivocopia.write(j)
        else:
          eliminar = eliminar - 1
      archivocliente.close()   
      archivocopia.close()

      archivocliente = open("Archivo.txt", "w")
      archivocopia = open("Archivocopia.txt","r")
      for j in archivocopia:
        archivocliente.write(j)
      archivocliente.close()
      archivocopia.close()
      os.remove("Archivocopia.txt")
    #Función para ver lista
    
    def view_list(self):
     archivocliente = open("Archivo.txt", "r")
     for j in archivocliente:
      print (j)
     archivocliente.close()
     op=int(input("Ingrese un número para continuar "))

    #FUNCIÓN MENÚ PRINCIPAL
    def menuprincipal(self):
     op = 0
     while op != 7:
      print("                                       ||||||BIENVENIDO AL MENÚ PRINCIPAL||||||  \n ")
      print("1.Crea una nueva cuenta")
      print("2.Editar información en una cuenta existente")
      print("3.Transacción")
      print("4.Checar los detalles de una cuenta existente")
      print("5.Borrar cuenta")
      print("6.Lista de los clientes existentes")
      print("7.Salir")
      op = int(input("Ingresa la opción "))
      if op == 1:
       Menu.NewAccount()
      elif op == 2:
       print("         ||||||||||EDITA UNA CUENTA||||||||||")
      elif op == 3:
       print("         ||||||||||REALIZA UNA TRANSACCIÓN ||||||||||")
      elif op == 4:
       print("         ||||||||||VER CLIENTE||||||||||")
       Menu.BuscarCliente(self)        
      elif op == 5:
       print("         |||||||||BORRAR CLIENTE||||||||")
       Menu.BorrarCliente(self)       
      elif op == 6:
       print("         |||||||||VER LISTA||||||||")
       Menu.view_list(self)
      elif op == 7:
       print("Gracias por usar el programa")
       exit   
      elif op != 1 or op != 2 or op != 3 or op != 4 or op != 5 or op != 6 or op != 7:
        print("Ingrese una opción correcta")
 

#Termina clase

#archivocliente = Cliente()
MenuBanco=Menu()
MenuBanco.menuprincipal()
