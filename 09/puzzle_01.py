#!/usr/bin/python3

import re
import sys


def read_input(filename):
    with open(filename, "r") as file:
        return file.read()


def decompress(stream):
    
    out = []
    
    while len(stream) > 0:
        head = re.search(r"^\((\d+)x(\d+)\)", stream)
        
        # skip - just pass the character through
        if head is None:
            out.append(stream[0])
            stream = stream[1:]
            continue
        
        # we have a match - prune our start
        stream = stream[head.span()[1]:]
        
        # grab the next sets of characters
        pull = int(head.groups()[0])
        reps = int(head.groups()[1])
        out.append(stream[:pull] * reps)
        stream = stream[pull:]
    
    
    return "".join(out)


if __name__ == "__main__":
    raw = read_input(sys.argv[-1])
    dec = decompress(raw)
    print("decompressed size == %d" % (len(dec),))
    