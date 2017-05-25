import sys,csv
import cPickle as pickle
with open(sys.argv[1],"wb") as pf:
	vocab, doc_bow = pickle.load(pf)
with open(sys.argv[2],"rb") as f:
documents = []
	reader = csv.reader(f)
	reader.next()
	for l in reader:
		documents.append({"id":l[0],"title":l[1],"authors":l[2],"raw":l[5],"topics":[float(t) for t in l[6:]]})
for i,d in enumerate(doc_bow):
	documents[i]["bow"] = d
	print documents[i]

