import pygame
from random import randrange
import time

# Настройки игры
res = 800        # Размер окна (800x800 пикселей)
size = 50        # Размер одной клетки (сетка 16x16)

# Загрузка изображений и их масштабирование под сетку
apple_img = pygame.image.load('lab_8/material/apple.png')
apple_img = pygame.transform.scale(apple_img, (size, size))

banana_img = pygame.image.load('lab_8/material/banana.png')
banana_img = pygame.transform.scale(banana_img, (size, size))

snake_img = pygame.image.load('lab_8/material/snake.png')
snake_img = pygame.transform.scale(snake_img, (size, size))

# Функция генерации еды (чтобы она не появлялась на змейке)
def generate_food(snake):
    while True:
        food = randrange(0, res, size), randrange(0, res, size)
        if food not in snake:
            return food

# Инициализация змейки
x, y = randrange(0, res, size), randrange(0, res, size)  # Случайное начальное положение
snake = [(x, y)]  # Список координат тела змейки
length = 1        # Длина змейки

# Генерация яблока и банана
apple = generate_food(snake)
banana = generate_food(snake)

# Таймеры для исчезновения еды
apple_timer = pygame.time.get_ticks()
banana_timer = pygame.time.get_ticks()
food_lifetime = 5000  # Еда исчезает через 5 секунд (в миллисекундах)

# Направления движения (запрет на разворот)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
dx, dy = 0, 0  # Направление движения
fps = 8        # Начальная скорость

score = 0
level = 1

# Инициализация Pygame и создание окна
pygame.init()
sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()

# Шрифты
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)

# Главный игровой цикл
while True:
    sc.fill(pygame.Color('black'))  # Очистка экрана

    # Отрисовка тела змейки
    for i, j in snake:
        sc.blit(snake_img, (i, j))

    # Проверка, не исчезла ли еда (по таймеру)
    current_time = pygame.time.get_ticks()
    if current_time - apple_timer > food_lifetime:
        apple = generate_food(snake)
        apple_timer = current_time
    if current_time - banana_timer > food_lifetime:
        banana = generate_food(snake)
        banana_timer = current_time

    # Отрисовка еды (яблоко и банан)
    sc.blit(apple_img, apple)
    sc.blit(banana_img, banana)

    # Отображение счёта и уровня
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    render_level = font_level.render(f'LEVEL: {level}', 1, pygame.Color('cyan'))
    sc.blit(render_score, (5, 5))
    sc.blit(render_level, (5, 35))

    # Движение змейки
    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]  # Обрезаем хвост, чтобы сохранить нужную длину

    # Проверка на столкновение со стеной или с собой
    if x < 0 or x >= res or y < 0 or y >= res or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (res // 2 - 200, res // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    # Проверка: съедено ли яблоко
    if snake[-1] == apple:
        apple = generate_food(snake)
        apple_timer = pygame.time.get_ticks()
        length += 1
        score += 1

    # Проверка: съеден ли банан
    if snake[-1] == banana:
        banana = generate_food(snake)
        banana_timer = pygame.time.get_ticks()
        length += 2
        score += 2

    # Увеличение уровня и скорости каждые 5 очков
    if score % 5 == 0 and score > 0:
        level += 1
        fps += 2
        score += 1  # Чтобы не повторять увеличение на той же отметке

    # Обновление экрана
    pygame.display.flip()
    clock.tick(fps)  # Ограничение FPS (скорости игры)

    # Обработка событий (выход из игры)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Управление змейкой стрелками (без разворота в себя)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if keys[pygame.K_DOWN] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if keys[pygame.K_LEFT] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if keys[pygame.K_RIGHT] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}