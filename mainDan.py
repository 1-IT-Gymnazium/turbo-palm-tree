import pygame


class Grid:
    def __init__(self, width, height, cell_size, margin, screen):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.margin = margin
        self.screen = screen
        self.grid_pos = {}

    def draw_single_grid(self, x, y):
        column_char = 65
        for x_pos in range(x, x + self.width * self.cell_size, self.cell_size):
            row_num = 1
            for y_pos in range(y, y + self.height * self.cell_size, self.cell_size):
                self.grid_pos[f"{chr(column_char)}{row_num}"] = (x_pos, y_pos)
                pygame.draw.rect(self.screen, pygame.Color('#ffffff'), (x_pos, y_pos, self.cell_size, self.cell_size),
                                 1)
                row_num += 1
            column_char += 1

    def draw_grid(self):
        total_width = self.width * self.cell_size
        x_start = (self.screen.get_width() - total_width) // 2
        y_start = (self.screen.get_height() - self.height * self.cell_size) // 2
        self.draw_single_grid(x_start, y_start)


class Ship:
    def __init__(self, positions, ship_id):
        self.positions = positions
        self.ship_id = ship_id

    @staticmethod
    def get_coords(positions):
        coords = []
        for position in positions:
            coords.append(f"{chr(position[0] + 64)}{position[1]}")
        return coords

    @staticmethod
    def rotate(positions):
        new_positions = []
        for position in positions:
            new_positions.append([position[1], position[0]])
        return new_positions


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # Example resolution
        self.grid = Grid(10, 10, 40, 160, self.screen)
        self.ships = []
        self.next_ship_id = 0

    def add_ship(self, positions):
        if self.check_valid_placement(positions):
            ship = Ship(positions, self.next_ship_id)
            self.ships.append(ship)
            self.next_ship_id += 1

    def check_valid_placement(self, positions):
        # Implement validation logic
        return True

    def draw_ships(self):
        for ship in self.ships:
            for position in ship.positions:
                pygame.draw.rect(self.screen, pygame.Color('#ffffff'), (
                    self.grid.grid_pos[f"{chr(position[0] + 64)}{position[1]}"][0],
                    self.grid.grid_pos[f"{chr(position[0] + 64)}{position[1]}"][1],
                    self.grid.cell_size, self.grid.cell_size), 0)

    def run_game(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False

            self.screen.fill(pygame.Color('#000000'))
            self.grid.draw_grid()
            self.draw_ships()
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.add_ship([[2, 2], [2, 3], [2, 4], [2, 5]])
    game.run_game()
