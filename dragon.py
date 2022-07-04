R = 0
L = 1


def next_steps(sequence: list[int]) -> list[int]:
    """
    Takes in a dragon curve sequence n, and returns the next items up to sequence n+1,
    i.e.:
        when sequence=[R], returns [R, L]

    Each dragon curve iteration can be found by copying the previous iteration,
    then an R, then a second copy of the previous iteration
    in reverse order with the L and R letters swapped.

    Source: https://en.wikipedia.org/wiki/Dragon_curve

    Args:
        sequence (str): dragon curve sequence, formatted "RRL" for sequence 2 of the dragon curve

    Returns:
        str: sequence n+1
    """
    return [R] + swap(reversed(sequence))


def swap(sequence: list[int]) -> list[int]:
    """
    Swap a dragon curve sequence.
    i.e.:
     when sequence [R, R, L], returns [L, L, R]
    """
    return [1 - letter for letter in sequence]


def dragon(n_iterations: int) -> list[int]:
    """Takes in a number n, an return the dragon curve sequence i.e.:
    When n=2, returns [R, R, L]

    Args:
        n_iterations (int): number of iterations of the dragon curve

    Returns:
        list: The dragon curve Sequence
    """
    sequence = [R,]
    for i in range(0, n_iterations):
        sequence.extend(next_steps(sequence))
    return sequence
