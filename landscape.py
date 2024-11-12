# Compound shapes and simple animation

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_x = 100
cloud_y = 110
cloud_z = 90
cloud_w = 80
cloud_v = 70
ground_height = 100
CLOUD_COLOR = (255,255,255)
SKY_COLOR = (27,224,221)
ROOF_COLOR = (139, 69, 19)
HOUSE_COLOR = (255, 0, 0)
WINDOW_COLOR = (0, 0, 255)
DOOR_COLOR = (0, 128, 0)
TRUNK_COLOR = (139, 69, 19)
LEAVES_COLOR = (34, 139, 34)
GROUND_COLOR = (0, 255, 0)
PANEL_COLOR = (0,0,0)

# Initialize ticks
ticks = 0
invert_ticks = 30  # Number of ticks before inversion
inversion_duration = 30  # Duration of inversion in ticks 
inverted = False
inversion_start_tick = 0

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # Update the tick count
    ticks += 1

    cloud_x += 10
    if cloud_x > WIDTH + 100:
        cloud_x = -100

    cloud_y += 10
    if cloud_y > WIDTH + 100:
        cloud_y = -100

    cloud_z += 10
    if cloud_z > WIDTH + 100:
        cloud_z = -100

    cloud_w += 10
    if cloud_w > WIDTH + 100:
        cloud_w = -100

    cloud_v += 10
    if cloud_v > WIDTH + 100:
        cloud_v = -100

    # DRAWING
    screen.fill(SKY_COLOR)  # always the first drawing command

    #Ground
    pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - ground_height, WIDTH, ground_height))

    # Draw the house body
    pygame.draw.rect(screen, HOUSE_COLOR, (300, 255, 200, 200))

    # Draw the roof
    pygame.draw.polygon(screen, ROOF_COLOR, [(270, 255), (525, 255), (400, 155)])

    # Draw the door
    pygame.draw.rect(screen, DOOR_COLOR, (370, 355, 60, 100))

    # Draw windows
    pygame.draw.rect(screen, WINDOW_COLOR, (320, 305, 50, 50))
    pygame.draw.rect(screen, WINDOW_COLOR, (430, 305, 50, 50))

    # Draw window panels
    pygame.draw.line(screen, PANEL_COLOR, (345, 305), (345, 355), 5)  # Vertical line for left window
    pygame.draw.line(screen, PANEL_COLOR, (320, 330), (370, 330), 5)  # Horizontal line for left window

    pygame.draw.line(screen, PANEL_COLOR, (455, 305), (455, 355), 5)  # Vertical line for right window
    pygame.draw.line(screen, PANEL_COLOR, (430, 330), (480, 330), 5)  # Horizontal line for right window

    #Clouds
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_x, 80), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_x + 34, 60), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_x + 45, 80), 30)

    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_y + 200, 80), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_y + 234, 60), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_y + 245, 80), 30)

    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_z - 200, 80), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_z - 166, 60), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_z - 155, 80), 30)

    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_w - 400, 80), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_w - 366, 60), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_w - 355, 80), 30)

    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_v - 600, 80), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_v - 566, 60), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (cloud_v - 555, 80), 30)

     # Draw trees
    # Tree 1
    pygame.draw.rect(screen, TRUNK_COLOR, (62, 409, 20, 45))  # trunk
    pygame.draw.circle(screen, LEAVES_COLOR, (72, 370), 40)  # leaves

    # Tree 2
    pygame.draw.rect(screen, TRUNK_COLOR, (174, 409, 20, 45))  # trunk
    pygame.draw.circle(screen, LEAVES_COLOR, (184, 370), 40)  # leaves

    # Tree 3
    pygame.draw.rect(screen, TRUNK_COLOR, (579, 409, 20, 50))  # trunk
    pygame.draw.circle(screen, LEAVES_COLOR, (589, 379), 40)  # leaves
    

    # Invert colors every invert_ticks, only if not currently inverted
    if ticks >= invert_ticks and not inverted:
        inverted = True
        inversion_start_tick = ticks

    # Check if the inversion duration has elapsed
    if inverted and ticks - inversion_start_tick >= inversion_duration:
        inverted = False
        ticks = 0  # Reset ticks for the next inversion

    # Determine colors based on inversion status
    if inverted:
        cloud_color = (0, 0, 0)
        sky_color = (228, 31, 34)
        roof_color = (116, 186, 236)
        house_color = (0, 255, 255)
        window_color = (255, 0, 0)
        door_color = (255, 127, 255)
        trunk_color = (116, 186, 236)
        leaves_color = (221, 116, 221)
        ground_color = (255, 0, 255)
        panel_color = (255, 255, 255)
    else:
        cloud_color = CLOUD_COLOR
        sky_color = SKY_COLOR
        roof_color = ROOF_COLOR
        house_color = HOUSE_COLOR
        window_color = WINDOW_COLOR
        door_color = DOOR_COLOR
        trunk_color = TRUNK_COLOR
        leaves_color = LEAVES_COLOR
        ground_color = GROUND_COLOR
        panel_color = PANEL_COLOR

    #Redraw with inverted colors

    # DRAWING
    screen.fill(sky_color)  

    #Ground
    pygame.draw.rect(screen, ground_color, (0, HEIGHT - ground_height, WIDTH, ground_height))

    # Draw the house body
    pygame.draw.rect(screen, house_color, (300, 255, 200, 200))

    # Draw the roof
    pygame.draw.polygon(screen, roof_color, [(270, 255), (525, 255), (400, 155)])

    # Draw the door
    pygame.draw.rect(screen, door_color, (370, 355, 60, 100))

    # Draw windows
    pygame.draw.rect(screen, window_color, (320, 305, 50, 50))
    pygame.draw.rect(screen, window_color, (430, 305, 50, 50))

    # Draw window panels
    pygame.draw.line(screen, panel_color, (345, 305), (345, 355), 5)  
    pygame.draw.line(screen, panel_color, (320, 330), (370, 330), 5)  

    pygame.draw.line(screen, panel_color, (455, 305), (455, 355), 5)  
    pygame.draw.line(screen, panel_color, (430, 330), (480, 330), 5)  

    #Clouds
    pygame.draw.circle(screen, cloud_color, (cloud_x, 80), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 34, 60), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 45, 80), 30)

    pygame.draw.circle(screen, cloud_color, (cloud_y + 200, 80), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_y + 234, 60), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_y + 245, 80), 30)

    pygame.draw.circle(screen, cloud_color, (cloud_z - 200, 80), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_z - 166, 60), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_z - 155, 80), 30)

    pygame.draw.circle(screen, cloud_color, (cloud_w - 400, 80), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_w - 366, 60), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_w - 355, 80), 30)

    pygame.draw.circle(screen, cloud_color, (cloud_v - 600, 80), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_v - 566, 60), 30)
    pygame.draw.circle(screen, cloud_color, (cloud_v - 555, 80), 30)

     # Draw trees
    # Tree 1
    pygame.draw.rect(screen, trunk_color, (62, 409, 20, 45))  # trunk
    pygame.draw.circle(screen, leaves_color, (72, 370), 40)  # leaves

    # Tree 2
    pygame.draw.rect(screen, trunk_color, (174, 409, 20, 45))  # trunk
    pygame.draw.circle(screen, leaves_color, (184, 370), 40)  # leaves

    # Tree 3
    pygame.draw.rect(screen, trunk_color, (579, 409, 20, 50))  # trunk
    pygame.draw.circle(screen, leaves_color, (589, 379), 40)  # leaves

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
