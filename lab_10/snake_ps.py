import pygame
import psycopg2
from random import randrange
import time
import sys

# PostgreSQL DB connection
conn = psycopg2.connect(
    dbname="snake",
    user="postgres",
    password="AlSanBek12",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Prompt user
username = input("Enter your username: ")
cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cursor.fetchone()

if user:
    user_id = user[0]
    cursor.execute("""
        SELECT score, level FROM user_scores
        WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1
    """, (user_id,))
    result = cursor.fetchone()
    if result:
        score, level = result
        fps = 8 + (level - 1) * 2
        print(f"Welcome back {username}! Continuing at level {level}.")
    else:
        score, level, fps = 0, 1, 8
else:
    cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cursor.fetchone()[0]
    conn.commit()
    score, level, fps = 0, 1, 8
    print(f"User {username} created!")

# Game settings
res = 800
size = 50
apple_img = pygame.transform.scale(pygame.image.load('lab_8/material/apple.png'), (size, size))
banana_img = pygame.transform.scale(pygame.image.load('lab_8/material/banana.png'), (size, size))
snake_img = pygame.transform.scale(pygame.image.load('lab_8/material/snake.png'), (size, size))

# Generate food
def generate_food(snake):
    while True:
        food = randrange(0, res, size), randrange(0, res, size)
        if food not in snake:
            return food

x, y = randrange(0, res, size), randrange(0, res, size)
snake = [(x, y)]
length = 1
apple = generate_food(snake)
banana = generate_food(snake)
apple_timer = pygame.time.get_ticks()
banana_timer = pygame.time.get_ticks()
food_lifetime = 5000
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
dx, dy = 0, 0

pygame.init()
sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)

# Main game loop
while True:
    sc.fill(pygame.Color('black'))
    for i, j in snake:
        sc.blit(snake_img, (i, j))

    current_time = pygame.time.get_ticks()
    if current_time - apple_timer > food_lifetime:
        apple = generate_food(snake)
        apple_timer = current_time
    if current_time - banana_timer > food_lifetime:
        banana = generate_food(snake)
        banana_timer = current_time

    sc.blit(apple_img, apple)
    sc.blit(banana_img, banana)

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    render_level = font_level.render(f'LEVEL: {level}', 1, pygame.Color('cyan'))
    sc.blit(render_score, (5, 5))
    sc.blit(render_level, (5, 35))

    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]

    if x < 0 or x >= res or y < 0 or y >= res or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (res // 2 - 200, res // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cursor.close()
                    conn.close()
                    pygame.quit()
                    sys.exit()

    if snake[-1] == apple:
        apple = generate_food(snake)
        apple_timer = pygame.time.get_ticks()
        length += 1
        score += 1

    if snake[-1] == banana:
        banana = generate_food(snake)
        banana_timer = pygame.time.get_ticks()
        length += 2
        score += 2

    if score % 5 == 0 and score > 0:
        level += 1
        fps += 2
        score += 1

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cursor.close()
            conn.close()
            pygame.quit()
            sys.exit()

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

    # Save game on pause (P key)
    if keys[pygame.K_p]:
        print("Game paused. Saving progress...")
        cursor.execute("""
            INSERT INTO user_scores (user_id, score, level)
            VALUES (%s, %s, %s)
        """, (user_id, score, level))
        conn.commit()
        paused = True
        pause_text = font_end.render('PAUSED', 1, pygame.Color('orange'))
        sc.blit(pause_text, (res // 2 - 150, res // 3))
        pygame.display.flip()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cursor.close()
                    conn.close()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    paused = False
