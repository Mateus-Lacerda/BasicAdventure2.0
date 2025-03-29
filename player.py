from main import main
import time

class player:
    
    def __init__(self, p_class):
        self.p_class = p_class.lower().strip()[0]
        self.attack_type = None

        if p_class == 'g':
            self.p_class = "Guerreiro"
            self.name = input("Escolha seu nome: \n")
            self.life = 70
            self.strength = 15
        
        elif p_class == 'm':
            self.p_class = "Mago"
            self.name = input("Escolha seu nome: \n")
            self.life = 50
            self.strength = 20
        
        else: 
            print("\033[31mEscolha apenas guerreiro ou mago!\033[m")
            time.sleep(2)
            main()

    def set_attack_type(self, attack_type):
        self.attack_type = attack_type