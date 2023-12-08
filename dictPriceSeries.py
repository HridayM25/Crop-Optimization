import pandas as pd
import numpy as np 

from CropModelFinalization import get_mapping
maps = get_mapping()

crops_list = maps.values()

#Add the time series for each data here!