import random

class Pokemon():
    def __init__(self):
        self.Pdv = 100
    def Charmander(self):
        self.Name = "Charmander"
        self.Tipo = "Fuego"
        self.Debilidades = "Agua"
        self._1_ = random.randint(10,25)
        self._2_ = random.randint(15,30)
        self._3_ = random.randint(20,40)
        self._4_ = random.randint(20,35)
        self.Ataque1 = "Arañazo"
        self.Ataque2 = "Pirotecnia"
        self.Ataque3 = "Furia_dragon"
        self.Ataque4 = "Lanzallamas"
        
    def Greninja(self):
        self.Name = "Greninja"
        self.Tipo = "Agua"
        self.Debilidades = "Electrico"
        self._1_ = random.randint(20,40)
        self._2_ = random.randint(15,30)
        self._3_ = random.randint(15,35)
        self._4_ = random.randint(15,25)
        self.Ataque1 = "Shuriken_de_agua"
        self.Ataque2 = "Niebla"
        self.Ataque3 = "Escudo_tatami"
        self.Ataque4 = "Destructor"
        
    def Turtwig(self):
        self.Name = "Turtwing"
        self.Tipo = "Planta"
        self.Debilidades = "Fuego"
        self._1_ = random.randint(15,25)
        self._2_ = random.randint(20,40)
        self._3_ = random.randint(15,25)
        self._4_ = random.randint(10,20)
        self.Ataque1 = "Hoja_afilada"
        self.Ataque2 = "Energibola"
        self.Ataque3 = "Golpe_cuerpo"
        self.Ataque4 = "Placaje"
        
    def Jolteon(self):
        self.Name = "Jolteon"
        self.Tipo = "Electrico"
        self.Debilidades = "Roca"
        self._1_ = random.randint(20,40)
        self._2_ = random.randint(15,25)
        self._3_ = random.randint(15,30)
        self._4_ = random.randint(20,30)
        self.Ataque1 = "Impactrueno"
        self.Ataque2 = "Latigo"
        self.Ataque3 = "Doble_patada"
        self.Ataque4 = "Chispazo"
        
    def Lycanroc(self):
        self.Name = "Lycanroc"
        self.Tipo = "Roca"
        self.Debilidades = "Planta"
        self._1_ = random.randint(15,30)
        self._2_ = random.randint(25,40)
        self._3_ = random.randint(30,50)
        self._4_ = random.randint(10,20)
        self.Ataque1 = "Treparrocas"
        self.Ataque2 = "Taladradora"
        self.Ataque3 = "Avalancha"
        self.Ataque4 = "Ataque_rapido"
        
    def Name_Pokemon(self):
        return self.Name
    
    
    def Habilidades(self):
        print(f"Las habilidades del pokemon {self.Name} son \n1-{self.Ataque1} {self._1_} Ap \n2-{self.Ataque2} {self._2_} Ap\n3-{self.Ataque3} {self._3_} Ap\n4-{self.Ataque4} {self._4_} Ap")
    
    def Juego(self,Inicio,Pdv_1,Pdv_2):
        if Inicio == 0:
            # Turnos = 0                
            while Pdv_1 > 0 and Pdv_2 > 0:
                Jugador1.Habilidades()
                self.Ataque_Jugador1 = int(input('Ingrese habilidad: '))
                                
                match self.Ataque_Jugador1:
                    case 1:
                        if Jugador1.Tipo == Jugador2.Debilidades:
                            Pdv_2 -= ((Jugador1._1_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_2 -= ((Jugador1._1_)*0.8)
                        else:
                            Pdv_2 -= Jugador1._1_
                    case 2:
                        if Jugador1.Tipo == Jugador2.Debilidades:
                            Pdv_2 -= ((Jugador1._2_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_2 -= ((Jugador1._2_)*0.8)
                        else:
                            Pdv_2 -= Jugador1._2_
                    case 3:
                        if Jugador1.Tipo == Jugador2.Debilidades:
                            Pdv_2 -= ((Jugador1._3_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_2 -= ((Jugador1._3_)*0.8)
                        else:
                            Pdv_2 -= Jugador1._3_
                    case 4:
                        if Jugador1.Tipo == Jugador2.Debilidades:
                            Pdv_2 -= ((Jugador1._4_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_2 -= ((Jugador1._4_)*0.8)
                        else:
                            Pdv_2 -= Jugador1._4_
                if Pdv_2<=0:
                    print(f"\n =========El ganador es {Jugador1.Name}=========")
                    break
                print(f"\n============Vida jugador 2 ==== {Pdv_2} % ================\n")
                
                Jugador2.Habilidades()       
                self.Ataque_Jugador2 = int(input('Ingrese habilidad: '))
                
                match self.Ataque_Jugador2:
                    case 1:
                        if Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._1_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._1_)*0.8)
                        else:
                            Pdv_1 -= Jugador2._1_
                    case 2:
                        if Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._2_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._2_)*0.8)
                        else:
                            Pdv_1 -= Jugador2._2_
                    case 3:
                        if Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._3_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._3_)*0.8)
                        else:
                            Pdv_1 -= Jugador2._3_
                    case 4:
                        if Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._4_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._4_)*0.8)
                        else:
                            Pdv_1 -= Jugador2._4_
                if Pdv_1<=0:
                    print(f"\n =========El ganador es {Jugador2.Name}=========")
                    break
                print(f"\n============Vida jugador 1 ==== {Pdv_1} % ================\n")

        else:
            # Turnos = 0
            while Pdv_1 > 0 and Pdv_2 > 0:
                Jugador2.Habilidades()
                self.Ataque_Jugador2 = int(input('Ingrese habilidad: '))
                                
                match self.Ataque_Jugador2:
                    case 1:
                        if Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._1_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._1_)*0.8)
                        else:
                            Pdv_1 -= Jugador2._1_
                    case 2:
                        if Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._2_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._2_)*0.8)
                        else:
                            Pdv_1 -= Jugador2._2_
                    case 3:
                        if Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._3_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._3_)*0.8)
                        else:
                            Pdv_1 -= Jugador2._3_
                    case 4:
                        if Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._4_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_1 -= ((Jugador2._4_)*0.8)
                        else:
                            Pdv_1 -= Jugador2._4_
                if Pdv_1<=0:
                    print(f"\n =========El ganador es {Jugador2.Name}=========")
                    break
                print(f"\n============Vida jugador 1 ==== {Pdv_1} % ================\n")
                
                Jugador1.Habilidades()       
                self.Ataque_Jugador1 = int(input('Ingrese habilidad: '))
                
                match self.Ataque_Jugador1:
                    case 1:
                        if Jugador1.Tipo == Jugador2.Debilidades:
                            Pdv_2 -= ((Jugador1._1_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_2 -= ((Jugador1._1_)*0.8)
                        else:
                            Pdv_2 -= Jugador1._1_
                    case 2:
                        if Jugador1.Tipo == Jugador2.Debilidades:
                            Pdv_2 -= ((Jugador1._2_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_2 -= ((Jugador1._2_)*0.8)
                        else:
                            Pdv_2 -= Jugador1._2_
                    case 3:
                        if Jugador1.Tipo == Jugador2.Debilidades:
                            Pdv_2 -= ((Jugador1._3_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_2 -= ((Jugador1._3_)*0.8)
                        else:
                            Pdv_2 -= Jugador1._3_
                    case 4:
                        if Jugador1.Tipo == Jugador2.Debilidades:
                            Pdv_2 -= ((Jugador1._4_)*1.2)
                            print("========= El ataque es muy eficiente ==========")
                        elif Jugador2.Tipo == Jugador1.Debilidades:
                            Pdv_2 -= ((Jugador1._4_)*0.8)
                        else:
                            Pdv_2 -= Jugador1._4_
                if Pdv_2<=0:
                    print(f"\n =========El ganador es {Jugador1.Name}=========")
                    break
                print(f"\n============Vida jugador 2 ==== {Pdv_2} % ================\n")
                
                    
    # def Restar_vida(self):
    #     self.Ataque_Jugador1 -= self.Ataque_Jugador2
    #     print(f"La vida restante del jugador 1 es {Pdv_1}")
    #     self.Ataque_Jugador2 -= self.Ataque_Jugador1
    #     print(f"La vida restante del jugador 2 es {Pdv_2}")
    
inicio = random.randint(0,1)
if inicio == 1:
    print("Inicia jugador 2")
else:
    print("Inicia jugador 1")
    
Jugador1 = Pokemon()
Pdv_1 = Jugador1.Pdv
Jugador2 = Pokemon()
Pdv_2 = Jugador2.Pdv


Pokemon_elegido_jugador1 = int(input("Seleccione el pokemon a usar.\n 1-Charmander \n 2-Greninja \n 3-Turtwig \n 4-Jolteon \n 5-Lycanroc \n ======: "))


Pokemon_elegido_jugador2 = int(input("Seleccione el pokemon a usar.\n 1-Charmander \n 2-Greninja \n 3-Turtwig \n 4-Jolteon \n 5-Lycanroc \n ======: "))


while Pokemon_elegido_jugador1 != 1 and Pokemon_elegido_jugador1 != 2 and Pokemon_elegido_jugador1 != 3 and Pokemon_elegido_jugador1 != 4 and Pokemon_elegido_jugador1 != 5:
    print("Eleccion errada")
    Pokemon_elegido_jugador1 = int(input("Seleccione el pokemon a usar.\n 1-Charmander \n 2-Greninja \n 3-Turtwig \n 4-Jolteon \n 5-Lycanroc \n ======: "))
    
while Pokemon_elegido_jugador2 != 1 and Pokemon_elegido_jugador2 != 2 and Pokemon_elegido_jugador2 != 3 and Pokemon_elegido_jugador2 != 4 and Pokemon_elegido_jugador2 != 5:
    print("Eleccion errada")
    Pokemon_elegido_jugador2 = int(input("Seleccione el pokemon a usar.\n 1-Charmander \n 2-Greninja \n 3-Turtwig \n 4-Jolteon \n 5-Lycanroc \n ======: "))
        
match Pokemon_elegido_jugador1:
    case 1:
        Jugador1.Charmander()
        print("Jugador 1 elijio a Charmander \n")
            
    case 2:
        Jugador1.Greninja()
        print("Jugador 1 elijio a Greninja \n")
        
    case 3:
        Jugador1.Turtwig()
        print("Jugador 1 elijio a Turtwing \n")
        
    case 4:
        Jugador1.Jolteon()
        print("Jugador 1 elijio a Jolteon \n")
        
    case 5:
        Jugador1.Lycanroc()
        print("Jugador 1 elijio a Lycanroc \n")
        
match Pokemon_elegido_jugador2:
    case 1:
        Jugador2.Charmander()
        print("Jugador 2 elijio a Charmander \n")

    case 2:
        Jugador2.Greninja()
        print("Jugador 2 elijio a Greninja \n")

    case 3:
        Jugador2.Turtwig()
        print("Jugador 2 elijio a Turtwing \n")

    case 4:
        Jugador2.Jolteon()
        print("Jugador 2 elijio a Jolteon \n")

    case 5:
        Jugador2.Lycanroc()
        print("Jugador 2 elijio a Lycanroc \n")

Jugador1.Juego(inicio,Pdv_2,Pdv_1)