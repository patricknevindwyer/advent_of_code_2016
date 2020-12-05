import sys


def read_keys(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().split("\n")


class Keypad:
    
    def __init__(self):
        self.loc_x = 0
        self.loc_y = 3
        self.keys = [
            [None, None, "1", None, None],
            [None, "2", "3", "4", None],
            ["5", "6", "7", "8", "9"],
            [None, "A", "B", "C", None],
            [None, None, "D", None, None]
        ]
    
    def move(self, inst):
        
        for m in inst:
            n_x = self.loc_x
            n_y = self.loc_y
            if m == "U":
                n_y = self.loc_y - 1
            elif m == "D":
                n_y = self.loc_y + 1
            elif m == "L":
                n_x = self.loc_x - 1
            elif m == "R":
                n_x = self.loc_x + 1
            
            # what don't we do?
            if n_x < 0:
                n_x = 0
            if n_x > 4:
                n_x = 4
            if n_y < 0:
                n_y = 0
            if n_y > 4:
                n_y = 4
            
            if self.keys[n_y][n_x] == None:
                n_x = self.loc_x
                n_y = self.loc_y
            
            
            self.loc_x = n_x
            self.loc_y = n_y
    
    def current_key(self):
        return self.keys[self.loc_y][self.loc_x]


if __name__ == "__main__":
    insts = read_keys(sys.argv[-1])
    
    keys = []
    keypad = Keypad()
    
    for inst in insts:
        keypad.move(inst)
        keys.append(keypad.current_key())
    
    print("".join([str(k) for k in keys]))