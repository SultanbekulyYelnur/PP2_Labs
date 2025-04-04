import pygame, sys, random, time

# Инициализация Pygame
pygame.init()

# Частота кадров
FPS = 60
clock = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

# Размеры экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Game")

# Шрифт
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# Переменные игры
speed = 5
score = 0
coins_collected = 0

# Фон
background = pygame.image.load("lab_8/material/AnimatedStreet.png")

# Игрок (машина)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab_8/material/Player.png")
        self.rect = self.image.get_rect(center=(160, 520))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

# Враг (другая машина)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab_8/material/Enemy.png")
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), 0))

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

# Монета
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab_8/material/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        # Спавним в нижней части экрана, там, где ездит машина
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(400, 550))

# Создание объектов
player = Player()
enemy = Enemy()
coin = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)
all_sprites = pygame.sprite.Group(player, enemy, coin)

# Цикл игры
running = True
while running:
    screen.blit(background, (0, 0))

    # Отображение счёта
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    coins_text = font_small.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(coins_text, (WIDTH - 100, 10))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение
    player.move()
    enemy.move()

    # Отображение всех объектов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Проверка на столкновение с монетой
    if pygame.sprite.spritecollideany(player, coins):
        coins_collected += 1
        coin.respawn()

        # Каждые 5 монет — увеличиваем скорость
        if coins_collected % 5 == 0:
            speed += 1

    # Проверка на аварию
    if pygame.sprite.spritecollideany(player, enemies):
        crash_sound = pygame.mixer.Sound("lab_8/material/crash.wav")
        crash_sound.play()
        time.sleep(1)

        screen.fill(RED)
        game_over_text = font_big.render("Game Over", True, BLACK)
        screen.blit(game_over_text, (30, 250))
        pygame.display.update()

        time.sleep(2)
        running = False

    pygame.display.update()
    clock.tick(FPS)

# Выход из игры
pygame.quit()
sys.exit()