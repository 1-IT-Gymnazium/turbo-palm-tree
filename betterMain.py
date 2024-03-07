import pygame
import  copy

class GameBoard:
    def __init__(self, screen, grid_width, grid_height, cell_size, margin, game_manager):
        self.screen = screen
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        self.margin = margin
        self.grid_total_width = grid_width * cell_size
        self.grid_total_height = grid_height * cell_size
        self.grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
        self.grid_pos = {}
        self.game_manager = game_manager

    def draw_single_grid(self, x, y, num_grids):
        column_char = 65
        for x_pos in range(x, x + self.grid_total_width, self.cell_size):
            row_num = 1
            for y_pos in range(y, y + self.grid_total_height, self.cell_size):
                # kazdemu policku dat nazev A-J,1-10 a udelat dictionary nazev pozice : jeho (x,y) pozicu
                if num_grids == 0:
                    self.grid_pos[f"{chr(column_char)}{row_num}"] = (x_pos, y_pos)
                # else:
                #     self.grid_pos[f"{chr(column_char)}{row_num}"] = (x_pos, y_pos)

                pygame.draw.rect(self.screen, pygame.Color('#ffffff'), (x_pos, y_pos, self.cell_size, self.cell_size), 1)
                row_num = row_num + 1
            column_char = column_char + 1

    def draw_grids(self, num_of_grids, margin):
        total_width = num_of_grids * self.grid_total_width + (num_of_grids - 1) * margin
        x_start = (self.game_manager.screen_w - total_width) // 2
        y_start = (self.game_manager.screen_h - self.grid_total_height) // 2

        for i in range(num_of_grids):
            self.draw_single_grid(x_start, y_start, i)
            x_start += self.grid_total_width + margin
class Ship:
    def __init__(self, ship_id, ship_positions):
        self.ship_id = ship_id
        self.ship_positions = ship_positions

class Player:
    def __init__(self, player_id, game_board):
        self.player_id = player_id
        self.game_board = game_board
        self.ships = {}

    def place_ship(self, ship_positions):
        # Place a ship on the player's game board
        pass

    def delete_ship(self, ship_id):
        # Delete a ship from the player's game board
        pass

    def rotate_ship(self, ship_id):
        # Rotate a ship on the player's game board
        pass

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_w, self.screen_h = self.screen.get_size()
        self.grid_width = 10  # Number of columns
        self.grid_height = 10  # Number of rows
        self.cell_size = 40  # Size of each grid cell
        self.margin = 160  # Size of margin
        self.player1 = Player(1, GameBoard(self.screen, self.grid_width, self.grid_height, self.cell_size, self.margin, self))
        self.player2 = Player(2, GameBoard(self.screen, self.grid_width, self.grid_height, self.cell_size, self.margin, self))
        self.current_player = self.player1
        self.player1.grid

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.current_player.rotate_ship()
                elif event.button == 3:
                    self.current_player.delete_ship()
        return True

    def run_game(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            running = self.handle_events()
            self.screen.fill((0, 0, 0))
            self.player1.game_board.draw_grids(1, self.margin)
            #self.player2.game_board.draw()
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.run_game()
