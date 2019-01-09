# Suggestions
#
# - You don't need left and right icons and images; make everything that has a direction 'point' in the same direction and 
# use image or sprite functions to 'flip' them when needed
# - Holding down and key is different than pressing and releasing a key; think about that for animation - maybe your character is 'running left' while holding down the left key; but pressing and releasing the SPACE key fires a rocket
# Think about how you want to handle events such as pressing and release a key or holding it down
# Write your code here :-)

import pygame
WIDTH = 800
HEIGHT = 600

center = WIDTH / 2, HEIGHT / 2
circle_image = 'circle'
left_arrow_image = 'left-arrow'
right_arrow_image = 'right-arrow'
current_actor = Actor(circle_image)
current_actor.pos = center


def draw():
    screen.fill((128, 0, 0))
    current_actor.draw()
    
def update():
    
    if keyboard.left:
        current_actor.image = left_arrow_image
    elif keyboard.right:
        current_actor.image = right_arrow_image
    else:
        current_actor.image = circle_image
