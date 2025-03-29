import os
import time

##FUNÇÕES DIVERSAS
def clean():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def gray(string):
      
      return f"\033[37m{string}\033[m"

def red(string):
    
    return f"\033[31m{string}\033[m"

def blue(string):

    return f"\033[34m{string}\033[m"

def green(string):

    return f"\033[32m{string}\033[m"

def brown(string):

    return f"\033[33m{string}\033[m"

def yellow(string):

    return f"\033[93m{string}\033[m"

def purple(string):
      
      return f"\033[35m{string}\033[m"

##TÍTULO
def title_ascii():
    clean()
    print(red(r"""
               
               
▀█████████▄     ▄████████    ▄████████  ▄█   ▄████████         ▄████████ ████████▄   ▄█    █▄     ▄████████ ███▄▄▄▄       ███     ███    █▄     ▄████████    ▄████████ 
  ███    ███   ███    ███   ███    ███ ███  ███    ███        ███    ███ ███   ▀███ ███    ███   ███    ███ ███▀▀▀██▄ ▀█████████▄ ███    ███   ███    ███   ███    ███ 
  ███    ███   ███    ███   ███    █▀  ███▌ ███    █▀         ███    ███ ███    ███ ███    ███   ███    █▀  ███   ███    ▀███▀▀██ ███    ███   ███    ███   ███    █▀  
 ▄███▄▄▄██▀    ███    ███   ███        ███▌ ███               ███    ███ ███    ███ ███    ███  ▄███▄▄▄     ███   ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄     
▀▀███▀▀▀██▄  ▀███████████ ▀███████████ ███▌ ███             ▀███████████ ███    ███ ███    ███ ▀▀███▀▀▀     ███   ███     ███     ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     
  ███    ██▄   ███    ███          ███ ███  ███    █▄         ███    ███ ███    ███ ███    ███   ███    █▄  ███   ███     ███     ███    ███ ▀███████████   ███    █▄  
  ███    ███   ███    ███    ▄█    ███ ███  ███    ███        ███    ███ ███   ▄███ ███    ███   ███    ███ ███   ███     ███     ███    ███   ███    ███   ███    ███ 
▄█████████▀    ███    █▀   ▄████████▀  █▀   ████████▀         ███    █▀  ████████▀   ▀██████▀    ██████████  ▀█   █▀     ▄████▀   ████████▀    ███    ███   ██████████ 
                                                                                                                                               ███    ███              
               """))

##INTRODUÇÃO
def intro_ascii1():
    clean()
    print(brown(rf"""                                                            
                                                                            o
                                                                        .-'"|
                                                                        |-'"|
                                                                            |   _.-'`.
                                                                           _|-"'_.-'|.`.
                                                                          |:^.-'_.-'`.;.`.
                                                                          | `.'.   ,-'_.-'|
                                                                          |   + '-'.-'   J
                                                       __.            .d88|    `.-'      |
                                                  _.--'_..`.    .d88888888|     |       J'b.
                                               +:" ,--'_.|`.`.d88888888888|-.   |    _-.|888b.
                                               | \ \-'_.--'_.-+888888888+'  _>F F +:'   `88888bo.
                                                L \ +'_.--'   |88888+"'  _.' J J J  `.    +8888888b.
                                                |  `+'        |8+"'  _.-'    | | |    +    `+8888888._-'.
                                              .d8L  L         J  _.-'        | | |     `.    `+888+^'.-|.`.
                                             d888|  |         J-'            F F F       `.  _.-"_.-'_.+.`.`.
                                            d88888L  L     _.  L            J J J          `|. +'_.-'    `_+ `;
                                            888888J  |  +-'  \ L         _.-+.|.+.          F `.`.     .-'_.-"J
                                            8888888|  L L\    \|     _.-'     '   `.       J    `.`.,-'.-"    |
                                            8888888PL | | \    `._.-'               `.     |      `..-"      J.b
                                            8888888 |  L L `.    \     _.-+.          `.   L+`.     |        F88b
                                            8888888  L | |   \   _..--'_.-|.`.          >-'    `., J        |8888b
                                            8888888  |  L L   +:" _.--'_.-'.`.`.    _.-'     .-' | |       JY88888b
                                            8888888   L | |   J \ \_.-'     `.`.`.-'     _.-'   J J        F Y88888b
                                            Y888888    \ L L   L \ `.      _.-'_.-+  _.-'       | |       |   Y88888b
                                            `888888b    \| |   |  `. \ _.-'_.-'   |-'          J J       J     Y88888b
                                             Y888888     +'\   J    \ '_.-'       F    ,-T"\   | |    .-'      )888888
                                              Y88888b.      \   L    +'          J    /  | J  J J  .-'        .d888888
                                               Y888888b      \  |    |           |    F  '.|.-'+|-'         .d88888888
                                                Y888888b      \ J    |           F   J    -.              .od88888888P
                                                 Y888888b      \ L   |          J    | .' ` \d8888888888888888888888P
                                                  Y888888b      \|   |          |  .-'`.  `\ `.88888888888888888888P
                                                   Y888888b.     J   |          F-'     \\ ` \ \88888888888888888P'
                                                    Y8888888b     L  |         J       d8`.`\  \`.8888888888888P'
                                                     Y8888888b    |  |        .+      d8888\  ` .'  `Y888888P'
                                                     `88888888b   J  |     .-'     .od888888\.-'
                                                      Y88888888b   \ |  .-'     d888888888P'
                                                      `888888888b   \|-'       d888888888P
                                                       `Y88888888b            d8888888P'
                                                         Y88888888bo.      .od88888888   hs
                                                         `8888888888888888888888888888
                                                          Y88888888888888888888888888P
                                                           `Y8888888888888888888888P'
                                                             `Y8888888888888P'
                                                                  `Y88888P'
    """))

def intro_ascii2(p_class):
    clean()
    if p_class == "Guerreiro":    
        print(green(r"""

                                                                        ,dM
                                                                       dMMP
                                                                      dMMM'
                                                                      \MM/
                                                                      dMMm.
                                                                     dMMP'_\---.
                                                                    _| _  p ;88;`.
                                                                  ,db; p >  ;8P|  `.
                                                                 (``T8b,__,'dP |   |
                                                                 |   `Y8b..dP  ;_  |
                                                                 |    |`T88P_ /  `\;
                                                                 :_.-~|d8P'`Y/    /
                                                                  \_   TP    ;   7`\
                                                       ,,__        >   `._  /'  /   `\_
                                                       `._ ''''~~~~------|`\;' ;     ,'
                                                          '''~~~-----~~~'\__[|;' _.-'  `\
                                                                  ;--..._     .-'-._     ;
                                                                 /      /`~~''   ,'`\_ ,/
                                                                ;_    /'        /    ,/
                                                                | `~-l         ;    /
                                                                `\    ;       /\.._|
                                                                  \    \      \     \
                                                                  /`---';      `----'
                                                                 (     /            fsc
                                                                  `---'
    """))
    elif p_class == "Mago":
        print(green(rf"""
                                                                                o
                                                                         O       /`-.__
                                                                                /  \�'^|
                                                                   o           T    l  *
                                                                              _|-..-|_
                                                                       O    (^ '----' `)
                                                                             `\-....-/^
                                                                   O       o  ) '/ ' (
                                                                             _( (-)  )_
                                                                         O  /\ )    (  /\
                                                                           /  \(    ) |  \
                                                                       o  o    \)  ( /    \
                                                                         /     |(  )|      \
                                                                        /    o \ \( /       \
                                                                  __.--'   O    \_ /   .._   \
                                                                 //|)\      ,   (_)   /(((\^)'\
                                                                    |       | O         )  `  |
                                                                    |      / o___      /      /
                                                                   /  _.-''^^__O_^^''-._     /
                                                                 .'  /  -''^^    ^^''-  \--'^
                                                               .'   .`.  `'''----'''^  .`. \
                                                             .'    /   `'--..____..--'^   \ \
                                                            /  _.-/                        \ \
                                                        .::'_/^   |                        |  `.
                                                               .-'|                        |    `-.
                                                         _.--'`   \                        /       `-.
                                                        /          \                      /           `-._
                                                        `'---..__   `.                  .�_.._   __       \
                                                                 ``'''`.              .'gnv   `'^  `''---'^
                                                                        `-..______..-'
    """))                                                          

