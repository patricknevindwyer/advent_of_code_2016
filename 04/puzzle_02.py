import sys


def read_rooms(filename):
    """
    Read a room file, returning the room name, a sector id, and
    a checksum.
    """
    rooms = []
    
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    for line in raw.split("\n"):
        room_raw, chk_raw = line.split("[")
        
        # gather all the pieces of a room code
        room = "".join(room_raw.split("-")[:-1])
        sector = int(room_raw.split("-")[-1])
        
        chk = chk_raw[:-1]
        rooms.append({"room": room, "sector": sector, "checksum": chk, "name_parts": room_raw.split("-")[:-1] })
        
    return rooms


def is_valid_room(room):
    digs = {}
    for c in room["room"]:
        if c not in digs:
            digs[c] = 0
        digs[c] += 1
    
    bits = digs.items()
    
    # sort first by alpha, then by count
    bits_sorted = sorted(bits, key=lambda b: b[0])
    bits_sorted = sorted(bits_sorted, key=lambda b: b[1], reverse=True)
    
    # calculte checksum
    calc_sum = "".join([c[0] for c in bits_sorted[:5]])
    return calc_sum == room["checksum"]


def decrypt_room(room):
    parts = room["name_parts"]
    decrypted_parts = []
    for part in parts:
        decrypted_parts.append(
            "".join([letter_shift(c, room["sector"]) for c in part])
        )
    return " ".join(decrypted_parts)
    

def letter_shift(l, rots):
    alphas = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    idx = alphas.find(l) + (rots % 26)
    return alphas[idx]
    

if __name__ == "__main__":
    rooms = read_rooms(sys.argv[-1])
    rooms = [room for room in rooms if is_valid_room(room)]
    for room in rooms:
        if decrypt_room(room) == "northpole object storage":
            print(room["sector"])