import rtyaml

fn = "misconduct.yaml"

with open(fn) as f:
	M = rtyaml.load(f)

with open(fn, "w") as f:
	f.write(rtyaml.dump(M))
