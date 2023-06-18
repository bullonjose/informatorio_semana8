from datetime import date
class Usuario():
    #El metodo constructor inicia con cadenas vacias ya que ciertos atributos solo serían necesarios si el usuario se registra.
    #Incluimos contraseña y usuario en el constructor porque mas adelante creamos instanciamos por defecto para facilitar las pruebas
    
    def __init__(self, contraseña, usuario):
        self.fecha_registro = date.today()
        self.online = False
        self.__contraseña = contraseña
        self.__username = usuario
        self.id = " "
        self.nombre = " "
        self.apellido = " "
        self.telefono = " "
        self.email = " "
       
        
    #Si el usuario se registra se le piden datos por consola para adjuntarlos a su perfil.
    #El usuario registrado posteriormente es cargado a una lista externa de usuarios :)
    def registrar(self):
        self.id = input("Ingrese DNI \n")
        self.nombre = input("Ingrese Nombre \n")
        self.apellido = input("Ingrese Apellido \n")
        self.telefono = input("Ingrese Telefono \n")
        self.email = input("Ingrese Email \n")
        
       
       
    #Se entiende que el estado inicial de un usuario que no esta logueado es offline, eso se modifica al iniciar sesion 
    #El metodo comprueba si las credenciales son correctas y modifica su estado a online.
    def login(self, username_ingresado, contraseña_ingresada):
        if self.__username == username_ingresado and self.__contraseña == contraseña_ingresada:
            self.online = True
            return True
        else:
            return False

    #Metodos para obtener atributos encapsulados           
    def get_contraseña(self):
        return self.__contraseña
    
    def get_usuario(self):
        return self.__username
            
             
class Publico(Usuario):
    
    def __init__(self, contraseña, usuario):
        super().__init__(contraseña, usuario)
        self.es_publico = True
        self.es_colaborador = False
        
          
    #Instanciando un objeto de la clase "comentario" podemos agregarlo a una lista como atributo de un articulo especifico
    #Trabajamos con dos metodos en conjunto, uno de ellos esta definido en la clase "Articulo". 
    #Externamente se recorre una lista de articulos para identificar el que quiere comentar el usuario.   
    def comentar(self,articulo, titulo):
        if titulo == articulo.titulo:
          texto = input("Escribe comentario: \n")
          objcomentario = Comentario(self.get_usuario(), articulo.id_articulo, texto)
          articulo.agregar_comentario(objcomentario)
          print(self.get_usuario() + " comentaste el articulo titulado " + articulo.titulo + " diciendo: " + texto)
          return True
        else:
            return False
      
        
        
class Colaborador(Usuario):
    
    def __init__(self, contraseña, usuario):
        super().__init__(contraseña, usuario)
        self.es_colaborador = True
        self.es_publico = False
      
    
    def comentar(self,articulo, titulo):
        if titulo == articulo.titulo:
          texto = input("Escribe comentario: \n")
          objcomentario = Comentario(self.get_usuario(), articulo.id_articulo, texto)
          articulo.agregar_comentario(objcomentario)
          print(self.get_usuario() + " comentaste el articulo del autor " + articulo.nombre_usuario + " titulado " + articulo.titulo + " diciendo: " + texto)
          return True
        else:
            return False
    
    
    #Instanciamos un articulo y lo relacionamos al colaborador que lo publica a traves de este metodo para posteriormente ser cargado en una lista de articulos externa.    
    def publicar(self):
        titulo_articulo = input("Cual es el titulo de su articulo? \n")
        resumen_articulo = input("Un resumen del articulo? \n")
        contenido_articulo = input("Contenido del articulo? \n")
        articulo = Articulo(self.get_usuario(), titulo_articulo, resumen_articulo, contenido_articulo)
        lista_articulos.append(articulo)
        print("Tu articulo titulado " + titulo_articulo + " fue publicado correctamente a la lista de articulos en nuestro blog")
        
    
class Articulo():
    id_articulo = 0
    def __init__(self, nombre_usuario, titulo, resumen, contenido):
        Articulo.id_articulo += 1 #cada vez que creamos un articulo, se auto incrementa el id. 
        self.nombre_usuario = nombre_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.comentarios = []
    
    #Trabaja en conjunto con el metodo comentar definido en las clases publico y colaborador 
    def agregar_comentario(self, comentario):
     self.comentarios.append(comentario)
        
class Comentario():
   
    def __init__(self, usuario, id_articulo, contenido):
        self.nombre_usuario = usuario
        self.id_articulo = id_articulo
        self.contenido = contenido
        
        
