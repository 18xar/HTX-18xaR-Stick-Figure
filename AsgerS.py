import arcade

def AsgerS(x,y):
    
    arcade.draw_circle_outline(x+20,y+60,10,arcade.color.BLACK)
    arcade.draw_line(x+20,y+50,x+20,y+30,arcade.color.BLACK)
    arcade.draw_line(x+20,y+30,x+10,y+10,arcade.color.BLACK)
    arcade.draw_line(x+20,y+30,x+30,y+10,arcade.color.BLACK)
    arcade.draw_line(x+10,y+45,x+30,y+45,arcade.color.BLACK)
    arcade.draw_circle_filled(x+15.5,y+62,1.5,arcade.color.BLACK)
    arcade.draw_circle_filled(x+23.5,y+62,1.5,arcade.color.BLACK)
    arcade.draw_line(x+17.5,y+55,x+23.5,y+55,arcade.color.BLACK)