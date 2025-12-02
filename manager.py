import random
dado=[1,2,3,4,5,6]

class manager:
    def __init__(self,nombre,color):
        self.nombre=nombre
        self.color=color
    def lanzar(self):
        numero=random.choice(dado)
        return numero

class contrincante():
    def __init__(self, nombre="peluchin", color="verde"):
        self.nombre=nombre
        self.color=color
    def lanzar(self):
        numero=random.choice(dado)
        return numero

class jefe1(contrincante):
    def __init__(self):
        super().__init__("peluchon", "negro")

class jefe2(contrincante):
    def __init__(self):
        super().__init__("peluchona", "rosa")
    

name=input("ingresa tu nombre de jugador: ")
colorado=input("ingresa tu color: ")

jugador1=manager(name, colorado)
enemigo=contrincante()
enemigo2=jefe1()
enemigo3=jefe2()

lanzar1=jugador1.lanzar()
lanzar2=enemigo.lanzar()
lanzar3=enemigo2.lanzar()
lanzar4=enemigo3.lanzar()

print(f"el jugador: {jugador1.nombre} saco {lanzar1}")
print(f"el contrincante: {enemigo.nombre} saco {lanzar2}")
print(f"el contrincante: {enemigo2.nombre} saco {lanzar3}")
print(f"el contrincante: {enemigo3.nombre} saco {lanzar4}")


