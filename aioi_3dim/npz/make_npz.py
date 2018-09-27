import numpy as np
from pathlib import Path

names = [f.with_suffix("").name for f in Path("../DATA/").glob("*.txt")]

datas = {name: np.loadtxt("../DATA/{}.txt".format(name)) for name in names}
phn   = {name: np.loadtxt("../LABEL/{}.lab".format(name)) for name in names}
wrd   = {name: np.loadtxt("../LABEL/{}.lab2".format(name)) for name in names}

np.savez("data.npz", **datas)
np.savez("phn_label.npz", **phn)
np.savez("wrd_label.npz", **wrd)
