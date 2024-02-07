import pygame
import os


WIDTH,HEIGHT = 500,800
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))


ROAD_IMAGE = pygame.image.load(os.path.join('assets','road.png'))
ROTATE_ROAD  = pygame.transform.rotate(ROAD_IMAGE,90)
SCALE_ROAD = pygame.transform.scale(ROTATE_ROAD,((WIDTH,HEIGHT)))
print(ROAD_IMAGE)


PLAYER = pygame.Rect(200,750,25,25)

def draw():
    pygame.draw.rect(WINDOW,'red',PLAYER,0)
    
def enemey():
    pass

def main():
    runnig = True

    while runnig:
        
        WINDOW.blit(SCALE_ROAD,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnig = False

        
    
        pos = pygame.mouse.get_pos()
        
        
        PLAYER.x = pos[0]
        PLAYER.y = pos[1]
        
        if PLAYER.x > 475:
            PLAYER.x = 475
            
        if PLAYER.y > 775 :
            PLAYER.y = 775
        draw()
        pygame.display.update()

if __name__ == "__main__":
    main()