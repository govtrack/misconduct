Congressional Misconduct
========================

This repository contains a single YAML file documenting instances of misconduct
by Members of the United States Congress, created by GovTrack.us.

For the purposes of this project, misconduct is any alleged act (and only those) that:

* is investigated by the House Office of Congressional Ethics, the House Committee on Ethics, or the Senate Select Committee on Ethics, or results in a settlement (e.g. from Congress's Office of Compliance), or
* results in a letter of reproval, censure, or expulsion from Congress, or
* results in a resignation from Congress (typically to head-off a Congressional investigation), or
* is investigated by any law enforcement agency _and_ the act occurred while the member was in Congress, during a congressional campaign, or was related to their service in Congress, or
* results in a conviction or guilty plea to a felony (whether or not related to service in Congress)

We note that investigations, settlements, and resignations do not imply guilt, and an investigation that ends without a guilty determination does not imply innocence.

Temporal coverage:

* This database is intended to be comprehensive going back 10 years from the date we began working
  on it, i.e. the start of 2007.
* We plan to add data going back to 1789 soon, but it will likely only cover ethics investigations, censure, expulsion.

This database can be viewed at:

* https://www.govtrack.us/misconduct

How Congress Deals With Misconduct
----------------------------------

Congressional ethics investigations, censure, and expulsion have a complex process and purpose. See:

* [Expulsion and Censure Actions Taken by the Full Senate Against Members](https://www.everycrsreport.com/reports/93-875.html) (CRS report)
* [Enforcement of Congressional Rules of Conduct: A Historical Overview](https://www.everycrsreport.com/reports/RL30764.html) (CRS report)
* [United States Senate Election, Expulsion, and Censure Cases](https://babel.hathitrust.org/cgi/pt?id=umn.31951p00933065r;view=1up;seq=7)

Data Dictionary
---------------

The data file [misconduct.yaml](misconduct.yaml) is a YAML-formatted text file containing
a list. Each entry in the list is an instance of misconduct. The file is ordered roughly
reverse chronologically --- we add new items to the top.

Each entry has five required fields:

`person` is the numeric ID of the person on GovTrack.

`name` is the name of the person.

`text` is a summary of the allegation, investigations, and corrective actions taken
in Markdown format (i.e. with light use of rich text like links).

`allegation` is a noun (`sexual harrassment`) or gerund phrase (`asking staff members to carry his surrogate child`)
summarizing the misconduct, which completes the sentence "The member was accused of...".

`consequences` is a list, in (forward) chronological order, of consequences that resulted
from the misconduct, including investigations, expulsion, resignation, conviction,
and other helpful notes that provide context.

Each consequence has its own fields. There are two forms for a consequence.

The first form has `date`, `body`, `action`, and `link` fields. `body` is the
name of a government body that took an action, such as the House Office of
Congressional Ethics. `action` is a sentence fragment (a verb phrase) that
has the action the body took --- `action` should complete the sentence that
starts with `body`.

The second form has `date`, `text`, and `link` fields. `text` is a full sentence
describing an event relevant to the misconduct.

Because some dates are unknown or actions may have ocurred over a time period
greater than a date, `date` may be either a year alone `YYYY`, a year and month
`YYYY-MM`, or a full date `YYYY-MM-DD`. Note that in YAML, a full date or a year
alone do not require quotes (the former is parsed as a date value and the latter
an integer) but a year and month do require quotes (it is parsed as a string).

`link` is a URL to any supporting evidence, usually a report, a press release,
or a news article.

Note that the date of the misconduct is only present in an unstructured way in
`text` and `allegation` because misconduct is often a set of events that don't
have a single precise date, and, further, the allegation may not have ocurred.
The date of the first consequence, typically the start of an investigation, is
the best date to use for sorting.
