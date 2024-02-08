import pygame

pygame.init();

clock = pygame.time.Clock();
screen = pygame.display.set_mode((800,800));
character_img = pygame.image.load('Attack (10).png');
character_img = pygame.transform.scale(character_img, (100,100))

character = character_img.get_rect();
character.left = 300 - character_img.get_width() // 2;
character.top = 800 - character_img.get_height();

while True:
    screen.fill((0,0,0));
    event = pygame.event.poll();
    if event.type == pygame.QUIT:
        break;
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            character.left = character.left - 50;
        elif event.key == pygame.K_RIGHT:
            character.right = character.right + 50;

    # 캐릭터가 화면 왼쪽으로 벗어나는 것을 방지
    if character.left < 0:
        character.left = 0;

    # 캐릭터가 화면 오른쪽으로 벗어나는 것을 방지
    if character.right > 800:
        character.right = 800;

    screen.blit(character_img, character);
    pygame.display.update();
    clock.tick(30);
pygame.quit();