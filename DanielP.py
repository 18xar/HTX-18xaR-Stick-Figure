# size skal være 2

def DanielP1(x, y, size=2):
    import arcade
    bw = int(0.75 * size)
    if (bw < 1):
        bw = 1
    arcade.draw_rectangle_outline(x + 10 * size, y + 20 * size, 20 * size, 40 * size, (255, 255, 255), 4, 0)
    arcade.draw_xywh_rectangle_filled(x, y, 20 * size, 40 * size / 4, (0, 255, 0))
    arcade.draw_xywh_rectangle_filled(x, y + 40 * size / 4, 20 * size, 40 * size / 4 * 3, (0, 255, 255))
    arcade.draw_circle_outline(x + 10 * size, y + 40 * size - 10 * size, 3.75 * size, (255, 0, 0), bw)
    arcade.draw_line(x + 10 * size, y + 40 * size - 10 * size - 3.75 * size, x + 10 * size,
                     y + 40 * size - 20 * size - 3.75 * size, (255, 0, 0), bw)
    arcade.draw_line(x + 10 * size, y + 40 * size - 20 * size - 3.75 * size, x + 5 * size,
                     y + 40 * size - 20 * size - 13 * size, (255, 0, 0), bw)
    arcade.draw_line(x + 10 * size, y + 40 * size - 20 * size - 3.75 * size, x + 15 * size,
                     y + 40 * size - 20 * size - 13 * size, (255, 0, 0), bw)
    arcade.draw_circle_filled(x + 8.5 * size, y + 40 * size - 9 * size, 0.7 * size, (255, 0, 0))
    arcade.draw_circle_filled(x + 11.5 * size, y + 40 * size - 9 * size, 0.7 * size, (255, 0, 0))
    arcade.draw_arc_outline(x + 10 * size, y + 40 * size - 10 * size, 2 * size, 2 * size, (255, 0, 0), 180, 360, bw)
    arcade.draw_arc_outline(x + 10 * size, y + 25 * size, 6 * size, 4 * size, (255, 0, 0), 180, 360, bw)


def DanielP2(x, y, size=2):
    import random, arcade
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    bw = int(0.75 * size)
    if (bw < 1):
        bw = 1
    arcade.draw_rectangle_outline(x + 10 * size, y + 20 * size, 20 * size, 40 * size, (255, 255, 255), 4, 0)
    arcade.draw_xywh_rectangle_filled(x, y, 20 * size, 40 * size / 4, (0, 255, 0))
    arcade.draw_xywh_rectangle_filled(x, y + 40 * size / 4, 20 * size, 40 * size / 4 * 3, (0, 255, 255))
    arcade.draw_circle_outline(x + 10 * size, y + 40 * size - 10 * size, 3.75 * size, color, bw)
    arcade.draw_line(x + 10 * size, y + 40 * size - 10 * size - 3.75 * size, x + 10 * size,
                     y + 40 * size - 20 * size - 3.75 * size, color, bw)
    arcade.draw_triangle_filled(x + 10 * size, y + 40 * size - 20 * size - 2 * size, x + 5 * size,
                                y + 40 * size - 20 * size - 9 * size, x + 15 * size,
                                y + 40 * size - 20 * size - 9 * size, color)
    arcade.draw_line(x + 7 * size, y + 40 * size - 20 * size - 9 * size, x + 7 * size,
                     y + 40 * size - 20 * size - 9 * size - 5 * size, color, bw)
    arcade.draw_line(x + 13 * size, y + 40 * size - 20 * size - 9 * size, x + 13 * size,
                     y + 40 * size - 20 * size - 9 * size - 5 * size, color, bw)
    arcade.draw_circle_filled(x + 8.5 * size, y + 40 * size - 9 * size, 0.7 * size, color)
    arcade.draw_circle_filled(x + 11.5 * size, y + 40 * size - 9 * size, 0.7 * size, color)
    arcade.draw_arc_outline(x + 10 * size, y + 40 * size - 10 * size, 2 * size, 2 * size, color, 180, 360, bw)
    arcade.draw_arc_outline(x + 10 * size, y + 18 * size, 6 * size, 4 * size, color, 0, 180, bw)


# import arcade
#
# arcade.open_window(400, 400, "test")
#
# while True:
#     arcade.start_render()
#
#     DanielP1(100, 200, 2)
#     DanielP2(300, 200, 2)
#
#     arcade.finish_render()
