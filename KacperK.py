import arcade
import random

def KacperK (x,y):

    y=y+1
    x=x+1

    arcade.draw_rectangle_filled(x+20 , y+ 40, 40, 80, (255,255,255))
    arcade.draw_rectangle_filled(x + 20, y + 2, 40, 4, (243, 0, 0))

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    arcade.draw_circle_filled(x+20, y+60, 10, (r,g,b))
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    arcade.draw_line(x+20,y+50 , x+20, y+20, (r,g,b),2)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    arcade.draw_line(x+20,y+20, x+30, y+4, (r,g,b),2)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    arcade.draw_line(x+20,y+20, x+10, y+4, (r,g,b),2)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    arcade.draw_line(x+20,y+40, x+10, y+ 20, (r,g,b),2)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    arcade.draw_line(x + 20, y + 40, x + 30, y + 20, (r,g,b),2)

    #ansigt
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    arcade.draw_circle_filled(x+24, y+65, 2, (r,g,b),)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    arcade.draw_circle_filled(x + 16, y + 65, 2, (r,g,b),)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    arcade.draw_line(x+24, y+55, x + 16, y + 55, (r,g,b),2)