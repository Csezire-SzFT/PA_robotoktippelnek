import random

#Random számok minta
#veletlen_szam = random.randint(1,12) #2..12
#print(veletlen_szam)
#print(f"Másik véletlenszám {random.randint(1,12)}")

#Robot gondol egy számra 1-10 között
#3 db kisrobot próbálja kitalálni 1-1 tippel

def kis_robot_tipp(robot_szama, gondolt_szam):
    kis_robot_tipp = random.randint(1,10)
    print(f"A(z) {robot_szama}. kis robot tippje: {kis_robot_tipp}", end="")
    if kis_robot_tipp == gondolt_szam:
        print(f", a(z) {robot_szama}. kis robot eltalálta!")
    else:
        print()


nagy_robot_gondol = random.randint(1,10)
print(f"A nagy robot gondolta: {nagy_robot_gondol}")
print()

kis_robot_tipp(1, nagy_robot_gondol)
kis_robot_tipp(2, nagy_robot_gondol)
kis_robot_tipp(3, nagy_robot_gondol)

print("Program vége...")

#Kipróbálni: tömb + lambda függvény
#Kipróbálni: objektummal __init__
