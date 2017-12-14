import os, sys
import pandas as pd
import numpy as np
from params import get_params


if __name__ == "__main__":
    params = get_params()
    file = open(os.path.join(params['root'],params['database'],'val','annotation.txt'),'r')
    file.readline()
    x=file.readlines()
    for lines in x:
        os.remove(os.path.join(params['root'],params['database'],'train', 'images',lines[0:10]+'.jpg'))