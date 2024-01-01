#generador de hashes para cifrar contraseñas,Hash soportados: (md5,sha1,sha224,sha384,sha256,sha512)


from hashlib import md5,sha1,sha224,sha384,sha256,sha512
import sys 
from os import system


class Codificador:


      def argumentos_entrada(self):
          '''
          creamos una funcion la cual tomara argumentos de entrada del usuario si es que los hubiera, por ejemplo ( -h  o --help ) y devolvera una salida
          '''
          if __name__ == "__main__":
            for self.x in sys.argv:
               self.x=self.x.lower()
               if bool(self.x) != False and self.x == "-h" or self.x == "--help":
                   print("""
GNU hasher 0.4 
Usage: python hasher.py

-h    --help    print this help   
                                                                   
                       """)

                   sys.exit()
                   
               
                
      def limpiador_consola(self):
          '''
           creamos una funcion la cual limpiara la consola dependiente del nucleo del sistema
          '''
          self.nucleo=sys.platform.lower()
          if self.nucleo in ["linux","darwin"]:
              system("clear")
          elif self.nucleo == "win32":
              system("cls")
          else:
              print("arquitectura no soportada")
              sys.exit()  

          return
        

      def contraseña_usuario(self):
           '''
           creamos una funcion la cual le pedira la contraseña al usuario
           '''
           while True:
            try:
               
               print("""
Bienvenido a hasher, la mejor herramienta de cifrado de contraseñas
                
                Lista de hash disponibles a utilizar:
                
                md5
                sha1
                sha224
                sha384
                sha256
                sha512
                
NOTA: \"sha1\" y \"md5\" se consideran inseguros ante ataques
                """)
               
               self.hash=input("que hash le gustaria utilizar >> ").lower()
               self.limpiador_consola()
               
               if bool(self.hash) != False and self.hash in ["md5","sha1","sha224","sha384","sha256","sha512"]:
                     self.clave_usuarioSin=input("ingrese su contraseña >> ")
                     break
                  
               else:
                    
                     self.consulta=input("valor incorrecto, deseas volver a intentarlo (SI o NO): ").lower()
                     if bool(self.consulta) == False or self.consulta != "si":
                       self.limpiador_consola()
                       print("bye")
                       sys.exit()

                    
                        


            except KeyboardInterrupt:
                    self.limpiador_consola()
                    print("bye")
                    sys.exit()    

 
      def guardar_hash(self):
          '''
          creamos una funcion la cual nos permitira guardar la contraseña codificada y no codificada
          '''
          while True:
             guardar_contraseña=input("a usted le gustaria guargar la contraseña >> ").lower()
             if guardar_contraseña == "si":

               #contraseña codificada
               self.Contraseña_Con_Hash="contraseñacodificada.txt"
               self.contraseña_ConHash=open(self.Contraseña_Con_Hash,'w')
               self.contraseña_ConHash.write(self.clave_usuario + "\n")
               self.contraseña_ConHash.close()


               #contraseña no codificada
               self.Contraseña_Sin_Hash="contraseña.txt"
               self.contraseña_SinHash=open(self.Contraseña_Sin_Hash,'w')
               self.contraseña_SinHash.write(self.clave_usuarioSin + "\n")
               self.contraseña_SinHash.close()
               
               break
             

             else:
                 return
             


      def cifrado(self):
          '''
          creamos una funcion la cual nos generara un hash de una contraseña brindada por el usuario
          '''
          try:

            
              if self.hash == "md5":
                self.clave_usuario=md5(self.clave_usuarioSin.encode('utf8')).hexdigest()
                self.limpiador_consola()
                print(f"Esta es la contraseña codificada por el hash md5: {self.clave_usuario} \n")
                self.guardar_hash()


              elif self.hash == "sha1":
                  self.clave_usuario=sha1(self.clave_usuarioSin.encode('utf8')).hexdigest()
                  self.limpiador_consola()
                  print(f"Esta es la contraseña codificada por el hash sha1: {self.clave_usuario} \n")
                  self.guardar_hash()


              elif self.hash == "sha224":
                  self.clave_usuario=sha224(self.clave_usuarioSin.encode("utf8")).hexdigest()
                  self.limpiador_consola()
                  print(f"Esta es la contraseña codificada por el hash sha224: {self.clave_usuario} \n")
                  self.guardar_hash()


              elif self.hash == "sha384":
                  self.clave_usuario=sha384(self.clave_usuarioSin.encode("utf8")).hexdigest() 
                  self.limpiador_consola()
                  print(f"Esta es la contraseña codificada por el hash sha384: {self.clave_usuario} \n")
                  self.guardar_hash()


              elif self.hash == "sha256":
                  self.clave_usuario=sha256(self.clave_usuarioSin.encode("utf8")).hexdigest()
                  self.limpiador_consola()
                  print(f"Esta es la contraseña codificada por el hash sha256: {self.clave_usuario} \n")
                  self.guardar_hash()


              elif self.hash == "sha512":
                  self.clave_usuario=sha512(self.clave_usuarioSin.encode("utf8")).hexdigest()
                  self.limpiador_consola()
                  print(f"Esta es la contraseña codificada por el hash sha512: {self.clave_usuario} \n")
                  self.guardar_hash()


              

          except KeyboardInterrupt:
                    self.limpiador_consola()
                    print("bye")
                    sys.exit()   


clave=Codificador()

clave.argumentos_entrada()
clave.limpiador_consola()
clave.contraseña_usuario()
clave.cifrado()



__name__="hasher"
__version__="0.4"