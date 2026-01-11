import sys, pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()
running = True


class Block:
    def __init__(self):
        self.x = 5
        self.y = 2
        self.pos = pygame.Vector2(self.x, self.y)
        self.locked = False
        
    def draw_block(self):
        self.block_rect = pygame.Rect(int(self.pos.x * cellsize), int(self.pos.y * cellsize), cellsize, cellsize)
        pygame.draw.rect(playfield_surface, "red", self.block_rect)
        
    def drop_block(self):
        # block has to go down each cycle
        if self.locked is False:
            self.pos.y += 1
        
    def check_landing(self):
        if self.pos.y == cellnumbers_height - 1:
            self.locked = True

class Main:
    def __init__(self):
        self.block = Block()
    
    def update(self):
        self.block.check_landing()
        self.block.drop_block()
    
    def draw_elements(self):
        screen.fill(background_color)
        playfield_surface.fill(playfield_color)
        self.draw_playfield_grid()
        self.block.draw_block()
        self.draw_playfield()
    
    def draw_playfield(self):
        screen.blit(playfield_surface, centered_rect)
        
    def draw_playfield_grid(self):
        print('draw grid')
        padding = 2
        for row in range(cellnumbers_height):
            for col in range(cellnumbers_width):
                self.grid_rect = pygame.Rect(int(col * cellsize + padding / 2), int(row * cellsize + padding / 2), cellsize - padding, cellsize - padding)
                pygame.draw.rect(playfield_surface, background_color, self.grid_rect)

cellsize = 40
cellnumbers_height = 20
cellnumbers_width = 10

# background_color = (140, 29, 60)
background_color = (30, 105, 166)
playfield_color = "black"
playfield_surface = pygame.Surface((cellnumbers_width * 40, cellnumbers_height * 40))
centered_rect = playfield_surface.get_rect(center=screen.get_rect().center)
  
main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 750)

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()

    # fill the screen with a color to wipe away anything from last frame
    # playfield_surface.fill(playfield_color)

    # RENDER YOUR GAME HERE
    main_game.draw_elements()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()