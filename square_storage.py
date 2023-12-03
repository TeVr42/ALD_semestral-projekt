import os
import random
from square import Square

class Storage:
    def __init__(self, adresar):
        files = os.listdir('static/squares/' + adresar)
        self.all_squares = []
        for file in files:
            for i in range(4):
                rotated_sides = ""
                for j in range(4):
                    rotated_sides += file[(j-i)%4]
                new_square = Square(
                    rotated_sides[0], rotated_sides[1], rotated_sides[2], rotated_sides[3],
                    filepath="squares/"+adresar+"/"+file,
                    rotation=i
                    )
                self.all_squares.append(new_square)
                
    def get_random_square(self, north=None, east=None, south=None, west=None):
        possible_squares = []
        for square in self.all_squares:
            if square.is_suitable(north, east, south, west):
                possible_squares.append(square)
        if len(possible_squares) == 0:
            return None
        return random.choice(possible_squares)