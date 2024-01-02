import numpy as np

zero = np.array([1, 0])
one = np.array([0, 1])
plus = 1/2**0.5 * (zero + one)
minus = 1/2**0.5 * (zero - one)

from measurement import *
def lec_4_example():
    """
    Example from lec 4 notes: https://math.mit.edu/~shor/435-LN/Lecture_04.pdf
    """

    phi = 4/5*zero + 3/5*one

    assert (np.isclose(raw_probabilities(phi, plus), 49/50, 0.01))
    assert (np.isclose(raw_probabilities(phi, minus), 1/50, 0.01))

    pi_A = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    pi_B = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    state = np.array([5/10, 7/10, 5/10, 1/10])
    print(measure(state, pi_A))

if __name__ == "__main__":
    lec_4_example()
