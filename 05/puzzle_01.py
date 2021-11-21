#!/usr/bin/python3

import hashlib

# Return a set of candidate password characters
def find_candidates(door_id, count=8):
    found = 0
    idx = 0
    while (found < count):
        candidate = door_id + str(idx)
        digest = hashlib.md5(candidate.encode()).hexdigest()
        if digest.startswith("00000"):
            yield (idx, digest)
            found += 1
        idx += 1


def find_passcode(door_id):
    digits = []
    for (idx, digest) in find_candidates(door_id):
        digits.append(digest[5])
    
    return "".join(digits)

    
if __name__ == "__main__":
    door_id = "cxdnnyjw"
    print("%s == %s" % (door_id, find_passcode(door_id),))