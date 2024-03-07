import pygame
import copy


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
            coords.append(f"{chr(position[1] + 65)}{position[0] + 1}")
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

        # Initialize variables for holding ship data
        self.p1_grid = [[0 for _ in range(10)] for _ in range(10)]
        self.p1_all_ships_id = {}  # key SHIP_ID, value list of ship position coords

    def add_ship(self, positions):
        if self.check_valid_placement(positions):
            ship = Ship(positions, self.next_ship_id)
            self.ships.append(ship)
            self.next_ship_id += 1
            self.place_ship(positions, self.next_ship_id - 1)

    def place_ship(self, ship_positions, ship_id):
        for position in ship_positions:
            self.p1_grid[position[1] - 1][position[0] - 1] = ship_id
        self.p1_all_ships_id[ship_id] = Ship.get_coords(ship_positions)

    def check_valid_placement(self, ship_positions):
        for position in ship_positions:
            if isinstance(position[0], str):  # Check if the position is in the format [letter, number]
                grid_pos_y = ord(position[0]) - 65
                grid_pos_x = int(position[1]) - 1
            else:  # If position is in [number, number] format
                grid_pos_y = position[1] - 1
                grid_pos_x = position[0] - 1

            for y in range(max(0, grid_pos_y - 1), min(10, grid_pos_y + 2)):
                for x in range(max(0, grid_pos_x - 1), min(10, grid_pos_x + 2)):
                    if self.p1_grid[y][x] != 0:
                        return False
        return True

    def delete_ship(self, ship_id):
        if ship_id in self.p1_all_ships_id:
            self.delete_ship_from_grid(self.p1_all_ships_id[ship_id])
            del self.p1_all_ships_id[ship_id]

    def delete_ship_from_grid(self, ship_positions):
        for position in ship_positions:
            if isinstance(position[0], str):
                grid_pos = (ord(position[0]) - 65, int(position[1]) - 1)
            else:
                grid_pos = (position[0] - 1, position[1] - 1)
            self.p1_grid[grid_pos[1]][grid_pos[0]] = 0

    def rotate_ship(self, ship_id):
        if ship_id in self.p1_all_ships_id:
            current_ship_positions = self.p1_all_ships_id[ship_id]
            new_ship_positions = Ship.rotate(copy.deepcopy(current_ship_positions))

            self.delete_ship_from_grid(current_ship_positions)

            if self.check_valid_placement(new_ship_positions):
                self.place_ship(new_ship_positions, ship_id)

    def draw_ships(self):
        for ship in self.ships:
            for position in ship.positions:
                pygame.draw.rect(self.screen, pygame.Color('#ffffff'), (
                    self.grid.grid_pos[f"{chr(position[0] + 65)}{position[1] + 1}"][0],
                    self.grid.grid_pos[f"{chr(position[0] + 65)}{position[1] + 1}"][1],
                    self.grid.cell_size, self.grid.cell_size), 0)

    def run_game(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        mouse_position = pygame.mouse.get_pos()
                        grid_coord = self.get_grid_coord(mouse_position)
                        if grid_coord:
                            self.rotate_ship(grid_coord)
                    elif event.button == 3:  # Right click
                        mouse_position = pygame.mouse.get_pos()
                        grid_coord = self.get_grid_coord(mouse_position)
                        if grid_coord:
                            ship_id = self.p1_grid[grid_coord[1] - 1][grid_coord[0] - 1]
                            if ship_id != 0:
                                self.delete_ship(ship_id)

            self.screen.fill(pygame.Color('#000000'))  # Clear the screen with a black background
            self.grid.draw_grid()  # Draw the grid
            self.draw_ships()  # Draw the ships
            pygame.display.flip()
            clock.tick(60)  # Limit the frame rate to 60 frames per second

        pygame.quit()

    def get_grid_coord(self, mouse_position):
        for key, value in self.grid.grid_pos.items():
            if value[0] <= mouse_position[0] <= value[0] + self.grid.cell_size and \
                    value[1] <= mouse_position[1] <= value[1] + self.grid.cell_size:
                return [ord(key[0]) - 64, int(key[1])]
        return None


if __name__ == "__main__":
    game = Game()
    game.add_ship([[2, 2], [2, 3], [2, 4], [2, 5]])  # Example ship placement
    game.run_game()
