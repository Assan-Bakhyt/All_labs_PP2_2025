import pygame
from color_palette import *

pygame.init()

# Set up window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(colorWHITE)  # Background color

clock = pygame.time.Clock()
font = pygame.font.SysFont('None', 30)

# Drawing state
draw = False
radius = 5
color = 'blue'
mode = 'circle'
start_pos = (0, 0)
end_pos = (0, 0)

# ---------- DRAWING FUNCTIONS ----------
def drawCircle(surf, start, end, width, color):
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
    radius = abs(start[0] - end[0]) // 2
    pygame.draw.circle(surf, pygame.Color(color), center, radius, width)

def drawRectangle(surf, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(surf, pygame.Color(color), rect, width)

def eraseRect(surf, start, end):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(surf, colorWHITE, rect)

# ---------- MAIN LOOP ----------
running = True
while running:
    # Start from the base layer
    screen.blit(base_layer, (0, 0))

    # If drawing, render the figure temporarily for preview
    if draw:
        if mode == 'circle':
            drawCircle(screen, start_pos, end_pos, radius, color)
        elif mode == 'rectangle':
            drawRectangle(screen, start_pos, end_pos, radius, color)
        elif mode == 'erase':
            eraseRect(screen, start_pos, end_pos)

    # Show current color and mode
    pygame.draw.rect(screen, pygame.Color(color), (10, 10, 30, 30))
    color_label = font.render(f"Color: {color}", True, pygame.Color('black'))
    screen.blit(color_label, (50, 15))

    mode_label = font.render(f"Mode: {mode}", True, pygame.Color('black'))
    screen.blit(mode_label, (50, 45))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---------- KEY CONTROLS ----------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = 'red'
            elif event.key == pygame.K_g:
                color = 'green'
            elif event.key == pygame.K_b:
                color = 'blue'
            elif event.key == pygame.K_1:
                mode = 'circle'
            elif event.key == pygame.K_2:
                mode = 'rectangle'
            elif event.key == pygame.K_3:
                mode = 'erase'

        # ---------- MOUSE CONTROLS ----------
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            draw = True
            start_pos = event.pos
            end_pos = event.pos

        if event.type == pygame.MOUSEMOTION and draw:
            end_pos = event.pos  # Update end position in real-time

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and draw:
            end_pos = event.pos

            # Final drawing onto the base layer
            if mode == 'circle':
                drawCircle(base_layer, start_pos, end_pos, radius, color)
            elif mode == 'rectangle':
                drawRectangle(base_layer, start_pos, end_pos, radius, color)
            elif mode == 'erase':
                eraseRect(base_layer, start_pos, end_pos)

            draw = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
