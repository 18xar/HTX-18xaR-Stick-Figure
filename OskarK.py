import arcade
def OskarK(x,y):
    #position

    #størrelse
    w=40
    h=80

    arcade.open_window(w, h, "stikfigure")
    arcade.set_background_color((0, 0, 255))

    arcade.draw_rectangle_filled(w/2+x, h/2+y, w, h/2,(100,173,200))



    arcade.draw_circle_filled(w/2+x, h*0.6+y, w/8,(0,0,0))

    #krop
    arcade.draw_line(w/2+x, h*0.6+y, w/2+x, h*0.35+y,(0,0,0), w/16)

    #arme
    arcade.draw_line(w/2+x, h*0.5+y, w/5+x, h*0.6+y,(0,0,0), w/16)

    #ben
    arcade.draw_line(w/2+x, h*0.35+y, w*0.65+x, h*0.1+y,(0,0,0), w/20)
    arcade.draw_line(w/2+x, h*0.35+y, w*0.35+x, h*0.1+y,(0,0,0), w/20)

    #telefon
    arcade.draw_line(w/2+x, h*0.3+y, w*0.33+x, h*0.3+y,(0,0,0), w/16)



    arcade.finish_render()

    arcade.run()

OskarK(0,0)