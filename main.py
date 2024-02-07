import pygame
import os
import random

WIDTH,HEIGHT = 500,800
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))


ROAD_IMAGE = pygame.image.load(os.path.join('assets','road.png'))
ROTATE_ROAD  = pygame.transform.rotate(ROAD_IMAGE,90)
SCALE_ROAD = pygame.transform.scale(ROTATE_ROAD,((WIDTH,HEIGHT)))
print(ROAD_IMAGE)

ENEMY_VEl = 100

Clock = pygame.time.Clock()

PLAYER = pygame.Rect(200,750,25,25)

def draw():
    pygame.draw.rect(WINDOW,'red',PLAYER,0)
  
def create_enemy(enemey_lyst):

    ennemy_x = [50,250,450,30,223,200,450 ]
    if len(enemey_lyst) < 3 :
        for i in range (3):
            ene_rect = pygame.Rect(ennemy_x[i],random.randint(10 ,50)*-1 ,25,75)
            enemey_lyst.append(ene_rect)
            
    return enemey_lyst
    
def enemey_draw(enemy_lyst):
    
    for ene in enemy_lyst:
        pygame.draw.rect(WINDOW,'blue',ene,0)
    

def main():
    runnig = True
    enemey_lyst = []
    enemey_lyst = create_enemy(enemey_lyst)
    ennemy_x = [50,250,450 ]


    



    while runnig:
        Clock.tick(10)
        
        if len(enemey_lyst) < 3 :
            enemey_lyst.append(pygame.Rect(random.choice(ennemy_x),random.randint(10,50)*-1,25,75))
            


        
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
        enemey_draw(enemey_lyst)
        for index,ene in enumerate (enemey_lyst):
            ene.y += ENEMY_VEl
            if ene.y > 800 :
                enemey_lyst.remove(ene)
                
         
 
                
        print(enemey_lyst)
                
        pygame.display.update()

if __name__ == "__main__":
    main()