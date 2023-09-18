from pico2d import *
import math

open_canvas()

grass = load_image("grass.png")
character = load_image("character.png")

x = 0
y = 90
init_y = 90

character.draw_now(0,90)

move_rect = True

up_x = 700
up_y = 550
offset =0

r = 10

while(True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if ( move_rect):
        if ( x < up_x and y == init_y):
            x = x+2
        elif (x >= up_x and y < up_y):
            y= y+2
        elif ( y>= up_y and x >= 0):
            x = x-2
        elif ( y >= init_y ):
            y= y-2
            move_rect = False
    else:
        # Move_circle
        start_pos = 400
        if ( x < start_pos):
           x = x+2
        else:    
            offset = offset +10
            theta_x  =r * math.cos( offset/360 * math.pi)
            theta_y = r * math.sin(offset/360 * math.pi)
            x= x + theta_x
            y= y + theta_y
            if ( y== init_y ):
                move_rect = True

    delay(0.01)

close_canvas()
