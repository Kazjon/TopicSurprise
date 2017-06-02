import sys,csv
import pandas as pd
import cPickle as pickle
import numpy as np
from itertools import combinations


with open(sys.argv[1],"rb") as pf:
	vocab = pickle.load(pf)
with open(sys.argv[2],"rb") as pf:
	documents = pickle.load(pf)

topic_pair_surps = np.genfromtxt(sys.argv[3],delimiter=",")
word_occs = topic_pair_surps[1,:]
topic_pair_surps = topic_pair_surps[1:,:]

surp_percentile = 5
for d in documents:
	d_sig_topics = [i for i,v in enumerate(d["sig_topics"]) if v]
	if len(d_sig_topics) > 1:
		d_topic_pairs = list(combinations(d_sig_topics,2))
		d_topic_pair_surps = [-np.log2(topic_pair_surps[i,j]) for i,j in d_topic_pairs]
		d["surps"] = zip(d_topic_pairs,d_topic_pair_surps)
		d["surp"] = np.percentile([s[1] for s in d["surps"]],surp_percentile)
	else:
		d["surps"] = []
		d["surp"] = float("nan")


sorted_docs = sorted([d for d in documents if not np.isnan(d["surp"])],key=lambda x: x["surp"])
for doc in sorted_docs[:10]:
	print "  Title:",doc["title"]
	print "  ID:",doc["id"]
	print "  Surprise:",doc["surp"]
	print "  Surprising Topic Pairs:",doc["surps"]
	print "  Abstract:",doc["raw"]
	print "-----"
print "----------------------------------------------------------------------------------------------------------------"
for doc in sorted_docs[-10:]:
	print "  Title:",doc["title"]
	print "  ID:",doc["id"]
	print "  Surprise:",doc["surp"]
	print "  Surprising Topic Pairs:",doc["surps"]
	print "  Abstract:",doc["raw"]
	print "-----"