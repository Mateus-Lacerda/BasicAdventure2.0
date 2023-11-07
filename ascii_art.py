import os
import time

##FUNÇÕES DIVERSAS
def clean():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def red(string):
    
    return f"\033[31m{string}\033[m"

def blue(string):

    return f"\033[34m{string}\033[m"

def green(string):

    return f"\033[32m{string}\033[m"

def brown(string):

    return f"\033[33m{string}\033[m"

##TÍTULO
def title_ascii():
    pass

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
def show_status_ascii(room, life, stgh, name, p_class, weakness):
    if p_class == "Guerreiro":    
        print(rf"""                     ____________________________________________________________________________
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
        print(rf"""                     ____________________________________________________________________________
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
    print(fr"""                              __________________________________________________________
                             /##|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|##\
                            /###|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|###\
                           /####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|####\
                          /#####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#####\
                         /######|WWWWWWWWWWWWWWWWWWW|2 - ENTRAR|WWWWWWWWWWWWWWWWWWWWW|######\
                        /#######|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#######\
                       /########|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|########\
                      /#########▓WWWWWWWWWWWWWWWWW)WWWWW.----.WWWWW)WWWWWWWWWWWWWWWWW|#########\
                     /##########▓WWWWWWWWWWWWWWWW(_)WW,'  ||  `.WW(_)WWWWWWWWWWWWWWWW|##########\
                    /###########▓▓WWWWWWWWWWWWWWW| |WI    ||    IW| |WWWWWWWWWWWWWWWW|###########\
                |3 - EXPLORAR|#▓▓▓▓WWWWWWWWWWWWWW| |WI    ||    IW| |WWWWWWWWWWWWWWWW|###########|
                    |#########▓▓▓▓▓▓▓WWWWWWWWWWWW|_|WI    ||    IW|_|WWWWWWWWWWWWWWWW|###########|
                    |#########▓▓▓▓▓▓▓▓WWWWWWWWWWWWWWWI   _||_   IWWWWWWWWWWWWWWWWWWWW|##,.-.#####|
                    |########▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWWI  ' || `  IWWWWWWWWWWWWWWWWWWWW|#I  |  .###|
                    |########▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI    ||    IWWWWWWWWWWWWWWWWWWWW|#I  |  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI    ||    IWWWWWWWWWWWWWWWWWWWW|#I  |  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI    ||    IWWWWWWWWWWWWWWWWWWWW|#I  |  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI____||____IWWWWWWWWWWWWWWWWWWWW|#I \|  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                           \#I  |\ I#|1 - ENTRAR|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                            \I  |  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓                                               \  |  I###|
                    |########▓▓▓▓▓▓▓▓▓                                                  \ |  I###|
                    |#######/ ▓▓▓▓▓                                                      \|  I###|
              |4 - BAÚ|###____                                                            \  I###|
                    |###/____/|                                                            \ I###|
                    |##/____/||                                                             \####|
                    |##|    | /                                                              \###|
                    |##|____|/                                                                \##|
                    |#/                                                                        \#|
                    |/__________________________________________________________________________\|""")
    show_status_ascii("Inicial", red(life), blue(stgh), name, p_class, weakness)

def second_room_ascii(life, stgh, name, p_class, weakness):
    clean()
    print(fr"""                                 ______________________________________________________
                               /|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|\
                              /#|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#\
                             /##|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|##\
                            /###|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|###\
                           /####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|####\
                          /#####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|#####\
                         /######|WWWWWWWWWWWWWWWWWWW|3 - ENTRAR|WWWWWWWWWWWWWWWWWWWWW|######\
                        /#######|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW|5- CONVERSAR|####\
                       /########|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.-.WW|########\
                      /#########▓WWWWWWWWWWWWWWWWW)WWWWW.----.WWWWW)WWWWWWWWWWW(o.o)W|#########\
                     /##########▓WWWWWWWWWWWWWWWW(_)WW,'  ||  `.WW(_)WWWWWWWWWWW|=|WW|##########\
                    /###########▓▓WWWWWWWWWWWWWWW| |WI    ||    IW| |WWWWWWWWWW__|__W|###########\
                |4 - EXPLORAR|#▓▓▓▓WWWWWWWWWWWWWW| |WI    ||    IW| |WWWWWWWW//.=|=.\\###########|
                    |#########▓▓▓▓▓▓▓WWWWWWWWWWWW|_|WI    ||    IW|_|WWWWWWW//W.=|=.W\\##########|
                    |#########▓▓▓▓▓▓▓▓WWWWWWWWWWWWWWWI   _||_   IWWWWWWWWWWW\\W.=|=.W//#,.-.#####|
                    |########▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWWI  ' || `  IWWWWWWWWWWWW\\(_=_)//#I  |  .###|
                    |########▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI    ||    IWWWWWWWWWWWWW(:|W|:)|#I  |  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI    ||    IWWWWWWWWWWWWWW||W||W|#I  |  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI    ||    IWWWWWWWWWWWWWW()W()W|#I  |  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓WWWWWWWWWWWI____||____IWWWWWWWWWWWWWW||W||W|#I \|  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                     || || \#I  |\ I#|2 - ENTRAR|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    ==' '== \I  |  I###|
                    |#######▓▓▓▓▓▓▓▓▓▓▓▓                                               \  |  I###|
                    |########▓▓▓▓▓▓▓▓▓                                                  \ |  I###|
                    |#######/ ▓▓▓▓▓                                                      \|  I###|
                    |######/                                                              \  I###|
                    |#####/                                                                \ I###|
                    |####/                                                                  \####|
                    |###/                                                                    \###|
                    |##/                       1- VOLTAR À SALA ANTERIOR                      \##|
                    |#/                                    |                                   \#|
                    |/_____________________________________V____________________________________\| """)
    show_status_ascii("Sala 2", red(life), blue(stgh), name, p_class, weakness)

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

def item_ascii():
    pass

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