#import pgzrun

# Write your code here :-)
WIDTH = 640
HEIGHT = 384

# General
center = WIDTH / 2, HEIGHT / 2
v_x = 0
max_speed = 5
background_pos = 0, 0

# images
bunny_ready = 'ready'
bunny_stand = 'stand'
walk_left_1 = 'walk_left_1'
walk_left_2 = 'walk_left_2'
walk_right_1 = 'walk_right_1'
walk_right_2 = 'walk_right_2'

# time
current_time = 0.0
current_animation_time = 0.0
animation_loop_time = 0.2

#animations    
animation_frame_index = 0
walking_left = [walk_left_1, walk_left_2]
walking_right = [walk_right_1, walk_right_2]

# actors
bunny = Actor(bunny_ready)
bunny.pos = center

def draw():
    screen.fill((128, 0, 0))
    bunny.draw()    
        
def update(timeDelta):
    global current_time, animation_frame_index, current_animation_time, animation_loop_time

    current_time += timeDelta    
    
    if keyboard.left:
        
        # holding left key so animate right        
        current_animation_time += timeDelta
        if current_animation_time >= animation_loop_time:
            current_animation_time = 0.0
            animation_frame_index = (animation_frame_index + 1) % len(walking_left)
        
        bunny.image = walking_left[animation_frame_index]

    elif keyboard.right:
                   
        # holding right key so animate right        
        current_animation_time += timeDelta
        if current_animation_time >= animation_loop_time:
            current_animation_time = 0.0
            animation_frame_index = (animation_frame_index + 1) % len(walking_right)        
            
        bunny.image = walking_right[animation_frame_index]

    else:
        # reset
        animation_frame_index = 0
        current_animation_time = 0.0
        bunny.image = bunny_stand                            
    
#pgzrun.go()