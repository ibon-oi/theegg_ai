from pokemon import pokemon
from entero import entero

if __name__ == "__main__":
    turno = 1
    pikachuAtaque = entero('Introduce el ataque de pikachu: \n')
    jigglypuffAtaque = entero('Introduce el ataque de jigglypuff: \n')
    pikachu = pokemon("pikachu",pikachuAtaque)
    jigglypuff = pokemon("jigglypuff",jigglypuffAtaque)
    pikachu.life()
    jigglypuff.life()
    print("-------------------------------------------------------")
    while jigglypuff.vida > 0 and pikachu.vida > 0:
        if turno == 1:
            jigglypuff.vida -= pikachu.ataque
            pikachu.life()
            jigglypuff.life()
            print("-------------------------------------------------------")
            turno = 0
        else:
            pikachu.vida -= jigglypuff.ataque
            pikachu.life()
            jigglypuff.life()
            print("-------------------------------------------------------")
            turno = 1
    if pikachu.vida <= 0:
        jigglypuff.win()
        pikachu.life()
        jigglypuff.life()
    else:
        pikachu.win()
        pikachu.life()
        jigglypuff.life()