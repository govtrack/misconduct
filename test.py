#!/usr/bin/python3

from datetime import date
import re
import sys
import rtyaml

has_error = False
def error(message):
	global has_error
	has_error = True
	print(message, file=sys.stderr)
	print(file=sys.stderr)

try:
	misconduct = rtyaml.load(open("misconduct.yaml"))
except Exception as e:
	error(str(e))
	sys.exit(1)

if not isinstance(misconduct, list):
	error("misconduct.yaml is not a list.")

for incident in misconduct:
	debug_id = rtyaml.dump(incident).strip().replace("\n", " --- ")

	if not isinstance(incident, dict):
		error("incident '{}' is not a dict.".format(debug_id))

	if not isinstance(incident.get("person"), int):
		error("incident '{}' is missing or has invalid 'person', should be an integer.".format(debug_id))
	# TODO: Check ID is a real GovTrack person ID.

	if not isinstance(incident.get("name"), str):
		error("incident '{}' is missing or has invalid 'name', should be a string.".format(debug_id))

	if not isinstance(incident.get("text"), str):
		error("incident '{}' is missing or has invalid 'text', should be a string.".format(debug_id))
		if not isinstance(incident.get("text", ""), str):
			continue

	debug_id = "<{}> <{}>".format(incident.get("name"), incident.get("text", "")[0:40]+"...")

	if not isinstance(incident.get("allegation"), str):
		error("incident {} is missing or has invalid 'text', should be a string.".format(debug_id))

	if not isinstance(incident.get("consequences"), list):
		error("incident {} is missing or has invalid 'consequences', should be a list.".format(debug_id))
		continue

	for cons in incident["consequences"]:
		debug_id2 = debug_id + " <{}>".format(rtyaml.dump(cons).strip().replace("\n", " --- "))

		if not isinstance(cons, dict):
			error("consequence {} should be a dict.".format(debug_id2))

		if isinstance(cons.get("date"), date):
			pass # good, a full date or a year
		elif not isinstance(cons.get("date"), (int, str)):
			error("consequence {} is missing or has an invalid date.".format(debug_id2))
		elif not re.match(r"(\d\d\d\d)(-(\d\d)(-(\d\d))?)?", str(cons["date"])):
			error("consequence {} has an invalid date.".format(debug_id2))

		if "body" not in cons and not isinstance(cons.get("text"), str):
			error("consequence {} is missing or has invalid 'text', should be a string, or should have body & action.".format(debug_id2))

		if "text" in cons:
			if cons["text"][0] == cons["text"][0].lower() or cons["text"][-1] != ".":
				error("consequence {} text should be a full sentence starting with a capital letter and ending in a period.".format(debug_id2))

		if "body" in cons and not isinstance(cons["body"], str):
			error("consequence {} 'body' should be a string if set.".format(debug_id2))

		if "body" in cons and not isinstance(cons.get("action"), str):
			error("consequence {}, with body, 'action' should be a string if set.".format(debug_id2))

		for field in ("text", "action"):
			if field in cons:
				if "](" in cons[field]:
					error("consequence {} {} looks like it has a Markdown link that should be in the link field instead.".format(debug_id2, field))

		if not isinstance(cons.get("link"), (type(None), str, list)):
			error("consequence {} has an invalid 'link' value.".format(debug_id2))
		if isinstance(cons.get("link"), list):
			for item in cons["link"]:
				if not isinstance(item, str):
					error("consequence {} has an invalid 'link' value.".format(debug_id2))

if has_error:
	sys.exit(1)
