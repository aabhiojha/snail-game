# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
running = True
clock = pygame.time.Clock()
game_active = True

test_font = pygame.font.Font("font\Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

score_surface = test_font.render("My game", False, "Black")
score_rectangle = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load("graphics\Player\player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

player_gravity = 0


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

    if game_active:
        # sky and ground background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # text score
        pygame.draw.rect(screen, "Pink", score_rectangle)
        pygame.draw.rect(screen, "Pink", score_rectangle, 10)
        screen.blit(score_surface, score_rectangle)
        # text_center_coordinates =

        # logic for updating the snail img
        snail_rectangle.left -= 4
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
        screen.fill("Yellow")

    pygame.display.update()
    clock.tick(60)

    # limits FPS to 60

pygame.quit()
