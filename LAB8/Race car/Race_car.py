import pygame, random, time
from pygame.locals import K_LEFT, K_RIGHT

# initilizes pygame sub-modules
pygame.init()
pygame.mixer.init()

# Screen settings
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race car")

# FPS
FPS = 60
clock = pygame.time.Clock()

# Upload resources 
image_background = pygame.image.load('Labs/LAB8/Race car/resources/road_0.png')
image_background = pygame.transform.scale(image_background, (WIDTH, HEIGHT))

# coin
image_coin = pygame.image.load('Labs/LAB8/Race car/resources/coin.png')
image_coin = pygame.transform.scale(image_coin, (30, 30))

# background music
pygame.mixer.music.load('Labs/LAB8/Race car/resources/background.wav')
pygame.mixer.music.play(-1)
sound_crash = pygame.mixer.Sound('Labs/LAB8/Race car/resources/car-crash_A_minor.wav')

# Font
font_big = pygame.font.SysFont("Verdana", 60)
image_game_over = font_big.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

SPEED = 5

# Game Objects
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Labs/LAB8/Race car/resources/Enemy.png')
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), -100))
        self.speed = 8

    def move(self):
        self.rect.move_ip(0, self.speed)  # move in place(x,y)
        if self.rect.top > HEIGHT:
            self.kill()  # delete enemy 


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Labs/LAB8/Race car/resources/Player.png')
        self.rect = self.image.get_rect(center=(WIDTH // 2, 500))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect(center=(random.randint(30, WIDTH - 30), -50))
        self.speed = 4

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.kill()


# Функция одной игровой сессии
def run_game():
    player = Player()

    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    coin_sprites = pygame.sprite.Group()

    # Enemy spawn
    enemy_spawn_delay = 60
    enemy_spawn_timer = 0

    # Other details
    road_y1 = 0
    road_y2 = -HEIGHT
    score = 0
    coins_collected = 0
    coins_spawn_timer = 0
    coins_spawn_delay = 120  # раз в 1.5 секунды 

    global SPEED
    SPEED = 5

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # road movement
        road_y1 += SPEED
        road_y2 += SPEED
        if road_y1 >= HEIGHT:
            road_y1 = -HEIGHT
        if road_y2 >= HEIGHT:
            road_y2 = -HEIGHT

        screen.blit(image_background, (0, road_y1))
        screen.blit(image_background, (0, road_y2))

        # player movement 
        player.move()
        screen.blit(player.image, player.rect)

        # enemy spawn
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= enemy_spawn_delay:
            enemy_spawn_timer = 0
            new_enemy = Enemy()
            all_sprites.add(new_enemy)
            enemy_sprites.add(new_enemy)

        # coin spawn
        coins_spawn_timer += 1
        if coins_spawn_timer >= coins_spawn_delay:
            coins_spawn_timer = 0
            new_coin = Coin()
            all_sprites.add(new_coin)
            coin_sprites.add(new_coin)

        for entity in all_sprites:
            entity.move()
            screen.blit(entity.image, entity.rect)

        score += 1
        if score % 300 == 0:
            SPEED += 0.5

        # Coin collection
        coins_got = pygame.sprite.spritecollide(player, coin_sprites, True)
        coins_collected += len(coins_got)

        coin_text = font_big.render(str(coins_collected), True, 'white')
        screen.blit(coin_text, (10, 10))

        # Collision with enemy
        if pygame.sprite.spritecollideany(player, enemy_sprites):
            sound_crash.play()
            time.sleep(1)

            running = False
            screen.fill("red")
            screen.blit(image_game_over, image_game_over_rect)
            pygame.display.flip()

            time.sleep(2)  

        pygame.display.flip()


# Game loop - auto restart game after collisions
while True:
    run_game()
