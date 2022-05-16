from Ciclista import Ciclista
ciclistas=[]
opcion=1
print("********* AÑADIR CICLISTA *********")
print("1---> Ingresar Ciclista")
print("2---> Mostrar el Ganador")
print("3---> Salir")
print("**********************************")

while(opcion!=3):
    opcion=int(input("digita una opcion: "))
    
    if(opcion==1):
        ciclista=Ciclista()
        ciclista.nombre=input("Digite el nombre del ciclista:  ")
        ciclista.edad=int(input("Digite la edad del ciclista:  "))
        ciclista.pais=input("Digite el pais del ciclista:  ")
        ciclista.tiempo=float(input("Digite el tiempo del ciclista:  "))
        ciclistas.append(ciclista)

    elif(opcion==2):
        
        menor=ciclistas[0].tiempo

        for ciclista in ciclistas:
            if(ciclista.tiempo <= menor):
                menor=ciclista.tiempo
                print(f"el menor es {menor} ")
            if(ciclista.tiempo == menor):
                nombre=ciclista.nombre
                edad=ciclista.edad
                pais=ciclista.pais
                tiempo=ciclista.tiempo
                print(f"el ganador es : {nombre} , {edad} , {pais} , con timpo de {tiempo}")
  

