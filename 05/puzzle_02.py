#!/usr/bin/python3

import hashlib

# Return a set of candidate password characters
def find_candidates(door_id):
    idx = 0
    while True:
        candidate = door_id + str(idx)
        digest = hashlib.md5(candidate.encode()).hexdigest()
        if digest.startswith("00000"):
            yield (idx, digest)
        idx += 1


def find_passcode(door_id):
    digits = ["_", "_", "_", "_", "_", "_", "_", "_"]
    for (idx, digest) in find_candidates(door_id):
        
        pos = digest[5]
        
        if pos not in "01234567":
            continue
            
        pos = int(pos)
        car = digest[6]
                    
        if digits[pos] == "_":
            digits[pos] = car
        
        if "_" not in digits:
            break
    
    return "".join(digits)

    
if __name__ == "__main__":
    door_id = "cxdnnyjw"
    print("%s == %s" % (door_id, find_passcode(door_id),))