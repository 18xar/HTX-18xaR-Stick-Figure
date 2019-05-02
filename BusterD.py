def BusterD(x, y):
    # baggrund
    arcade.draw_rectangle_filled(10 * 2 + x, 20 * 2 + y, 20 * 2, 40 * 2, (102, 204, 255))
    # Hoved
    arcade.draw_circle_filled(10 * 2 + x, 30 * 2 + y, 5 * 2, (255, 204, 102))
    # Arme
    arcade.draw_line(7 + x, 45 + y, 2 * 17 + x, 45 + y, (0, 0, 0))
    # mave
    arcade.draw_ellipse_filled(20 + x, 35 + y, 8.5, 15, (255, 0, 0))
    # mund
    arcade.draw_arc_outline(20 + x, 60 + y, 5, 5, (0, 0, 0), 180, 360)
    # skæg
    arcade.draw_circle_filled(13 + x, 53 + y, 2, (255, 255, 255))
    arcade.draw_circle_filled(16 + x, 55 + y, 2, (255, 255, 255))
    arcade.draw_circle_filled(19 + x, 53 + y, 2, (255, 255, 255))
    arcade.draw_circle_filled(22 + x, 55 + y, 2, (255, 255, 255))
    arcade.draw_circle_filled(25 + x, 53 + y, 2, (255, 255, 255))
    arcade.draw_circle_filled(16 + x, 51 + y, 2, (255, 255, 255))
    arcade.draw_circle_filled(22 + x, 51 + y, 2, (255, 255, 255))
    arcade.draw_circle_filled(19 + x, 48 + y, 3, (255, 255, 255))
    arcade.draw_circle_filled(16 + x, 49 + y, 2, (255, 255, 255))
    arcade.draw_circle_filled(22 + x, 49 + y, 2, (255, 255, 255))
    # Krop
    # arcade.draw_line(2*10+x,2*25+y,2*10+x,2*10+y,(0,0,0))
    # Guld knapper
    arcade.draw_circle_filled(20 + x, 25 + y, 2, (255, 204, 0))
    arcade.draw_circle_filled(20 + x, 33 + y, 2, (255, 204, 0))
    arcade.draw_circle_filled(20 + x, 41 + y, 2, (255, 204, 0))
    # Ben
    arcade.draw_line(2 * 10 + x, 2 * 10 + y, 2 * 5 + x, 2 * 5 + y, (255, 0, 0), 5)
    arcade.draw_line(10 * 2 + x, 10 * 2 + y, 15 * 2 + x, 5 * 2 + y, (255, 0, 0), 5)
    # Hat
    arcade.draw_triangle_filled(20 + x, 80 + y, 10 + x, 65 + y, 30 + x, 65 + y, (255, 0, 0))

    # øjne
    arcade.draw_circle_filled(17 + x, 63 + y, 1, (0, 0, 0))
    arcade.draw_circle_filled(23 + x, 63 + y, 1, (0, 0, 0))
    # fødder
    arcade.draw_line(2 * 5 + x, 2 * 5 + y, 3 + x, 13 + y, (102, 51, 0), 2)
    arcade.draw_line(15 * 2 + x, 5 * 2 + y, 37 + x, 13 + y, (102, 51, 0), 2)
    # dutpåhat
    arcade.draw_circle_filled(20 + x, 78 + y, 2, (255, 255, 255))
