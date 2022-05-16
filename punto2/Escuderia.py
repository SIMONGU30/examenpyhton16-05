class Escuderia :
    def __init__(self):

        self.__nombre=None
        self.__motor=None
        self.__piloto=None
        self.__costoAnual=None


      #getters***************************

    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def motor(self):
        return(self.__motor)

    @property
    def piloto(self):
        return(self.__piloto)

    @property
    def costoAnual(self):
        return(self.__costoAnual)


    #setter**************************************

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @motor.setter
    def motor(self,motor):
        self.__motor=motor


    @piloto.setter
    def piloto(self,piloto):
        self.__piloto=piloto

    @costoAnual.setter
    def costoAnual(self,costoAnual):
        self.__costoAnual=costoAnual