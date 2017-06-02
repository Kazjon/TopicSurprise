import sys,csv

books = []
with open(sys.argv[1],"r") as f:
	for row in f:
		splitrow = row.split("||")
		if len(splitrow) > 3:
			splitrow = splitrow[:2] + [" ".join(splitrow[3:])]
		books.append([s.strip().rstrip("\n") for s in splitrow])

with open(sys.argv[2],"w") as f:
	writer = csv.writer(f,quotechar="~",quoting=csv.QUOTE_ALL)
	writer.writerows(books)
