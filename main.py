import Cardenas_script_1_stat as statsc 
import Cardenas_script_2_ev as evsc

def option_menu():
    opt = int(input("Press 1 to compute again Press 2 to exit. "))
    if opt ==1:
        main()
    elif opt ==2:
        exit()
    else:   
        option_menu()

def main():
    base1 = int(input("Base: "))
    trap = 1
    while trap == 1:
        iv = int(input("Individual Value: "))
        if iv>= 0 and iv<=31:
            trap1=0
        else:
            print("wrong input")
    trap = 1

    while trap1 ==1:
        ev = int(input("Effort Values: "))
        if ev >= 0 and ev <- 255:
            trap1=0
        else:
            print("Wrong input")
    
    Level= int(input(" Input Level: "))
    trap1=1 
    nature_input = int(input("1. beneficial or 2. Hindering": ))
    if nature_input==1:
        nature = 1.1
    else:
        nature=0.9

    select = int(input("1. Stat or 2. EV: "))
    if select ==1:
        hp = statsc.pokestats.statReturnHP(base1,iv,Level)
        otherstat =statsc.pokestats.startReturnOtherStat(base1,iv,ev,Level,nature)
        print("HP: ", hp)
        print("Other Stats: ", otherstat)
        option_menu();

    elif select==2:
        stats = int(input("Stats: "))
        dsi= evsc.pokeev.statsReturnDsi(base1,iv,ev,Level)
        print("Desired Stat Increase: ", dsi)
        evs = evsc.pokeev.statREturnEvs(stats,nature,dsi,Level)
        print("Evs Needed: ", evs,'\n')
        option_menu()

    else:
        print("Wrong Input!: ")
main()


