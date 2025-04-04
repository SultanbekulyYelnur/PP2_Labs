import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A clock")

clock = pygame.image.load("C:\\Users\\Elnur\\Desktop\\PP2_Labs\\lab_7\\img\\clock.png")
min_hand = pygame.image.load("C:\\Users\\Elnur\\Desktop\\PP2_Labs\\lab_7\\img\\min_hand.png")
sec_hand = pygame.image.load("C:\\Users\\Elnur\\Desktop\\PP2_Labs\\lab_7\\img\\sec_hand.png")

clock = pygame.transform.scale(clock, (300, 300))
min_hand = pygame.transform.scale(min_hand, (200, 300))
sec_hand = pygame.transform.scale(sec_hand, (300, 300))

center_x, center_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill((0, 0, 0))  
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    minute_angle = - (minutes * 6)  
    second_angle = - (seconds * 6)  
    
    rotated_right_hand = pygame.transform.rotate(min_hand, minute_angle)
    rotated_left_hand = pygame.transform.rotate(sec_hand, second_angle)
    
    screen.blit(clock, (center_x - 150, center_y - 150))
    
    right_hand_rect = rotated_right_hand.get_rect(center=(center_x, center_y))
    left_hand_rect = rotated_left_hand.get_rect(center=(center_x, center_y))
    
    screen.blit(rotated_right_hand, right_hand_rect)
    screen.blit(rotated_left_hand, left_hand_rect)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(100)

pygame.quit()