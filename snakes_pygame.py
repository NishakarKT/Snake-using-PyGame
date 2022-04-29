import pygame
import random

pygame.init()


# Colours defined based on rgb values
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Dimensions
width = 900
height = 500
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snakes")

font = pygame.font.SysFont(None, 55)
bg1 = pygame.image.load("snake.jpg")
bg1 = pygame.transform.scale(bg1, (width, height)).convert_alpha()
bg2 = pygame.image.load("snake2.jpg")
bg2 = pygame.transform.scale(bg2, (width, height)).convert_alpha()


def text_screen(text, colour, x_coord, y_coord):
    score_screen = font.render(text, True, colour)
    game_window.blit(score_screen, [x_coord, y_coord])


def plot_snake(game_window, colour, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, colour, [
            x, y, snake_size, snake_size])


def open_window():
    # Background Image
    pygame.display.update()
    exit_game = False
    while not exit_game:
        game_window.blit(bg2, (0, 0))
        text_screen("Welcome to snakes", black, width/3, height/2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
        pygame.display.update()

    pygame.time.Clock.tick(30)


def game_loop():
    # Background Music
    pygame.mixer.music.load('naagin.mp3')
    pygame.mixer.music.play(-1)

    # Game variables
    exit_game = False
    game_over = False
    snake_x = 50  # x coordinate variable for snake
    snake_y = 50  # y coordinate variable for snake
    food_x = random.randint(10, 890)  # x coordinate variable for snake's food
    food_y = random.randint(10, 490)  # y coordinate variable for snake's food
    snake_size = 20
    fps = 30
    snake_velocity_x = 0  # velocity X
    snake_velocity_y = 0  # velocity Y
    clock = pygame.time.Clock()
    score = 0

    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over:
            game_window.blit(bg2, (0,0))
            text_screen("GAME OVER !", black, width/3, height/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        open_window()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                # key bindings (one press = one move)
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_RIGHT):
                        snake_velocity_x = 10
                        snake_velocity_y = 0
                    if(event.key == pygame.K_LEFT):
                        snake_velocity_x = -10
                        snake_velocity_y = 0
                    if(event.key == pygame.K_UP):
                        snake_velocity_x = 0
                        snake_velocity_y = -10
                    if(event.key == pygame.K_DOWN):
                        snake_velocity_x = 0
                        snake_velocity_y = 10

            snake_x += snake_velocity_x
            snake_y += snake_velocity_y

            # Score
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:  # "abs" gives absolute value
                # eating sound effect in background
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("eat.wav"))

                score += 10
                snake_length += 5
                # x coordinate variable for snake's food
                food_x = random.randint(10, 890)
                # y coordinate variable for snake's food
                food_y = random.randint(10, 490)

            # background colour
            game_window.blit(bg1, (0, 0))
            # score printing
            text_screen(f"Score : {score}", black, 5, 5)

            # Position of food
            pygame.draw.rect(game_window, white, [
                food_x, food_y, snake_size, snake_size])

            # increasing snake length
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            # Game Over
            # sanke_list[:-1] --> all elements excluding last one...
            if(snake_x >= width or snake_x <= 0 or snake_y >= height or snake_y <= 0 or head in snake_list[:-1]):
                game_over = True
                # game over music
                pygame.mixer.Channel(0).stop()
                pygame.mixer.music.load('over.wav')
                pygame.mixer.music.play()

            # Snake Montioring
            plot_snake(game_window, black, snake_list, snake_size)

        pygame.display.update()  # any change in the display must be updated

        # FPS
        clock.tick(fps)


# Calling game loop
open_window()
