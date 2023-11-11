def reverse(string):
    for line in string.splitlines():
        print(line[::-1])

    print("Quantidade de linhas: ", len(string.splitlines()))
    print("Quantidade de colunas: ", len(string.splitlines()[1]))

reverse("""
####▓WWWWWWWWW
####▓WWWWWWWWW
####▓▓WWWWWWWW
###▓▓▓▓WWWWWWW
##▓▓▓▓▓▓▓WWWWW
##▓▓▓▓▓▓▓▓WWWW
#▓▓▓▓▓▓▓▓▓▓▓▓W
#▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓  
#▓▓▓▓▓▓▓▓▓    
\ ▓▓▓▓▓       
        """)