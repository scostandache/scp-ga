from CoverSet import *
from GA import *
from niche import *


if __name__=="__main__":

    test_set = CoverSet(1000, 300, 80, 10)

    galg = GA()
    galg.solve(test_set, 40, deterministic_crowding, 15)


