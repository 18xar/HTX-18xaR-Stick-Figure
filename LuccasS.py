import arcade

def LuccasS1(x, y):

    # Draw background
    arcade.draw_rectangle_filled(x + 20, y + 40, 40, 80, (255, 255, 255))

    # Draw sky and grass
    arcade.draw_rectangle_filled(x + 20, y + 75, 40, 10, (0, 100, 150))
    arcade.draw_rectangle_filled(x + 20, y + 10, 40, 20, (0, 100, 0))

    # Draw stick figure
    # Draw head
    arcade.draw_circle_outline(x + 20, y + 60, 7, (0, 0, 0))
    arcade.draw_circle_filled(x + 17, y + 62, 1, (0, 0, 0))
    arcade.draw_circle_filled(x + 23, y + 62, 1, (0, 0, 0))
    arcade.draw_arc_outline(x + 20, y + 59, 3, 2, (0, 0, 0), 190, 350, 1)

    # Draw arms
    arcade.draw_arc_outline(x + 20, y + 52, 10, 7, (0, 0, 0), 190, 350, 1)

    # Draw body
    arcade.draw_line(x + 20, y + 53, x + 20, y + 35, (0, 0, 0))

    # Draw legs
    arcade.draw_line(x + 20, y + 35, x + 15, y + 15, (0, 0, 0))
    arcade.draw_line(x + 20, y + 35, x + 25, y + 15, (0, 0, 0))

    # Draw hat
    arcade.draw_triangle_filled(x + 12, y + 64, x + 20, y + 75, x + 28, y + 64, (200, 0, 0))


def LuccasS2(x, y):

    # Draw background
    arcade.draw_rectangle_filled(x + 20, y + 40, 40, 80, (255, 255, 255))

    # Draw sky and grass
    arcade.draw_rectangle_filled(x + 20, y + 75, 40, 10, (0, 100, 150))
    arcade.draw_rectangle_filled(x + 20, y + 10, 40, 20, (0, 100, 0))

    # Draw stick figure
    # Draw head
    arcade.draw_circle_outline(x + 20, y + 60, 7, (0, 0, 0))
    arcade.draw_circle_filled(x + 17, y + 62, 1, (0, 0, 0))
    arcade.draw_circle_filled(x + 23, y + 62, 1, (0, 0, 0))
    arcade.draw_arc_outline(x + 20, y + 59, 3, 2, (0, 0, 0), 190, 350, 1)

    # Draw arms
    arcade.draw_arc_outline(x + 20, y + 40, 10, -7, (0, 0, 0), 190, 350, 1)

    # Draw body
    arcade.draw_line(x + 20, y + 53, x + 20, y + 35, (0, 0, 0))

    # Draw legs
    arcade.draw_line(x + 20, y + 35, x + 15, y + 15, (0, 0, 0))
    arcade.draw_line(x + 20, y + 35, x + 25, y + 15, (0, 0, 0))

    # Draw dress
    arcade.draw_triangle_filled(x + 10, y + 22, x + 20, y + 43, x + 30, y + 22, (200, 0, 100))

