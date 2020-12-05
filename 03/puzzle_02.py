import sys
import json


def read_triangles(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    data = []
    triangles = []
    
    for line in raw.split("\n"):
        bits = line.strip().split(" ")
        bits = [b for b in bits if b.strip() != ""]
        nums = [int(n) for n in bits]
        data.append(nums)
    
    # pivot our triangles by segmented columns
    sections = int(len(data) / 3)
    
    for base_idx in range(sections):
        row_idx = base_idx * 3
        for col_idx in range(3):
            triangles.append(
                (
                    data[row_idx][col_idx],
                    data[row_idx + 1][col_idx],
                    data[row_idx + 2][col_idx]                    
                )
            )
    
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
