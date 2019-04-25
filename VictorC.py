import arcade

x=0
y=0

arcade.open_window(40,80,"stick")
arcade.set_background_color((0,0,0))

def VictorC(x,y):
    arcade.start_render()
    arcade.draw_circle_outline(x+10*2,y+30*2,5*2,(255,255,255))#head
    arcade.draw_line(x+10*2,y+25*2,x+10*2,y+12*2,(255,255,255),1)#body
    arcade.draw_line(x+10*2,y+12*2,x+5*2,y+2*2,(255,255,255))#left leg
    arcade.draw_line(x+10*2,y+12*2,x+15*2,y+2*2,(255,255,255))#right leg
    arcade.draw_line(x+3*2,y+20*2,x+17*2,y+20*2,(255,255,255)) #arms
    arcade.draw_circle_filled(x+8*2,y+31*2,0.8*2,(0,0,255))#Left eye
    arcade.draw_circle_filled(x+12*2,y+31*2,0.8*2,(0,0,255)) #Right eye
    arcade.finish_render()
    arcade.run()