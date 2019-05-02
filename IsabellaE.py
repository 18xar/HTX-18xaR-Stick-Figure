import math
import arcade

#billede = arcade.load_texture("C:/Users/Isabella/OneDrive/_Aarhus Tech/Fag/Programmering B/Opgave/_14_billeder/baggrund.png")

arcade.open_window(40, 80, "Animation Window")

def IsabellaE(x,y):

    arcade.set_background_color((136,252,146))

    #arcade.start_render()

    arcade.draw_rectangle_filled(x+20, y+50, 25, 2, (255, 232, 209))

    arcade.draw_rectangle_filled(x+20, y+50, 10, 2, (219, 76, 76))

    arcade.draw_rectangle_filled(x+20, y+48, 2, 25, (219, 76, 76))

    arcade.draw_circle_filled(x+20, y+65, 10, (255, 232, 209))

    arcade.draw_triangle_filled(x+20, y+42, 10, 20, 30, 20, (219, 76, 76))

    arcade.draw_rectangle_filled(x+18, y+15, 2, 10, (255, 232, 209))

    arcade.draw_rectangle_filled(x+22, y+15, 2, 10, (255, 232, 209))

    arcade.draw_rectangle_filled(x+16, y+10, 4, 2, (0, 0, 0))

    arcade.draw_rectangle_filled(x+24, y+10, 4, 2, (0, 0, 0))

    #arcade.finish_render()

#arcade.run()