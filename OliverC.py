import arcade

def OliverC(x, y):
    #Position
    x = 0
    y = 0

    #Størrelse SKAL IKKE ÆNDRES
    w = 40
    h = 80

    #arcade.open_window(w + x, h + y, "stckman")
    #arcade.set_background_color((45, 121, 183))

    #Baggrund
    arcade.draw_rectangle_filled(w/2 + x, h/2 + y, w, h, (0, 0, 255))

    #Hoved
    arcade.draw_circle_filled(w/2 + x, h/1.5 + y, w/6, (255, 255, 255))
    #arcade.draw_triangle_filled(w*())

    #Krop
    arcade.draw_line(w/2 + x, h/1.5 + y, w/2 + x, h/4 + y, (255, 255, 255), w/10)

    #Ben
    arcade.draw_line(w/2 + x, h/4 + y, w/4 + x, h/10 + y, (255, 255, 255), w/10)
    arcade.draw_line(w/2 + x, h/4 + y, w*(3/4) + x, h/10 + y, (255, 255, 255), w/10)

    #Arme
    arcade.draw_line(w*0.20 + x, h*0.5 + y, w*0.80 + x, h*0.5 + y, (255, 255, 255), w/10)

    #arcade.finish_render()

    #arcade.run()