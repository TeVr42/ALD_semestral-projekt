class Square:
    def __init__(self, north, east, south, west, filepath, rotation):
        self.sides = [north, east, south, west]
        self.path = filepath
        self.rotation = rotation
    
    def is_suitable(self, north=None, east=None, south=None, west=None):
        if north is not None:
            if north != self.sides[0]:
                return False
        if east is not None:
            if east != self.sides[1]:
                return False
        if south is not None:
            if south != self.sides[2]:
                return False
        if west is not None:
            if west != self.sides[3]:
                return False
        return True

    def get_limit(self, side_index):
        return self.sides[side_index]
    
    def get_address(self):
        return self.path

    def get_rotation(self):
        return self.rotation

    def to_string(self):
        return f"{self.sides}\n{self.path}, pootoceni {self.rotation}"