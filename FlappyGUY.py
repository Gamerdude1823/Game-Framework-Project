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
OBSTACLE_HEIGHT = random.randint(100 , 300)
OBSTACLE_GAP = 150
FPS = 30

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
obstacle_img = pygame.transform.scale(obstacle_img, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))


# Clock to control the frame rate
clock = pygame.time.Clock()

# Game variables
bird_y = HEIGHT // 2
bird_velocity = 0
obstacle_x = WIDTH
obstacle_passed = False
score = 0

# Menu variables
menu_font = pygame.font.Font(None, 50)
menu_text = menu_font.render("Press SPACE to Start", True, WHITE)
menu_text_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Function to reset the game state
def reset_game():
    global bird_y, bird_velocity, obstacle_x, obstacle_passed, score
    bird_y = HEIGHT // 2
    bird_velocity = 0
    obstacle_x = WIDTH
    obstacle_passed = False
    score = 0

bird_rect = pygame.Rect(50, bird_y, BIRD_SIZE, BIRD_SIZE)
obstacle_rect_top = pygame.Rect(obstacle_x, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
obstacle_rect_bottom = pygame.Rect(obstacle_x, OBSTACLE_HEIGHT + OBSTACLE_GAP, OBSTACLE_WIDTH, HEIGHT - OBSTACLE_HEIGHT - OBSTACLE_GAP)

# Function to display the menu
def show_menu():
    screen.blit(background_img, (0, 0))
    screen.blit(menu_text, menu_text_rect)
    pygame.display.flip()

# Function to handle events in the menu
def handle_menu_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return True
    return False

# Function to handle events in the game
def handle_game_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if bird_y > HEIGHT - BIRD_SIZE:
                return True
            elif bird_velocity == 0:
                bird_velocity = -JUMP_HEIGHT
    return False

# Menu loop
while True:
    if handle_menu_events():
        break
    show_menu()
    clock.tick(FPS)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    obstacle_x -= 5
    if obstacle_x < 0:
        obstacle_x = WIDTH + random.randint(50, 200)  # Randomize obstacle position when it goes off-screen
        obstacle_height = random.randint(100, 300)
        obstacle_passed = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if bird_y > HEIGHT - BIRD_SIZE:  # Allow jumping even if not on the ground
            reset_game()
        else:
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
        pygame.mixer.music.stop()
        time.sleep (2)
        reset_game()
        

    # Check for collisions with the obstacle
    bird_rect = pygame.Rect(50, bird_y, BIRD_SIZE, BIRD_SIZE)
    obstacle_rect_top = pygame.Rect(obstacle_x, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    obstacle_rect_bottom = pygame.Rect(obstacle_x, OBSTACLE_HEIGHT + OBSTACLE_GAP, OBSTACLE_WIDTH, HEIGHT - OBSTACLE_HEIGHT - OBSTACLE_GAP)

    if bird_rect.colliderect(obstacle_rect_top) or bird_rect.colliderect(obstacle_rect_bottom):
        pygame.display.set_caption('You Crashed! Game Over')
        pygame.mixer.music.stop()
        time.sleep(2)
        reset_game()

    # Check if the bird has passed the obstacle
    if obstacle_x < 50 < obstacle_x + OBSTACLE_WIDTH and not obstacle_passed:
        score += 1
        obstacle_passed = True

    # Draw background
    screen.blit(background_img, (0, 0))

    # Draw bird
    screen.blit(bird_img, (50, bird_y))

    # Draw obstacle
    screen.blit(obstacle_img, (obstacle_x, 0))
    screen.blit(obstacle_img, (obstacle_x, OBSTACLE_HEIGHT + OBSTACLE_GAP))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)   

