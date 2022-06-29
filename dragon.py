""" Each dragon curve iteration can be found by copying the previous iteration, 
    then an R, then a second copy of the previous iteration 
    in reverse order with the L and R letters swapped.[1]

    https://en.wikipedia.org/wiki/Dragon_curve
"""
R = "R"
L = "L"


def iterate(sequence: str):
    sequence = sequence+R+swapLetters(sequence[::-1])
    return sequence


def swapLetters(sequence: str):
    newSequence = ""
    for letter in sequence:
        if letter == R:
            newSequence = newSequence + L
        else:
            newSequence = newSequence + R
    return newSequence


def dragon(n_iterations: int) -> str:
    initial_sequence = R
    for i in range(0, n_iterations):
        initial_sequence = iterate(initial_sequence)
    return initial_sequence
