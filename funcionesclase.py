class Gato:
    def __init__(self,nombre,color,raza,edad,peso):
        self.nombre = nombre
        self.color = color
        print (f"se ha creado la clase gato {self.nombre} de color {self.color} y raza {self.raza}, es viejito y tiene {self.edad} años, pero es flaco porque pesa {self.peso}")
        input ("presione enter para continuar")

    def describir(self):
        print (f"{self.nombre} es un gato de color {self.color}")
        input (f"{self.nombre} pulsa enter para continuar")

    def maullar(self):
        print (f"{self.nombre} dice miau")
        input (f"{self.nombre} pulsa enter para conrinuar")

    def comer(self):
        print (f"{self.nombre} come muy poco por eso es flaco")
        input (f"{self.raza} pulsa enter para continuar")


mi_gato=Gato("Rufus","Rojo","12 años","3 kg")
        
mi_gato.describir()
mi_gato.maullar()
mi_gato.comer()