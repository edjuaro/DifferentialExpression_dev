import copy
import itertools
import os
import pickle
import re
import sys
from pprint import pprint

import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sns

sys.path.insert(0, '../tools/')
print('Added \'../tools/\' to the path.')
 
from ccal import modalities
from ccal.ccal.match.match.make_match_panel import make_match_panel