#Instanciamos clases de usuarios por defecto utilizando argumentos de clave.
#Se pueden utilizar las credenciales predefinidas de los usuarios registrados para acceder por consola 
#Los animales domesticos son publico y los salvajes colaboradores :)        
usuario1 = Publico(contraseña = "gato", usuario = "gato")
usuario2 = Publico(contraseña = "perro", usuario = "perro")
usuario3 = Colaborador(contraseña = "leon", usuario = "leon")
usuario4 = Colaborador(contraseña = "tigre", usuario = "tigre")

#Por consola se comentan los articulos ingresando los titulos de los articulos precargados en la lista "blancanieves" / "transformers"
#Tambien se puede cargar un articulo y luego comentarlo :) 
articulo1 = Articulo("hermanos grimm", "blancanieves", "la princesa con 7 enanos", "asdasd")
articulo2 = Articulo("Michael Bay", "transformers", "Robots Epikos", "habia una vez..." )


lista_usuarios =[usuario1, usuario2, usuario3, usuario4]
lista_articulos = [articulo1, articulo2]
"""__________________________________________________________________________________________________________"""

print("BIENVENIDO AL BLOG, SELECCIONA LA OPCION A REALIZAR:")


#Si el usuario elige registrarse tiene la opcion de hacerlo como publico o colaborador.
  #En ambos casos primero se le pide crear un usuario y contraseña. Datos necesarios para instanciar la clase.
  #Posteriormente se utiliza el metodo registrar para agregar los demas atributos requeridos.
  #dicho objeto (o usuario) es agregado a una lista de usuarios registrados. 
menu = "no"
while menu == "no": 
    opcion = int(input("Opcion 1: Registrarse, Opcion 2: Acceder \n"))
    if opcion == 1:
     categoria = int(input("1.Registrarse como Administrador, 2.Registrarse como publico \n"))
  
     if categoria == 1:
      contraseña = input("Ingrese Contraseña \n")
      usuario = input("Ingrese Nombre de Usuario \n")
      adm = Colaborador(contraseña, usuario) 
      adm.registrar()
      lista_usuarios.append(adm)
      
      print("Felicidades " + adm.get_usuario() + " desde hoy " + str(adm.fecha_registro) + " formas parte de este blog como Colaborador! :)")
   
     if categoria == 2:
      contraseña = input("Ingrese Contraseña \n")
      usuario = input("Ingrese Nombre de Usuario \n")
      pub = Publico(contraseña, usuario)
      pub.registrar()
      lista_usuarios.append(pub)
      
      print("Felicidades " + pub.get_usuario() + " desde hoy " + str(pub.fecha_registro) + " formas parte de este blog como Publico! :)")
   
   
   #Si el usuario elige loguearse se le van a pedir las credenciales por consola
   #Se verifica iterando la lista de usuarios registrados la existencia de alguno con las credenciales ingresadas.
   #De ser favorable el ingreso se verifica si el usuario es colaborador o publico. En base a su categoria se le muestra lo que puede hacer.
   
    if opcion == 2:
        username_ingresado = input("Ingrese su nombre de usuario: \n")
        contraseña_ingresada = input("Ingrese su contraseña: \n")
        for usuario in lista_usuarios:
            if usuario.login(username_ingresado, contraseña_ingresada):
                 print("Inicio de sesión exitoso.")
                 break
        else: 
            print("Usuario o contraseña incorrecta")         
        while usuario.online == True:                
         if usuario.es_publico == True and usuario.online == True:
              print(f"Bien {usuario.get_usuario()} ahora podes comentar los articulos de nuestro blog")
              titulo = input("ingrese el titulo del articulo a comentar \n")
              for art in lista_articulos:
                  if usuario.comentar(art, titulo):
                      break
              else:
                   print("No tenemos ese articulo")
        
         if usuario.es_colaborador == True and usuario.online == True:
              print(f"{usuario.get_usuario()} sos colaborador y por eso podes comentar articulos y publicar los mismos")
              que_hacer = int(input("1: Comentar Articulo, 2: Publicar Articulo \n"))
              
              if que_hacer == 1:
               titulo = input("Ingrese el titulo del articulo a comentar \n")
               for art in lista_articulos:
                  if usuario.comentar(art, titulo):
                      break
               else:
                   print("No tenemos ese articulo")
              
              if que_hacer == 2:
                  print("Estas a un paso de publicar tu articulo...")
                  usuario.publicar()
                 
         seguir = input("Quiere seguir en linea? [si/no] \n").lower()
         if seguir == "si":
          usuario.online = True
         else:
          usuario.online = False
                  
    menu = input("Quieres salir del blog? [si/no] \n").lower()
                 
    
          
                  
                  
              
    


   
     

 

