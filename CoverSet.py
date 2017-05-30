import random


class CoverSet(object):
    # class to represent a set and its subsets
    def __init__(self, n_range, set_size, n_subsets, max_k):
        """
        :param n_range: max value of numbers in set
        :param set_size: number of elements in set
        :param n_subsets: number of subsets
        """
        self.K = max_k
        possible_numbers = range(n_range)

        self._U = set(random.sample(possible_numbers, set_size))

        self._S = []
        control = set()

        for i in range(n_subsets - 1):
            sub_size = random.randrange(set_size)
            sub = set(random.sample(self._U, sub_size))
            self._S += [sub]
            control |= sub

        rest = self._U - control

        if rest:
            self._S += [rest]

    @property
    def U(self):
        return self._U

    @property
    def S(self):
        return self._S
