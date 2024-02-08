'''
pip install pygame
'''
import pygame

pygame.init() # 파이 게임 초기화
# 창 크기 지정
screen = pygame.display.set_mode((700,800));

'''
게임 fps 설정 
- 초당 프레임을 의미함
* 프레임에 따라서 게임에서 캐릭터가 움직이는 속도가 다름 
'''
clock = pygame.time.Clock();
while True:
    screen.fill((0,0,0));
    event = pygame.event.poll();
    if event.type == pygame.QUIT:
        break;

    # 화면 그리기
    pygame.display.update();
    # 30fps(초당 프레임 수) 를 위한 딜레이 추가
    clock.tick(30);

pygame.quit()
