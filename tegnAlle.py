# Henter funktionerne fra alle de forskellige filer
import arcade
from NikolajK import *
from SamuelS import *
from AslakD import *
from LuccasS import *
from VictorC import *
from AndreasP import *
from MartinP import *
from ThomasS import *
from ChristianW import *
from OttoJ import *
from KasperP import *
from DanielP import *
from OskarK import *
from KristofferW import *
from LauritsH import *
from BusterD import *
import random

arcade.open_window(600, 400, "Wassup")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# Liste med alle de funktioner som kan vælges imellem.
ListMedFunktioner = [NikolajK, SamuelS1, SamuelS2, AndreasP, LuccasS1, LuccasS2, AslakD, VictorC, ThomasS, ChristianW,
                     OttoJ, KasperEBP, DanielP1, DanielP2, OskarK, KristofferW, LauritsHMan1, LauritsHMan2, BusterD,
                     MartinP]

# Kører igennem alle koordinatsættene på skærmen.
for x in range(0, 600, 40):
    for y in range(0, 400, 80):
        valg = random.choice(ListMedFunktioner)
        valg(x, y)
        print(str(x) + ", " + str(y) + " : " + str(valg).split(" ")[1])

arcade.finish_render()
arcade.run()
