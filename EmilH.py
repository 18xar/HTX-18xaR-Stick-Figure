


def EmilH(X, Y):
	import arcade
	bWidth = 60
	bHeight = 120
	headreadius = 10
	bodylength = 25

	headCenterY = Y+bHeight/2-headreadius*2 - (bHeight/10)
	bodyCenter = headCenterY-headreadius-(bodylength/2)
	legLength = 7
	bodyBottom = bodyCenter - bodylength/2


	# background
	arcade.draw_rectangle_filled(X, Y, bWidth, bHeight, arcade.color.BLUE)
	#head
	arcade.draw_circle_outline(X, headCenterY, headreadius, arcade.color.BLACK)
	#face
	arcade.draw_point(X-headreadius/2, headCenterY + (headreadius/4), arcade.color.BLACK, 2)
	arcade.draw_point(X + headreadius/2, headCenterY + (headreadius/4), arcade.color.BLACK, 2)
	#mouth
	arcade.draw_arc_outline(X, headCenterY-headreadius/2, headreadius-(headreadius/2), headreadius-headreadius/2, arcade.color.BLACK, 0,180)
	#hat
	arcade.draw_line(X-headreadius*2, headCenterY+headreadius, X+headreadius*2, headCenterY+headreadius, arcade.color.BLACK)
	arcade.draw_rectangle_filled(X, headCenterY+headreadius+headreadius/4, headreadius*3, headreadius/2, arcade.color.BLACK)

	# body
	arcade.draw_rectangle_filled(X,headCenterY-headreadius-(bodylength/2), 2, bodylength, arcade.color.BLACK)
	#arms
	arcade.draw_rectangle_filled(X,headCenterY-headreadius-(bodylength/2),bodylength,2, arcade.color.BLACK)
	#legs
	arcade.draw_line(X, bodyBottom, X-legLength, bodyCenter-bodylength/2 - legLength*2, arcade.color.BLACK)
	arcade.draw_line(X, bodyBottom, X+legLength, bodyCenter-bodylength/2 - legLength*2, arcade.color.BLACK)