from pico2d import *
import math

open_canvas()

grass = load_image("grass.png")
character = load_image("character.png")

x = 0
y = 90

dir = 'right'
offset =0 
radius = 4

move_rect = False
start_move = False

character.draw_now(0,90)

while(True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if ( move_rect):
       if (dir == 'right' ):
           x = x+2
           if ( x >= 700 ):
              dir = 'up'

       elif (dir == 'up'):
          y= y+2
          if ( y >= 500 ):
             dir = 'left'
       elif (dir == 'left'):
          x= x-2
          if ( x <= 100):
             dir = 'down'
       elif ( dir == 'down'):
          y= y-2
          if ( y <=90 ):
             dir = 'right'
             move_rect = False

    else:
        # Move_circle
        start_pos = 400
        if ( x < start_pos and not start_move) :
            x = x +2
            if ( x >= start_pos ):
                start_move = True 

        else:   
            offset = offset +1
            theta_x  =radius * math.cos( 2*(offset)/360*math.pi)
            theta_Y = radius * math.sin( 2*(offset)/360*math.pi)
            x= x + theta_x
            y= y + theta_Y

            if ( offset == 360 ):
               start_move = False
               move_rect = True
               offset = 0

    #delay(0.01)

close_canvas()