import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
SPEED = 1

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a rectangle
rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    # Move the rectangle
    if keys[pygame.K_w]:
        rect.move_ip(0, -SPEED)
    if keys[pygame.K_a]:
        rect.move_ip(-SPEED, 0)
    if keys[pygame.K_s]:
        rect.move_ip(0, SPEED)
    if keys[pygame.K_d]:
        rect.move_ip(SPEED, 0)

    # Check if no keys are pressed
    if not any(keys):
        rect.center = (WIDTH // 2, HEIGHT // 2)

    # Make sure the rectangle does not go off-screen
    rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the rectangle
    pygame.draw.rect(screen, (255, 255, 255), rect)

    # Flip the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
