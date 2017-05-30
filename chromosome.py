# todo-me set subset size limit to [1, test_instance.kmax]
import numpy as np
import copy
import random


class Chromosome(object):
    """ Class to represent a collection of subsets of U"""

    def __init__(self, test_instance):
        """
        Class constructor
        
        :param test_instance: an instance of a test set
        """
        self.SUBSETS = test_instance.S
        self.max_k = test_instance.K
        self.subsets_bitarr = np.array([random.randint(0, 1) for _ in xrange(len(self.SUBSETS))])
        self.subsets_idx = np.where(self.subsets_bitarr == 1)[0]
        self.subsets_chosen = [self.SUBSETS[i] for i in self.subsets_idx]
        self.elements_fitness = len(set.union(*self.SUBSETS) - set.union(*self.subsets_chosen))
        self.subsets_fitness = len(self.subsets_chosen)

    def recalc_fitness(self):
        self.subsets_idx = np.where(self.subsets_bitarr == 1)[0]
        self.subsets_chosen = [self.SUBSETS[i] for i in self.subsets_idx]
        if len(self.subsets_chosen) == 0:
            self.elements_fitness = len(set.union(*self.SUBSETS))
            self.subsets_fitness = len(self.subsets_chosen)
        else:
            self.elements_fitness = len(set.union(*self.SUBSETS) - set.union(*self.subsets_chosen))
            self.subsets_fitness = len(self.subsets_chosen)

    def dominates(self, chromosome):
        # check if both fitness functions are <= chromosome fitnesses
        if self.elements_fitness <= chromosome.elements_fitness and \
                        self.subsets_fitness <= chromosome.subsets_fitness:

            # so they are
            # we now check if at least one fitness < chromosome fitness
            if self.elements_fitness < chromosome.elements_fitness or \
                            self.subsets_fitness < chromosome.subsets_fitness:
                return True

        return False

    def distance(self, chromosome):
        return np.count_nonzero(self.subsets_bitarr != chromosome.subsets_bitarr)

    def mutate(self):
        mut_idx = random.randint(0, len(self.subsets_bitarr) - 1)
        self.subsets_bitarr[mut_idx] = int(not self.subsets_bitarr[mut_idx])

    def crossover(self, second_parent):
        # fixme add k size limit for descendents
        first_desc = copy.deepcopy(self)
        second_desc = copy.deepcopy(second_parent)
        cut_point = random.randint(0, len(self.subsets_bitarr))
        for i in xrange(cut_point):
            first_desc.subsets_bitarr[i], second_desc.subsets_bitarr[i] = \
                second_desc.subsets_bitarr[i], first_desc.subsets_bitarr[i]

        first_desc.recalc_fitness()
        second_desc.recalc_fitness()
        if first_desc.subsets_chosen > first_desc.max_k:
            first_desc = copy.deepcopy(self)
        if second_desc.subsets_chosen > second_desc.max_k:
            second_desc = copy.deepcopy(second_parent)
        return first_desc, second_desc
