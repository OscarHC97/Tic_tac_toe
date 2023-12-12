import sys
import copy 
import random
import pygame
import numpy as np 
from constants import *
#PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TiC TAC TOE AI')
screen.fill(BG_COLOR)

class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqr = self.squares
        self.mark_sqr = 0
        #print(self.squares)
        #self.mark_sqr(1,1,2)
        #print(self.squares)

    def final_state(self, show = False):
        '''
        @return 0 si no a ganado aun
        @return 1 si el jugador 1 gano
        @return 2 si el jugador 2 gano 
        '''

        #ganadas verticales 
        for col in range(COLS):
            if self. squares[0][col] == self.squares[1][col] == self.squares[2][col] !=0:
                if show: #mUESTRA LAS LINEAS DE GANADOR..
                    color  = CIRC_COLOR if self.squares[0][col]  == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2,20)  
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT-20)              
                    pygame.draw.line(screen,color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]
            
        #ganadas horizontales
        for row in range(ROWS):
            if self. squares[row][0] == self.squares[row][1] == self.squares[row][2] !=0:
                if show: #mUESTRA LAS LINEAS DE GANADOR..
                    color  = CIRC_COLOR if self. squares[row][0]   == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE +SQSIZE // 2)  
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE //2)              
                    pygame.draw.line(screen,color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]
        
        #Diagonal ganadores
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] !=0:
            if show: #mUESTRA LAS LINEAS DE GANADOR..
                    color  = CIRC_COLOR if self.squares[1][1]   == 2 else CROSS_COLOR
                    iPos = (20, 20)  
                    fPos = (WIDTH - 20, HEIGHT -20)              
                    pygame.draw.line(screen,color, iPos, fPos, LINE_WIDTH)
            return self.squares[1][1]
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] !=0:
            if show: #mUESTRA LAS LINEAS DE GANADOR..
                    color  = CIRC_COLOR if self.squares[1][1]   == 2 else CROSS_COLOR
                    iPos = (20, HEIGHT - 20)  
                    fPos = (WIDTH - 20, 20)              
                    pygame.draw.line(screen,color, iPos, fPos, LINE_WIDTH)
            return self.squares[1][1]
        return 0
        
    def mark_sqrs(self, row, col, player):
        self.squares[row][col]= player
        self.mark_sqr +=1 

    def empty_sqrs(self, row, col):
        return self.squares[row][col] == 0 
    def get_empty_sqrs(self):
        empty_sqrsss = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqrs(row, col):
                    empty_sqrsss.append((row,col))
        return empty_sqrsss
    
    def isfull(self):
        return self.mark_sqr ==9
    def isempty(self):
        return self.mark_sqr == 0    
class AI:
    def __init__(self, level=1, player=2): #level cambia el modo de IA para enfrentarse. Player inicia o segundo
        self.level = level
        self.player = player
    def rnd(self, board ):
        empty_stra = board.get_empty_sqrs()
        idx = random.randrange(0,len(empty_stra))
        return empty_stra[idx] #(row,col)
    def minimax(self, board, maximazing):
        #caso terminal o final
        case = board.final_state()

        #player 1 gana
        if case ==1 :
            return 1, None #eval move
        #player 2 gana
        if case == 2:
            return -1, None
        #empate
        elif board.isfull():
            return 0, None
        if maximazing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()


            for (row, col)in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqrs(row, col, 1)
                eval = self.minimax(temp_board,False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move=(row, col)
            return max_eval, best_move
        

        elif not maximazing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()


            for (row, col)in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqrs(row, col, self.player)
                eval = self.minimax(temp_board,True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move=(row, col)
            return min_eval, best_move

    def eval(self, main_board):
        if self.level == 0:
            #eleccion aleatoria
            eval = "random"
            move = self.rnd(main_board)
        else:
            #algoritmo MINIMAX
            eval,move = self.minimax(main_board, False)
        print(f'AI escogio la posicion: {move} con una evaluacion de {eval}')
        return move

    
class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1  # 1-cruz 2- circulos
        self.gamemode = "ai" # persona vs paersona o   ia
        self.running  = True
        
        self.show_lines()
    def make_move(self, row, col):
        self.board.mark_sqrs(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def show_lines(self):
        #fill screen
        screen.fill(BG_COLOR)
        #vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE,0),(SQSIZE,HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH-SQSIZE,0),(WIDTH-SQSIZE,HEIGHT), LINE_WIDTH)

        #Horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE),(WIDTH,SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE),(WIDTH,HEIGHT - SQSIZE), LINE_WIDTH)
    def draw_fig(self, row, col):
        if self.player == 1: #pintar Cruz 
            #barra decendente
            star_desc = (col * SQSIZE +OFFSET, row *SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE- OFFSET, row * SQSIZE +SQSIZE -OFFSET )
            pygame.draw.line(screen, CROSS_COLOR, star_desc, end_desc, CROSS_WIDTH) 
            
            #barra ascendente
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH) 
            
        elif self.player == 2:  # pintar Circulo 
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE //2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)
    def next_turn(self):
        self.player = self.player % 2+1 #sacar el turno, uno con residuo y otro no 
    
    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'
    def reset(self):
        self.__init__()
    def isover(self):
        return self.board.final_state(show= True) !=0 or self.board.isfull()




def main():
    #object
    game = Game()
    board = game.board
    ai = game.ai
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
           
            
            if event.type == pygame.KEYDOWN:
                #g- gamemode
                if event.key == pygame.K_g:
                    game.change_gamemode()
                
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai


                #0 .random ai
                if event.key == pygame.K_0:
                    ai.level = 0
                #1- minimax ai
                if event.key == pygame.K_1:
                    ai.level = 1 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos  
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE 
                
                if board.empty_sqrs(row,col) and game.running:
                    game.make_move(row, col)
                    if game.isover():
                        game.running = False
                    print(board.squares )

        if game.gamemode == "ai" and game.player == ai.player and game.running:
            #actualiza la pantalla 
            pygame.display.update()

            #ai metodos
            row, col = ai.eval(board)
            game.make_move(row, col)
            

        pygame.display.update()
main()

