class Curso:
    """------------------
    #metodos
    ------------------"""

    def __init__(self):
        self.__notas=[4,5,3,2,3.5,1,0,4,5,5,4.5,4.2]

    def TotalNotas(self):
        return len(self.__notas)
    
    def PromedioNotas(self):
        suma=0.0
        indice=0
    while indice<12:
        suma+=self.__notas[indice]
        indice+=1
    return suma/indice