##BARRA DE JOGADOR

class Minimap(): ## EM ANDAMENTO
    pass

def show_status_ascii(room, life, stgh, name, p_class, weakness):
    if p_class == "Guerreiro":    
        print(rf"""                                         ____________________________________________________________________________
                                        |  ^   ________________________________________________________________   ^  |
                                        | / \ |                                                                | / \ |
                                        | | | | GUERREIRO                                                      | | | |
                                        | | | | NOME: {name.ljust(20,' ')}                                     | | | |
                                        | | | | VIDA: {str(life).ljust(33,' ')}                                | | | |
                                        | | | | FORÇA: {str(stgh).ljust(33,' ')}                               | | | |
                                        | | | | SALA: {room.ljust(20,' ')}                                     | | | |
                                        |o===o| FRAQUEZA: {weakness.ljust(24,' ')}                             |o===o|
                                        |  H  |                                                                |  H  |
                                        |  *  |________________________________________________________________|  *  |
                                        |____________________________________________________________________________|""")
    elif p_class == "Mago":
        print(rf"""                                         ____________________________________________________________________________
                                        | .||,   ____________________________________________________________   .||, |
                                        |\.`',/ |                                                            | \.`',/|
                                        |= ,. = |  MAGO                                                      | = ,. =|
                                        |/ || \ |  NOME: {name.ljust(20,' ')}                                | / || \|
                                        |  ||   |  VIDA: {str(life).ljust(33,' ')}                           |   ||  |
                                        |  ||   |  FORÇA: {str(stgh).ljust(33,' ')}                          |   ||  |
                                        |  ||   |  SALA: {room.ljust(20,' ')}                                |   ||  |
                                        |  ||   |  FRAQUEZA: {weakness.ljust(24,' ')}                        |   ||  |
                                        |  ||   |                                                            |   ||  |
                                        |  ||   |____________________________________________________________|   ||  |
                                        |____________________________________________________________________________|""")

##SALAS
def first_room_ascii(life, stgh, name, p_class, weakness):
    clean()
    print(gray(fr"""                                                  __________________________________________________________
                                                 /##|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|##\
                                                /###|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|###\
                                               /####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|####\
                                              /#####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#####\
                                             /######|WWWWWWWWWWWWWWWWWWW{yellow("|2 - ENTRAR|")}WWWWWWWWWWWWWWWWWWWWW|######\
                                            /#######|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#######\
                                           /########|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|########\
                                          /#########▓WWWWWWWWWWWWWWWWW{red(")")}WWWWW.----.WWWWW{red(")")}WWWWWWWWWWWWWWWWW|#########\
                                         /##########▓WWWWWWWWWWWWWWWW{yellow("(_)")}WW,'  ||  `.WW{yellow("(_)")}WWWWWWWWWWWWWWWW|##########\
                                        /###########▓▓WWWWWWWWWWWWWWW| |WI    ||    IW| |WWWWWWWWWWWWWWWW|###########\
                                    {yellow("|3 - EXPLORAR|")}#▓▓▓▓WWWWWWWWWWWWWW| |WI    ||    IW| |WWWWWWWWWWWWWWWW|###########|
                                        |#########▓▓▓▓▓▓▓WWWWWWWWWWWW|_|WI    ||    IW|_|WWWWWWWWWWWWWWWW|###########|
                                        |#########▓▓▓▓▓▓▓▓WWWWWWWWWWWWWWWI   _||_   IWWWWWWWWWWWWWWWWWWWW|##,.-.#####|
                                        |########▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWWI  ' || `  IWWWWWWWWWWWWWWWWWWWW|#I  |  .###|
                                        |########▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI    ||    IWWWWWWWWWWWWWWWWWWWW|#I  |  I###|
                                        |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI    ||    IWWWWWWWWWWWWWWWWWWWW|#I  |  I###|
                                        |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI    ||    IWWWWWWWWWWWWWWWWWWWW|#I  |  I###|
                                        |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI____||____IWWWWWWWWWWWWWWWWWWWW|#I \|  I###|
                                        |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                           \#I  |\ I#{yellow("|1 - ENTRAR|")}
                                        |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                            \I  |  I###|
                                        |#######▓▓▓▓▓▓▓▓▓▓▓▓                                               \  |  I###|
                                        |########▓▓▓▓▓▓▓▓▓                                                  \ |  I###|
                                        |#######/ ▓▓▓▓▓                                                      \|  I###|
                                  {yellow("|4 - BAÚ|")}###____                                                            \  I###|
                                        |###/____/|                                                            \ I###|
                                        |##/____/||                                                             \####|
                                        |##|    | /                                                              \###|
                                        |##|____|/                                                                \##|
                                        |#/                                                                        \#|
                                        |/__________________________________________________________________________\|"""))
    show_status_ascii("Inicial", red(life), blue(stgh), name, p_class, weakness)

def second_room_ascii(life, stgh, name, p_class, weakness):
    clean()
    print(gray(fr"""                                                     ______________________________________________________
                                                   /|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|\
                                                  /#|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#\
                                                 /##|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|##\
                                                /###|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|###\
                                               /####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|####\
                                              /#####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#####\
                                             /######|WWWWWWWWWWWWWWWWWWW{yellow("|3 - ENTRAR|")}WWWWWWWWWWWWWWWWWWWWW|######\
                                            /####{yellow("|5 - CONVERSAR|")}WWWWW     WWWWWWWWWWWW    WWWWWWWWWWWWWWW|#######\
                                           /########|W(o.o)  WWWWWWWWW{red("(")}  WWW.----.WWWWW{red("(")}  WWWWWWWWWWWWWWW▓########\
                                          /#########|WW|=|   WWWWWWWW{yellow("(_)")}   `  ||  ',WW{yellow("(_)")}    WWWWWWWWWWWW▓#########\
                                         /##########|W__|__   WWWWWWW| |      ||    IW| |  WWWWWWWWWWWWW▓▓##########\
                                        |###########//.=|=.\\  WWWWWW| |      ||    IW| |  WWWWWWWWWWWW▓▓▓▓#{yellow("|4 - EXPLORAR|")}
                                        |##########//W.=|=.W\\  WWWWW|_|      ||    IW|_|  WWWWWWWWWW▓▓▓▓▓▓▓#########|
                                        |#####.-.,#\\W.=|=.W//  WWWWWWWWWI   _||_   IWWWWWWWWWWWWWWW▓▓▓▓▓▓▓▓#########|
                                        |###.  |  I#\\(_=_)//  WWWWWWWWWWI  ' || `  IWWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓########|
                                        |###I  |  I#|(:| |:)  WWWWWWWWWWWI    ||    IWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓▓########|
                                        |###I  |  I#|W|| ||  WWWWWWWWWWWWI    ||    IWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
                                        |###I  |  I#|W() ()  WWWWWWWWWWWWI    ||    IWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
                                        |###I  |/ I#|W|| ||  WWWWWWWWWWWWI____||____IWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
                               {yellow("|2 - ENTRAR|")}#I /|  I#/ || ||                                     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
                                        |###I  |  I/ ==' '==                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
                                        |###I  |  /                                               ▓▓▓▓▓▓▓▓▓▓▓▓#######|
                                        |###I  | /                                                  ▓▓▓▓▓▓▓▓▓########|
                                        |###I  |/                                                      ▓▓▓▓▓ \#######|
                                        |###I  /                                                              \######|
                                        |###I /                                                                \#####|
                                        |####/                                                                  \####|
                                        |###/                                                                    \###|
                                        |##/                      {yellow("|1- VOLTAR À SALA ANTERIOR|")}                     \##|
                                        |#/                                    |                                   \#|
                                        |/_____________________________________V____________________________________\| """))
    show_status_ascii("Sala 2", red(life), blue(stgh), name, p_class, weakness)

