import random

#Random számok minta
#veletlen_szam = random.randint(1,12) #2..12
#print(veletlen_szam)
#print(f"Másik véletlenszám {random.randint(1,12)}")

#Robot gondol egy számra 1-10 között
#3 db kisrobot próbálja kitalálni 1-1 tippel

nagy_robot_gondol = random.randint(1,10)
kis_robot_1_tipp = random.randint(1,10)
kis_robot_2_tipp = random.randint(1,10)
kis_robot_3_tipp = random.randint(1,10)

print(f"A nagy robot gondolta: {nagy_robot_gondol}")
print()
print(f"Az első kis robot tippje: {kis_robot_1_tipp}", end="")
if kis_robot_1_tipp == nagy_robot_gondol:
    print(", az első kis robot eltalálta!")
else:
    print()

print(f"A második kis robot tippje: {kis_robot_2_tipp}", end="")
if kis_robot_2_tipp == nagy_robot_gondol:
    print(", a második kis robot eltalálta!")
else:
    print()

print(f"A harmadik kis robot tippje: {kis_robot_1_tipp}", end="")
if kis_robot_1_tipp == nagy_robot_gondol:
    print(", a harmadik kis robot eltalálta!")
else:
    print()

print("Program vége...")

#Kipróbálni: tömb + lambda függvény
#Kipróbálni: objektummal __init__
