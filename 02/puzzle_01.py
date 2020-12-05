import sys


def read_keys(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().split("\n")


class Keypad:
    
    def __init__(self):
        self.loc_x = 1
        self.loc_y = 1
        self.keys = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    
    def move(self, inst):
        
        for m in inst:
            if m == "U":
                self.loc_y -= 1
            elif m == "D":
                self.loc_y += 1
            elif m == "L":
                self.loc_x -= 1
            elif m == "R":
                self.loc_x += 1
            
            if self.loc_x < 0:
                self.loc_x = 0
            if self.loc_x > 2:
                self.loc_x = 2
            if self.loc_y < 0:
                self.loc_y = 0
            if self.loc_y > 2:
                self.loc_y = 2
            
    
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