def third_room_ascii(life, stgh, name, p_class, weakness):
    clean()
    print(gray(fr"""            ___________________________________________________________________________________________________________________________________
           /|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########|WWWWWWWWWWWWWWWWWWW{yellow("|5 - ABRIR O BAÚ|")} WWWWWWWWWWWWW|###########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|\
          /#|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########|WWWWWWWWWWWWWW                            WWWWWWWW|###########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|#\
         /##|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########|WWWWWWW        ____...------------...____        W|###########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|##\
        /###|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########|WWWWW     _.-"` /o/__ ____ __ __  __ \o\_`"-._     ###########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###\
       /####|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########|WWWWW   .'     / /                    \ \     '.   ###########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|####\
      /#####|WWWWWWWWWWWW     WWWWWWWWWW|###########|WWWW    |=====/o/======================\o\=====|    ##########|WWWWWWWWWW     WWWWWWWWWWWW|#####\
     /######|WWWWWWWWWWWW {red(")")}    WWWWWWWWW|###########|WWWW    |____/_/________..____..________\_\____|    ##########|WWWWWWWWWW {red(")")}    WWWWWWWWWWW|######\
    /#######|WWWWWWWWWWWW{yellow("(_)")}  WWWWWWWWWW|###########|WWWW    /   _/ \_     <_o#\__/#o_>     _/ \_   \    ##########|WWWWWWWWWW{yellow("(_)")}  WWWWWWWWWWWW|#######\
  {yellow("|4 - EXPLORAR?|")}WWWWWWWW| | WWWWWWWWWWW|###########|WWWWW   \______________\########/______________/    ##########|WWWWWWWWWW| | WWWWWWWWWWWWW|########\ 
  /#########|WWWWWWWWWWWW| | WWWWWWWWWWW|##########/          |===\!/========================\!/===|    \##########|WWWWWWWWWW| | WWWWWWWWWWWWW|#########\
 /##########▓WWWWWWWWWWWW|_| WWWWWWWWWWW|#########/           |   |=|          .---.         |=|   |     \#########|WWWWWWWWWW|_| WWWWWWWWWWWWW|##########\
/###########▓▓WWWWWWWWWWWWWWWWWWWWWWWWWW|########/            |===|o|=========/     \========|o|===|      \########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########
|##########▓▓▓▓WWWWWWWWWWWWWWWWWWwwWWWWW|#######/             |   | |         \() ()/        | |   |       \#######|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########|
|#########▓▓▓▓▓▓▓WWWWWWWWWWWWWWWWWWWWWWW|######/              |===|o|======('-.) A (.-')=====|o|===|        \######|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########|
|#########▓▓▓▓▓▓▓▓WWWWWWWWWWWWWWWWWWWWWW|#####/               | __/ \__     '-.\uuu/.-'    __/ \__ |         \#####|WWWWWWWWWWWWWWWWWWWWWWWWWWW|##,.-.#####|
|########▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWWWWWWWWW|####/                |=== .'.'^'.'.====||==== .'.'^'.'.===|          \####|WWWWWWWWWWWWWWWWWWWWWWWWWWW|#I  |  .###|
|########▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWWWWWWWW|###/                 |  _\o/   __  (.' __  '.) _   _\o/  _|           \###|WWWWWWWWWWWWWWWWWWWWWWWWWWW|#I  |  I###|
|#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWWWWWWWW|##/                  `''''-''''''''''''''''''''''''''-''''`            \##|WWWWWWWWWWWWWWWWWWWWWWWWWWW|#I  |  I###|
|#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWWWWWWWW|#/                                                                      \#|WWWWWWWWWWWWWWWWWWWWWWWWWWW|#I  |  I###|
|#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWWWWWWWW|/________________________________________________________________________\|WWWWWWWWWWWWWWWWWWWWWWWWWWW|#I \|  I###|
|#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                                                                         \#I   \ I#{yellow("|3 - ENTRAR|")}
|#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                                                                          \I  |  I###|
|#######▓▓▓▓▓▓▓▓▓▓▓▓                                                                                                                             \  |  I###|
|########▓▓▓▓▓▓▓▓▓                                                                                                                                \ |  I###|
|#######/ ▓▓▓▓▓                                                                                                                                    \|  I###|
|######/                                                                                                                                            \  I###|
|#####/                                                                                                                                              \ I###|
|####/                                                                                                                                                \####|
|###/                                                                                                                                                  \###|
|##/                          {yellow("|1 - PRIMEIRA SALA|")}                                                            {yellow("|2 - SEGUNDA SALA|")}                         \##|
|#/                                   |                                                                              |                                   \#|
|/____________________________________V______________________________________________________________________________V____________________________________\|"""))
    show_status_ascii("Sala 4", red(life), blue(stgh), name, p_class, weakness)

