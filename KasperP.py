import arcade


def KasperEBP(x,y):
    brede = 40
    højde = 80
    arcade.draw_rectangle_filled(x+brede/2,y+højde/2,brede,højde,(0,255,0))
    arcade.draw_line(x + 25, y + 25, x + 25, y + 10, (0, 0, 0))
    arcade.draw_arc_filled(x+26,y+højde-42, 14, 16,(255,240,0), 90, 270, 30)
    arcade.draw_circle_filled(x+15,y+højde-20,10,(255,255,0))
    arcade.draw_circle_filled(x+14,y+højde-18,2,(0,0,0))
    arcade.draw_arc_filled(x+10,y+højde-22, 10, 3,(255,200,0), 180,270)
    arcade.draw_line(x+15,y+10,x+20,y+25,(0,0,0))
