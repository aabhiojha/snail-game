# Example file showing a circle moving on screen
import pygame


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time = int(current_time / 1000)
    score_surface = test_font.render(f"{current_time}", False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
running = True
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0

test_font = pygame.font.Font("font\Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load("graphics\Player\player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

player_gravity = 0

player_stand_surface = pygame.image.load(
    "graphics\Player\player_stand.png"
).convert_alpha()
player_stand_surface = pygame.transform.rotozoom(player_stand_surface, 0, 2)
player_stand_rect = player_stand_surface.get_rect(center=(400, 200))

game_name = test_font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render("Press space to run", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 340))


# game run loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        # sky and ground background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # text score
        score = display_score()

        # logic for updating the snail img
        snail_rectangle.left -= 8
        if snail_rectangle.right < -100:
            snail_rectangle.left = 800

        screen.blit(snail_surface, snail_rectangle)

        # Player and gravity sim
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collisions
        if snail_rectangle.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_surface, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        score_message = test_font.render(f"Your Score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 340))

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)

    # limits FPS to 60

pygame.quit()