def fourth_room_ascii(life, stgh, name, p_class, weakness):
    clean()
    print(gray(fr"""                                                     ____________________________________________________
                                                   /|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|\
                                                  /#|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#\
                                                 /##|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|##\
                                                /###|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|###\
                                               /####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|####\
                                              /#####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#####\
                                             /######|WWWWWWWWWWWWWWWWWWW{yellow("|3 - LUTAR|")}WWWWWWWWWWWWWWWWWWWW|######\
                                            /#######|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#######\
                                           /########|WW.-. WWWWWWWWW     WWWWWWWWWWWW     WWWWWWWW.-. W|########\
                                          /#########|W(o.o) WWWWWWWW {red(")")}    W.----.WWWWW{red(")")}    WWWWWW(o.o) |#########\
                                         /##########|WW|=|  WWWWWWWW{yellow("(_)")}  ,'  ||  `.WW{yellow("(_)")}  WWWWWWWW|=|   ##########\
            ____________________________/###########|W__|__   WWWWWW| | I    ||    IW| | WWWWWWWW__|__   ##########\____________________________
           /|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########//.=|=.\\  WWWWW| | I    ||    IW| | WWWWWW//.=|=.\\  #########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|\
          /#|WWWWWWWWWWWWWWWWWWWWWWWWWWW|##########// .=|=. \\  WWWW|_| I    ||    IW|_| WWWWW// .=|=. \\  ########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|#\
         /##|WWWWWWWWWWWWWWWWWWWWWWWWWWW|##########\\ .=|=. //  WWWWWWWWI   _||_   IWWWWWWWWWW\\ .=|=. //  ########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|##\
        /###|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########\\(_=_)//  WWWWWWWWWI  ' || `  IWWWWWWWWWWW\\(_=_)//   ########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###\
       /####|WWWWWWWWWWWWWWWWWWWWWWWWWWW|###########|(:| |:)  WWWWWWWWWWI    ||    IWWWWWWWWWWWW(:| |:)   #########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|####\
      /#####|WWWWWWWWWWWW     WWWWWWWWWW|###########|W|| ||  WWWWWWWWWWWI    ||    IWWWWWWWWWWWWW|| ||  ###########|WWWWWWWWWW     WWWWWWWWWWWW|#####\
     /######|WWWWWWWWWWWW {red(")")}    WWWWWWWWW|###########|W() ()  WWWWWWWWWWWI    ||    IWWWWWWWWWWWWW() ()  ###########|WWWWWWWWWW {red(")")}    WWWWWWWWWWW|######\
    /#######|WWWWWWWWWWWW{yellow("(_)")}  WWWWWWWWWW|###########|W|| ||  WWWWWWWWWWWI____||____IWWWWWWWWWWWWW|| ||  ###########|WWWWWWWWWW{yellow("(_)")}  WWWWWWWWWWWW|#######\
   /########|WWWWWWWWWWWW| | WWWWWWWWWWW|###########/ || ||                                      || ||   ##########|WWWWWWWWWW| | WWWWWWWWW{yellow("|4 - EXPLORAR?|")} 
  /#########|WWWWWWWWWWWW| | WWWWWWWWWWW|##########/ ==' '==                                    ==' '==  ##########|WWWWWWWWWW| | WWWWWWWWWWWWW▓#########\
 /##########|WWWWWWWWWWWW|_| WWWWWWWWWWW|#########/                                                      \#########|WWWWWWWWWW|_| WWWWWWWWWWWWW▓##########\
/###########|WWWWWWWWWWWWWWWWWWWWWWWWWWW|########/                                                        \########|WWWWWWWWWWWWWWWWWWWWWWWWWW▓▓###########\
|###########|WWWWWWW{yellow("|5 - ABRIR?|")}WwwWWWWW|#######/                                                          \#######|WWWWWWWWWWWWWWWWWWWWWWWWW▓▓▓▓##########|
|###########|WWWWWW_______________  WWWW|######/                                                            \######|WWWWWWWWWWWWWWWWWWWWWWW▓▓▓▓▓▓▓#########|
|###########|WWWW/______________/ \  WWW|#####/                                                              \#####|WWWWWWWWWWWWWWWWWWWWWW▓▓▓▓▓▓▓▓#########|
|###########|WWW(§   § §§§ §   §)  ) WWW|####/                                                                \####|WWWWWWWWWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓########|
|###########|WWW( § § §§§§§ § § ) /| WWW|###/                                                                  \###|WWWWWWWWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓▓########|
|###########|WWW(__§___§§§___§__)//| WWW|##/                                                                    \##|WWWWWWWWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
|###########|WWW|       M       |//| WWW|#/                                                                      \#|WWWWWWWWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
|###########|WWW|~~~~~~~~~~~~~~~|/ | WWW|/________________________________________________________________________\|WWWWWWWWWWWWWWWWWW▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
|###########/   |~~~~~~~~~~~~~~~| /                                                                                                   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
|##########/    |_______________|/                                                                                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓#######|
|#########/                                                                                                                             ▓▓▓▓▓▓▓▓▓▓▓▓#######|
|########/                  {yellow("|2 - TERCEIRA SALA|")}                                                            {yellow("|1 - SEGUNDA SALA|")}             ▓▓▓▓▓▓▓▓▓########|
|#######/                            |                                                                              |                        ▓▓▓▓▓ \#######|
|######/_____________________________V______________________________________________________________________________V_______________________________\######|"""))
    show_status_ascii("Sala 4", red(life), blue(stgh), name, p_class, weakness)

##BOSS
def boss_room_ascii():
    clean()
    print(gray(r"""
                                                              _________________
                                                         ____/#################\____
                                                     ___/################,##########\___
                                                   _/################/##/ \##\##########\_
                                                  /#################/\##| |##/\###########\
                                                 /##################\ \#| |#/ /############\
                                                |##DWB###############\ \| |/ /#########JRB##|
                                                |####################{{{\ /}}}##############|
                                                |###################{{<.> <.>}}#############|
                                                |#####################{ | | }###############|
                                                |#####################{ | | }####_#######__#|
                                                |#####################/_| |_\##_( )###__(  )_
                                                |####################{(_)_(_)}(  ` )_( '__ ` )
                                                |#####################{VV_VV}##(__( `)_(  )-` )
                                                |#####################\^^))^/######(   )_')  )
                                                |######################--((-########( ' _)__)
                                                |########################))##########(__)###|
                                                |########################(##################|
                                                |###########################################|
                                                |###########################################|
                                                |###########################################|
                                                |###########################################|
                                            \ | /########| |################################| \ | /
                                            _\|/|#######/   \####################\|/########|__\|/___
                                                        \   /
                                                         \ /"""
             ))    

