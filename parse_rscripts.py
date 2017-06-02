import sys,csv
import cPickle as pickle
import numpy as np
import pandas as pd
import rpy2.robjects as robjects

robjects.r["load"](sys.argv[1])
out = robjects.r["out"]
vocab = out[out.names.index("vocab")]
with open("vocab.pkl","wb") as pf:
	pickle.dump(vocab,pf,protocol=pickle.HIGHEST_PROTOCOL)

doc_bow = out[out.names.index("documents")]

documents = []
thresh = float(sys.argv[3])
with open(sys.argv[2],"rb") as f:
	reader = csv.reader(f)
	reader.next()
	for k,l in enumerate(reader):
		topics = [float(t) for t in l[6:]]
		documents.append({"id":l[0],"title":l[1],"authors":l[2],"raw":l[5],"topics":topics,
						  "sig_topics":[True if t > thresh else False for t in topics]})
for i,d in enumerate(doc_bow):
	ld = list(d)
	documents[i]["bow"] = dict(zip(ld[::2], ld[1::2]))

with open("documents.pkl","wb") as pf:
	pickle.dump(documents,pf,protocol=pickle.HIGHEST_PROTOCOL)


sig_topics = pd.DataFrame([d["sig_topics"] for d in documents])
topic_pair_surps = np.zeros([sig_topics.shape[1],sig_topics.shape[1]])
topic_sig_occs = []
for topic in sig_topics:
	sig_topics_t = sig_topics.groupby(topic)
	topic_pair_surps[topic,:] += np.array(sig_topics_t.get_group(True).sum(axis=0))
	topic_sig_occs.append(topic_pair_surps[topic,topic])
	topic_pair_surps[topic,:] /= topic_pair_surps[topic,topic]
with open("topic_pair_surps.csv","wb") as f:
	writer = csv.writer(f)
	writer.writerow(topic_sig_occs)
	writer.writerows([topic_pair_surps[i,:] for i in range(len(topic_sig_occs))])