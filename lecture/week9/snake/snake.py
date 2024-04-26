import pygame 
from random import randrange
res=800
size=40
pygame.init()
img=pygame.image.load('1.jpg')
x,y=randrange(size, res - size, size),randrange(size,res-size,size)
apple=randrange(size,res-size,size),randrange(size,res-size,size)
apple1=randrange(size,res-size,size),randrange(size,res-size,size)
boom=randrange(size,res-size,size),randrange(size,res-size,size)
dirs={'W':True,'S':True,'A':True,'D':True,}
font_score=pygame.font.SysFont("Arial", 26)
font_end=pygame.font.SysFont("Arial", 66)
#fender_end=font_end.render('GAME OVER',True,pygame.Color('orange'))


fps=6
snake=[(x,y)]
dx,dy=0,0
length=1
score=0
#speed_count, snake_speed = 0, 10
food_timer=0
food_respawn_time=5000


screnn=pygame.display.set_mode((res,res))
pygame.display.set_caption('Snake')
clock=pygame.time.Clock()

Color=randrange(0,255)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    screnn.blit(img, (0,0))
    #drawing snake, apple
    [(pygame.draw.rect(screnn,Color,(i,j,size-2,size-2))) for i,j in snake]
    pygame.draw.rect(screnn,pygame.Color('red'),(*apple,size,size))
    pygame.draw.rect(screnn,pygame.Color('yellow'),(*apple1,size,size))
    #show score
    fender_score=font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    screnn.blit(fender_score, (5,5))
    #snake movement
    '''speed_count += 2
    if not speed_count % snake_speed:'''
    x+=dx*size
    y+=dy*size
    snake.append((x,y))
    snake=snake[-length:]
    
    #eating apple
    if snake[-1]==apple:
        #[(pygame.draw.rect(screnn,Color,(i,j,size-2,size-2))) for i,j in snake]
        apple=randrange(0,res,size),randrange(0,res,size)
        length +=1
        fps +=1
        score+=1
        food_timer=pygame.time.get_ticks()
    if snake[-1]==apple1:
        apple1=randrange(0,res,size),randrange(0,res,size)
        
        length +=2
        fps +=2
        score+=2
        food_timer=pygame.time.get_ticks()

    #REspawn food after a certain time
    if pygame.time.get_ticks()-food_timer>food_respawn_time:
        apple=randrange(size,res-size,size),randrange(size,res-size,size)
        food_timer=pygame.time.get_ticks()
       # snake_speed -= 1
        #snake_speed = max(snake_speed, 4)
    #game over
    if x<0 or x>res-size or y<0 or y>res-size or len(snake) != len(set(snake)):
        running=False
        fender_end=font_end.render('GAME OVER',True,pygame.Color('orange'))
        screnn.blit(fender_end,(res//2-250,res//3))
        pygame.display.flip()
        break
    #control
    key=pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx,dy=0,-1
        dirs={'W':True,'S':False,'A':True,'D':True,}
    if key[pygame.K_s] and dirs['S']:
        dx,dy=0,1
        dirs={'W':False,'S':True,'A':True,'D':True,}
    if key[pygame.K_a] and dirs['A']:
        dx,dy=-1,0
        dirs={'W':True,'S':True,'A':True,'D':False,}
    if key[pygame.K_d] and dirs['D']:
        dx,dy=1,0
        dirs={'W':True,'S':True,'A':False,'D':True,}

    pygame.display.flip()
    clock.tick(fps)
