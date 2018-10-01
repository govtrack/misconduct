#!/usr/bin/python3

from datetime import date
import re
import sys
import rtyaml

has_error = False
def error(*args):
	global has_error
	has_error = True
	if len(args) == 1:
		incident, consequence, message = None, None, args[0]
	elif len(args) == 2:
		incident, consequence, message = args[0], None, args[1]
	elif len(args) == 3:
		incident, consequence, message = args
	else:
		raise ValueError(args)
	if incident: print("In <", rtyaml.dump(incident)[:64].replace("\n"," --- "), ">", file=sys.stderr)
	if consequence: print("... <", rtyaml.dump(consequence)[:64].replace("\n"," --- "), ">", file=sys.stderr)
	print(message, file=sys.stderr)
	print(file=sys.stderr)

def remove_markdown_link_urls(s):
	return re.sub("\(http.*?\)", "", s)

try:
	misconduct = rtyaml.load(open("misconduct.yaml"))
except Exception as e:
	error(str(e))
	sys.exit(1)

if not isinstance(misconduct, list):
	error("misconduct.yaml is not a list.")

for incident in misconduct:
	if not isinstance(incident, dict):
		error(incident, "Incident is not a dict.")

	if not isinstance(incident.get("person"), int):
		error(incident, "Incident is missing or has invalid 'person', should be an integer.")
	# TODO: Check ID is a real GovTrack person ID.

	if not isinstance(incident.get("name"), str):
		error(incident, "Incident is missing or has invalid 'name', should be a string.")

	if not isinstance(incident.get("text"), str):
		error(incident, "Incident is missing or has invalid 'text', should be a string.")
		if not isinstance(incident.get("text", ""), str):
			continue

	if not isinstance(incident.get("allegation"), str):
		error(incident, "Incident is missing or has invalid 'allegation', should be a string.")

	if not isinstance(incident.get("consequences"), list):
		error(incident, "Incident is missing or has invalid 'consequences', should be a list.")
		continue

	if not isinstance(incident.get("tags"), str):
		error(incident, "Incident is missing or has invalid 'tags', should be a string.")
		continue
	elif "tags" in incident:
		tags = set(incident["tags"].split(" "))
		bad_tags = tags - {
			"elections", "corruption", "sexual-harassment-abuse", "crime",
			"ethics", "resolved", "unresolved"}
		if bad_tags:
			error(incident, "Incident has invalid 'tags': {}".format(bad_tags))

	for cons in incident["consequences"]:
		if not isinstance(cons, dict):
			error(incident, cons, "Consequence should be a dict.")

		if isinstance(cons.get("date"), date):
			pass # good, a full date or a year
		elif not isinstance(cons.get("date"), (int, str)):
			error(incident, cons, "Consequence is missing or has an invalid date.")
		elif not re.match(r"(\d\d\d\d)(-(\d\d)(-(\d\d))?)?$", str(cons["date"])):
			error(incident, cons, "Consequence has an invalid date.")

		if "body" not in cons and "text" not in cons:
			error(incident, cons, "Consequence should have either 'body' or 'text'.")
		elif "body" in cons and "text" in cons:
			error(incident, cons, "Consequence cannot have both 'body' and 'text'.")

		elif "text" in cons:
			if not isinstance(cons["text"], str):
				error(incident, cons, "Consequence 'text' should be a string.")
			elif cons["text"][0] == cons["text"][0].lower() or cons["text"][-1] != ".":
				error(incident, cons, "Consequence text should be a full sentence starting with a capital letter and ending in a period.")

		else:
			if not isinstance(cons["body"], str):
				error(incident, cons, "Consequence 'body' should be a string.")
			if not isinstance(cons.get("action"), str):
				error(incident, cons, "In consequence with body, 'action' should be a string.")

		for field in ("text", "action"):
			if field in cons:
				if "](" in cons[field]:
					error(incident, cons, "Consequence looks like it has a Markdown link in {} that should be in the link field instead.".format(field))

		if not isinstance(cons.get("link"), (type(None), str, list)):
			error(incident, cons, "Consequence has an invalid 'link' value.")
		if isinstance(cons.get("link"), list):
			for item in cons["link"]:
				if not isinstance(item, str):
					error(incident, cons, "Consequence has an invalid 'link' value.")

		if "tags" in cons and not isinstance(cons["tags"], str):
			error(incident, cons, "Consequence has invalid 'tags', should be a string.")
			continue
		elif "tags" in cons:
			tags = set(cons["tags"].split(" "))
			bad_tags = tags - {
				"expulsion", "censure", "reprimand", "resignation", "exclusion",
				"settlement", "conviction", "plea" }
			if bad_tags:
				error(incident, cons, "Consequence has invalid 'tags': {}.".format(bad_tags))

	# Suggest incidents whose allegation or text fields probably could be shortened.
	if len(incident["allegation"]) > 750:
		error(incident, "'allegation' could probably be shorter.")
	if len(incident["consequences"]) > 2 and len(remove_markdown_link_urls(incident["text"])) > 800:
		error(incident, "'text' could probably be shorter.")
	elif len(incident["consequences"]) > 2 and len(incident["text"]) > 400 and len(remove_markdown_link_urls(incident["text"])) > .8 * (len(incident["allegation"]) + len(" ".join(remove_markdown_link_urls(str(cons)) for cons in incident["consequences"]))):
		error(incident, "'text' could probably be shorter.")


if has_error:
	sys.exit(1)
