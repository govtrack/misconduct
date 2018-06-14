Congressional Misconduct
========================

This repository contains a single YAML file documenting instances of misconduct
and alleged misconduct by Members of the United States Congress, created by GovTrack.us,
covering 1789 to the present. A CSV file is also included for those wishing to import the data into a spreadsheet.

This database contains:

* All letters of reproval, censures, and expulsions from Congress from 1789 to the present.
* All investigations by the [House Office of Congressional Ethics (OCE)](https://oce.house.gov/), the [House Committee on Ethics (HCE)](https://ethics.house.gov/), and the [Senate Select Committee on Ethics (SSCE)](https://www.ethics.senate.gov/public/), and other investigations by a body of Congress that involved alleged personal misconduct from 1789 to the present, including all investigations by the Senate on whether to allow a senator-elect to be seated when it stemmed from allegations of personal misconduct.
* Failed votes on simple resolutions sanctioning a member without a formal investigation when we came across them.
* As many monetary settlements that we are aware of, e.g. those administered by Congress's [Office of Compliance](https://www.compliance.gov/) regarding sexual harassment claims, but many settlements are not known to the public.
* Resignations and announcements of an intention not to run for re-election that we believe to be likely relevant to an allegation of misconduct, because Members of Congress often resign to head-off a Congressional investigation.
* Felony convictions and other cases of misconduct with national significance before and after the Member's time in Congress.

Investigations, settlements, and resignations **do not imply guilt**. Some investigations are motivated by politics or a personal grudge, settlements are often used when it would be less costly than defending a law suit, and Members of Congress often resign when they are likely to lose re-election (regardless of why). We include investigations even if the Member of Congress is exonerated, per the above rubrik, because the investigation and exoneration are themselves important events not to be forgotten. Conversely, an investigation that ends without a guilty determination **does not imply innocence** --- Congress polices itself in many cases and Members of Congress are reluctant to punish their peers.

Unique to our database are tags describing the type of misconduct such as corruption, general ethical violations or sexual harassment and abuse; consequences including censure, expulsion, resignation and convictions; and case status of resolved/unresolved. Using these filters you can see for example that at least two still open cases have been extended through multiple Congresses with no end date in sight.


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

The data file [misconduct.yaml](misconduct.yaml) is a YAML-formatted text file.

The file is a list of instances of misconduct or alleged misconduct, i.e. each entry repreents an allegation or a collection of related allegations. These entries have fields describing the misconduct or alleged misconduct, including which Member of Congress is accused, a textual summary of the allegation and consequences, a field for just the allegation, and detailed data on consequences.

We add new instances of misconduct or alleged misconduct to the top of the file,
but the file is not otherwise in any particular order. We recommend sorting based
on the the date of the first consequence.

### Instances of misconduct or alleged misconduct

Each entry in [misconduct.yaml](misconduct.yaml) has the following fields:

`person` is the numeric ID of the accused Member of Congress on GovTrack. See [https://github.com/unitedstates/congress-legislators/](https://github.com/unitedstates/congress-legislators/) for metadata on Members of Congress.

`name` is the name of the person for debugging purposes only.

`text` is a summary of the allegation, investigations, and corrective actions taken. It is written in [Markdown format](https://daringfireball.net/projects/markdown/) with light use of rich text like links.

`allegation` is a noun (e.g. `sexual harrassment`) or gerund phrase (e.g. `asking staff members to carry his surrogate child`)
summarizing the misconduct, which completes the sentence "The member was accused of ...".

`consequences` is a list, in (forward) chronological order, of consequences that resulted
from the misconduct, including investigations, expulsion, resignation, conviction,
and other helpful notes that provide context. The data format of a consequence is documented next.

`tags` is a space-separated, alphabetically ordered list of tags. Tags for these records describe the nature of the allegations and are one or more of:

* `elections` - Elections and campaign-related allegations.
* `corruption` - Bribery, extortion, and other criminal corruption.
* `sexual-harassment-abuse` - Sexual harassment and abuse.
* `crime` - Tax evation, murder, fraud, and other crimes (besides corruption and sexual harassment and abuse).
* `ethics` - Violations of congressional rules that are not crimes.
* `resolved` - Either the investigation has formally ended, the legal process has concluded, the member has left Congress, or the member has died. Every instance of misconduct or alleged misconduct is tagged with either `resolved` or `unresolved`.
* `unresolved` - There is an open or pending investigation or other ongoing legal process related to this instance of misconduct or alleged misconduct. Every instance of misconduct or alleged misconduct is tagged with either `resolved` or `unresolved`.

Note that consequences can also have tags but use a different set of tags.

The date of the misconduct or alleged misconduct is only present in an unstructured way in
`text` and `allegation` because misconduct is often a set of events that don't
have a single precise date, and, further, the allegation may not have ocurred.
Instead, each consequence is listed with a date. The date of the first (oldest) consequence,
which is typically about the start of an investigation, is the best date to use for sorting.

### Consequences

Each consequence has its own fields. There are two forms for a consequence.

#### Actions taken by governmental bodies

The first form has `date`, `body`, `action`, and `link` fields and represents an
action taken by a governmental body.

`body` is the name of a governmental body that took an action, such as the House Office of
Congressional Ethics.

`action` is a sentence fragment --- a verb phrase --- that has the action the body took. It should complete the sentence that starts with `body`, so `action` normally starts with a lowercase letter, and it should not end with a period. (`action` may not contain Markdown.)

`link` is a URL to any supporting evidence, often a report or press release issued by
`body` documenting the action they took. News articles or other links may also appear.
In rare cases multiple links may be given in YAML list notation.

#### Other consequences and contextual notes

The second form has `date`, `text`, and `link` fields to represent other consequences
not caused by actions of governmental bodies and other contextual notes.

`text` may be either a full sentence or a sentence fragment starting with the verb. In
either case, `text` starts with a capital letter and ends with a period. (This `text`
may not contain Markdown.)

`link` is a URL to any supporting evidence, such as a contemporary news article or a
primary source government document. In rare cases multiple links may be given in YAML
list notation.

#### Consequence dates

Because some dates are unknown or actions may have ocurred over a time period
greater than a date, `date` may be either a year alone `YYYY`, a year and month
`YYYY-MM`, or a full date `YYYY-MM-DD`. Note that in YAML, a full date or a year
alone do not require quotes (the former is parsed as a date value and the latter
an integer) but a year and month do require being surrounded in quotes to be
valid YAML.

#### Tags

Consequences may also have `tags`. The `tags` field is a space-separated, alphabetical
list of tags from the following set:

* `expulsion` - Expulsion by the Senate or House.
* `censure` - Censure by the Senate or House. (Committee recommendations of censure are not tagged.)
* `reprimand` - Admonishment, reprimand, or letter of reproval.
* `resignation` - Resignation from office because of the allegation.
* `exclusion` - A member-elect was prevented from being seated by the Senate or House.
* `settlement` - Monetary settlement.
* `conviction` - Conviction in a court.
* `plea` - Pleaded in a court.

## Public domain

This project is dedicated to the public domain. Copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](http://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project must be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of your copyright interest.
