R = "R"
L = "L"


def iterate(sequence: str) -> str:
    """
    Takes in a dragon curve sequence n, and returns sequence n+1, 
    i.e.: 
        when n= "R", returns "RRL"

    Each dragon curve iteration can be found by copying the previous iteration, 
    then an R, then a second copy of the previous iteration 
    in reverse order with the L and R letters swapped.

    Source: https://en.wikipedia.org/wiki/Dragon_curve

    Args:
        sequence (str): dragon curve sequence, formatted "RRL" for sequence 2 of the dragon curve

    Returns:
        str: sequence n+1
    """
    sequence = sequence+R+swapLetters(sequence[::-1])
    return sequence


def swapLetters(sequence: str) -> str:
    """
    Swap a dragon curve sequence. 
    i.e.:
     when sequence "RRL", returns "LLR"
    """
    newSequence = ""
    for letter in sequence:
        if letter == R:
            newSequence = newSequence + L
        else:
            newSequence = newSequence + R
    return newSequence


def dragon(n_iterations: int) -> str:
    """Takes in a number n, an return the dragon curve sequence i.e.:
    When n=2, returns "RRL"

    Args:
        n_iterations (int): number of iterations of the dragon curve

    Returns:
        str: The dragon curve Sequence
    """
    initial_sequence = R
    for i in range(0, n_iterations):
        initial_sequence = iterate(initial_sequence)
    return initial_sequence
