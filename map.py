from square_storage import Storage
from collections import defaultdict

class Map:
    def __init__(self, width, height, folder):
        self.width = width
        self.height = height
        self.storage = Storage(folder)
        self.squares = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(None)
            self.squares.append(row)
        self.fill_map()

    def fill_map(self):
        items_history = defaultdict(int)
        item = 0
        while item < (self.height*self.width):
            i = item // self.width
            j = item % self.width
            north_limit = self.squares[i-1][j].get_limit(2) if i > 0 else None
            west_limit = self.squares[i][j-1].get_limit(1) if j > 0 else None
            new_square = self.storage.get_random_square(north=north_limit, west=west_limit)
            if new_square is None:
                item -= 1
                i = item // self.width
                j = item % self.width
                self.squares[i][j] = None
            else:
                self.squares[i][j] = new_square
                item += 1
            items_history[item] += 1
            if items_history[item] > 10:
                for next_item in range(item, self.height*self.width):
                    items_history[next_item] = 0
                item -= 1
                
    def get_item(self, i, j):
        return self.squares[i][j]
    
    def get_squares(self):
        return self.squares

    def get_addresses(self):
        addresses = []
        for i in range(self.height):
            for j in range(self.width):
                addresses.append(self.squares[i][j].get_address())
        return addresses

    def get_rotations(self):
        rotations = []
        for i in range(self.height):
            for j in range(self.width):
                rotations.append(self.squares[i][j].get_rotation())
        return rotations