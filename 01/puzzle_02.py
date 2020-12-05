import sys


class Map:
    
    def __init__(self, instructions):
        self.instructions = instructions
        self.loc_x = 0
        self.loc_y = 0
        self.heading = "N"
        self.locations = []
        
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
            
            # write out all of our steps
            if step_x != 0:
                base = self.loc_x
                mod = int(abs(step_x) / step_x)
                for x_off in range(abs(step_x)):
                    self.locations.append((self.loc_x + (x_off * mod), self.loc_y))
            
            if step_y != 0:
                base = self.loc_y
                mod = int(abs(step_y) / step_y)
                for y_off in range(abs(step_y)):
                    self.locations.append((self.loc_x, self.loc_y + (y_off * mod)))
            
            self.loc_x += step_x
            self.loc_y += step_y
            

            
    def distance_from_start(self, loc_x = None, loc_y = None):
        """
        Manhattan distance from 0, 0
        """
        if loc_x == None:
            loc_x = self.loc_x
        if loc_y == None:
            loc_y = self.loc_y
            
        return abs(loc_x) + abs(loc_y)
        
    def find_first_loop_location(self):
        """
        Return the location of the first loop we visit twice
        """
        hits = {}
        
        for loc in self.locations:
            if loc in hits:
                return loc
            hits[loc] = True
            

def read_instructions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        insts = f.read()
    
    return insts.split(", ")


if __name__ == "__main__":
    
    instructions = read_instructions(sys.argv[-1])
    m = Map(instructions)
    m.walk()
    
    (x, y) = m.find_first_loop_location()
    dist = m.distance_from_start(loc_x=x, loc_y=y)
    
    print("loop (%d, %d)" % (x, y))
    print("Disance: %d" % (dist,))
