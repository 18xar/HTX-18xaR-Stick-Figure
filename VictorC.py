import arcade


def VictorC(x, y):
    arcade.draw_circle_outline(x + 10 * 2, y + 30 * 2, 5 * 2, arcade.color.BLACK)  # head
    arcade.draw_line(x + 10 * 2, y + 25 * 2, x + 10 * 2, y + 12 * 2, arcade.color.BLACK, 1)  # body
    arcade.draw_line(x + 10 * 2, y + 12 * 2, x + 5 * 2, y + 2 * 2, arcade.color.BLACK)  # left leg
    arcade.draw_line(x + 10 * 2, y + 12 * 2, x + 15 * 2, y + 2 * 2, arcade.color.BLACK)  # right leg
    arcade.draw_line(x + 3 * 2, y + 20 * 2, x + 17 * 2, y + 20 * 2, arcade.color.BLACK)  # arms
    arcade.draw_circle_filled(x + 8 * 2, y + 31 * 2, 0.8 * 2, (0, 0, 255))  # Left eye
    arcade.draw_circle_filled(x + 12 * 2, y + 31 * 2, 0.8 * 2, (0, 0, 255))  # Right eye
