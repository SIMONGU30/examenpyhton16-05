from Escuderia import Escuderia
escuderia=[]
opcion=1
print("********* ESCUDERIA *********")
print("1---> Ingresar Escuderia")
print("2---> Mostrar la Escuderia mas cara")
print("3---> Mostrar cantidad de escuderias por motor")
print("4---> salir")
print("**********************************")

while(opcion!=4):
    opcion=int(input("digita una opcion: "))
    
    if(opcion==1):
        escuderia=Escuderia()
        escuderia.nombre=input("Digite el nombre del ciclista:  ")
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