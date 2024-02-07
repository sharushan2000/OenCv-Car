import pygame
import os
import random

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 400, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enemy Dodger")

# Load and transform road image
ROAD_IMAGE = pygame.image.load(os.path.join('assets', 'road.png'))
ROTATE_ROAD = pygame.transform.rotate(ROAD_IMAGE, 90)
SCALE_ROAD = pygame.transform.scale(ROTATE_ROAD, (WIDTH, HEIGHT))

ENEMY_VEL = 5  # Adjusted for a reasonable speed
CLOCK = pygame.time.Clock()

PLAYER = pygame.Rect(200, 750, 25, 25)

def draw_window(player_rect, enemy_list):
    WINDOW.blit(SCALE_ROAD, (0, 0))
    pygame.draw.rect(WINDOW, (255, 0, 0), player_rect)  # Red for player
    for enemy in enemy_list:
        pygame.draw.rect(WINDOW, (0, 0, 255), enemy)  # Blue for enemies
    pygame.display.update()

def create_enemy(enemy_list):
    enemy_x_positions = [50, 175, 350]
    while len(enemy_list) < 3:
        x_pos = random.choice(enemy_x_positions)
        y_pos = random.randint(-50, -10)
        enemy_rect = pygame.Rect(x_pos, y_pos, 25, 75)
        enemy_list.append(enemy_rect)

def move_enemies(enemy_list):
    for enemy in enemy_list:
        enemy.y += ENEMY_VEL
        if enemy.y > HEIGHT:
            enemy_list.remove(enemy)

def check_collisions(player_rect, enemy_list):
    for enemy in enemy_list:
        if player_rect.colliderect(enemy):
            return True  # Collision detected
    return False  # No collision

def main():
    running = True
    enemy_list = []
    create_enemy(enemy_list)

    while running:
        CLOCK.tick(60)  # Adjust for smoother gameplay
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        PLAYER.x = mouse_x - PLAYER.width // 2
        PLAYER.y = mouse_y - PLAYER.height // 2
        PLAYER.x = max(0, min(WIDTH - PLAYER.width, PLAYER.x))
        PLAYER.y = max(0, min(HEIGHT - PLAYER.height, PLAYER.y))

        move_enemies(enemy_list)
        if len(enemy_list) < 3:
            create_enemy(enemy_list)

        if check_collisions(PLAYER, enemy_list):
            print("Collision detected! Game over.")
            running = False  # End the game on collision

        draw_window(PLAYER, enemy_list)

    pygame.quit()

if __name__ == "__main__":
    main()
