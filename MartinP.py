import arcade
import random


def MartinP(x, y, arm=random.randint(0, 4)):
    arcade.draw_rectangle_filled(x + 10 * 2, y + 20 * 2, 20 * 2, 40 * 2, (50, 50, 255))  # baggrund
    arcade.draw_circle_filled(x + 10 * 2, y + 30 * 2, 10, arcade.color.BLACK)  # hoved
    arcade.draw_circle_outline(x + 8 * 2, y + 32 * 2, 1, (255, 0, 0))  # venstre øje
    arcade.draw_circle_outline(x + 12 * 2, y + 32 * 2, 1, (255, 0, 0))  # højre øje
    arcade.draw_line(x + 8 * 2, y + 28 * 2, x + 12 * 2, y + 28 * 2, arcade.color.WHITE)  # mund
    arcade.draw_line(x + 10 * 2, y + 25 * 2, x + 10 * 2, y + 10 * 2, arcade.color.BLACK)  # torso
    arcade.draw_line(x + 10 * 2, y + 10 * 2, x + 5 * 2, y + 0, arcade.color.BLACK)  # venstre ben
    arcade.draw_line(x + 10 * 2, y + 10 * 2, x + 15 * 2, y + 0, arcade.color.BLACK)  # højre ben

    if arm == 1:
        arcade.draw_line(x + 5 * 2, y + 17 * 2, x + 15 * 2, y + 17 * 2, arcade.color.BLACK)  # arme
    elif arm == 2:
        arcade.draw_line(x + 5 * 2, y + 22 * 2, x + 15 * 2, y + 12 * 2, arcade.color.BLACK)  # arme
    elif arm == 3:
        arcade.draw_line(x + 5 * 2, y + 12 * 2, x + 15 * 2, y + 22 * 2, arcade.color.BLACK)  # arme
    else:
        arcade.draw_line(x + 5 * 2, y + 17 * 2, x + 15 * 2, y + 17 * 2, arcade.color.BLACK)  # arme