def boss_battle_ascii(boss, life, stgh, name, p_class, weakness):
    for _ in range(2):
      clean()
      print(purple(r"""                                                           )        ||                           //    (          
                                                         'X\        ||                          //     (          
                                                          )\\       ||                         //      (          
                                                          ) \\      ||                        //       /          
                                                           ) \\     ||                       //       (           
                                                           )  \\    ||                      //        (           
                                                            \  \\   ||                     //         (_          
                                                             )  \\  ||                    //           (_         
                                                              )  \\ ||                   //             (_        
                                                              \   \\||                  //                \       
                                                               )   >. )               _/(__________________X`     
                                                               \  //||               (  .------------------.>     
                                                               _)// ||                )/\\             __.-'      
                                                              _)//  ||               //  \\          _(           
                                                              )//.. ||              //    \\       _(             
                                                              X/'  \||             //      \\     (               
                                                 __   _____,_,,_,,,,||            //        \\   (                
                                               .-` \_/.-._______)   )|           //.--------.\\ (                 
                                               `  `-- )        /  \'||   .--.__.//'-.________`\X'                 
                                                     '        (   ,)||  <\--<_(//-/> \       `.                   
                                                               \ /(\||  /   ^.'/_/(\  \        `.                 
                                                               (   \|`./  ^.' /<   .-  \/\___    \                
                                                                \ |/) | ^ /  /  \ /    /( \  `-.  \               
                                                                ( `/  ^  ^   (  \/>   /(   \    \  \              
                                                                 >--) ^  L/     \(   /(     )    )  )             
                                                              .(\  / ^/)/ \   ( / \ ((     /    /  /              
                                                            .'  )\/ ^/(/  (    \)  `-\\   /\   /  /               
                                                           /    > ^   /,   |  //      `\   /  ( .'                
                                                          /    (=  =)).'  /  //,        ) (    \`.                
                                                         /  ,  <, ,_>/    > '/',       /   >    \ )               
                                                         ) '  _/ /\>'    / ~ )'    ___/ _>'     (/                
                                                        /  .-(^-^)/}-.  / / /     (---. `--.                      
                                                       /  (  (-^-(/   ) \' /       `   \ \--)                     
                                                      /  /    )   )   ._/ /             `-)'                      
                                                      ) /    (   (   (-^. \-._           '                        
                                                     /  >             `  \)`--)                                   
                                                    (   `--.             '   '                     
                                                    / />----)                                                     
                                                   / /\)   '"""))
      show_status_ascii(purple(boss), red(life), blue(stgh), name, p_class, weakness)
      time.sleep(0.5)
      clean()
      print(purple(r"""                                                                   )        ||                                            //    (          
                                                                 'X\        ||                                          //     (          
                                                                  )\\       ||                                        //      (          
                                                                  ) \\      ||                                      //       /          
                                                                   ) \\     ||                                    //       (           
                                                                   )  \\    ||                                  //        (           
                                                                    \  \\   ||                                //         (_          
                                                                     )  \\  ||                              //           (_         
                                                                      )  \\ ||                            //             (_        
                                                                      \   \\||                          //                \       
                                                                       )   >. )                      _/(__________________X`     
                                                                       \  //||                    (  .------------------.>     
                                                                       _)// ||                      )/\\             __.-'      
                                                                      _)//  ||                    //  \\          _(           
                                                                      )//.. ||                  //    \\       _(             
                                                                      X/'  \||                //      \\     (               
                                                         __   _____,_,,_,,,,||              //        \\   (                
                                                       .-` \_/.-._______)   )|            //.--------.\\ (                 
                                                       `  `-- )        /  \'||   .--.__.//'-.________`\X'                 
                                                             '        (   ,)||  <\--<_(//-/> \       `.                   
                                                                       \ /(\||  /   ^.'/_/(\  \        `.                 
                                                                       (   \|`./  ^.' /<   .-  \/\___    \                
                                                                        \ |/) | ^ /  /  \ /    /( \  `-.  \               
                                                                        ( `/  ^  ^   (  \/>   /(   \    \  \              
                                                                         >--) ^  L/     \(   /(     )    )  )             
                                                                      .(\  / ^/)/ \   ( / \ ((     /    /  /              
                                                                    .'  )\/ ^/(/  (    \)  `-\\   /\   /  /               
                                                                   /    > ^   /,   |  //      `\   /  ( .'                
                                                                  /    (=  =)).'  /  //,        ) (    \`.                
                                                                 /  ,  <, ,_>/    > '/',       /   >    \ )               
                                                                 ) '  _/ /\>'    / ~ )'    ___/ _>'     (/                
                                                                /  .-(^-^)/}-.  / / /     (---. `--.                      
                                                               /  (  (-^-(/   ) \' /       `   \ \--)                     
                                                              /  /    )   )   ._/ /             `-)'                      
                                                              ) /    (   (   (-^. \-._           '                        
                                                             /  >             `  \)`--)                                   
                                                            (   `--.             '   '                     
                                                            / />----)                                                     
                                                           / /\)   '"""))
      show_status_ascii(purple(boss), red(life), blue(stgh), name, p_class, weakness)
      time.sleep(0.5)
      clean()
    print(purple(r"""                                                           )        ||                           //    (          
                                                         'X\        ||                          //     (          
                                                          )\\       ||                         //      (          
                                                          ) \\      ||                        //       /          
                                                           ) \\     ||                       //       (           
                                                           )  \\    ||                      //        (           
                                                            \  \\   ||                     //         (_          
                                                             )  \\  ||                    //           (_         
                                                              )  \\ ||                   //             (_        
                                                              \   \\||                  //                \       
                                                               )   >. )               _/(__________________X`     
                                                               \  //||               (  .------------------.>     
                                                               _)// ||                )/\\             __.-'      
                                                              _)//  ||               //  \\          _(           
                                                              )//.. ||              //    \\       _(             
                                                              X/'  \||             //      \\     (               
                                                 __   _____,_,,_,,,,||            //        \\   (                
                                               .-` \_/.-._______)   )|           //.--------.\\ (                 
                                               `  `-- )        /  \'||   .--.__.//'-.________`\X'                 
                                                     '        (   ,)||  <\--<_(//-/> \       `.                   
                                                               \ /(\||  /   ^.'/_/(\  \        `.                 
                                                               (   \|`./  ^.' /<   .-  \/\___    \                
                                                                \ |/) | ^ /  /  \ /    /( \  `-.  \               
                                                                ( `/  ^  ^   (  \/>   /(   \    \  \              
                                                                 >--) ^  L/     \(   /(     )    )  )             
                                                              .(\  / ^/)/ \   ( / \ ((     /    /  /              
                                                            .'  )\/ ^/(/  (    \)  `-\\   /\   /  /               
                                                           /    > ^   /,   |  //      `\   /  ( .'                
                                                          /    (=  =)).'  /  //,        ) (    \`.                
                                                         /  ,  <, ,_>/    > '/',       /   >    \ )               
                                                         ) '  _/ /\>'    / ~ )'    ___/ _>'     (/                
                                                        /  .-(^-^)/}-.  / / /     (---. `--.                      
                                                       /  (  (-^-(/   ) \' /       `   \ \--)                     
                                                      /  /    )   )   ._/ /             `-)'                      
                                                      ) /    (   (   (-^. \-._           '                        
                                                     /  >             `  \)`--)                                   
                                                    (   `--.             '   '                     
                                                    / />----)                                                     
                                                   / /\)   '"""))
    show_status_ascii(purple(boss), red(life), blue(stgh), name, p_class, weakness)

def boss_death_ascii():
    clean()
    print(red(r"""                                                              /                            )
                                                              (                             |\
                                                             /|                              \\
                                                            //                                \\
                                                           ///                                 \|
                                                          /( \                                  )\
                                                          \\  \_                               //)
                                                           \\  :\__                           ///
                                                            \\     )                         // \
                                                             \\:  /                         // |/
                                                              \\ / \                       //  \
                                                               /)   \   ___..-'           (|  \_|
                                                              //     /   _.'              \ \  \
                                                             /|       \ \________          \ | /
                                                            (| _ _  __/          '-.       ) /.'
                                                             \\ .  '-.__            \_    / / \
                                                              \\_'.     > --._ '.     \  / / /
                                                               \ \      \     \  \     .' /.'
                                                                \ \  '._ /     \ )    / .' |
                                                                 \ \_     \_   |    .'_/ __/
                                                                  \  \      \_ |   / /  _/ \_
                                                                   \  \       / _.' /  /     \
                                                                   \   |     /.'   / .'       '-,_
                                                                    \   \  .'   _.'_/             \
                                                       /\    /\      ) ___(    /_.'           \    |
                                                      | _\__// \    (.'      _/               |    |
                                                      \/_  __  /--'`    ,                   __/    /
                                                      (X) /X)   \  '.   :            \___.-'_/ \__/
                                                      /:/:  ,     ) :        (      /_.'__/-'|_ _ /
                                                     /:/: __/\ >  __,_.----.__\    /        (/(/(/
                                                    (_(,_/V .'/--'    _/  __/ |   /
                                                     VvvV  //`    _.-' _.'     \   \
                                                       n_n//     (((/->/        |   /
                                                       '--'         ~='          \  |
                                                                                  | |_,,,
                                                                                  \  \  /
                                                                                   '.__)"""))

