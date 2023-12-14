import pygame
import time
import sys
import random

# Initialize Pygame
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("F:\Game Framework Project\sound\Thirst - (Wanna Sprite Cranberry Trap Remix) [Prod. Ranch] (Free Use).mp3") 
pygame.mixer.music.play(-1,0.0)

# Constants
WIDTH, HEIGHT = 600, 400
BIRD_SIZE = 40
GRAVITY = 0.5
JUMP_HEIGHT = 10
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = random.randint(100, 300)
OBSTACLE_GAP = 150
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 139, 71)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wanna Sprite Cranberry?")

# Load bird image
bird_img = pygame.image.load("F:\Game Framework Project\images\Sprite Cranberry Game - Lebron Icon.png")
bird_img = pygame.transform.scale(bird_img, (BIRD_SIZE, BIRD_SIZE))

# Load background image
background_img = pygame.image.load("F:\Game Framework Project\images\Sprite Cranberry Game - Background Image.jpg ")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Load obstacle images
obstacle_img = pygame.image.load("F:\Game Framework Project\images\Sprite Cranberry Game - Obstacle Image.png")
obstacle_img = pygame.transform.scale(obstacle_img, (WIDTH, HEIGHT))


# Clock to control the frame rate
clock = pygame.time.Clock()

# Game variables
bird_y = HEIGHT // 2
bird_velocity = 0
obstacle_x = WIDTH
obstacle_passed = False
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -JUMP_HEIGHT

    # Update bird position and velocity
    bird_y += bird_velocity
    bird_velocity += GRAVITY

    # Update obstacle position
    obstacle_x -= 5
    if obstacle_x < 0:
        obstacle_x = WIDTH
        obstacle_height = random.randint(100, 300)
        obstacle_passed = False

    # Check for collisions with the ground or ceiling
    if bird_y > HEIGHT - BIRD_SIZE or bird_y < 0:
        pygame.display.set_caption('You Crashed! Game Over')
        pygame.mixer.music.stop
        time.sleep (5)
        pygame.quit()
        sys.exit()

    # Check for collisions with the obstacle
    if obstacle_x < BIRD_SIZE < obstacle_x + OBSTACLE_WIDTH:
        if bird_y < OBSTACLE_HEIGHT or bird_y > OBSTACLE_HEIGHT + OBSTACLE_GAP:
            pygame.display.set_caption('You Crashed! Game Over')
            pygame.mixer.music.stop
            time.sleep (5)
            pygame.quit()
            sys.exit()

    # Check if the bird has passed the obstacle
    if obstacle_x + OBSTACLE_WIDTH < BIRD_SIZE and not obstacle_passed:
        score += 1
        obstacle_passed = True

    # Draw background
    screen.blit(background_img, (0, 0))

    # Draw bird
    screen.blit(bird_img, (50, bird_y))

    # Draw obstacle
    pygame.draw.rect(screen, GREEN, (obstacle_x, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    pygame.draw.rect(screen, GREEN, (obstacle_x, OBSTACLE_HEIGHT + OBSTACLE_GAP, OBSTACLE_WIDTH, HEIGHT))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)
