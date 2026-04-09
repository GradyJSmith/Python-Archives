import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PADDLE_SPEED = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
WINNING_SCORE = 10

# Colors for skins
SKINS = [WHITE, RED, GREEN, BLUE]

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Ball setup
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Paddle setup
player = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH - 10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Game state variables
difficulty = 'Medium'
player_skin = WHITE
opponent_skin = WHITE
control_method = 'Keyboard'
game_started = False
player_score = 0
opponent_score = 0
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y
player_speed = 0
opponent_speed = 7

# Clock setup
clock = pygame.time.Clock()

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
    ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
    if difficulty == 'Baby Mode':
        ball_speed_x *= 0.2
        ball_speed_y *= 0.2
    elif difficulty == 'Sloth Mode':
        ball_speed_x *= 0.25
        ball_speed_y *= 0.25
    elif difficulty == 'Extra Easy':
        ball_speed_x *= 0.5
        ball_speed_y *= 0.5
    elif difficulty == 'Easy':
        ball_speed_x *= 0.8
        ball_speed_y *= 0.8
    elif difficulty == 'Hard':
        ball_speed_x *= 1.5
        ball_speed_y *= 1.5
    elif difficulty == 'Impossible':
        ball_speed_x *= 5
        ball_speed_y *= 5
    elif difficulty == 'Glitch':
        ball_speed_x *= 15
        ball_speed_y *= 15
    elif difficulty == 'Burn Yo Computer':
        ball_speed_x *= 1000000
        ball_speed_y *= 1000000

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def show_start_menu():
    menu = True
    global difficulty, player_skin, opponent_skin, control_method, game_started
    
    while menu:
        screen.fill(BLACK)
        draw_text('Pong', font, WHITE, screen, SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 4)
        draw_text('Press Enter to Start', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 30)
        draw_text('Press 1 for Difficulty', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 10)
        draw_text('Press 2 for Skin', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 50)
        draw_text('Press 3 for Control Method', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 90)
        draw_text('Press 4 for Instructions', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 130)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                    game_started = True
                if event.key == pygame.K_1:
                    show_difficulty_menu()
                if event.key == pygame.K_2:
                    show_skin_menu()
                if event.key == pygame.K_3:
                    show_control_menu()
                if event.key == pygame.K_4:
                    show_instructions_menu()

        pygame.display.flip()
        clock.tick(60)

def show_difficulty_menu():
    menu = True
    global difficulty
    
    while menu:
        screen.fill(BLACK)
        draw_text('Select Difficulty:', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 5)
        draw_text('1. Baby Mode', small_font, BLUE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 140)
        draw_text('2. Sloth Mode', small_font, GREEN, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 100)
        draw_text('3. Extra Easy', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 60)
        draw_text('4. Easy', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 20)
        draw_text('5. Medium', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 20)
        draw_text('6. Hard', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 60)
        draw_text('7. Impossible', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 100)
        draw_text('8. Glitch', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 140)
        draw_text('9. Burn Yo Computer', small_font, RED, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 180)
        draw_text('Press Esc to go back', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 240)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 'Baby Mode'
                    menu = False
                if event.key == pygame.K_2:
                    difficulty = 'Sloth Mode'
                    menu = False
                if event.key == pygame.K_3:
                    difficulty = 'Extra Easy'
                    menu = False
                if event.key == pygame.K_4:
                    difficulty = 'Easy'
                    menu = False
                if event.key == pygame.K_5:
                    difficulty = 'Medium'
                    menu = False
                if event.key == pygame.K_6:
                    difficulty = 'Hard'
                    menu = False
                if event.key == pygame.K_7:
                    difficulty = 'Impossible'
                    menu = False
                if event.key == pygame.K_8:
                    difficulty = 'Glitch'
                    menu = False
                if event.key == pygame.K_9:
                    difficulty = 'Burn Yo Computer'
                    menu = False
                if event.key == pygame.K_ESCAPE:
                    menu = False

        pygame.display.flip()
        clock.tick(60)

