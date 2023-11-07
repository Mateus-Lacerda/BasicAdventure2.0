import random
import time
import bat as ba
import boss as bo
import player as p
import rooms as r
import squeleton as s
import ascii_art as a
from pygame import mixer

##FUNÇÕES DE SOM
##Som do jogador 
def load_greeting_sound():
    mixer.init()
    mixer.music.load('sounds/greeting.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()

##Som mecânicos
def load_doors_sound():
  mixer.init()
  mixer.music.load('sounds/door_sound.mp3')
  mixer.music.set_volume(1)
  mixer.music.play()

def load_chest_sound():
    mixer.init()
    mixer.music.load('sounds/chest.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()

#Sons das salas falta som de canto escuro, de poçao e de 
def load_rooms_sound():
  mixer.init()
  mixer.music.load('sounds/rooms_sound.mp3')
  mixer.music.set_volume(1)
  mixer.music.play()

def stop_rooms_sound():
  mixer.init()
  mixer.music.stop()

def load_battle_sound():
  mixer.init()
  mixer.music.load('sounds/battle.mp3')
  mixer.music.set_volume(1)
  mixer.music.play()

def stop_battle_sound():    
  mixer.init()
  mixer.music.stop()

def load_dark_corner_sound():
    mixer.init()
    mixer.music.load('sounds/dark_corner.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()

def load_victory_sound():
  mixer.init()
  mixer.music.load('sounds/victory.mp3')
  mixer.music.set_volume(1)
  mixer.music.play()

#Som dos inimigos
def load_bat_sound():
    mixer.init()
    mixer.music.load('sounds/bat.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()

def load_squeleton_sound():
    mixer.init()
    mixer.music.load('sounds/squeleton.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()

def load_boss_sound():
    mixer.init()
    mixer.music.load('sounds/boss.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()

def stop_boss_sound():
    mixer.init()
    mixer.music.stop()

def main():
    mixer.init()
    ## Criação de personagem 
    print("\033[34mBem vindo ao BasicAdventure! Um jogo genérico de aventura, feito como um teste para exercitar conceitos de Python, divirta-se!\n","_"*125,"\033[m")
    time.sleep(2)
    player = p.player(input("Escolha entre as classes guerreiro ou mago, digite \"g\" ou \"m\": \nMagos dão mais dano, mas têm menos vida. ").lower().strip()[0])
    boss = bo.boss(input("Quem é seu maior inimigo? \n"), input("Qual é o seu maior medo? "))
    time.sleep(1)
    a.clean()

    ## Criação de salas e inimigos

    fst_room = r.rooms("Primeira Sala")
    s_room = r.rooms("Segunda Sala")
    t_room = r.rooms("Terceira Sala")
    fth_room = r.rooms("Quarta Sala")

    fst_room.bat = True
    fst_room.chest = True

    s_room.corner = True
    s_room.squeleton = True

    t_room.bat = True
    t_room.chest = True
    t_room.key = False

    fth_room.squeleton1 = True
    fth_room.squeleton2 = True
    fth_room.corner = True
    fth_room.chest = True
    fth_room.bat = True

    bat_1 = ba.bat()
    bat_2 = ba.bat()
    squeleton_1 = s.squeleton()
    squeleton_2 = s.squeleton()
    squeleton_3 = s.squeleton()

    ## Iniciar o jogo
    a.intro_ascii1()
    print("\nVocê acorda em uma sala escura sem se lembrar do que ocorreu na noite anterior, com uma dor irritante na cabeça.\n")
    time.sleep(5)
    a.intro_ascii2(player.p_class)
    print(f"Isso lhe enfurece mas te enche de energia, agora você lembra que seu nome é {player.name} e você é um {player.p_class} destemido.\n")
    time.sleep(5)
    a.intro_ascii3()
    print(f"Isso deve ser coisa do {boss.name}, vou encontrá-lo!\n")
    time.sleep(3)
    print("Você observa a sala ao seu redor para achar uma saída.")
    time.sleep(3)
    a.clean()


    def death(): 
        a.death_ascii()
        main()


    def show_status():
        print(f"\033[31mVida: {player.life}\033[m\n\033[34mForça: {player.strength}\033[m")


    def credits():
        print("FIM")
        time.sleep(1)
        print("Obrigado por jogar!")
        time.sleep(1)
        print("Créditos:")
        time.sleep(1)
        print("Mateus Lacerda")
        time.sleep(1)        
        print("Agradecimentos especiais:")
        time.sleep(1)
        print("Mateus Lacerda")
        time.sleep(2)


    def boss_room():
        time.sleep(2)
        stop_rooms_sound()
        load_boss_sound()
        print("\033[35mOlá.")
        time.sleep(2)
        print("\033[35mQue bom que você veio...")
        time.sleep(2)
        print(f"\033[35mSinceramente, eu estou cansado de todo esse ódio entre nós, {player.name}.")
        time.sleep(2)
        print("\033[35mPor quê não deixamos isso pra trás?")
        time.sleep(2)
        choice_6 = input(f"Você tem duas Opções:\n\033[34m1- Fazer as pazes\033[m\n\033[31m2- Lutar até a morte com {boss.name}\033[m\n"
                             "Digite \033[34m1\033[m ou \033[31m2\033[m para responder. ")
            
        show_status()

        match choice_6:
            case "1":
                def ending_1():    
                    print(f"\033[34mVocê faz as pazes com {boss.name}, afinal, pra que guardar rancor? ")
                    time.sleep(2)
                    print("Vocês conversam sobre as aventuras que você percorreu até aqui, sobre os monstros, armadilhas e...\033[m")
                    time.sleep(2)
                    print("\033[31mPera aí!")
                    time.sleep(1)
                    print("Porque tantos monstros e armadilhas, se ele só queria fazer as pazes? Tem coisa errada aí.")
                    time.sleep(2)
                    print(f"Você percebe que {boss.name} estava apenas te enganando, pois percebeu o aumento de sua força após sua curta jornada.")
                    time.sleep(2)
                    print("E o apunhala pelas costas.\033[m")
                    time.sleep(2)
                    print("\033[34mJogo zerado pacifista!\033[m")
                    time.sleep(2)
                    credits()
                    choice_7 = input("Jogar de novo? Digite s ou n para responder: ")
                        
                    match choice_7:
                        case "s":
                            stop_boss_sound()
                            main()
                    

                        case "n":
                            print("Obrigado por jogar!")
                        case _:
                            print("\033[31mEntrada inválida!\033[m")
                            time.sleep(2)
                            ending_1()

                ending_1()
                
            case "2":
                def ending_2():
                    print("\033[31mMuito bem... Eu estava mentindo de qualquer forma, hahaha...")
                    time.sleep(2)
                    print('_'*20)
                    stop_boss_sound()
                    load_battle_sound()
                    print("Entrando em batalha!")
                    time.sleep(2)

                    while boss.life >= 0 and player.life >=0:
                        print(f"Você ataca com {player.attack_type}! ")
                        boss.life -= player.strength
                        time.sleep(2)
                        print(f"{boss.name} te ataca com {boss.attack_type}\033[m")
                        player.life -= boss.strength
                        time.sleep(2)

                    if player.life >= 0:
                        stop_battle_sound()
                        load_victory_sound()
                        time.sleep(1)
                        load_boss_sound()
                        print("\033[34mParabéns, você destruiu seu maior inimigo, enfrentando seus maiores medos!\033[m")
                        time.sleep(2)
                        print("\033[31mJogo zerado sanguinário!\033[m")
                        time.sleep(2)
                        credits()
                        choice_8 = input("Jogar de novo? Digite s ou n para responder: ")
                        
                        match choice_8:
                            case "s":
                                stop_boss_sound()
                                main()
                            case "n":
                                    print("Obrigado por jogar!")
                            case _:
                                    print("\033[31mEntrada inválida!\033[m")
                                    time.sleep(2)
                                    ending_2()
                        
                    else:
                        death()

                ending_2()

            case _:
                print("\033[31mEntrada inválida!\033[m")
                time.sleep(2)
                boss_room()


    def fourth_room():
        time.sleep(2)
        stop_rooms_sound()
        load_rooms_sound()
        print("_"*20,"\nQuarta sala.")
        show_status()
        time.sleep(2)    
        print("Você tem 5 opções:\n1- Ir à segunda sala.\n2- Ir à terceira sala.\n3- Há dois esqueletos em frente a uma porta, lutar?\n4- Há um canto escuro, explorar?"
                        "\n5- Abrir baú.")
        time.sleep(2)    
        choice_4 = input("Digite 1, 2, 3, 4 ou 5 para escolher sua ação. ").lower()

        match choice_4:
            case "1":
                stop_rooms_sound()
                load_doors_sound()
                print("Você decide ir à  segunda sala.")
                time.sleep(2)
                second_room()
                
            case "2":
                stop_rooms_sound()
                load_doors_sound()
                print("Você decide ir à terceira sala.")
                time.sleep(2)
                third_room()
                
            case "3":
                print("Você decide enfrentar os dois esqueletos!")
                time.sleep(2)
                if fth_room.squeleton1 == True and fth_room.squeleton2 == True:
                    stop_rooms_sound()
                    print('_'*20)
                    print("Entrando em batalha! ")
                    load_squeleton_sound()
                    time.sleep(1)
                    load_battle_sound()
                    a.squeleton_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                        
                    while squeleton_2.life > 0 and player.life > 0:
                        print(f"Você ataca com {player.attack_type}! ")
                        squeleton_2.life -= player.strength
                        time.sleep(2)
                        print(f"O esqueleto te ataca com {squeleton_2.attack_type}")
                        player.life -= squeleton_2.strength
                        time.sleep(2)
                        a.squeleton_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                        time.sleep(2)
                    fth_room.squeleton1 = False
                        
                    if squeleton_2.life <= 0:
                        stop_battle_sound()
                        load_victory_sound()
                        a.squeleton_death_ascii()
                        time.sleep(2)                                                

                    if player.life <= 0:
                        death()

                    stop_rooms_sound()
                    print('_'*20)
                    print("Entrando em batalha! ")
                    load_squeleton_sound()
                    time.sleep(1)
                    load_battle_sound()
                    a.squeleton_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                    
                    while squeleton_3.life > 0 and player.life > 0:
                        print(f"Você ataca com {player.attack_type}! ")
                        squeleton_3.life -= player.strength
                        time.sleep(2)
                        print(f"O esqueleto te ataca com {squeleton_3.attack_type}")
                        player.life -= squeleton_3.strength
                        time.sleep(2)
                        a.squeleton_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                        time.sleep(2)
                    fth_room.squeleton2 = False
                        
                    if squeleton_3.life <= 0:
                        stop_battle_sound()
                        load_victory_sound()
                        a.squeleton_death_ascii()
                        time.sleep(2)           

                    if player.life <= 0:
                        death()
                
                elif fth_room.squeleton1 == False and fth_room.squeleton2 == False: 
                    print("Você acabou de matá-los!")
                    time.sleep(2)
                        
                if t_room.key == True:
                    time.sleep(2)
                    print("Você encontrou uma porta trancada, deseja abrir e entrar?\n\033[31mAviso! Essa decisão te levará ao fim do jogo!\033[m")
                    time.sleep(2)
                    choice_5 = input("Digite \"s\" ou \"n\", para sim ou não. " ).lower()
                        
                    match choice_5:
                        case "s":
                            time.sleep(2)
                            print("Você decide entrar na sala.")
                            load_doors_sound()
                            time.sleep(2)
                            boss_room()
                        case "n":
                            time.sleep(2)
                            print("Voltando a explorar.")
                            time.sleep(2)
                            fourth_room()
                else: 
                    time.sleep(2)
                    print("Você encontrou uma porta, mas está trancada, continue explorando...")
                    time.sleep(2)
                    fourth_room()

            case "4":
                stop_rooms_sound()
                load_dark_corner_sound()
                print("Você decide explorar o canto escuro...")
                time.sleep(2)
                
                if fth_room.corner == True:
                    print("Você achou um item de força, sua força aumenta!")
                    player.strength += random.randint(1,5)
                    fth_room.corner = False
                    time.sleep(2)
                    fourth_room()

                else:
                    time.sleep(2)
                    print("Não tem nada aqui...")
                    time.sleep(2)
                    fourth_room()
            
            case "5":
                print("Você decide abrir o baú.")
                stop_rooms_sound()
                load_chest_sound()
                a.chest_ascii()
                time.sleep(2)

                if fth_room.chest == True:
                    cure = random.randint(5,20)
                    player.life += cure
                    a.potion_ascii("cura", cure)
                    print("Você achou uma poção de cura! ")
                    fth_room.chest = False
                    time.sleep(2)
                    fourth_room()

                else:
                    time.sleep(2)
                    print("Está vazio...")
                    time.sleep(2)
                    fourth_room()
            
            case _:
                    print("\033[31mEntrada inválida!\033[m")
                    time.sleep(2)
                    fourth_room()

                            
    def third_room():
        time.sleep(2)
        stop_rooms_sound()
        load_rooms_sound()
        print("_"*20,"\nTerceira sala.")
        show_status()
        time.sleep(2)    
        print("Você tem 5 opções:\n1- Ir à primeira sala.\n2- Ir à segunda sala.\n3- Abrir a porta à sua frente.\n4- Há um canto escuro, explorar?"
                            "\n5- Abrir o baú.")
        time.sleep(2)    
        choice_4 = input("Digite 1, 2, 3, 4 ou 5 para escolher sua ação. ")

        match choice_4:
            case "1":
                stop_rooms_sound()
                load_doors_sound()
                print("Você decide ir à  primeira sala")
                time.sleep(2)
                first_room()
                
            case "2":
                stop_rooms_sound()
                load_doors_sound()
                print("Você decide ir à segunda sala.")
                time.sleep(2)
                second_room()

            case "3":
                stop_rooms_sound()
                load_doors_sound()
                print("Você decide abrir a porta a sua frente.")
                time.sleep(2)
                fourth_room()

            case "4":
                stop_rooms_sound()
                load_dark_corner_sound()
                print("Você decide explorar o canto escuro...")
                time.sleep(2)
                print("Você achou um morcego!")
                time.sleep(2)
                    
                if t_room.bat == True:
                    stop_rooms_sound()
                    print('_'*20)
                    print("Entrando em batalha! ")                    
                    load_bat_sound()
                    time.sleep(1)
                    load_battle_sound()
                    a.bat_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                    time.sleep(2)
                        
                    while bat_2.life > 0 and player.life > 0:
                        print(f"Você ataca com {player.attack_type}! ")
                        bat_2.life -= player.strength
                        time.sleep(2)
                        print(f"O morcego te ataca com {bat_2.attack_type}")
                        player.life -= bat_1.strength
                        time.sleep(2)
                        a.bat_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                        time.sleep(2)
                    t_room.bat = False
                    
                    if bat_2.life <= 0:
                        stop_battle_sound()
                        load_victory_sound()
                        a.bat_death_ascii()
                        time.sleep(2)
                        third_room()

                    if player.life <= 0:
                        death()
                        
                    else:
                        time.sleep(2)
                        print("Ele já estava morto... ")
                        time.sleep(2)
                        third_room()
                    
            case "5":
                print("Você decide abrir o baú...")
                stop_rooms_sound()
                load_chest_sound()
                a.chest_ascii()
                    
                if t_room.chest == True:
                    time.sleep(2)
                    print("Vocẽ achou uma chave! ")
                    t_room.key = True
                    t_room.chest = False
                    time.sleep(2)
                    third_room()
                
                else:
                    print("O baú está vazio...")
                    time.sleep(2)
                    third_room()

            case _:
                print("\033[31mEntrada inválida!\033[m")
                time.sleep(2)
                third_room()


    def first_room():
        time.sleep(2)
        a.first_room_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
        stop_rooms_sound()
        load_rooms_sound()
        print("Você tem 4 opções:\n1- Abrir a porta à sua direita.\n2- Abrir a porta à sua frente.\n3- Há um canto escuro, explorar?"
              "\n4- Abrir o baú á sua esquerda.")
        time.sleep(2)    
        choice_2 = input("Digite 1, 2, 3 ou 4 para escolher sua ação. ")
        
        match choice_2:
            case "1":
                stop_rooms_sound()
                load_doors_sound()
                print("Você escolhe entrar na porta a sua direita. ")
                time.sleep(2)
                second_room()
            
            case "2":
                stop_rooms_sound()
                load_doors_sound()
                print("Você escolhe entrar na porta à sua frente. ")
                time.sleep(2)
                third_room()
            
            case "3":
                stop_rooms_sound()
                load_dark_corner_sound()
                print("Você decide explorar o canto escuro...")
                time.sleep(2)
                print("Você achou um morcego!")
                time.sleep(2)
                
                if fst_room.bat == True:
                    stop_rooms_sound()
                    print('_'*20)
                    print("Entrando em batalha! ")
                    load_bat_sound()
                    time.sleep(1)
                    load_battle_sound()
                    a.bat_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                    time.sleep(2)
                    
                    while bat_1.life > 0 and player.life > 0:
                        print(f"Você ataca com {player.attack_type}! ")
                        bat_1.life -= player.strength
                        time.sleep(2)
                        print(f"O morcego te ataca com {bat_1.attack_type}")
                        player.life -= bat_1.strength
                        time.sleep(2)
                        a.bat_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                        time.sleep(2)
                    fst_room.bat = False
                    
                    if bat_1.life <= 0:
                        stop_battle_sound()
                        load_victory_sound()
                        a.bat_death_ascii()
                        time.sleep(2)
                        first_room()

                    if player.life <= 0:
                        death()

                else:
                    time.sleep(2)
                    print("Ele já estava morto... ")
                    time.sleep(2)
                    first_room()

            case "4":  
                print("Você decide abrir o baú...")
                stop_rooms_sound()
                load_chest_sound()
                a.chest_ascii()
                if fst_room.chest == True:
                    time.sleep(2)
                    cure = random.randint(5,20)
                    player.life += cure
                    a.potion_ascii("cura", cure)
                    print("Vocẽ achou uma poção de cura! ")
                    fst_room.chest = False
                    time.sleep(2)
                    first_room()
                
                else:
                    print("O baú está vazio...")
                    time.sleep(2)
                    first_room()

            case _:
                print("\033[31mEntrada inválida!\033[m")
                time.sleep(2)
                first_room()


    def second_room():
        time.sleep(2)
        a.second_room_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
        stop_rooms_sound()
        load_rooms_sound()    
        print("Você tem 5 opções:\n1- Ir à primeira sala.\n2- Abrir a porta à sua direita.\n3- Abrir a porta à sua frente.\n4- Há um canto escuro, explorar?"
                        "\n5- Conversar com uma figura humanóide presente.")
        time.sleep(2)    
        choice_3 = input("Digite 1, 2, 3, 4 ou 5 para escolher sua ação. ").lower()
        
        match choice_3:
            case "1":
                stop_rooms_sound()
                load_doors_sound()
                print("Você decide voltar.")
                first_room()
            
            case "2":
                stop_rooms_sound()
                load_doors_sound()
                print("Você escolhe entrar na porta a sua direita. ")
                time.sleep(2)
                third_room()
            
            case "3":
                stop_rooms_sound()
                load_doors_sound()
                print("Você escolhe entrar na porta à sua frente. ")
                time.sleep(2)
                fourth_room()
            
            case "4":
                stop_rooms_sound()
                load_dark_corner_sound()
                print("Você decide explorar o canto escuro...")
                time.sleep(2)
                
                if s_room.corner == True:
                    print("Você achou um item de força, sua força aumenta!")
                    player.strength += random.randint(1,5)
                    s_room.corner = False
                    second_room()

                else:
                    time.sleep(2)
                    print("Não tem nada aqui...")
                    time.sleep(2)
                    second_room()

            case "5":
                stop_rooms_sound()
                load_greeting_sound()  
                print("Você decide falar com a figura humanóide...")
                time.sleep(2)
                print("Você achou um esqueleto!")
                time.sleep(2)
                
                if s_room.squeleton == True:
                    stop_rooms_sound()
                    print('_'*20)
                    print("Entrando em batalha! ")
                    load_squeleton_sound()
                    time.sleep(1)
                    load_battle_sound()
                    a.squeleton_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                    
                    while squeleton_1.life > 0 and player.life > 0:
                        print(f"Você ataca com {player.attack_type}! ")
                        squeleton_1.life -= player.strength
                        time.sleep(2)
                        print(f"O esqueleto te ataca com {squeleton_1.attack_type}")
                        player.life -= squeleton_1.strength
                        time.sleep(2)
                        a.squeleton_battle_ascii(player.life, player.strength, player.name, player.p_class, boss.attack_type)
                        time.sleep(2)
                    s_room.squeleton = False
                    
                    if squeleton_1.life <= 0:
                        load_victory_sound()
                        stop_battle_sound()
                        a.squeleton_death_ascii()
                        time.sleep(2)  
                        second_room()

                    if player.life <= 0:
                        death()

                else:
                    time.sleep(2)
                    print("Ele já estava morto...")
                    time.sleep(2)
                    second_room()

            case _:
                print("\033[31mEntrada inválida!\033[m")
                time.sleep(2)
                second_room()


    first_room() ## Comando que inicializa o jogo


if __name__ == '__main__':
    main()
