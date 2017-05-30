import random
import numpy as np
import copy
from chromosome import *
from CoverSet import *
from GA import *
from niche import *

n = 1000
m = 300 #size of set
l = 5 #size of list of subsets

test_set = CoverSet(10000,300,200,10)

galg = GA()
galg.solve(test_set, 150, deterministic_crowding, 20)