def show_skin_menu():
    menu = True
    global player_skin, opponent_skin
    
    while menu:
        screen.fill(BLACK)
        draw_text('Select Skin:', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
        draw_text('1. White', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 60)
        draw_text('2. Red', small_font, RED, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 20)
        draw_text('3. Green', small_font, GREEN, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 20)
        draw_text('4. Blue', small_font, BLUE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 60)
        draw_text('Press Esc to go back', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 160)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_skin = SKINS[0]
                    opponent_skin = SKINS[0]
                    menu = False
                if event.key == pygame.K_2:
                    player_skin = SKINS[1]
                    opponent_skin = SKINS[1]
                    menu = False
                if event.key == pygame.K_3:
                    player_skin = SKINS[2]
                    opponent_skin = SKINS[2]
                    menu = False
                if event.key == pygame.K_4:
                    player_skin = SKINS[3]
                    opponent_skin = SKINS[3]
                    menu = False
                if event.key == pygame.K_ESCAPE:
                    menu = False

        pygame.display.flip()
        clock.tick(60)

def show_control_menu():
    menu = True
    global control_method
    
    while menu:
        screen.fill(BLACK)
        draw_text('Select Control Method:', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
        draw_text('1. Keyboard', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 20)
        draw_text('2. Mouse', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 20)
        draw_text('Press Esc to go back', small_font, WHITE, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 80)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    control_method = 'Keyboard'
                    menu = False
                if event.key == pygame.K_2:
                    control_method = 'Mouse'
                    menu = False
                if event.key == pygame.K_ESCAPE:
                    menu = False

        pygame.display.flip()
        clock.tick(60)

def show_instructions_menu():
    menu = True
    
    while menu:
        screen.fill(BLACK)
        draw_text('Instructions:', small_font, WHITE, screen, SCREEN_WIDTH // 12, SCREEN_HEIGHT // 4)
        draw_text('Use the arrow keys to move the paddle up and down (Keyboard)', small_font, WHITE, screen, SCREEN_WIDTH // 12, SCREEN_HEIGHT // 2 - 60)
        draw_text('Or use the mouse to move the paddle up and down (Mouse)', small_font, WHITE, screen, SCREEN_WIDTH // 12, SCREEN_HEIGHT // 2)
        draw_text('First to score 10 points wins.', small_font, WHITE, screen, SCREEN_WIDTH // 12, SCREEN_HEIGHT // 2 + 60)
        draw_text('Press Esc to go back', small_font, WHITE, screen, SCREEN_WIDTH // 12, SCREEN_HEIGHT // 2 + 120)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = False

        pygame.display.flip()
        clock.tick(60)

# Main game loop
while True:
    if not game_started:
        show_start_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if control_method == 'Keyboard':
                    player_speed = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                if control_method == 'Keyboard':
                    player_speed = PADDLE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                if control_method == 'Keyboard':
                    player_speed = 0

    if control_method == 'Mouse':
        mouse_y = pygame.mouse.get_pos()[1]
        if mouse_y < PADDLE_HEIGHT // 2:
            player.top = 0
        elif mouse_y > SCREEN_HEIGHT - PADDLE_HEIGHT // 2:
            player.bottom = SCREEN_HEIGHT
        else:
            player.centery = mouse_y

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        if player_score >= WINNING_SCORE:
            # Display winner and reset game
            screen.fill(BLACK)
            draw_text('You WON!!!', font, WHITE, screen, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
            pygame.display.flip()
            pygame.time.wait(2000)
            game_started = False
            player_score = 0
            opponent_score = 0
            ball_restart()
            continue
        ball_restart()
    if ball.right >= SCREEN_WIDTH:
        opponent_score += 1
        if opponent_score >= WINNING_SCORE:
            # Display winner and reset game
            screen.fill(BLACK)
            draw_text('You got TOASTED!!!', font, RED, screen, SCREEN_WIDTH // 3 - 150, SCREEN_HEIGHT // 2 - 50)
            pygame.display.flip()
            pygame.time.wait(2000)
            game_started = False
            player_score = 0
            opponent_score = 0
            ball_restart()
            continue
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Player movement
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

    # Opponent AI
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, player_skin, player)
    pygame.draw.rect(screen, opponent_skin, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    player_text = font.render(f"{player_score}", True, WHITE)
    screen.blit(player_text, (SCREEN_WIDTH // 2 + 20, 10))

    opponent_text = font.render(f"{opponent_score}", True, WHITE)
    screen.blit(opponent_text, (SCREEN_WIDTH // 2 - 60, 10))

    # Update the screen
    pygame.display.flip()
    clock.tick(60)