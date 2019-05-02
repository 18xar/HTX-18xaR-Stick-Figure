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
import random

arcade.open_window(600, 400, "Wassup")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

ListMedFunktioner = [NikolajK, dreng, pige, AndreasP, LuccasS1, LuccasS2, AslakD, VictorC, MartinP, ThomasS, ChristianW,
                     OttoJ, KasperEBP]

for x in range(0, 600, 40):
    for y in range(0, 400, 80):
        valg = random.choice(ListMedFunktioner)
        valg(x, y)
        print(str(x) + ", " + str(y) + " : " + str(valg).split(" ")[1])

arcade.finish_render()
arcade.run()
