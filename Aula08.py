class Dispositivo():
    def __init__(self, nome):
        self.nome = nome
    def retornaID(self):
        return self.nome
    
class Atuador(Dispositivo):
    def __init__(self, nome, estado = None):
        super().__init__(nome)
        self.estado = estado
    def estado(self, estado):
        import random
        estado = random.randrange(0,1)
        if estado == 0:
            return self.desliga
        else:
            return self.liga
    def exibeEstado(self):
        print("O nome do atuador é", self.nome,"e o estado é", self.estado)        
        
    
class Led(Atuador):
    def __init__(self, nome, estado = None):
        super().__init__(estado)
        self.liga = 1
        self.desliga = 0
    def liga(self):
        return self.liga
    def desliga(self):
        return self.desliga
    
class Motor(Atuador):
    def __init__(self, nome, estado, direcao = None, velocidade = None):
        super().__init__(estado) 
        self.direcao = direcao
        self. velocidade = velocidade
    def direcao(self):
        direcao = int(input("A direção é 1 (Horário) ou 0 (anti-horário)?"))
        self.direcao = direcao

    def velocidade(self):
        import random
        velocidade = random.randrange(0,256)
        self.velocidade = velocidade
    def atribuiVelocidade(self, velocidade, estado):
        if velocidade > 0:
            estado == 1
        else:
            estado == 0
    def atribuiDirecao(self, direcao):
        if direcao == 0:
            print("Anti-Horário")
        if direcao == 1:
            print("Horário")
        else:
            print("Os valores são 0 ou 1")
    def exibeEstado(self, estado):
        if estado == 1:
            print("O motor está ligado, sua direção é", self.direcao, "e sua velocidade é", self.velocidade)
        else:
            print("O motor está desligado")

motor1 = Motor("Motor Ligado", 1, 1, 13)
motor1.exibeEstado(0)
            

    