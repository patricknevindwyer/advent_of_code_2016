#!/usr/bin/python3

import re
import sys


def read_input(filename):
    with open(filename, "r") as file:
        return file.read()


# could we assume non-overlapping?
# INCOMPLETE

def decompress(stream):
    print("$$ %d" % (len(stream),))
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


def wrapper(stream):
    lead_size = 0
    stream_suffix = stream
    
    while "(" in stream_suffix:
        # find our pivot
        pivot = stream_suffix.find("(")
        stream_suffix = stream_suffix[pivot:]
        lead_size += pivot
        stream_suffix = decompress(stream_suffix)
    return lead_size + len(stream_suffix)
    

if __name__ == "__main__":
    raw = read_input(sys.argv[-1])
    dec = wrapper(raw)
    print("decompressed size == %d" % (dec,))
    