def WilliamT (x,y):

import arcade
x=40
y=80
arcade.draw_rectangle_filled(x/2,y-20,x,y*0.5,(34,128,178),0)
arcade.draw_rectangle_filled(x/2,y-60,x,y*0.5,(34,178,34),0)
arcade.draw_circle_outline(x*0.5,y-20,x/6,(255,255,0),1)
arcade.draw_line(x*0.5,y-20-x/6-1,x/2,y-50,(255,100,0),1.5)
arcade.draw_line(x*0.5,y*0.5,x-30,y*0.7,(255,100,0),1.5)
arcade.draw_line(x*0.5,y*0.5,x-10,y*0.4,(255,100,0),1.5)
arcade.draw_line(x*0.5,y-50,x/1.5,y-70,(255,100,0),1.5)
arcade.draw_line(x*0.5,y-50,x-x/1.5,y-70,(255,100,0),1.5)
arcade.draw_line(x*0.5,y-60,x*0.5,y-60,(101,67,33),1.6)
