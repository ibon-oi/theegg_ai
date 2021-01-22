from pokemon import pokemon

if __name__ == "__main__":
    turno = 1
    pikachu = pokemon("pikachu",55)
    jigglypuff = pokemon("jigglypuff",45)
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