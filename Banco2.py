class Cliente(object):
    count=0
    #Los atributos de cliente
    def __init__(self):
     self.name = input("Ingrese el nombre del cliente: ")
     self.date = input("Ingrese la fecha de nacimiento dd/mm/yyyy: ")
     self.curp = input("Ingrese CURP de la persona: ")
     self.address = input("Ingrese la dirección: ")
     self.phone = int(input("Ingrese el número de teléfono: "))
     self.first_deposit = int(input("Ingrese el deposito: "))
     self.account_type = input("Seleccione el tipo de cuenta: \n1. Ahorro \n2. Actual \n3. Por un año. \n4. Por dos años \n5. Por tres años \n")
     Cliente.count=Cliente.count+1  

class Menu():
    num=0
    global listaclientes
    listaclientes = []
    
    #FUNCIÓN PARA CREAR CLIENTE  
    def NewAccount():
     print("        ||||||||||CREA UNA NUEVA CUENTA||||||||||")
     listaclientes.append(Cliente())
     op=int(input("Ingrese un número para continuar "))
    #FUNCIÓN PARA EDITAR
    def edit():
     print("         ||||||||||EDITA UNA CUENTA||||||||||")
     num = input("Ingrese la CURP de la persona: ")
     for j in listaclientes:
      if j.curp == num:
       a = int(input("¿Qué desea modificar:\n1. Dirección\n2. Número de teléfono "))
       if a == 1:     
         modificacion = input("Ingrese la nueva dirección: ")
         j.address = modificacion
       elif a == 2:
         modificacion = input("Ingrese el nuevo número: ")
         j.phone = modificacion
      elif a != 1 or a != 2:
         print("No existe tal cuenta")     
    #FUNCIÓN PARA TRANSACCIÓN
    def transaccion():
     print("         ||||||||||REALIZA UNA TRANSACCIÓN ||||||||||")
     num=input("Ingrese la CURP de la persona: ")
     for j in listaclientes:
      if j.curp == num:
       a = input("Desea\n1. Depositar\n2. Sacar dinero: ")
       if a == 1:
     
    #FUNCIÓN PARA VER 
    def ver():
     print("         ||||||||||VER CLIENTE||||||||||")
     num=int(input("Lo buscará en base en: \n1. CURP\n2. Nombre\n"))
     if num == 1:
      a=input("CURP de la cuenta: ")
      for j in listaclientes:
       if j.curp == a:
        print('Nombre : {}, Fecha de nacimiento : {}, CURP : {}, Dirección : {}, Teléfono : {}, Deposito : {}, Tipo de cuenta : {} '.format(j.name,j.date,j.curp,j.address,j.phone,j.phone,j.first_deposit,j.account_type))
       else:
         print("No existe tal cuenta")
     elif num == 2:
       a=input("Nombre de la cuenta: ")
       for j in listaclientes:
        if j.name == a:
         print('Nombre : {}, Fecha de nacimiento: {}, CURP: {}, Dirección: {}, Teléfono: {}, Deposito: {}, Tipo de cuenta: {} '.format(j.name,j.date,j.curp,j.address,j.phone,j.phone,j.first_deposit,j.account_type))  
        elif j.name != a:
         print("No existe tal cuenta")
    #FUNCIÓN PARA BORRAR 
    def delete():
     print("         |||||||||BORRAR CLIENTE||||||||")
     num = input("Ingrese la CURP de la cuenta ")
     for j in listaclientes:
      if j.curp == num:
       listaclientes.remove(j)
      else:
       print("No existe tal cuenta")
     op=int(input("Ingrese un número para continuar "))
    #FUNCIÓN PARA VER LISTA 
    def view_list():
     print("         |||||||||VER LISTA||||||||")
     for j in listaclientes:
      print('Nombre : {}, Fecha de nacimiento: {}, CURP: {}, Dirección: {}, Teléfono: {}, Deposito: {}, Tipo de cuenta: {} '.format(j.name,j.date,j.curp,j.address,j.phone,j.phone,j.first_deposit,j.account_type))
     op=int(input("Ingrese un número para continuar "))
    #FUNCIÓN PARA SALIR 
    def salida():
     print("Gracias por usar el programa")
     exit    
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
      print("6.Ver los clientes")
      print("7.Salir")
      op = int(input("Ingresa la opción "))
      if op == 1:
       Menu.NewAccount()
      elif op == 2:
       Menu.edit()
      elif op == 3:
       Menu.transaccion()
      elif op == 4:
       Menu.ver()
      elif op == 5:
       Menu.delete()
      elif op == 6:
       Menu.view_list()
      elif op == 7:
       Menu.salida()
      elif op != 1 or op != 2 or op != 3 or op != 4 or op != 5 or op != 6 or op != 7:
        print("Ingrese una opción correcta")
 

#Termina clase
MenuBanco=Menu()
MenuBanco.menuprincipal()
