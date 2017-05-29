import random
import numpy as np
import copy
from chromosome import *
from CoverSet import *

n = 1000
m = 300 #size of set
l = 5 #size of list of subsets

cs = CoverSet(100,30,5)

a=[0,0,1,1,0]
a[2] = int(not a[2])
print a
