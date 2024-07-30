import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Life & Death Animation")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define the circle properties
x, y = width // 2, height // 2
radius = 0
max_radius = 100
growth_speed = 2
shrinking = False

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    window.fill(white)

    # Draw the circle
    pygame.draw.circle(window, black, (x, y), radius)

    # Update the circle's radius
    if not shrinking:
        radius += growth_speed
        if radius >= max_radius:
            shrinking = True
    else:
        radius -= growth_speed
        if radius <= 0:
            shrinking = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
