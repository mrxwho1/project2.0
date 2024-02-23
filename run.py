import pygame

# Инициализация игры(модуль PyGame)
pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

# определение шрифта
font = pygame.font.SysFont('Bauhaus 93', 60)

# определите цвета
white = (255, 255, 255)

# Игровые переменные
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500  # значение в миллисекундах
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

# Фон отображения игры
# Импорт файлов из каталога
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')
bg = pygame.image.load('img/fon1.png')
ground_img = pygame.image.load('img/ground.png')
#!!!! button_img = pygame.image.load('img/restart.png')


run = True
while run:

    clock.tick(fps)

    screen.blit(bg, (0, 0))
    screen.blit(ground_img, (ground_scroll, 768))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
