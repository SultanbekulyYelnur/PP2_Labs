# Импорт библиотеки pygame
import pygame

# Названия фигур
SQUARE = 'SQUARE'
RIGHT_TRIANGLE = 'RIGHT_TRIANGLE'
EQUILATERAL_TRIANGLE = 'EQUILATERAL_TRIANGLE'
RHOMBUS = 'RHOMBUS'
ERASER = 'ERASER'

# Настройки экрана
WIDTH = 640
HEIGHT = 480

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (180, 180, 180)

# Список для хранения всех нарисованных фигур
figures = []

# Инициализация pygame и создание окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Фигурки")
clock = pygame.time.Clock()

# Начальные настройки
current_shape = SQUARE  # Фигура по умолчанию
current_color = BLACK   # Цвет по умолчанию

# Функции для добавления фигур в список

def add_square(x, y, color):
    figures.append({'shape': SQUARE, 'x': x, 'y': y, 'color': color})

def add_right_triangle(x, y, color):
    points = [(x, y), (x, y + 50), (x + 50, y + 50)]
    figures.append({'shape': RIGHT_TRIANGLE, 'points': points, 'color': color})

def add_equilateral_triangle(x, y, color):
    points = [(x, y), (x - 25, y + 43), (x + 25, y + 43)]
    figures.append({'shape': EQUILATERAL_TRIANGLE, 'points': points, 'color': color})

def add_rhombus(x, y, color):
    points = [(x, y - 30), (x - 30, y), (x, y + 30), (x + 30, y)]
    figures.append({'shape': RHOMBUS, 'points': points, 'color': color})

# Функция стирания фигур

def erase(x, y):
    for fig in figures[:]:
        if fig['shape'] == SQUARE and fig['x'] <= x <= fig['x'] + 50 and fig['y'] <= y <= fig['y'] + 50:
            figures.remove(fig)
        elif 'points' in fig:
            poly = pygame.draw.polygon(pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA), (0,0,0,0), fig['points'])
            if poly.collidepoint(x, y):
                figures.remove(fig)

# Основной цикл программы
running = True
while running:
    screen.fill(WHITE)

    # Отображение всех фигур
    for fig in figures:
        if fig['shape'] == SQUARE:
            pygame.draw.rect(screen, fig['color'], (fig['x'], fig['y'], 50, 50))
        else:
            pygame.draw.polygon(screen, fig['color'], fig['points'])

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Выбор фигуры по клавишам
            if event.key == pygame.K_1:
                current_shape = SQUARE
            elif event.key == pygame.K_2:
                current_shape = RIGHT_TRIANGLE
            elif event.key == pygame.K_3:
                current_shape = EQUILATERAL_TRIANGLE
            elif event.key == pygame.K_4:
                current_shape = RHOMBUS
            elif event.key == pygame.K_e:
                current_shape = ERASER

            # Выбор цвета по клавишам
            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_o:
                current_color = ORANGE

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if current_shape == SQUARE:
                add_square(x, y, current_color)
            elif current_shape == RIGHT_TRIANGLE:
                add_right_triangle(x, y, current_color)
            elif current_shape == EQUILATERAL_TRIANGLE:
                add_equilateral_triangle(x, y, current_color)
            elif current_shape == RHOMBUS:
                add_rhombus(x, y, current_color)
            elif current_shape == ERASER:
                erase(x, y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()