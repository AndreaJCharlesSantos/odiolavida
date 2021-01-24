class Cliente(object):
    count=0
    #Los atributos de cliente
    def __init__(self):
     self.name = input("Ingrese el nombre del cliente ")
     self.date = input("Ingrese la fecha de nacimiento dd/mm/yyyy ")
     self.curp = input("Ingrese CURP de la persona ")
     self.address = input("Ingrese la dirección ")
     self.phone = int(input("Ingrese el número de teléfono "))
     self.first_deposit = int(input("Ingrese el deposito "))
     self.account_type = input("Seleccione el tipo de cuenta: \n1. Ahorro \n2. Actual \n3. Por un año. \n4. Por dos años \n5. Por tres años \n")
     
     Cliente.count=Cliente.count+1  
    #FUNCIÓN PARA IMPRIMIR CLIENTE     
    def ImprimeCliente(self):
     print("Datos de usuario:\nNombre:",self.name,"\nFecha de nacimiento:",self.date,"\nCURP:",self.curp,"\nDirección:",self.address,"\nTeléfono:",self.phone,"\nPrimer deposito:",self.first_deposit,"\nTipo de cuenta:",self.account_type)
     print("Total de usuarios: ", self.count)
     
     
class Menu():
    op=0
    global listaclientes
    listaclientes = []
    
    #FUNCIÓN PARA CREAR CLIENTE  
    def NewAccount():
     print("        ||||||||||CREA UNA NUEVA CUENTA||||||||||")
     listaclientes.append(Cliente())
    #FUNCIÓN PARA EDITAR
    def edit(self):
     print("         ||||||||||EDITA UNA CUENTA||||||||||")
    #FUNCIÓN PARA TRANSACCIÓN
    def transaccion(self):
     print("         ||||||||||REALIZA UNA TRANSACCIÓN ||||||||||")
    #FUNCIÓN PARA VER 
    def ver(self):
     print("         ||||||||||VER CLIENTE||||||||||")
      
    #FUNCIÓN PARA BORRAR 
    def delete(self):
     print("         |||||||||BORRAR CLIENTE||||||||")
    #FUNCIÓN PARA VER LISTA 
    def view_list():
     print("         |||||||||VER LISTA||||||||")
     for j in listaclientes:
      clientes_1 = listaclientes[j]
      print(Clientes_1)
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
 

#Termina clase
MenuBanco=Menu()
MenuBanco.menuprincipal()
print (listaclientes[0].date)
