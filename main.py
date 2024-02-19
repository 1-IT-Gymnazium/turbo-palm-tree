import pygame
import  copy

class Game:
    def __init__(self):
        pygame.init()

        # Create a Pygame surface
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_w, self.screen_h = self.screen.get_size()

        # Grid parameters
        self.grid_width = 10  # Number of columns
        self.grid_height = 10  # Number of rows
        self.cell_size = 40  # Size of each grid cell
        self.margin = 160  # Size of margin
        self.grid_total_width = self.grid_width * self.cell_size
        self.grid_total_height = self.grid_height * self.cell_size

        self.grid_x = (self.screen_w - self.grid_total_width) // 2
        self.grid_y = (self.screen_h - self.grid_total_height) // 2

        self.black = pygame.Color('#000000')
        self.white = pygame.Color('#ffffff')

        self.p1_grid = [[0 for x in range(self.grid_width)] for x in range(self.grid_height)]
        self.p1_grid_pos = {}  # All grid cells coords and pixel positions
        self.p1_all_ships_id = {}  # key SHIP_ID, value list of ship position coords
        self.p2_grid = [[0 for x in range(self.grid_width)] for x in range(self.grid_height)]
        self.p2_grid_pos = {}

    def place_ship(self, ship_positions):  # 1-4, [[2, 2], [2,3], [2,4]], p1_grid[0[0]]
        """

        :param ship_positions:
        :return:
        """
        if self.check_valid_placement(ship_positions):
            self.p1_all_ships_id[len(self.p1_all_ships_id)] = self.get_coords(ship_positions)
            for position in ship_positions:
                self.p1_grid[position[1] - 1][position[0] - 1] = 1
        else:
            pass

    def delete_ship(self, get_mouse_position_output):
        if type(get_mouse_position_output[2]) == int:
            self.delete_ship_from_grid(self.p1_all_ships_id[get_mouse_position_output[2]])
            self.delete_ship_from_dict(get_mouse_position_output[2])

    def delete_ship_from_grid(self, ship_positions):
        for count, ele in enumerate(ship_positions):
            grid_pos = self.get_grid_pos_from_coords(ele)
            self.p1_grid[grid_pos[0]][grid_pos[1]] = 0
    def delete_ship_from_dict(self, get_ship_id):
        del self.p1_all_ships_id[get_ship_id]

    def rotate_ship(self, get_mouse_position_output):
        if type(get_mouse_position_output[2]) == int:
            mouse_position = get_mouse_position_output[0]
            grid_coord = get_mouse_position_output[1]
            ship_id = get_mouse_position_output[2]
            if isinstance(ship_id, int):
                p1_grid_original_position = copy.deepcopy(self.p1_grid)

                # Get the current ship positions
                current_ship_positions = self.p1_all_ships_id[ship_id]
                new_ship_positions = []

                for position in current_ship_positions:
                    a = ord(position[0]) - 64
                    b = position[1]
                    new_ship_positions.append([int(b),a])

                self.delete_ship_from_grid(current_ship_positions) #smazat v copy puvodni pozici, aby check valid nekontroloval novou pozici se starou, udelam funkci na mazani z gridu

                # Check if the new positions are valid
                if self.check_valid_placement(new_ship_positions):
                    self.place_ship(new_ship_positions)

                    # Update the ship positions in the dictionary
                    # self.p1_all_ships_id[ship_id] = self.get_coords(new_ship_positions)
                    self.delete_ship_from_dict(ship_id)
                else:
                    # Handle invalid rotation (optional)
                    pass

    def check_valid_placement(self, ship_positions):
        for position in ship_positions:
            grid_pos_y = position[1] - 1
            grid_pos_x = position[0] - 1
            for y in range(max(0, grid_pos_y - 1), min(self.grid_height, grid_pos_y + 2)):
                for x in range(max(0, grid_pos_x - 1), min(self.grid_width, grid_pos_x + 2)):
                    if self.p1_grid[y][x] != 0:
                        return False
        return True

    def draw_all_ships(self):
        for ship in self.p1_all_ships_id:
            for part in self.p1_all_ships_id[ship]:
                pygame.draw.rect(self.screen, self.white, (
                self.p1_grid_pos[f"{part}"][0], self.p1_grid_pos[f"{part}"][1], self.cell_size, self.cell_size), 0)

    def get_coords(self, input):  # Change from [3][5]([y][x]) to E3
        coords = []
        for coord in input:
            coords.append(f"{chr(coord[0] + 64)}{coord[1]}")
        return coords

    def get_grid_pos_from_coords(self, input):
        if isinstance(input, str):
            positionY = int(input[1]) - 1
            positionX = ord(input[0]) - 65
        return positionY, positionX

    def get_mouse_pos(self):
        mouse_position = pygame.mouse.get_pos()
        grid_coord = False
        ship_id = False
        for key, value in self.p1_grid_pos.items():
            if mouse_position[0] in range(value[0], (value[0] + self.cell_size) + 1) and mouse_position[1] in range(
                    value[1], (value[1] + self.cell_size) + 1):
                grid_coord = key
                for inner_key, inner_value in self.p1_all_ships_id.items():
                    for part_coord in inner_value:
                        if part_coord == grid_coord:
                            ship_id = inner_key
        return [mouse_position, grid_coord, ship_id]

    def draw_single_grid(self, x, y, num_grids):
        column_char = 65
        for x_pos in range(x, x + self.grid_total_width, self.cell_size):
            row_num = 1
            for y_pos in range(y, y + self.grid_total_height, self.cell_size):
                # kazdemu policku dat nazev A-J,1-10 a udelat dictionary nazev pozice : jeho (x,y) pozicu
                if num_grids == 0:
                    self.p1_grid_pos[f"{chr(column_char)}{row_num}"] = (x_pos, y_pos)
                else:
                    self.p2_grid_pos[f"{chr(column_char)}{row_num}"] = (x_pos, y_pos)

                pygame.draw.rect(self.screen, self.white, (x_pos, y_pos, self.cell_size, self.cell_size), 1)
                row_num = row_num + 1
            column_char = column_char + 1

    def draw_grids(self, num_of_grids, margin):
        total_width = num_of_grids * self.grid_total_width + (num_of_grids - 1) * margin
        x_start = (self.screen_w - total_width) // 2
        y_start = (self.screen_h - self.grid_total_height) // 2

        for i in range(num_of_grids):
            self.draw_single_grid(x_start, y_start, i)
            x_start += self.grid_total_width + margin

    def run_game(self):
        running = True
        clock = pygame.time.Clock()
        # self.place_ship([[2, 2], [2, 3], [2, 4], [2, 5]])
        # self.place_ship([[8, 10], [8, 9], [8, 7], [8, 8]])
        # self.place_ship([[6, 7], [7, 7], [8, 7]])
        self.place_ship([[4, 4], [5, 4], [6, 4]])
        # self.place_ship([[5, 5], [5, 6]])
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False  # Exit the game when the Esc key is pressed
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.rotate_ship(self.get_mouse_pos())
                    elif event.button == 3:
                        self.delete_ship(self.get_mouse_pos())

            self.screen.fill((0, 0, 0))  # Clear the screen with a black background
            self.draw_grids(1, self.margin)  # Draw the grid
            self.draw_all_ships()
            pygame.display.flip()
            clock.tick(60)  # Limit the frame rate to 60 frames per second

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()
