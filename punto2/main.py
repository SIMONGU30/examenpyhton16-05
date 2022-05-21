from Escuderia import Escuderia
escuderias=[]
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
        escuderia.nombre=input("Digite el nombre de la escuderia:  ")
        escuderia.motor=input("Digite el nombre del motor:  ")
        escuderia.piloto=input("Digite el nombre del piloto: ")
        escuderia.costoAnual=input("Digite el valor del costo anual: ")
        escuderias.append(escuderia)

    elif(opcion==2):
        masCara=escuderias[0].costoAnual
        for escuderia in escuderias:
            if(escuderia.costoAnual >= masCara):
                masCara=escuderia.costoAnual
                nombre=escuderia.nombre
                motor=escuderia.motor
                print(f"la escuderia mas cara es de {masCara}")
                print(f"El nombre de la escuderia es  {nombre}")
                print(f"El nombre del motor es  {motor}")
            else:
                print(f"Error")
    elif(opcion==3):
        opcionMotor=1
        print("1---> mercedes")
        print("2---> ferrari")
        print("3---> renault")
        print("4---> Salir")
        while (opcionMotor!=4):
            opcionMotor=int(input("digite una opcion : "))
            contador=0
            conMercedes=0
            conFerrari=0
            conRenault=0
            if(opcionMotor==1):
                while(1>contador):
                    for escuderia in escuderias:
                        if(escuderia.motor=="mercedes"):
                            conMercedes=conMercedes+1
                        contador=contador+1   
                print(f"la cantidad de escuderias que tienen el motor mercedes es de : {conMercedes}") 
                        
            elif(opcionMotor==2):
                while(1>contador):
                    for escuderia in escuderias:
                        if(escuderia.motor=="ferrari"):
                            conFerrari=conFerrari+1
                        contador=contador+1
                print(f"la cantidad de escuderias que tienen el motor ferrari es de : {conFerrari}")
                        
            elif(opcionMotor==3):
                while(1>contador):
                    for escuderia in escuderias:
                        if(escuderia.motor=="renault"):
                            conRenault=conRenault+1
                        contador=contador+1
                print(f"la cantidad de escuderias que tienen el motor renault es de : {conRenault}")

            

                        