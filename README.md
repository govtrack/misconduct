Congressional Misconduct
========================

This repository contains a single YAML file documenting instances of misconduct
and alleged misconduct by Members of the United States Congress, created by GovTrack.us,
covering 1789 to the present.

This database contains:

* All letters of reproval, censures, and expulsions from Congress from 1789 to the present.
* All investigations by the [House Office of Congressional Ethics (OCE)](https://oce.house.gov/), the [House Committee on Ethics (HCE)](https://ethics.house.gov/), and the [Senate Select Committee on Ethics (SSCE)](https://www.ethics.senate.gov/public/), and other investigations by a body of Congress that involved alleged personal misconduct from 1789 to the present, including all investigations by the Senate on whether to allow a senator-elect to be seated when it stemmed from allegations of personal misconduct.
* As many monetary settlements that we are aware of, e.g. those administered by Congress's [Office of Compliance](https://www.compliance.gov/) regarding sexual harassment claims, but many settlements are not known to the public.
* Resignations that we believe to be likely relevant to an allegation of misconduct, because Members of Congress often resign to head-off a Congressional investigation.
* Law enforcement investigations, convictions, and pleas that we are aware of, except in cases when the investigation resulted in exoneration, was not conducted by Congress, and was not related to the Member's official duties.

Investigations, settlements, and resignations **do not imply guilt**. Some investigations are motivated by politics or a personal grudge, settlements are often used when it would be less costly than defending a law suit, and Members of Congress often resign when they are likely to lose re-election (regardless of why). We include investigations even if the Member of Congress is exonerated, per the above rubrik, because the investigation and exoneration are themselves important events not to be forgotten. Conversely, an investigation that ends without a guilty determination **does not imply innocence** --- Congress polices itself in many cases and Members of Congress are reluctant to punish their peers.

This database can be viewed at:

* https://www.govtrack.us/misconduct

Sources
-------

* The House’s [Office of Congressional Ethics (OCE)](https://oce.house.gov/)
* The [House Committee on Ethics (HCE)](https://ethics.house.gov/)
* The House's [Historical Summary of Conduct Cases in the House of Representatives, Committee on Standards of Official Conduct,1798-2004](https://ethics.house.gov/sites/ethics.house.gov/files/Historical_Chart_Final_Version%20in%20Word_0.pdf)
* The [Senate Select Committee on Ethics](https://www.ethics.senate.gov/public/)
* [Wikipedia’s list of convictions of American politicians](https://en.wikipedia.org/wiki/List_of_American_federal_politicians_convicted_of_crimes), as of Jan 23, 2018
* [The Washington Post’s list of indictments](https://www.washingtonpost.com/news/the-fix/wp/2015/07/29/more-than-two-dozen-members-of-congress-have-been-indicted-since-1980/)
* [United States Senate Election, Expulsion, and Censure Cases](https://babel.hathitrust.org/cgi/pt?id=umn.31951p00933065r;view=1up;seq=7)
* [Congress.gov](https://www.congress.gov/)

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

### Entry

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

### Consequences

Each consequence has its own fields. There are two forms for a consequence.

The first form has `date`, `body`, `action`, and `link` fields. `body` is the
name of a government body that took an action, such as the House Office of
Congressional Ethics. `action` is a sentence fragment that has the action the
body took --- `action` should complete the sentence that starts with `body`, so
`action` normally starts with a lowercase letter, and it should not end with a
period. (`action` does not contain Markdown.)

The second form has `date`, `text`, and `link` fields. `text` is a full sentence
or a fragment starting with the verb (in any case, starting with a capital letter
and ending with a period) describing an event relevant to the misconduct. (This
`text` does not contain Markdown.)

Because some dates are unknown or actions may have ocurred over a time period
greater than a date, `date` may be either a year alone `YYYY`, a year and month
`YYYY-MM`, or a full date `YYYY-MM-DD`. Note that in YAML, a full date or a year
alone do not require quotes (the former is parsed as a date value and the latter
an integer) but a year and month do require quotes (it is parsed as a string).

`link` is a URL to any supporting evidence, usually a report, a press release,
or a news article, or in a few cases a list of such URLs.

Note that the date of the misconduct is only present in an unstructured way in
`text` and `allegation` because misconduct is often a set of events that don't
have a single precise date, and, further, the allegation may not have ocurred.
The date of the first consequence, typically the start of an investigation, is
the best date to use for sorting.

### Tags

Allegation records and consequences can both have `tags`, which contains a space-separated,
alphabetically ordered list of tags.

Tags for top-level allegation records describe the nature of the allegations and are one or more of:

* `elections` - Elections and campaign-related allegations.
* `corruption` - Bribery, extortion, and other criminal corruption.
* `sexual-harassment-abuse` - Sexual harassment and abuse.
* `crime` - Tax evation, murder, fraud, and other crimes (besides corruption and sexual harassment and abuse).
* `ethics` - Violations of congressional rules that are not crimes.

Tags for consequences are:

* `expulsion` - Expulsion by the Senate or House.
* `censure` - Censure by the Senate or House. (Committee recommendations of censure are not tagged.)
* `reprimand` - Admonishment, reprimand, or letter of reproval.
* `resignation` - Resignation from office because of the allegation.
* `exclusion` - A member-elect was prevented from being seated by the Senate or House.
* `settlement` - Monetary settlement.
* `conviction` - Conviction in a court.
* `plea` - Pleaded in a court.

Tags for investigation status are:

* `resolved` - either the investigation has formally ended, the legal process has concluded, the member has left Congress or the member has died.
* `unresolved` - either the investigation has not formally ended or the legal process not concluded and the member remains in Congress
