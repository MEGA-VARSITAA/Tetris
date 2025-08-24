import pygame
import sys
from game import Game
from colors import Color
##########################################################################################
#Game setup start
pygame.init()   #initializing

##Defining font and console elements
title_font=pygame.font.Font(None,40)
score_surface=title_font.render("Score",True,Color.white)
score_rect=pygame.Rect(320,55,170,60)

next_surface=title_font.render("Next",True,Color.white)
next_rect=pygame.Rect (320,215,170,180)

game_over_surface=title_font.render("GAME OVER",True,Color.white)

screen=pygame.display.set_mode((500,620))   #Set screen size 
pygame.display.set_caption("Tetris")

clock=pygame.time.Clock()  #clock object to manage the speed of game
game=Game()

GAME_UPDATE = pygame.USEREVENT   ## for custom user event
pygame.time.set_timer(GAME_UPDATE,200)  ## triggers event GAME_UPDATE every 200 ms
##########################################################################################
#Game loop start

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # check for quit event (close)
            pygame.quit()   # uninitialize pygame
            sys.exit()      #closes program completely
        if event.type==pygame.KEYDOWN:  #check for key press
            if game.game_over==True:
                game.game_over=False
                game.reset()
            if event.key==pygame.K_LEFT and game.game_over==False:
                game.move_left()
            if event.key==pygame.K_RIGHT and game.game_over==False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over==False:
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_UP and game.game_over==False:
                game.rotate()
        if event.type==GAME_UPDATE and game.game_over==False:
            game.move_down()    #descends the block every 200ms (for completion of each GAME_UPDATE)
    #Drawing code
    screen.fill(Color.dark_blue)  #background coloring

    # Draw console before grid
    pygame.draw.rect(screen,Color.light_blue,score_rect,0,10)   ##0,10 makes the rectangle corners rounded
    pygame.draw.rect(screen,Color.light_blue,next_rect,0,10)


    ## Score is dynamically updated so we define it in loop
    score_value_surface=title_font.render(str(game.score),True,Color.white)
    
    if game.game_over==True:
        screen.blit(game_over_surface,(320,450,50,50))
    
    
    screen.blit(score_surface,(365,20,50,50))
    screen.blit(next_surface,(365,180,50,50))
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))  ## centers the score on the surface 

    #draw game grid and blocks
    game.draw(screen)

    pygame.display.update() #check for updates and do them
    clock.tick(60)  # code in while runs 60 times per second (60 FPS)

