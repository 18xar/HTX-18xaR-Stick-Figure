import arcade

def WilfredH(x,y):
    arcade.open_window(600, 400, "Window")
    arcade.set_background_color((255,255,255))

    arcade.start_render()


    #draw background
    arcade.draw_rectangle_filled(x + 20,y + 10,40,20,(20,200,20),0)
    #arcade.draw_rectangle_filled(x + 20,y + 65,40,15,(100,100,255),0)

    #draw stickman
    #head
    arcade.draw_circle_outline(x + 20,y + 60,10,(0,0,0),2)
    arcade.draw_circle_outline(x + 16,y + 63,2,(0,0,0),1)
    arcade.draw_circle_outline(x + 24,y + 63,2,(0,0,0),1)
    arcade.draw_arc_outline(x + 20,y + 58,6,3,(0,0,0),200,340,1,0)

    arcade.draw_triangle_outline(x + 20,y + 80,x + 13,y + 70,x + 27,y + 70,(0,0,0),1)
    #body
    arcade.draw_arc_outline(x + 20,y + 49,10,5,(0,0,0),190,350,2,0)

    arcade.draw_line(x + 20,y + 50,x + 20,y + 30,(0,0,0),2)
    arcade.draw_line(x + 20,y + 30,x + 30,y + 10,(0,0,0),2)
    arcade.draw_line(x + 20,y + 30,x + 10,y + 10,(0,0,0),2)

    arcade.draw_line(x + 15,y + 40,x + 10,y + 50,(0,0,0),1)

    arcade.finish_render()

    arcade.run()