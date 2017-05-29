# todo-me implement Deterministic Crowding
import random
import copy


def deterministic_crowding(population):
    for _ in xrange(len(population.MEMBERS) / 2):
        first_parent = random.choice(population.MEMBERS)
        population.MEMBERS.remove(first_parent)
        second_parent = random.choice(population.MEMBERS)
        population.MEMBERS.remove(second_parent)

        first_desc, second_desc = first_parent.crossover(second_parent)

        first_desc.mutate()
        second_desc.mutate()

        first_desc.recalc_fitness()
        second_desc.recalc_fitness()

        if first_parent.distance(first_desc) + second_parent.distance(second_desc) <= \
                        first_parent.distance(second_desc) + second_parent.distance(first_desc):
            if first_desc.dominates(first_parent):
                population.MEMBERS.append(first_desc)
            else:
                population.MEMBERS.append(first_parent)

            if second_desc.dominates(second_parent):
                population.MEMBERS.append(second_desc)
            else:
                population.MEMBERS.append(second_parent)

        else:
            if second_desc.dominates(first_parent):
                population.MEMBERS.append(second_desc)
            else:
                population.MEMBERS.append(first_parent)

            if first_desc.dominates(second_parent):
                population.MEMBERS.append(first_desc)
            else:
                population.MEMBERS.append(second_parent)
