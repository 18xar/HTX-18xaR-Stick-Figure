import arcade


def KristofferW (x,y):


    arcade.draw_lrtb_rectangle_outline(x,x+40,y+80,y,(0,0,0),1)
    arcade.draw_rectangle_filled(x+20,y+60,40,40,arcade.color.BLIZZARD_BLUE)

    arcade.draw_circle_outline(x+20,y+62,8,(0,0,0),4)
    arcade.draw_line(x+20,y+54,x+20,y+25,(0,0,0),4)
    arcade.draw_line(x+20,y+40,x+10,y+46,arcade.color.BLACK,4)
    arcade.draw_line(x+20,y+40,x+30,y+46,arcade.color.BLACK,4)

    arcade.draw_line(x+10,y+25,x+30,y+25,(0,0,0),4)
    arcade.draw_line(x+10,y+25,x+6,y+13,arcade.color.BLACK,4)
    arcade.draw_line(x+30,y+25,x+34,y+13,arcade.color.BLACK,4)

    arcade.draw_arc_filled(x+20,y+62,6,4,arcade.color.DARK_YELLOW,90,0)

# arcade.open_window(600,600,"ArcadeWindow")
# arcade.set_background_color((255,255,255))
# arcade.start_render()
#
#
# KristofferW (300,300)
#
# arcade.finish_render()
# arcade.run()
