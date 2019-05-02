import arcade


def ThomasS (x, y):
    arcade.draw_rectangle_filled(20 + x, 40 + y, 40, 80, (255, 255, 255))
    arcade.draw_circle_filled(35 + x, 45 + y, 3, (0, 0, 255))
    arcade.draw_circle_filled(5 + x, 45 + y, 3, (0, 0, 255))
    arcade.draw_circle_filled(20 + x, 60 + y, 10, (0, 0, 255))
    arcade.draw_circle_filled(17 + x, 63 + y, 2, (255, 0, 0))
    arcade.draw_circle_filled(23 + x, 63 + y, 2, (255, 0, 0))
    arcade.draw_line(20 + x, 60 + y, 20 + x, 25 + y, (0, 0, 255), 2)
    arcade.draw_line(5 + x, 45 + y, 35 + x, 45 + y, (0, 0, 255), 2)
    arcade.draw_line(10 + x, 5 + y, 20 + x, 25 + y, (0, 0, 255), 2)
    arcade.draw_line(30 + x, 5 + y, 20 + x, 25 + y, (0, 0, 255), 2)
    arcade.draw_ellipse_filled(20 + x, 55 + y, 4, 2, (0, 0, 0))
    arcade.draw_ellipse_filled(8 + x, 5 + y, 4, 2, (0, 0, 0))
    arcade.draw_ellipse_filled(32 + x, 5 + y, 4, 2, (0, 0, 0))
    arcade.draw_triangle_filled(20 + x, 75 + y, 5 + x, 65 + y, 35 + x, 65 + y, (200, 150, 90))

# arcade.open_window(500, 500, "Test")
# arcade.set_background_color((0, 0, 0))
# while (True):
#     arcade.start_render()
#
#     ThomasS(0, 0)
#
#     arcade.finish_render()
# arcade.run()
