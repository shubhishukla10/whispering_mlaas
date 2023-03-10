from time import perf_counter
import numpy as np
import pandas as pd
import ctypes
import pathlib
import os
from pathlib import Path

base_path = str(Path(__file__).parent.parent.parent.parent) + "/"

libname = base_path + "utils/lib_flush.so"
flush_lib = ctypes.CDLL(libname)

libname = base_path + "utils/lib_flush_pipe.so"
flush_lib_pipe = ctypes.CDLL(libname)


for i in range(1000):   # Collect inference timing traces for 10 classes over 1000 time instances
    # Flush cache and pipeline
    flush_lib.main()
    flush_lib_pipe.main()
    os.system("taskset -c 0 python3 Generate_timing_samples.py "+str(i))
    