def bloody_end_ascii():
    clean()
    print(red(r"""
                                                 .-----------------------'\               /`----------.            
                                                /.-----------------------( \             / (`---------.\           
                                               //                       //\ \           //\_\          \\          
                                              //                       //  `.\         //   \\          ).         
                                             //     /\     /\         //     \\       /(     \\        ( |         
                                            //     ( (  .--) )--.-'\ //______ )\  .--------.  \\        ||         
                                           //       \ \'  / /------{/_/-'/___}---/          \  \\       ||         
                                          //        /'' '''/  .-------/__>,          \     ,<\  )\      ||         
                                         ( )        >@) (@)' /\_/---<__.-'            `-.   //  \ \     ||         
                                          \\      .<``/ ;,,'')  ___.---'__.----.        (\  \\   \ \    |'         
                                           \\    {O__O}' )  /.--'_.-' ________,-\        \` ' )   \ \   |          
                                            \\   (/^^\) /  //_,-'----'    \-.---^----,--' >-  >    \ \  |          
                                             \\  ,-----/  //   ___LL.----._>-\           (   /\     \ \ |          
                                              \)'   (\'/)'/`. /.-_          ` >-----.   .-.  )/`.    \ )|          
                                               `    (_._(/   (/ /_X \--------/,        (|^|_.-.  `.  // |          
                                                    `(T\'     \(<_)__)     .'        .-^(|) |^|    `((  |          
                                                    ._)\\--.   \) ||     ,/  ,      ( X_ V, (|)      \\ |          
                                                   (.--)\-'`\   ` ||   ,'|           `(_>-^-'V)       )\|          
                                                    `\(('`\       |( ,'  |  ,              ` (        \ |          
                                                       `\         | )    |  @               ) \        )|          
                                                                  |/     `-                / -(        )|          
                                                                  `       `._\            '    `.     / |          
                                                             _____________(   `---------'___.---<    (  |          
                                                            /                           /_       \    \ |          
                                                          .'      _________.  `      .--'         )    \|          
                                                         (  _,   `              \  .'            /      '          
                                                          \ `       \__________.-^/      .   -,-'                  
                                                           \         |          _/  ___.   -' /                    
                                                            \        ,\        /   _/-------^T                     
                                                             \        \)    .-'  /(  (     ) |                     
                                                              \      ` \   (/-/._.'  (_   _) '                     
                                                               \      \ \  ' /'      (   ' )/                      
                                                                `.     \<           (`  , )'                       
                                                                  ` .   ))        _(` ,  /                         
                                                                     \_   >    _-' ,   .'                          
                                                                     .'  /   .',  _.--'                            
                                                               .----' _ (   (/.--'                 
                                                               (-'-._/(_ )  ('                                     
                                                                      (-'
                                """))

def peaceful_end_ascii():
    clean()
    print(green(fr"""
                                                               __/>^^^;:,
                                                  __  __      /-.       :,/|/|
                                                 /  \/  \  __/ ^         :,/ \__
                                                |        |(~             ;/ /  /
                                                \        / `-'--._       / / ,<  ___
                                                 \      /,__.   /=\     /  _/  >|_'.
                                                  \    /  `_ `--------'    __ / ',\ \
                                                   \  / ,_// ,---_____,   ,_  \_  ,| |
                                                    \/   `--' |=|           \._/ ,/  |
                                                               \=\            `,,/   |
                                                                \=\            ||    /
                                                                 \=\____       |\    \
                                                                / \/    `     <__)    \
                                                                | |                    |
                                                              ,__\,\                   /
                                                             ,--____>    /\.         ./
                                                             '-__________>  \.______/
                                                          """))

def peaceful_end_trap_ascii():
    clean()
    print(red(fr"""
                                                               __/>^^^;:,
                                                  __  __      /-.       :,/|/|
                                                 /  \/  \  __/ X         :,/ \__
                                                |        |(~             ;/ /  /
                                                \        / `-'--._       / / ,<  ___
                                                 \      /,__.   /=\     /  _/  >|_'.
                                                  \    /  `_ `--------'    __ / ',\ \
                                                   \  / ,_// ,---_____,   ,_  \_  ,| |
                                                    \/   `--' |=|           \._/ ,/  |
                                                               \=\            `,,/   |
                                                                \=\            ||    /
                                                                 \=\____       |\    \
                                                                / \/    `     <__)    \
                                                                | |                    |
                                                              ,__\,\                   /
                                                             ,--____>    /\.         ./
                                                             '-__________>  \.______/
                                                          """))    
##BATALHAS
def squeleton_battle_ascii(life, stgh, name, p_class, weakness):
    for _ in range(2):
        clean()
        print(red(r"""    
                                                      .7
                                                    .'/
                                                   / /
                                                  / /
                                                 / /
                                                / /
                                               / /
                                              / /
                                             / /         
                                            / /          
                                          __|/
                                        ,-\__\                      |ESQUELETO|
                                        |f-'Y\|
                                        \()7L/
                                         cgD                            __ _
                                         |\(                          .'  Y '>,
                                          \ \                        / _   _   \
                                           \\\                       )(_) (_)(|}
                                            \\\                      {  4A   } /
                                             \\\                      \uLuJJ/\l
                                              \\\                     |3    p)/
                                               \\\___ __________      /nnm_n//
                                               c7___-__,__-)\,__)('.  \_>-<_/D
                                                          //V     \_'-._.__G G_c__.-__<'/ ( \
                                                                 <'-._>__-,G_.___)\   \7\
                                                                ('-.__.| \'<.__.-' )   \ \
                                                                |'-.__'\  |'-.__.-'.\   \ \
                                                                ('-.__''. \'-.__.-'.|    \_\
                                                                \'-.__''|!|'-.__.-'.)     \ \
                                                                 '-.__''\_|'-.__.-'./      \ l
                                                                  '.__'''>G>-.__.-'>       .--,_
                                                                      ''  G 
        """))
        show_status_ascii("BATALHA", red(life), blue(stgh), name, p_class, weakness)
        time.sleep(0.5)
        clean()
        print(red(r"""
                                                                    _____
                                                                 .7________
                                                               .'/ _____ __ __
                                                              / / ____ ___
                                                             / / ____ __ ______
                                                            / / ___ ______ _____
                                                           / / _________ ___
                                                          / / _____ ____ ___
                                                         / /________ ______
                                                        / /_______ _____ _____         
                                                       / /________ ___________          
                                                   _  _|/
                                                 ,-\__\             |ESQUELETO|
                                                 |f-'Y\|
                                                \()7L/
                                                 cgD                            __ _
                                                 |\(                          .'  Y '>,
                                                  \ \                        / _   _   \
                                                   \\\                       )(_) (_)(|}
                                                    \\\                      {  4A   } /
                                                     \\\                      \uLuJJ/\l
                                                      \\\                     |3    p)/
                                                       \\\___ __________      /nnm_n//
                                                       c7___-__,__-)\,__)('.  \_>-<_/D
                                                                  //V     \_'-._.__G G_c__.-__<'/ ( \
                                                                         <'-._>__-,G_.___)\   \7\
                                                                        ('-.__.| \'<.__.-' )   \ \
                                                                        |'-.__'\  |'-.__.-'.\   \ \
                                                                        ('-.__''. \'-.__.-'.|    \_\
                                                                        \'-.__''|!|'-.__.-'.)     \ \
                                                                         '-.__''\_|'-.__.-'./      \ l
                                                                          '.__'''>G>-.__.-'>       .--,_
                                                                              ''  G 
        """))
        show_status_ascii("BATALHA", red(life), blue(stgh), name, p_class, weakness)
        time.sleep(0.5)
        clean()

    print(red(r"""
                                                      .7
                                                    .'/
                                                   / /
                                                  / /
                                                 / /
                                                / /
                                               / /
                                              / /
                                             / /         
                                            / /          
                                          __|/
                                        ,-\__\                      |ESQUELETO|
                                        |f-'Y\|
                                        \()7L/
                                         cgD                            __ _
                                         |\(                          .'  Y '>,
                                          \ \                        / _   _   \
                                           \\\                       )(_) (_)(|}
                                            \\\                      {  4A   } /
                                             \\\                      \uLuJJ/\l
                                              \\\                     |3    p)/
                                               \\\___ __________      /nnm_n//
                                               c7___-__,__-)\,__)('.  \_>-<_/D
                                                          //V     \_'-._.__G G_c__.-__<'/ ( \
                                                                 <'-._>__-,G_.___)\   \7\
                                                                ('-.__.| \'<.__.-' )   \ \
                                                                |'-.__'\  |'-.__.-'.\   \ \
                                                                ('-.__''. \'-.__.-'.|    \_\
                                                                \'-.__''|!|'-.__.-'.)     \ \
                                                                 '-.__''\_|'-.__.-'./      \ l
                                                                  '.__'''>G>-.__.-'>       .--,_
                                                                      ''  G 
    """))
    show_status_ascii("BATALHA", red(life), blue(stgh), name, p_class, weakness)

