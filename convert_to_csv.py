import rtyaml, csv, re
from functools import reduce

with open("misconduct.yaml") as f1:
  misconduct = rtyaml.load(f1)

def get_tags(instance, only=None):
  tags = []
  if only != "consequence":
    tags.extend(re.findall("[\w-]+", instance.get("tags", "")))
  if only != "instance":
    for consequence in instance["consequences"]:
      tags.extend(re.findall("[\w-]+", consequence.get("tags", "")))
  if "" in tags: tags.remove("")
  return set(tags)

all_instance_tags = reduce(lambda x,y:x|y, (get_tags(instance, only="instance") for instance in misconduct))
all_consequence_tags = reduce(lambda x,y:x|y, (get_tags(instance, only="consequence") for instance in misconduct))

with open("misconduct-instances.csv", "w") as f2:
  # Make the columns.
  date_cols = ["first_date", "last_date", ]
  metadata_cols = ["person", "name", "allegation", "text"]
  tags_cols = sorted(all_instance_tags) + sorted(all_consequence_tags)

  # Write out.
  w = csv.writer(f2)
  w.writerow(date_cols + metadata_cols + tags_cols)
  for instance in misconduct:
    tags = get_tags(instance)
    w.writerow(
      [ instance["consequences"][0]["date"], instance["consequences"][-1]["date"] ] +
      [ instance[field] for field in metadata_cols ] +
      [ ("X" if tag in tags else "") for tag in tags_cols ]
      )

