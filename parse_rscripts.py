import sys
import cPickle as pickle
import numpy as np

import rpy2.robjects as robjects

robjects.r["load"](sys.argv[1])
out = robjects.r["out"]
vocab = list(out[out.names.index("vocab")])
doc_bow = list(out[out.names.index("documents")])
with open("vocab_and_bow.pkl","wb") as pf:
	pickle.dump((vocab,doc_bow),pf)