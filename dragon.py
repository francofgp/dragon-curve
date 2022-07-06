from itertools import count


R = 1
L = 0


def dragon():
    """Yields an infinite dragon curve.

    dragon(n) is the complement of the bit to the left of the least
    significant "1" in the binary expansion of n+1.

    E.g., n = 3, n+1 = 4 = 100_2, so a(3) = (complement of bit to left of 1) = 1. -

    Robert L. Brown, Nov 28 2001 [Adjusted to match offset by
    N. J. A. Sloane, Apr 15 2021]
    """
    for n in count():
        binary = f"0{n+1:b}"
        yield 1 - int(binary[binary.rfind("1") - 1])
