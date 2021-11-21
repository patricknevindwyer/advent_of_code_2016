#!/usr/bin/python3

import sys


def read_addresses(filename):
    with open(filename, "r") as file:
        return file.read().split("\n")


def supports_ssl(address):
    """
    Determine if an address support/matches the TLS criteria
    """
    
    # test all runs, and make sure it's not in a bracketed range
    ssl_seqs = list(get_sequences(address))
        
    # compare sequence types, but let's group by sequence first
    seq_dict = {}
    
    for (idx, bracket_depth, cars) in ssl_seqs:
        
        # addresses are inverted inside blocks
        realized_car = cars
        if bracket_depth > 0:
            realized_car = cars[1] + cars[0] + cars[1]
            
        if realized_car not in seq_dict:
            seq_dict[realized_car] = []
        seq_dict[realized_car].append(bracket_depth)
    
    # now, if we have any sequence set that has a 0 and 1, we're good
    for bracket_depths in seq_dict.values():
        if 0 in bracket_depths and 1 in bracket_depths:
            return True
    
    return False
    

def get_sequences(address):
    
    bracket_depth = 0
    
    for idx in range(len(address) - 2):
        cars = address[idx:idx+3]
        
        # check for which sequence type?
        if cars[0] == "[":
            bracket_depth += 1
        if cars[0] == "]":
            bracket_depth -= 1
            
        # is this a sequence?
        if cars[0] == cars[-1] and cars[0] != cars[1]:
            yield (idx, bracket_depth, cars)


if __name__ == "__main__":
    addrs = read_addresses(sys.argv[-1])
    supported = 0
    for addr in addrs:
        if supports_ssl(addr):
            supported += 1
            print("[+] -- %s" % (addr,))
        else:
            print("[-] -- %s" % (addr,))
    print("%d addresses support SSL" % (supported,))