
def SamuelS1(x, y):
    scale = 2
    colorR = random.randint(0, 255)
    colorG = random.randint(0, 255)
    colorB = random.randint(0, 255)
    # frame
    arcade.draw_rectangle_outline(10 * scale + x, 20 * scale + y, 20 * scale, 40 * scale, arcade.color.BLACK)
    # hovede
    arcade.draw_circle_outline(10 * scale + x, 30 * scale + y, 5 * scale, arcade.color.BLACK)
    # krop
    arcade.draw_line(10 * scale + x, 25 * scale + y, 10 * scale + x, 10 * scale + y, arcade.color.BLACK)
    # arme
    arcade.draw_line(3 * scale + x, 21 * scale + y, 17 * scale + x, 21 * scale + y, arcade.color.BLACK)
    # ben
    arcade.draw_line(10 * scale + x, 10 * scale + y, 5 * scale + x, 3 * scale + y, arcade.color.BLACK)
    arcade.draw_line(10 * scale + x, 10 * scale + y, 15 * scale + x, 3 * scale + y, arcade.color.BLACK)
    # fødder
    arcade.draw_line(5 * scale + x, 3 * scale + y, 3 * scale + x, 3 * scale + y, arcade.color.BLACK)
    arcade.draw_line(15 * scale + x, 3 * scale + y, 17 * scale + x, 3 * scale + y, arcade.color.BLACK)
    # øjne
    arcade.draw_circle_filled(8 * scale + x, 32 * scale + y, 1 * scale, arcade.color.BLACK)
    arcade.draw_circle_filled(12 * scale + x, 32 * scale + y, 1 * scale, arcade.color.BLACK)
    # highlight
    arcade.draw_circle_filled(8.5 * scale + x, 32 * scale + y, 0.3 * scale, arcade.color.WHITE)
    arcade.draw_circle_filled(12.5 * scale + x, 32 * scale + y, 0.3 * scale, arcade.color.WHITE)
    # mund
    arcade.draw_arc_outline(10 * scale + x, 29 * scale + y, 2, 1.5, (0, 0, 0), 180, 360)


def SamuelS2(x, y):
    scale = 2
    colorR = random.randint(0, 255)
    colorG = random.randint(0, 255)
    colorB = random.randint(0, 255)
    # frame
    arcade.draw_rectangle_outline(10 * scale + x, 20 * scale + y, 20 * scale, 40 * scale, arcade.color.BLACK)
    # hovede
    arcade.draw_circle_outline(10 * scale + x, 30 * scale + y, 5 * scale, arcade.color.BLACK)
    # krop
    arcade.draw_line(10 * scale + x, 25 * scale + y, 10 * scale + x, 10 * scale + y, arcade.color.BLACK)
    # arme
    arcade.draw_line(3 * scale + x, 21 * scale + y, 17 * scale + x, 21 * scale + y, arcade.color.BLACK)
    # ben
    arcade.draw_line(10 * scale + x, 10 * scale + y, 5 * scale + x, 3 * scale + y, arcade.color.BLACK)
    arcade.draw_line(10 * scale + x, 10 * scale + y, 15 * scale + x, 3 * scale + y, arcade.color.BLACK)
    # fødder
    arcade.draw_line(5 * scale + x, 3 * scale + y, 3 * scale + x, 3 * scale + y, arcade.color.BLACK)
    arcade.draw_line(15 * scale + x, 3 * scale + y, 17 * scale + x, 3 * scale + y, arcade.color.BLACK)
    # øjne
    arcade.draw_circle_filled(8 * scale + x, 32 * scale + y, 1 * scale, arcade.color.BLACK)
    arcade.draw_circle_filled(12 * scale + x, 32 * scale + y, 1 * scale, arcade.color.BLACK)
    # highlight
    arcade.draw_circle_filled(8.5 * scale + x, 32 * scale + y, 0.3 * scale, arcade.color.WHITE)
    arcade.draw_circle_filled(12.5 * scale + x, 32 * scale + y, 0.3 * scale, arcade.color.WHITE)
    # mund
    arcade.draw_arc_outline(10 * scale + x, 29 * scale + y, 2, 1.5, (0, 0, 0), 180, 360)
    # kjole
    arcade.draw_rectangle_filled(10 * scale + x, 15 * scale + y, 5 * scale, 15 * scale, (colorR, colorG, colorB))
    arcade.draw_triangle_filled(10 * scale + x, 17 * scale + y, 2 * scale + x, 7 * scale + y,
                                18 * scale + x, 7 * scale + y, (colorR, colorG, colorB))
