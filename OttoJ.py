def OttoJ(x, y):
    xCenter = x + 20
    yCenter = y + 40

    arcade.draw_rectangle_filled(x + 20, y + 40, 40, 80, arcade.color.BLACK)
    arcade.draw_line(x + 5, y + 5, x + 35, y + 75, (255, 255, 255), 10)
    arcade.draw_line(x + 35, y + 5, x + 5, y + 75, (255, 255, 255), 10)
    arcade.draw_circle_filled(xCenter, yCenter - 15, 5, (255, 0, 8))
    arcade.draw_triangle_filled(xCenter, yCenter + 10, xCenter - 8, yCenter - 10, xCenter + 8, yCenter - 10, (255, 0, 8))
    arcade.draw_line(xCenter - 8, yCenter - 10, xCenter - 12, yCenter - 25, (255, 0, 8), 2)
    arcade.draw_line(xCenter + 8, yCenter - 10, xCenter + 12, yCenter - 25, (255, 0, 8), 2)
    arcade.draw_line(xCenter - 3, yCenter + 3, xCenter - 10, yCenter + 25, (255, 0, 8), 2)
    arcade.draw_line(xCenter + 3, yCenter + 3, xCenter + 10, yCenter + 25, (255, 0, 8), 2)
