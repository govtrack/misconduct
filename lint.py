import rtyaml

fn = "misconduct.yaml"

with open(fn) as f:
	M = rtyaml.load(f)

for record in M:
	if "tags" in record:
		record["tags"] = " ".join(sorted(set(record["tags"].split(" "))))
	for cons in record["consequences"]:
		if "tags" in cons:
			cons["tags"] = " ".join(sorted(set(cons["tags"].split(" "))))

with open(fn, "w") as f:
	f.write(rtyaml.dump(M))
