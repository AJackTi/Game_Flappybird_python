import pygame, time
from random import randint, randrange

black = (0,0,0)
white = (255,255,255)
sunset = (253,72,47)
greenyellow = (184,255,0)
brightblue = (47,228,253)
orange = (255,113,0)
yellow = (255,236,0)
purple = (252,67,255)
violetblue = (117,20,246)
colorChoices = [greenyellow,brightblue,orange,yellow,purple,sunset]

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 64
imageWidth = 100

surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Flappy Bird') # title
clock = pygame.time.Clock()

# background
bg = pygame.image.load("bg.png")

# image icon
img = pygame.image.load('flappy_bird.png')
# location display

def score(count):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Score: " + str(count), True, violetblue)
        surface.blit(text, [0,0])


def helicopter(x, y, image): # display image flappy_bird
        surface.blit(img, (x,y))

def blocks(x_block, y_block, block_width, block_height, gap, colorChoice): # gap la lo trong o giua
        pygame.draw.rect(surface, colorChoice, [x_block, y_block, block_width, block_height])
        pygame.draw.rect(surface, colorChoice, [x_block, y_block + block_height+gap, block_width, surfaceHeight])
        

def replay_or_quit(): # choi tiep hay dung lai
        for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                elif event.type == pygame.KEYDOWN:
                        continue
                return event.key
        return None

def makeTextObjs(text, font):
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()
        
    
def msgSurface(text):
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        largeText = pygame.font.Font('freesansbold.ttf', 150)

        titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
        titleTextRect.center = surfaceWidth/2, surfaceHeight/2 # vi tri chu cai se xuat hien
        surface.blit(titleTextSurf, titleTextRect) # chen chu vao

        typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
        typTextRect.center = surfaceWidth/ 2, ((surfaceHeight / 2) + 100)
        surface.blit(typTextSurf, typTextRect) # chen chu vao man hinh tai vi tri nhu tren
        pygame.display.update()
        time.sleep(1)
        while replay_or_quit() == None:
                clock.tick()
        main()
        
def gameOver():
    msgSurface('Game Over')

def main():
        x = 150
        y = 200
        y_move = 0 # =1 thi no se chuyen dong ngay sau khi app load len, =0 thi no se dung yen

        x_block = surfaceWidth
        y_block = 0

        block_width = 75
        block_height = randint(0,surfaceHeight/2)
        gap = imageHeight * 3 # do rong cua lo trong
        block_move = 4
        
        current_score = 0

        blockColor = colorChoices[randrange(0,len(colorChoices))]
        
        game_over = False
        while not game_over:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                game_over = True
                        if event.type == pygame.KEYDOWN: # key down
                                    if event.key == pygame.K_UP: # key up
                                        y_move = -5
                        if event.type == pygame.KEYUP:
                                    if event.key == pygame.K_UP:
                                        y_move = 5

                                
                y += y_move
                
                #surface.fill(black) # screen color black
                surface.blit(bg,(0,0)) # fill image into screen
                helicopter(x,y,img)
                score(current_score)
                
                blocks(x_block, y_block, block_width, block_height, gap, blockColor)
                x_block -= block_move

                if y > surfaceHeight-40 or y < 0 :
                      gameOver()

                if x_block < (-1*block_width):
                        x_block = surfaceWidth
                        block_height = randint(0, surfaceHeight/2)
                        blockColor = colorChoices[randrange(0,len(colorChoices))]
                if x + imageWidth > x_block:
                        if x < x_block + block_width:
                                if y < block_height:
                                        if x - imageWidth < block_width + x_block:
                                                gameOver()
                if x + imageWidth > x_block:
                        if y + imageHeight > block_height + gap:
                                if x < block_width + x_block:
                                        gameOver()

                if x_block < (x-block_width) < x_block + block_move + block_move - 1: 
                        current_score += 1
                # chinh sua lo thong qua tung so diem khac nhau
                if 3 <= current_score < 5:
                        block_move = 5
                        gap = imageHeight * 2.9
                if 5 <= current_score < 8:
                        block_move = 6
                        gap = imageHeight * 2.8                
                if 8 <= current_score < 14:
                        block_move = 7
                        gap = imageHeight * 2.7
                
                pygame.display.update() # update display
                clock.tick(60) # chay nhanh hay cham
main()
pygame.quit()
quit()
