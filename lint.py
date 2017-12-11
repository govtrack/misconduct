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

misconduct = rtyaml.load(open("misconduct.yaml"))

if not isinstance(misconduct, list):
	error("misconduct.yaml is not a list.")

for incident in misconduct:
	debug_id = rtyaml.dump(incident).strip().replace("\n", " --- ")

	if not isinstance(incident, dict):
		error("incident '{}' is not a dict.".format(debug_id))

	if not isinstance(incident.get("person"), int):
		error("incident '{}' is missing or has invalid 'person', should be an integer.".format(debug_id))
	# TODO: Check ID is a real GovTrack person ID.

	#if not isinstance(incident.get("name"), str):
	#	error("incident '{}' is missing or has invalid 'name', should be a string.".format(debug_id))

	if not isinstance(incident.get("text"), str):
		error("incident '{}' is missing or has invalid 'text', should be a string.".format(debug_id))
		continue

	debug_id = "<{}> <{}>".format(incident.get("name"), incident["text"][0:40]+"...")

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
			pass # good
		elif not isinstance(cons.get("date"), str):
			error("consequence {} is missing or has an invalid date.".format(debug_id2))
		elif not re.match(r"(\d\d\d\d)(-(\d\d)(-(\d\d))?)?", cons["date"]):
			error("consequence {} has an invalid date.".format(debug_id2))

if has_error:
	sys.exit(1)
