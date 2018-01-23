Congressional Misconduct
========================

This repository contains a single YAML file documenting instances of misconduct
and alleged misconduct by Members of the United States Congress, created by GovTrack.us,
covering 1789 to the present.

For the purposes of this project, misconduct is any alleged act (and only those) that:

* is investigated by the House Office of Congressional Ethics, the House Committee on Ethics, the Senate Select Committee on Ethics, or other investigative committee of Congress, or resulted in a monetary settlement (e.g. from Congress's Office of Compliance), or
* results in a letter of reproval, censure, or expulsion from Congress, or
* results in a resignation from Congress (typically to head-off a Congressional investigation), or
* is investigated by any law enforcement agency _and_ the act occurred while the member was in Congress, during a congressional campaign, or was related to their service in Congress, or
* results in a conviction or guilty plea (whether or not related to service in Congress)

Investigations, settlements, and resignations do not imply guilt, and an investigation that ends without a guilty determination does not imply innocence.

In terms of coverage, this database contains

* all instances of letters of reproval, censures, and expulsions from Congress from 1789 to the present
* all investigations by a body of Congress from 1789 to the present that involved alleged personal misconduct
* some election-related investigations by the Senate on whether to allow a senator-elect to be seated stemming from allegations of personal misconduct
* some monetary settlements that we are aware of (many are not publicly known)
* some resignations that we believe to be likely relevant to an allegation of misconduct
* some instances of law enforcement investigations, convictions, and pleas that we are aware of

This database can be viewed at:

* https://www.govtrack.us/misconduct

Sources
-------

* The House’s [Office of Congressional Ethics (OCE)](https://oce.house.gov/)
* The [House Committee on Ethics (HCE)](https://ethics.house.gov/)
* The [Senate Select Committee on Ethics](https://www.ethics.senate.gov/public/)
* [Wikipedia’s list of convictions of American politicians](https://en.wikipedia.org/wiki/List_of_American_federal_politicians_convicted_of_crimes), as of Jan 23, 2018
* [The Washington Post’s list of indictments](https://www.washingtonpost.com/news/the-fix/wp/2015/07/29/more-than-two-dozen-members-of-congress-have-been-indicted-since-1980/)
* [United States Senate Election, Expulsion, and Censure Cases](https://babel.hathitrust.org/cgi/pt?id=umn.31951p00933065r;view=1up;seq=7)

How Congress Deals With Misconduct
----------------------------------

Congressional ethics investigations, censure, and expulsion have a complex process and purpose. See:

* [Expulsion and Censure Actions Taken by the Full Senate Against Members](https://www.everycrsreport.com/reports/93-875.html) (CRS report)
* [Enforcement of Congressional Rules of Conduct: A Historical Overview](https://www.everycrsreport.com/reports/RL30764.html) (CRS report)

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
Congressional Ethics. `action` is a sentence fragment that has the action the
body took --- `action` should complete the sentence that starts with `body`, so
`action` normally starts with a lowercase letter, and it should not end with a
period.

The second form has `date`, `text`, and `link` fields. `text` is a full sentence
or a fragment starting with the verb (in any case, starting with a capital letter
and ending with a period) describing an event relevant to the misconduct.

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
