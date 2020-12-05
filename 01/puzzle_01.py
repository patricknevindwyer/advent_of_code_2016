import sys


class Map:
    
    def __init__(self, instructions):
        self.instructions = instructions
        self.loc_x = 0
        self.loc_y = 0
        self.heading = "N"
        
    def walk(self):
        """
        Interpret our directions and start walking
        """
        headings = ["N", "E", "S", "W"]
        
        for inst in self.instructions:
            
            # parse the instructions
            dir_change = inst[0]
            dist = int(inst[1:])
            
            # figure out our new neading
            wheel = 0
            if dir_change == "L":
                wheel = -1
            else:
                wheel = 1
                        
            cur_dir = headings.index(self.heading)
            nex_dir = cur_dir + wheel
            
            if nex_dir == -1:
                self.heading = headings[-1]
            elif nex_dir == 4:
                self.heading = headings[0]
            else:
                self.heading = headings[nex_dir]
            
            # directionality
            step_x = 0
            step_y = 0
            
            if self.heading == "N":
                step_y = -1 * dist
            elif self.heading == "S":
                step_y = dist
            elif self.heading == "E":
                step_x = dist
            elif self.heading == "W":
                step_x = -1 * dist
            
            self.loc_x += step_x
            self.loc_y += step_y
    
    def distance_from_start(self):
        """
        Manhattan distance from 0, 0
        """
        return abs(self.loc_x) + abs(self.loc_y)


def read_instructions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        insts = f.read()
    
    return insts.split(", ")


if __name__ == "__main__":
    
    instructions = read_instructions(sys.argv[-1])
    m = Map(instructions)
    m.walk()
    print("location (%d, %d)" % (m.loc_x, m.loc_y))
    print("Disance: %d" % (m.distance_from_start(),))
