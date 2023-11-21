import pygame

class Game:
    def __init__(self):
        pygame.init()

        # Create a Pygame surface
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_w, self.screen_h = self.screen.get_size()
        window = pygame.display.set_mode((self.screen_w, self.screen_h), pygame.FULLSCREEN)

        # Grid parameters
        self.grid_width = 10  # Number of columns
        self.grid_height = 10  # Number of rows
        self.cell_size = 40  # Size of each grid cell
        self.margin = 160     # Size of margin
        self.grid_total_width = self.grid_width * self.cell_size
        self.grid_total_height = self.grid_height * self.cell_size

        self.grid_x = (self.screen_w - self.grid_total_width) // 2
        self.grid_y = (self.screen_h - self.grid_total_height) // 2

        self.black = pygame.Color('#000000')
        self.white = pygame.Color('#ffffff')

        self.p1_grid = [[0 for x in range(self.grid_width)] for x in range(self.grid_height)]
        self.p2_grid = [[0 for x in range(self.grid_width)] for x in range(self.grid_height)]

    def place_ship(self, ship_positions):  #1-4, [2[2]], [2[3]], [2[4]], p1_grid[0[0]]
        self.check_valid_placement(ship_positions)      #                                    [y[x]]
        for positions in ship_positions:
            self.p1_grid[positions[1]][positions[0]] = 1


    # def rotate_ship(self, ship_length, ship_positions):
    #     is_horizontal = all(y == ship_positions[0][1] for x, y in ship_positions)
    #     if is_horizontal:
    #         for ship_postion in(ship_positions):
    #             for y,x in(ship_postion):

    def check_valid_placement(self, ship_positions):        #1-4, [2, 2], [2][3], [2][4]], p1_grid[0[0]]
        for position in ship_positions:
            pos_x = position[0]
            pos_y = position[1]
            for x in range(max(0, pos_x - 1), min(self.grid_width, pos_x + 1)):
                for y in range(max(0, pos_y - 1), min(self.grid_height, pos_y + 1)):
                    if self.p1_grid[y][x] != 0:
                        return False
            return True


    def draw_single_grid(self, x, y):
        for x_pos in range(x, x + self.grid_total_width, self.cell_size):
            for y_pos in range(y, y + self.grid_total_height, self.cell_size):
                pygame.draw.rect(self.screen, self.white, (x_pos, y_pos, self.cell_size, self.cell_size), 1)

    def draw_grids(self, num_of_grids, margin):
        total_width = num_of_grids * self.grid_total_width + (num_of_grids - 1) * margin
        x_start = (self.screen_w - total_width) // 2
        y_start = (self.screen_h - self.grid_total_height) // 2

        for i in range(num_of_grids):
            self.draw_single_grid(x_start, y_start)
            x_start += self.grid_total_width + margin

    def run_game(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False  # Exit the game when the Esc key is pressed

            self.screen.fill((0, 0, 0))  # Clear the screen with a black background
            self.draw_grids(2, self.margin)  # Draw the grid
            #self.draw_single_grid(self.grid_x,self.grid_y)
            self.place_ship([[2, 2], [2,3], [2,4]])
            pygame.display.flip()
            clock.tick(60)  # Limit the frame rate to 60 frames per second

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run_game()