import pygame
import random

pygame.init()

# --- Constants ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WINNING_SCORE = 10

# --- Setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 60)
menu_font = pygame.font.Font(None, 40)

# --- Game Variables ---
PADDLE_SPEED = 8
BALL_SPEED_X = 6
BALL_SPEED_Y = 6

player = pygame.Rect(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SIZE, BALL_SIZE)

player_speed = 0
opponent_speed = 7
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

player_score = 0
opponent_score = 0
difficulty = 'Medium'
control_method = 'Keyboard'
player_skin = WHITE
opponent_skin = WHITE
game_started = False


# --- Functions ---

def ball_restart():
    """Reset the ball and adjust speed based on difficulty."""
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
    ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

    # Ball speed difficulty modifiers
    if difficulty == 'Baby Mode':
        ball_speed_x *= 0.2
        ball_speed_y *= 0.2
    elif difficulty == 'Sloth Mode':
        ball_speed_x *= 0.4
        ball_speed_y *= 0.4
    elif difficulty == 'Extra Easy':
        ball_speed_x *= 0.6
        ball_speed_y *= 0.6
    elif difficulty == 'Easy':
        ball_speed_x *= 0.8
        ball_speed_y *= 0.8
    elif difficulty == 'Medium':
        ball_speed_x *= 1
        ball_speed_y *= 1
    elif difficulty == 'Hard':
        ball_speed_x *= 1.3
        ball_speed_y *= 1.3
    elif difficulty == 'Impossible':
        ball_speed_x *= 1.6
        ball_speed_y *= 1.6
    elif difficulty == 'Burn Yo Computer':
        ball_speed_x *= 100
        ball_speed_y *= 100


def set_difficulty_values():
    """Set opponent AI speed based on difficulty."""
    global opponent_speed
    if difficulty == 'Baby Mode':
        opponent_speed = 2
    elif difficulty == 'Sloth Mode':
        opponent_speed = 3
    elif difficulty == 'Extra Easy':
        opponent_speed = 4
    elif difficulty == 'Easy':
        opponent_speed = 5
    elif difficulty == 'Medium':
        opponent_speed = 7
    elif difficulty == 'Hard':
        opponent_speed = 10
    elif difficulty == 'Impossible':
        opponent_speed = 14
    elif difficulty == 'Burn Yo Computer':
        opponent_speed = 10000
    else:
        opponent_speed = 7


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))


