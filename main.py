# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
running = True
clock = pygame.time.Clock()

test_font = pygame.font.Font("font\Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

score_surface = test_font.render("My game", False, "Black")
score_rectangle = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load("graphics\Player\player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # sky and ground background
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # pygame.draw.line(screen, "Red", (800, 0), pygame.mouse.get_pos(), 4)
    pygame.draw.ellipse(screen, "Brown", pygame.Rect(left))

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

    # Player image
    screen.blit(player_surf, player_rect)

    # if player_rect.collidepoint(snail_rectangle):
    #     print("collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)

    # limits FPS to 60

pygame.quit()
