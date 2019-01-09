# Write your code here :-)
# You have choices.  
# - Is this infinite scroll or a 'level' with a fixed number of screens
# - I will show you inifinite scroll and also give you code for a fixed number of screens for a 'level' 
# - Its best to use images that are designed to 'overlap' at each edges so there are no seams when you move the the image tiles around
WIDTH = 640
HEIGHT = 384

# General
center = WIDTH / 2, HEIGHT / 2
v_x = 0
max_speed = 10
background_pos = 0,0

# Background
desert_background = 'desert'
background = Actor(desert_background)

# Arrow
circle_image = 'circle'
left_arrow_image = 'left-arrow'
right_arrow_image = 'right-arrow'
pointer = Actor(circle_image)
pointer.pos = center

def draw():
    screen.fill((128, 0, 0))
    background.draw()    
    pointer.draw()

def update():
    
    if keyboard.left:
        v_x = -max_speed
        pointer.image = left_arrow_image

    elif keyboard.right:
        v_x = max_speed
        pointer.image = right_arrow_image

    else:
        v_x = 0
        pointer.image = circle_image
        
    # simple movement
    background.left += -v_x