import pygame
import random


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
apple_red = (145, 28, 20)
deep_red = (127, 19, 19)
head_color = (37, 84, 49)
background = (178, 178, 178)

width = 800
height = 600


game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slither")

fps_clock = pygame.time.Clock()
fps = 60
vel = 5
block_size = 20
apple_size = 20

font = pygame.font.SysFont('8bitoperatorregular', 25)


def call_snake(snake_list, block_size):
    for XY in snake_list:
        game_display.fill(head_color, rect=[XY[0], XY[1], block_size, block_size])


def text_objects(text, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_screen(msg, color):
    text_surface, text_rect = text_objects(msg, color)
    text_rect.center = (width/2), (height/2)
    game_display.blit(text_surface, text_rect)

def game_loop():
    game_exit = False
    game_over = False

    lead_x = width / 2
    lead_y = height / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    apple_x = round(random.randrange(0, width - apple_size))
    apple_y = round(random.randrange(0, height - apple_size))

    while not game_exit:

        while game_over:
            game_display.fill(background)
            message_screen("Game over, press C to play again or Q to leave", deep_red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_exit = True
                if event.key == pygame.K_LEFT:
                    lead_x_change = -vel
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = vel
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    lead_y_change = -vel
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = vel
                    lead_x_change = 0

        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(background)
        game_display.fill(apple_red, rect=[apple_x, apple_y,apple_size,apple_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for seg in snake_list[:-1]:
            if seg == snake_head:
                game_over = True

        call_snake(snake_list, block_size)

        pygame.display.update()

        if lead_x > apple_x and lead_x < apple_x + apple_size or lead_x + block_size > apple_x and lead_x + block_size < apple_x + apple_size:
            if lead_y > apple_y and lead_y < apple_y + apple_size or lead_y + block_size > apple_y and lead_y + block_size < apple_y + apple_size:
                apple_x = round(random.randrange(0, width - block_size) / 10.0) * 10
                apple_y = round(random.randrange(0, height - block_size) / 10.0) * 10
                snake_length += 10

        fps_clock.tick(fps)

    pygame.quit()
    quit()


game_loop()
