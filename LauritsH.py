def LauritsHMan1(x, y):
    #Woman
    pointlist1 = {
        (x, y),
        (x+40, y),
        (x, y+80),
        (x+40, y+80)
    }
    arcade.draw_polygon_outline(pointlist1, arcade.color.ELECTRIC_CRIMSON)
    arcade.draw_circle_filled(x+20, y+67, 8, arcade.color.OLD_GOLD)

    pointlist4 = {
        (x+4, y+60),
        (x+2, y+35),
        (x+8, y+30)
    }

    #arcade.draw_polygon_filled(pointlist4, arcade.color.GOLDENROD)
    pointlist2 = {
        (x+11, y+32),
        (x+29, y+32),
        (x + 4, y + 60),
        (x + 36, y + 60)
    }
    arcade.draw_polygon_filled(pointlist2,arcade.color.ROYAL_PURPLE)

    arcade.draw_rectangle_filled(x+14, y+16, 5, 32, arcade.color.GOLDENROD)
    arcade.draw_rectangle_filled(x+26, y+16, 5, 32, arcade.color.GOLDENROD)
    #arcade.draw_rectangle_filled(x+20, y+27, 12, 10, arcade.color.GOLD)

    pointlist3 = {
        (x + 1, y + 1),
        (x + 39, y + 1),
        (x + 11, y + 32),
        (x + 29, y + 32),
        (x + 1, y + 1),

    }
    arcade.draw_polygon_filled(pointlist3, arcade.color.ROYAL_PURPLE)

def LauritsHMan2(x, y):
    #Man
    pointlist1 = {
        (x + 40, y),
        (x + 40, y + 80),
        (x, y + 80),
        (x, y),
    }
    arcade.draw_polygon_outline(pointlist1, arcade.color.ELECTRIC_CRIMSON)
    arcade.draw_circle_filled(x + 20, y + 67, 8, arcade.color.OLD_GOLD)
    arcade.draw_rectangle_filled(x+20, y+40, 4, 40, arcade.color.OLD_GOLD)
    arcade.draw_rectangle_filled(x+20, y+52, 40, 4, arcade.color.OLD_GOLD)
    arcade.draw_rectangle_filled(x+28, y+11, 4, 26, arcade.color.OLD_GOLD, 45)
    arcade.draw_rectangle_filled(x+12, y+11, 4, 26, arcade.color.OLD_GOLD, 315)

