def MartinP (x,y):
    import arcade
    import time
    import random;
    arcade.start_render()
    arcade.draw_rectangle_filled(10*2, 20*2, 20*2, 40*2, (50, 50, 255))#baggrund
    arcade.draw_circle_filled(x + 10*2, y + 30*2, 10, (255, 255, 255))  # hoved
    arcade.draw_circle_outline(x + 8*2, y + 32*2, 1, (255, 0, 0))  # venstre øje
    arcade.draw_circle_outline(x + 12*2, y + 32*2, 1, (255, 0, 0))  # højre øje
    arcade.draw_line(x + 8*2, y + 28*2, x + 12*2, y + 28*2, (0, 0, 0))  # mund
    arcade.draw_line(x + 10*2, y + 25*2, x + 10*2, y + 10*2, (255, 255, 255))  # torso
    arcade.draw_line(x + 10*2, y + 10*2, x + 5*2, y + 0, (255, 255, 255))  # venstre ben
    arcade.draw_line(x + 10*2, y + 10*2, x + 15*2, y + 0, (255, 255, 255))  # højre ben

    arm=random.randint(1,3)
    if arm == 1:
        arcade.draw_line(x+5*2,y+17*2,x+15*2,y+17*2,(255,255,255))#arme
    elif arm == 2:
        arcade.draw_line(x + 5*2, y + 22*2, x + 15*2, y + 12*2, (255, 255, 255))  # arme
    elif arm == 3:
        arcade.draw_line(x + 5*2, y + 12*2, x + 15*2, y + 22*2, (255, 255, 255))  # arme
    else:
        arcade.draw_line(x + 5 * 2, y + 17 * 2, x + 15 * 2, y + 17 * 2, (255, 255, 255))  # arme
    arcade.finish_render()
    time.sleep(1)