def bat_battle_ascii(life, stgh, name, p_class, weakness):
    for _ in range(2):    
        clean()
        print(red(r"""
                  

                  


                  


                                                            |MORCEGO|

                                                      ._.                  _.____.
                                                       ) \.              /    .(
                                                       )  |            .'   .(
                                                       ). ).          .'  .(
                                                         ) |.        .'  (
                                                         ). ;      ./  .(
                                                          ) |      )  (
                                                          ).;      :.(
                                                           )|    .|.;
                                                           .^--^./ (.
                                                           ;0..0;   \
                                                            'vv'_.:_.;   
                                                                 m  M
                  






        """))
        show_status_ascii("BATALHA", red(life), blue(stgh), name, p_class, weakness)
        time.sleep(0.5)
        clean()
        print(red(r"""
                  







                                                            |MORCEGO|
      
                                                           ._. _____                _.____.______
                                                            ) \._____              /    .(_______
                                                            )  |_____            .'   .(_____ _
                                                            ). )._____          .'  .(_____
                                                              ) |. _____      .'  (_____
                                                                ). ;_____   ./  .(_____
                                                                 ) |_____  )  (_____
                                                                 ).;_____ :.(_____
                                                                  )|    .|.;
                                                                   .^--^./ (.
                                                                   ;0..0;   \
                                                                    'vv'_.:_.;   
                                                                         m  M
        
                  
                  
                  
                  
                  
                  
                  """))
        show_status_ascii("BATALHA", red(life), blue(stgh), name, p_class, weakness)
        time.sleep(0.5)
        clean()
    print(red(r"""
              







                                                            |MORCEGO|

                                                      ._.                  _.____.
                                                       ) \.              /    .(
                                                       )  |            .'   .(
                                                       ). ).          .'  .(
                                                         ) |.        .'  (
                                                         ). ;      ./  .(
                                                          ) |      )  (
                                                          ).;      :.(
                                                           )|    .|.;
                                                           .^--^./ (.
                                                           ;0..0;   \
                                                            'vv'_.:_.;   
                                                                 m  M
    
              
              
              
              
              
              
              """))
    show_status_ascii("BATALHA", red(life), blue(stgh), name, p_class, weakness)

##TESOUROS
def chest_ascii():
    for _ in range(3):    
        clean()
        print(green(r"""
                                                    |ABRINDO O BAÚ...|
                            
                                                ____...------------...____
                                           _.-"` /o/__ ____ __ __  __ \o\_`"-._
                                         .'     / /                    \ \     '.
                                         |=====/o/======================\o\=====|
                                         |____/_/________..____..________\_\____|
                                         /   _/ \_     <_o#\__/#o_>     _/ \_   \
                                         \_________\####/_________/
                                          |===\!/========================\!/===|
                                          |   |=|          .---.         |=|   |
                                          |===|o|=========/     \========|o|===|
                                          |   | |         \() ()/        | |   |
                                          |===|o|======{'-.) A (.-'}=====|o|===|
                                          | __/ \__     '-.\uuu/.-'    __/ \__ |
                                          |==== .'.'^'.'.====|
                                          |  _\o/   __  {.' __  '.} _   _\o/  _|
                                          `""""-""""""""""""""""""""""""""-""""`
        """))
        time.sleep(0.5)
        clean()
        print(green(r"""
                                                    |ABRINDO O BAÚ...|

                                                    ____...------------...____
                                             _.-"` /o/__ ____ __ __  __ \o\_`"-._
                                           .'     / /                    \ \     '.
                                           |=====/o/======================\o\=====|
                                           |____/_/________..____..________\_\____|
                                           /   _/ \_     <_o#\__/#o_>     _/ \_   \
                                           \              _________\####/_________/
                                            |===\!/========================\!/===|
                                            |   |=|          .---.         |=|   |
                                            |===|o|=========/     \========|o|===|
                                            |   | |         \() ()/        | |   |
                                            |===|o|======{'-.) A (.-'}=====|o|===|
                                            | __/ \__     '-.\uuu/.-'    __/ \__ |
                                            |==== .'.'^'.'.====|
                                            |  _\o/   __  {.' __  '.} _   _\o/  _|
                                            `""""-""""""""""""""""""""""""""-""""`
        """))
        time.sleep(0.5)
    clean()
    print(green(r"""
                                                    |ABRINDO O BAÚ...|

                                                ____...------------...____
                                           _.-"` /o/__ ____ __ __  __ \o\_`"-._
                                         .'     / /                    \ \     '.
                                         |=====/o/======================\o\=====|
                                         |____/_/________..____..________\_\____|
                                         /   _/ \_     <_o#\__/#o_>     _/ \_   \
                                         \_________\####/_________/
                                          |===\!/========================\!/===|
                                          |   |=|          .---.         |=|   |
                                          |===|o|=========/     \========|o|===|
                                          |   | |         \() ()/        | |   |
                                          |===|o|======{'-.) A (.-'}=====|o|===|
                                          | __/ \__     '-.\uuu/.-'    __/ \__ |
                                          |==== .'.'^'.'.====|
                                          |  _\o/   __  {.' __  '.} _   _\o/  _|
                                          `""""-""""""""""""""""""""""""""-""""`
        """))
    time.sleep(0.5)
    clean()
    print(green(r"""                       
                                                    |VOCÊ ABRIU O BAÚ!|

                                                                _.--.
                                                            _.-'_:-'||
                                                        _.-'_.-::::'||
                                                   _.-:'_.-::::::'  ||
                                                 .'`-.-:::::::'     ||
                                                /.'`;|:::::::'      ||_
                                               ||   ||::::::'     _.;._'-._
                                               ||   ||:::::'  _.-!oo @.!-._'-.
                                               \'.  ||:::::.-!()oo @!()@.-'_.|
                                                '.'-;|:.-'.&$@.& ()$%-'o.'\U||
                                                  `>'-.!@%()@'@_%-'_.-o _.|'||
                                                   ||-._'-.@.-'_.-' _.-o  |'||
                                                   ||=[ '-._.-\U/.-'    o |'||
                                                   || '-.]=|| |'|      o  |'||
                                                   ||      || |'|        _| ';
                                                   ||      || |'|    _.-'_.-'
                                                   |'-._   || |'|_.-'_.-'
                                                    '-._'-.|| |' `_.-'
                                                        '-.||_/.-'
    """))

