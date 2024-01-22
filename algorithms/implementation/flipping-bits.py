def _flip(b):
    return "0" if b == "1" else "1"


def flipping_bits(n):
    return n ^ 0xFFFFFFFF
    # return int("".join(list(map(_flip, bin(n)[2:].zfill(32)))), 2)


print(flipping_bits(9))
