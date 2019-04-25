import arcade

x = 0
y = 0

arcade.open_window(40, 80, "hyggefar")
arcade.set_background_color((255, 255, 255))

#legs
arcade.draw_rectangle_filled(x+12, y+14, x+6, y+28, (30, 30, 255))
arcade.draw_rectangle_filled(x+25, y+14, x+6, y+28, (30, 30, 255))

#body
arcade.draw_rectangle_filled(x+19, y+36, x+19, y+36, (30, 30, 255))

#arms
arcade.draw_rectangle_filled(x+6, y+51, x+6, y+6,(30,30,255))
arcade.draw_rectangle_filled(x+31, y+51, x+6, y+6,(30,30,255))

#neck
arcade.draw_rectangle_filled(x+19, y+57, x+8, y+6,(30,30,255))

#head
arcade.draw_rectangle_filled(x+19, y+66, x+12, y+16,(255,255,255))

arcade.finish_render()

arcade.run()