import pygame

pygame.init()

w_size = (800,600)
screen = pygame.display.set_mode(w_size)

pygame.display.set_caption("Draw Circle")

ball_color = pygame.Color('red')
bg_color = pygame.Color('white')

ball_position = [400,300]
ball_radius = 25
speed = 20

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_position[1] = max(ball_position[1] - speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_position[1] = min(ball_position[1] + speed, w_size[1] - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_position[0] = max(ball_position[0] - speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_position[0] = min(ball_position[0] + speed, w_size[0] - ball_radius)

    screen.fill(bg_color)
    pygame.draw.circle(screen,ball_color,ball_position,ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(60)