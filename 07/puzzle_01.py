#!/usr/bin/python3

import sys


def read_addresses(filename):
    with open(filename, "r") as file:
        return file.read().split("\n")


def supports_tls(address):
    """
    Determine if an address support/matches the TLS criteria
    """
    
    # test all runs, and make sure it's not in a bracketed range
    tls_seqs = list(get_sequences(address))
    
    has_bracketed_tls = False
    
    for tls_seq in tls_seqs:
        if tls_seq[1] > 0:
            has_bracketed_tls = True
    
    if has_bracketed_tls:
        return False
    
    if len(tls_seqs) > 0:
        return True
    
    return False
    

def get_sequences(address):
    
    bracket_depth = 0
    
    for idx in range(len(address) - 3):
        cars = address[idx:idx+4]
        
        if cars[0] == "[":
            bracket_depth += 1
        if cars[0] == "]":
            bracket_depth -= 1
            
        # is this a sequence?
        if cars[0] == cars[-1] and cars[1] == cars[2] and cars[0] != cars[1]:
            yield (idx, bracket_depth, cars)


if __name__ == "__main__":
    addrs = read_addresses(sys.argv[-1])
    supported = 0
    for addr in addrs:
        if supports_tls(addr):
            supported += 1
            print("[+] -- %s" % (addr,))
        else:
            print("[-] -- %s" % (addr,))
    print("%d addresses support TLS" % (supported,))