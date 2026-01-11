import sys, pygame

class Block:
    def __init__(self, grid):
        self.x = 5
        self.y = 2
        self.pos = pygame.Vector2(self.x, self.y)
        self.grid = grid
        self.locked = False
        
    def draw_block(self, grid):
        self.block_rect = pygame.Rect(int(self.pos.x * grid.cellsize + grid.padding / 2), int(self.pos.y * grid.cellsize + grid.padding / 2), grid.cellsize, grid.cellsize)
        pygame.draw.rect(grid.playfield_surface, "red", self.block_rect)
        
    def move_block(self, direction):
        # block has to go down each cycle
        if self.locked is False:
            self.pos += direction
        else:
            self.grid.update_grid_list(self)
            self.respawn_block()
             
    def check_landing(self, grid):
        if self.pos.y == grid.cellnumbers_height - 1:
            self.locked = True
            
    def respawn_block(self):
        self.pos = pygame.Vector2(self.x, self.y)
        self.locked = False

class Tetromino:
    def __init__(self):
        body = []

class Shape:
    
    # Shapes: 4 rotation states each (SRS-like pivot at (0,0) for simplicity)
    PIECES = {
    'I': [
        [( -1, 0), ( 0, 0), ( 1, 0), ( 2, 0)],
        [( 1, -1), ( 1,  0), ( 1, 1), ( 1, 2)],
        [( -1, 1), ( 0, 1), ( 1, 1), ( 2, 1)],
        [( 0, -1), ( 0,  0), ( 0, 1), ( 0, 2)]
    ],
    'O': [
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)]
    ],
    'T': [
        [(0, 0), (-1, 0), (1, 0), (0, 1)],
        [(0, 0), (0, -1), (0, 1), (1, 0)],
        [(0, 0), (-1, 0), (1, 0), (0, -1)],
        [(0, 0), (0, -1), (0, 1), (-1, 0)]
    ],
    'S': [
        [(0, 0), (1, 0), (0, 1), (-1, 1)],
        [(0, 0), (0, 1), (1, 0), (1, -1)],
        [(0, 0), (1, 0), (0, 1), (-1, 1)],
        [(0, 0), (0, 1), (1, 0), (1, -1)]
    ],
    'Z': [
        [(0, 0), (-1, 0), (0, 1), (1, 1)],
        [(0, 0), (0, -1), (1, 0), (1, 1)],
        [(0, 0), (-1, 0), (0, 1), (1, 1)],
        [(0, 0), (0, -1), (1, 0), (1, 1)]
    ],
    'J': [
        [(0, 0), (-1, 0), (-1, 1), (1, 0)],
        [(0, 0), (0, -1), (0, 1), (1, 1)],
        [(0, 0), (-1, 0), (1, 0), (1, -1)],
        [(0, 0), (0, -1), (0, 1), (-1, -1)]
    ],
    'L': [
        [(0, 0), (-1, 0), (1, 0), (1, 1)],
        [(0, 0), (0, -1), (0, 1), (1, -1)],
        [(0, 0), (-1, 0), (1, 0), (-1, -1)],
        [(0, 0), (0, -1), (0, 1), (-1, 1)]
    ],
    }

    COLORS = {
    'I': (0, 255, 255), 'O': (255, 217, 0), 'T': (200, 60, 200),
    'S': (0, 200, 0),   'Z': (200, 0, 0),   'J': (0, 0, 200),
    'L': (255, 120, 0),
    }

    
    def __init__(self):
        pass

class Grid:
    def __init__(self):
        # Initializing grid variables
        self.grid_list = []
        self.cellsize = 40
        self.cellnumbers_height = 20
        self.cellnumbers_width = 10
        self.padding = 3

        # Initializing grid List
        print('creating grid list')
        for row in range(self.cellnumbers_height):
            self.grid_list.append([])
            for col in range(self.cellnumbers_width):
                self.grid_list[row].insert(0,'0')
        print(self.grid_list)
        
        # Drawing Grid
        self.background_color = (30, 105, 166)
        self.grid_line_color = "black"
        self.playfield_surface = pygame.Surface((self.cellnumbers_width * 40 + self.padding, self.cellnumbers_height * 40 + self.padding))
        self.centered_rect = self.playfield_surface.get_rect(center=screen.get_rect().center)
    
    def update_grid_list(self, block):
        self.grid_list[int(block.pos.y)][int(block.pos.x)] = 1
        print(self.grid_list)
    
    def draw_playfield_grid(self):
        self.playfield_surface.fill(self.grid_line_color)
        for row in range(self.cellnumbers_height):
            for col in range(self.cellnumbers_width):
                self.grid_rect = pygame.Rect(int(col * self.cellsize + self.padding), int(row * self.cellsize + self.padding), self.cellsize - self.padding, self.cellsize - self.padding)
                pygame.draw.rect(self.playfield_surface, self.background_color, self.grid_rect)
        
        for y,row in enumerate(self.grid_list):
            for x,cell in enumerate(row):
                if cell != '0':
                    self.block_rect = pygame.Rect(int(x * self.cellsize + self.padding / 2), int(y * self.cellsize + self.padding / 2), self.cellsize, self.cellsize)
                    pygame.draw.rect(self.playfield_surface, "red", self.block_rect)

class Main:
    def __init__(self):
        self.grid = Grid()
        self.block = Block(self.grid)
        
    def update(self):
        self.block.check_landing(self.grid)
        self.block.move_block(pygame.Vector2(0,1))
    
    def draw_elements(self):
        screen.fill(self.grid.background_color)
        self.grid.draw_playfield_grid()
        self.block.draw_block(self.grid)
        self.load_playfield()
    
    def load_playfield(self):
        screen.blit(self.grid.playfield_surface, self.grid.centered_rect)
        
  
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()
running = True

main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT

GRAVITY_MS_NORMAL = 750     # normal gravity
GRAVITY_MS_SOFT   = 50      # soft drop gravity (fast)

soft_drop = False

pygame.time.set_timer(SCREEN_UPDATE, GRAVITY_MS_NORMAL)

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if main_game.block.pos.x > 0:
                    main_game.block.move_block(pygame.Vector2(-1,0))
            if event.key == pygame.K_RIGHT:
                if main_game.block.pos.x < 9:
                    main_game.block.move_block(pygame.Vector2(1,0))
            if event.key == pygame.K_DOWN and not soft_drop:
                soft_drop = True
                pygame.time.set_timer(SCREEN_UPDATE, GRAVITY_MS_SOFT)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and soft_drop:
                soft_drop = False
                pygame.time.set_timer(SCREEN_UPDATE, GRAVITY_MS_NORMAL)


    # fill the screen with a color to wipe away anything from last frame
    # playfield_surface.fill(playfield_color)

    # RENDER YOUR GAME HERE
    main_game.draw_elements()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()