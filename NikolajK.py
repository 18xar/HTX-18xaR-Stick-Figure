import arcade

def NikolajK(x, y, sizeScale=2):
    sizeX = 20 * sizeScale
    sizeY = 40 * sizeScale
    # ----- Baggrund
    arcade.draw_rectangle_filled(x + sizeX/2, y + sizeY/2, sizeX, sizeY, arcade.color.GREEN)
    arcade.draw_rectangle_filled(x + sizeX/2, y + sizeY * 25/40, sizeX, sizeY * 3/4, arcade.color.SKY_BLUE)
    # ----- Stick figure
    arcade.draw_circle_filled(x + sizeX/2, y + sizeY * 3/4, 5 * sizeScale, arcade.color.BLACK)
    arcade.draw_line(x + sizeX/2, y + sizeY * 3/4, x + sizeX/2, y + sizeY * 1/4, arcade.color.BLACK, 2 * sizeScale)
    # Draw arms
    arcade.draw_line(x + sizeX/2, y + sizeY/2 - 3 * sizeScale, x + 3 * sizeScale, y + sizeY/2 + 3 * sizeScale, arcade.color.BLACK, 2 * sizeScale)
    arcade.draw_line(x + 3 * sizeScale, y + sizeY/2 + 3 * sizeScale, x + 1.5 * sizeScale, y + sizeY/2 - 4 * sizeScale, arcade.color.BLACK, 2 * sizeScale)
    arcade.draw_line(x + sizeX/2, y + sizeY/2 - 3 * sizeScale, x + sizeX - 3.5 * sizeScale, y + sizeY/2 + 1 * sizeScale, arcade.color.BLACK, 2 * sizeScale)
    arcade.draw_line(x + sizeX - 3.5 * sizeScale, y + sizeY/2 + 1 * sizeScale, x + sizeX - 3 * sizeScale, y + sizeY/2 + 7 * sizeScale, arcade.color.BLACK, 2 * sizeScale)
    # Draw legs
    arcade.draw_line(x + sizeX/2, y + sizeY * 1/4, x + sizeX/2 - 6 * sizeScale, y + 4, arcade.color.BLACK, 2 * sizeScale)
    arcade.draw_line(x + sizeX/2, y + sizeY * 1/4, x + sizeX/2 + 6 * sizeScale, y + 4, arcade.color.BLACK, 2 * sizeScale)
    # Draw face
    arcade.draw_circle_filled(x + sizeX/2 - 2.5 * sizeScale, y + sizeY * 3/4, 2 * sizeScale, arcade.color.WHITE)
    arcade.draw_circle_filled(x + sizeX/2 + 2.5 * sizeScale, y + sizeY * 3/4, 2 * sizeScale, arcade.color.WHITE)
    arcade.draw_ellipse_outline(x + sizeX/2, y + sizeY * 70/80, 5 * sizeScale, 1.75 * sizeScale, arcade.color.GOLD, 1.5 * sizeScale)


# arcade.open_window(600, 400, "Wassup")
# arcade.set_background_color(arcade.color.WHITE)

# arcade.start_render()

# NikolajJ(200, 125)

# arcade.finish_render()
# arcade.run()
