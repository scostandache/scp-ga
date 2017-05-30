from chromosome import *


class Population(object):
    # class to represent the population

    def __init__(self, pop_size, test_instance):
        """
        
        :param pop_size: number of chromosomes in population 
        :param test_instance: a test instance composed of a set U and its subsets
        """
        self.MEMBERS = [Chromosome(test_instance) for _ in xrange(pop_size)]
