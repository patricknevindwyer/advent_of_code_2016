import sys


def read_triangles(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    triangles = []
    
    for line in raw.split("\n"):
        bits = line.strip().split(" ")
        bits = [b for b in bits if b.strip() != ""]
        nums = [int(n) for n in bits]
        triangles.append(nums)
    
    return triangles
    

def remove_impossible(triangles):
    poss = []
    
    for tri in triangles:
        t = sorted(tri)
        if t[0] + t[1] > t[2]:
            poss.append(tri)
    return poss


if __name__ == "__main__":
    tris = read_triangles(sys.argv[-1])
    poss = remove_impossible(tris)
    print("%d out of %d are valid" % (len(poss), len(tris)))