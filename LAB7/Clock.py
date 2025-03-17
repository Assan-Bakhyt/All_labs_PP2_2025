import pygame 
import time
import math
pygame.init()


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


pygame.display.set_caption("Mickey clock`")


leftarm = pygame.image.load("Labs/LAB7/Images/min_hand.png")
rightarm = pygame.image.load("Labs/LAB7/Images/sec_hand.png")
mainclock = pygame.transform.scale(pygame.image.load("Labs/LAB7/Images/clock.png"), (800, 600))

running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    minute_angle = minute * 6   + (second / 60) * 6   
    second_angle = second * 6
    
    screen.blit(mainclock, (0,0))
    
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -second_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (800, 600)), -minute_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() 
    clock.tick(60) #fps
    
