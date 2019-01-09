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
max_speed = 5
background_pos = 0,0

# Background
desert_background = 'desert'
background_one = Actor(desert_background)
background_two = Actor(desert_background)
background_three = Actor(desert_background)
backgrounds = [background_one, background_two, background_three]

# Arrow
circle_image = 'circle'
left_arrow_image = 'left-arrow'
right_arrow_image = 'right-arrow'
pointer = Actor(circle_image)
pointer.pos = center

# Set initial positions
for index in range(0, len(backgrounds) - 1):
    backgrounds[index].left = (index * WIDTH) - WIDTH
    
def draw():
    screen.fill((128, 0, 0))

    # move all backgrounds
    for background in backgrounds:
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
        
    # move all backgrounds
    min_x = WIDTH
    max_x = 0
    for background in backgrounds:
        background.left += -v_x
        min_x = min(background.left, min_x)
        max_x = max(background.right, max_x)
        
    # adjust
    for background in backgrounds:
        
        # move if needed
        if background.right < 0:
           # move two to right 
            background.left = max_x
        elif background.left > WIDTH:
            background.left = min_x - WIDTH
            
    