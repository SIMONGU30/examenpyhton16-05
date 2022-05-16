class Ciclista:
    def __init__(self):

        self.__nombre=None
        self.__edad=None
        self.__pais=None
        self.__tiempo=None


      #getters***************************

    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def edad(self):
        return(self.__edad)

    @property
    def pais(self):
        return(self.__pais)

    @property
    def tiempo(self):
        return(self.__tiempo)


    #setter**************************************

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @edad.setter
    def edad(self,edad):

        if(edad>0 and edad<110):
            self.__edad=edad
        else:
            self.__edad=edad
            print("Edad erronea")


    @pais.setter
    def pais(self,pais):
        self.__pais=pais


    @tiempo.setter
    def tiempo(self,tiempo):
        self.__tiempo=tiempo

        