def potion_ascii(potion_type, cure):
    clean()
    print(green(fr"""
                                                           ,--,
                                                           )""(
                                                          .%nn%.
                                                         /%%%%%%\
                                                        .%%%%%%%%.
                                                        |"*%%%%*"|
                                                        |POÇÃO DE|
                                                        |{potion_type.upper().ljust(8,' ')}|
                                                        |8n....n8|
                                                        |%%%%%%%%|
                                                        |%%%%%%%%|
                                                         "*%%%%*"
                                                         Vida +{cure}
    """))

def item_ascii(item_type, value):
    clean()
    print(blue(rf"""
                
                                                           |VOCÊ ACHOU UM ITEM DE {item_type}!|
                                                                    |{item_type} +{value}|   
 
                                                                      
                                                            ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣶⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                            ⠀⠀⠀⠀⢀⡄⢸⣿⣿⡿⠛⠉⠁⠀⠀⠈⠉⠻⢿⣷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀
                                                            ⠀⠀⢀⣴⣿⣷⠀⣿⣿⠀⠀⠀⣠⣤⣤⣤⣄⡀⠀⠉⠻⣿⣿⣿⣿⣆⠀⠀⠀⠀
                                                            ⠀⠀⢸⣿⣿⣿⡄⢸⣿⡄⠀⠘⣿⡁⠀⣴⣿⣿⣷⣦⡀⠙⣿⡿⢿⣿⣆⠀⠀⠀
                                                            ⠀⠀⠀⣿⣿⣿⣧⠈⣿⣿⣦⡀⠈⠳⢤⣿⣿⣿⣿⣿⣷⣄⠘⣿⠀⢻⣿⣆⠀⠀
                                                            ⠀⠀⠀⢸⣿⣿⣿⡄⢹⣿⣿⣿⣷⣦⣄⡈⠉⠛⠻⢿⣿⣿⣆⣿⠀⣸⣿⣿⡆⠀
                                                            ⠀⠀⠀⠀⣿⣿⣿⣇⠈⣿⣿⣿⣿⡏⠉⠙⢿⣶⣤⣀⠈⠙⠿⣿⣾⣿⣿⡿⠁⠀
                                                            ⠀⠀⠀⠀⢻⣿⣿⣿⡀⢻⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣦⡀⠈⢿⣿⡿⠁⠀⠀
                                                            ⠀⠀⠀⠀⠈⣿⣿⣿⣇⠘⣿⣿⣿⣿⣧⠙⢿⣿⣿⣿⣿⣿⠃⠀⢸⡿⠁⠀⠀⠀
                                                            ⠀⠀⠀⠀⠀⢹⣿⣿⣿⣤⣿⣿⣿⣿⣿⣷⣄⠈⠉⠛⠋⠀⠀⣠⡾⠁⠀⠀⠀⠀
                                                            ⠀⠀⠀⠀⠀⠈⣿⡿⠋⣹⣿⣄⣈⡉⠛⠛⠿⠷⣶⣤⣤⣶⣾⡿⠁⠀⠀⠀⠀⠀
                                                            ⠀⠀⠀⠀⠀⠀⠙⢀⣴⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣈⣉⠙⠛⠀⠀⠀⠀⠀⠀⠀
                                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠿⠿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀
                                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀
               
               
               
               """))

def key_ascii(boss):
    clean()
    print(green(rf"""                  
                

                


                                                                   |VOCÊ PEGOU A CHAVE!|
                                                                           
                                                           
                                                                      ___________ @ @
                                                                     /{boss.ljust(9, ' ')}(@\   @
                                                                     \___________/  _@
                                                                               @  _/@ \_____
                                                                                @/ \__/-="="`
                                                                                 \_ /
                                                                                  <|
                                                                                  <|
                                                                                  <|
                                                                                  `

                                                                                  





                """))

##MORTES
def squeleton_death_ascii():
    clean()
    print(red(r"""                                                                  
                                                                         ,--.
                                                                        {    }
                                                                        K,   }
                                                                       /  `Y`
                                                                  _   /   /
                                                                 {_'-K.__/
                                                                   `/-.__L._
                                                                   /  ' /`\_}
                                                                  /  ' /     -VOCÊ DERROTOU O ESQUELETO!-
                                                          ____   /  ' /
                                                   ,-'~~~~    ~~/  ' /_
                                                 ,'             ``~~~%%',
                                                (                     %  Y
                                               {                      %% I
                                              {      -                 %  `.
                                              |       ',                %  )
                                              |        |   ,..__      __. Y
                                              |    .,_./  Y ' / ^Y   J   )|
                                              \           |' /   |   |   ||
                                               \          L_/    . _ (_,.'(
                                                \,   ,      ^^""' / |      )
                                                  \_  \          /,L]     /
                                                    '-_`-,       ` `   ./`
                                                       `-(_            )
                                                           ^^\..___,."""))

def bat_death_ascii():
    clean()
    print(red(r"""

                                                  ._.                  _.____.
                                                   ) \.              /    .(
                                                   )  |            .'   .(
                                                   ). ).          .'  .(
                                                     ) |.        .'  (
                                                     ). ;      ./  .(  -VOCÊ DERROTOU O MORCEGO!-
                                                      ) |      )  (
                                                      ).;      :.(
                                                       )|    .|.;
                                                       .^--^./ (.
                                                       ;X..X;   \
                                                        'vv'_.:_.;     
                                                             m  M
    """))

def death_ascii():
    clean()
    print(red(r""""
                                                             _..--'"'---.
                                                            /           '.
                                                            `            l
                                                            |'._  ,._ l/'\
                                                            |  _J<__/.v._/
                                                             \( ,~._,,,,-)
                                                              `-\' \`,,j|
                                                                 \_,____J
                                                            .--.__)--(__.--.
                                                           /  `-----..--'. j
                                                           '.- '`--` `--' \\
                                                          //  '`---'`  `-' \\
                                                         //   '`----'`.-.-' \\
                                                       _//     `--- -'   \' | \________
                                                      |  |         ) (      `.__.---- -'\
                                                       \7          \`-(               74\\\
                                                       ||       _  /`-(               l|//7__
                                                       |l    ('  `-)-/_.--.          f''` -.-'|
                                                       |\     l\_  `-'    .'         |     |  |
                                                       llJ   _ _)J--._.-('           |     |  l
                                                       |||( ( '_)_  .l   '. _    ..__I     |  L
                                                       ^\\\||`'   '   ''-. ' )''`'---'     L.-'`-.._
                                                            \ |           ) /.              ``'`-.._``-.
                                                            l l          / / |     VOCÊ MORREU!     |''|
                                                             ' \        / /   '-..__                |  |
                                                             | |       / /          1       ,- t-...J_.'
                                                             | |      / /           |       |  |
                                                             J  \  /'  (            l       |  |
                                                             | ().'`-()/            |       |  |
                                                            _.-'_.____/             l       l.-l
                                                        _.-'_.+'|                  /        \.  \
                                                  /'\.-'_.-'  | |                 /          \   \
                                                  \_   '      | |                1            | `'|
                                                    |ll       | |                |            i   |
                                                    \\\       |-\               \j ..          L,,'. `/
                                                   __\\\     ( .-\           .--'    ``--../..'      '-..
                                                     `'''`----`\\\\ .....--'''
                                                                \\\\                             
    """))
    time.sleep(5)
    clean()