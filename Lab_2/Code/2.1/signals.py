import numpy as np
import matplotlib.pyplot as plt
import radiolab

f_lo = 100.e3

radiolab.set_srs(1, f_lo, vpp=None, dbm=0., off=None, pha=None)

#radiolab.set_srs(1, f_lo + f_lo*(5./100.), vpp=None, dbm=0., off=None, pha=None)

radiolab.set_srs(2, f_lo - f_lo*(5./100.), vpp=None, dbm=0., off=None, pha=None)

radiolab.sampler(16000,20.*2.*f_lo, fileName='2_1_minus', dual=False, low=False, integer=False, timeWarn=False)