def show_start_menu():
    """Start menu to pick difficulty and control type."""
    global difficulty, control_method, player_skin, opponent_skin, game_started

    while True:
        screen.fill(BLACK)
        draw_text("PONG", font, WHITE, screen, SCREEN_WIDTH // 2 - 70, 100)
        draw_text("Press 1 to Start", menu_font, WHITE, screen, SCREEN_WIDTH // 2 - 110, 220)
        draw_text("Press 2 for Difficulty", menu_font, WHITE, screen, SCREEN_WIDTH // 2 - 140, 280)
        draw_text("Press 3 for Controls", menu_font, WHITE, screen, SCREEN_WIDTH // 2 - 120, 340)
        draw_text("Press 4 for Paddle Colors", menu_font, WHITE, screen, SCREEN_WIDTH // 2 - 180, 400)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    set_difficulty_values()
                    ball_restart()
                    game_started = True
                    return
                elif event.key == pygame.K_2:
                    show_difficulty_menu()
                elif event.key == pygame.K_3:
                    show_control_menu()
                elif event.key == pygame.K_4:
                    show_color_menu()


def show_difficulty_menu():
    """Menu to select difficulty."""
    global difficulty
    difficulties = ['Baby Mode', 'Sloth Mode', 'Extra Easy', 'Easy', 'Medium', 'Hard', 'Impossible', 'Burn Yo Computer']
    selected = difficulties.index(difficulty)

    while True:
        screen.fill(BLACK)
        draw_text("Select Difficulty", font, WHITE, screen, SCREEN_WIDTH // 2 - 160, 100)
        for i, d in enumerate(difficulties):
            color = WHITE if i == selected else (100, 100, 100)
            draw_text(d, menu_font, color, screen, SCREEN_WIDTH // 2 - 120, 200 + i * 40)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(difficulties)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(difficulties)
                elif event.key == pygame.K_RETURN:
                    difficulty = difficulties[selected]
                    set_difficulty_values()
                    ball_restart()
                    return
                elif event.key == pygame.K_ESCAPE:
                    return


def show_control_menu():
    """Select mouse or keyboard control."""
    global control_method
    options = ['Keyboard', 'Mouse']
    selected = options.index(control_method)

    while True:
        screen.fill(BLACK)
        draw_text("Select Controls", font, WHITE, screen, SCREEN_WIDTH // 2 - 140, 100)
        for i, opt in enumerate(options):
            color = WHITE if i == selected else (100, 100, 100)
            draw_text(opt, menu_font, color, screen, SCREEN_WIDTH // 2 - 90, 220 + i * 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    control_method = options[selected]
                    return
                elif event.key == pygame.K_ESCAPE:
                    return


def show_color_menu():
    """Select paddle colors."""
    global player_skin, opponent_skin
    colors = {
        'White': WHITE,
        'Red': (255, 0, 0),
        'Green': (0, 255, 0),
        'Blue': (0, 0, 255),
        'Yellow': (255, 255, 0),
        'Cyan': (0, 255, 255),
        'Magenta': (255, 0, 255)
    }
    color_names = list(colors.keys())
    selected = color_names.index('White')

    while True:
        screen.fill(BLACK)
        draw_text("Select Paddle Color", font, WHITE, screen, SCREEN_WIDTH // 2 - 190, 100)
        for i, name in enumerate(color_names):
            color = WHITE if i == selected else (100, 100, 100)
            draw_text(name, menu_font, color, screen, SCREEN_WIDTH // 2 - 80, 220 + i * 40)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(color_names)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(color_names)
                elif event.key == pygame.K_RETURN:
                    player_skin = colors[color_names[selected]]
                    opponent_skin = colors[color_names[selected]]
                    return
                elif event.key == pygame.K_ESCAPE:
                    return


# --- Main Game Loop ---
while True:
    if not game_started:
        show_start_menu()
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if control_method == 'Keyboard':
                if event.key == pygame.K_UP:
                    player_speed = -PADDLE_SPEED
                elif event.key == pygame.K_DOWN:
                    player_speed = PADDLE_SPEED
        if event.type == pygame.KEYUP:
            if control_method == 'Keyboard' and (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                player_speed = 0

    # Player movement
    if control_method == 'Mouse':
        mouse_y = pygame.mouse.get_pos()[1]
        player.centery = mouse_y
    else:
        player.y += player_speed
    player.clamp_ip(screen.get_rect())

    # Opponent AI
    if opponent.centery < ball.centery - 15:
        opponent.y += opponent_speed
    elif opponent.centery > ball.centery + 15:
        opponent.y -= opponent_speed
    opponent.clamp_ip(screen.get_rect())

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Wall collision
    if ball.top <= 0:
        ball.top = 0
        ball_speed_y *= -1
    elif ball.bottom >= SCREEN_HEIGHT:
        ball.bottom = SCREEN_HEIGHT
        ball_speed_y *= -1

    # Paddle collisions
    if ball.colliderect(player):
        offset = (ball.centery - player.centery) / (PADDLE_HEIGHT / 2)
        ball_speed_x = -abs(ball_speed_x)
        ball_speed_y += offset * 4
        ball.right = player.left - 1
    elif ball.colliderect(opponent):
        offset = (ball.centery - opponent.centery) / (PADDLE_HEIGHT / 2)
        ball_speed_x = abs(ball_speed_x)
        ball_speed_y += offset * 4
        ball.left = opponent.right + 1

    ball.clamp_ip(screen.get_rect())

    # Scoring
    if ball.left <= 0:
        player_score += 1
        ball_restart()
    elif ball.right >= SCREEN_WIDTH:
        opponent_score += 1
        ball_restart()

    # Win check
    if player_score >= WINNING_SCORE or opponent_score >= WINNING_SCORE:
        screen.fill(BLACK)
        if player_score > opponent_score:
            draw_text('You WON!!!', font, WHITE, screen, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
        else:
            draw_text('You got TOASTED!!!', font, RED, screen, SCREEN_WIDTH // 3 - 150, SCREEN_HEIGHT // 2 - 50)
        pygame.display.flip()
        pygame.time.wait(2000)
        game_started = False
        player_score = 0
        opponent_score = 0
        continue

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, player_skin, player)
    pygame.draw.rect(screen, opponent_skin, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    screen.blit(font.render(str(player_score), True, WHITE), (SCREEN_WIDTH // 2 + 20, 10))
    screen.blit(font.render(str(opponent_score), True, WHITE), (SCREEN_WIDTH // 2 - 60, 10))

    pygame.display.flip()
    clock.tick(60)
