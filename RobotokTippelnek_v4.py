import random

#Random számok minta
#veletlen_szam = random.randint(1,12) #2..12
#print(veletlen_szam)
#print(f"Másik véletlenszám {random.randint(1,12)}")

#Robot gondol egy számra 1-10 között
#3 db kisrobot próbálja kitalálni 1-1 tippel

#Itt a robotok tippelnek, de ha valamelyik eltalálta, akkor már nem tippel a többi.

def kis_robot_tipp(robot_szama, tipp_szama, gondolt_szam):
    kis_robot_tipp = random.randint(1,10)
    talalat = False
    print(f"A(z) {robot_szama}. kis robot {tipp_szama}. tippje: {kis_robot_tipp}", end="")
    if kis_robot_tipp == gondolt_szam:
        print(f", a(z) {robot_szama}. kis robot eltalálta!")
        talalat = True
    else:
        print()
    return talalat

def kis_robot_3tipp(robot_szama, gondolt_szam):
    talalat_3 = False
    if kis_robot_tipp(robot_szama, 1, gondolt_szam):
        talalat_3 = True
    elif kis_robot_tipp(robot_szama, 2, gondolt_szam):
        talalat_3 = True
    elif kis_robot_tipp(robot_szama, 3, gondolt_szam):
        talalat_3 = True
    return talalat_3


nagy_robot_gondol = random.randint(1,10)
print(f"A nagy robot gondolta: {nagy_robot_gondol}")
print()

if not kis_robot_3tipp(1, nagy_robot_gondol):
    if not kis_robot_3tipp(2, nagy_robot_gondol):
        if not kis_robot_3tipp(3, nagy_robot_gondol):
            print("Egyik robot sem találta el!")

print("Program vége...")

