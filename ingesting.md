# Ingesting Content

## Scan vs Discovery vs Preview (real-time ingestion)

Discovery does not extract or store content. It is used for merely statistical purposes - such as providing a word count, or mapping a site's URL structure.
A Scan writes into the database. It extracts and stores the source content.

When you visit a page with the preview proxy, real-time ingestion occurs.
Pages with new content downloaded through the proxy will be ingested automatically. When Easyling encounters content without matching source entries, it will create a new entry - new content will show up. Read below for ways to circumvent bleed through in these cases.

## Cache (Source, Target, Keep)

After running a Scan and making sure everything is in order, it's the perfect time to build source cache to avoid future bleed through.<br>
*Source cache* will take a snapshot of the site, and use that to serve any further requests.
Source cache stores CSS and HTML. Easyling does not store images, form data, etc.
When a website owner removes images from a banner slideshow for example, even if a Source cache is live and serving, the images are removed and they will show up as missing.

*Target and Keep cache:*<br>
If you think of Source cache as input, then target (Binary) cache is the output - it's the traslated page at the end of the translation process. The Target cache's primary goal is to speed up the site.
*Keep cache*'s primary goal is to prevent premature translations from appearing on the site in question - even if the source site changes unexpectedly, Easyling will keep serving the Target cache's contents, until the cache is cleared, maintaining the illusion of a fully translated site.

## Entry level exclusion

There are three translation states that segments can be set to: 
Approved, excluded and pending.
The customer role under Dashboard / Sharing Settings is used to give the client access to approve segments. The customer role is a read-only role.

Clicking the Manage Segments link will show Externalized entries only. The client can choose to approve them for translation, or leave them out of the process.
This feature is useful, when the client requests to control what goes into the translation process.

## Page Freeze and Dictionary Freeze

These two functions go hand-in-hand. Page freeze prevents picking up pages and adding them to the pages list.
TM freeze prevents addition of new content, when it's turned on no new content makes it to the dictionary.

See this tutorial for more information on freezes: [http://lesson102.tutorial.easyling.com/](http://lesson102.tutorial.easyling.com/)

# XLIFF export + work packages

Work package generation is the recommended method of dealing with exports.

Once you create a work package, after naming it Easyling creates an internal package in our database which then may be be filtered further.
Once a Work package is generated it becomes accessible in other parts of Easyling. Just to name one, you can filter for Work packages in the Workbench, making it easier to edit only select content.
Work packages can be exported as XLIFF. Exports can be done automatically on creation, or manually via the work packages menu.

When creating a work package you can filter for several aspects. You can create work packages from select pages or folder just to name a few.

A timeline can also be set. This can range from project creation to the latest action taken on the project.
This lets you filter for content picked up in a desired time-frame.

## XLIFF import + log

Every time an import is done an email is sent out containing an import log.
Usually the import log only consists of two lines: import started and import finished.
However the log can be of great use should anything go wrong during an import.

Using the log, you can search for a problematic segment in the XLIFF imported by searching for it's unique ID, the TM key.

Here's an example log containing an error:

````
info Processing www.somedomain.com_en-US_projectcode_1432654611173.xlf
error The XML structure has been changed so much that it is now unmappable from the source (projectcode_tm:m+vULvNWZF5teJg4zV8q5RV4frz0HYjyBOWeeQEkBdc=mJAJOo+O1NoLJDdf+n1AI5eE3u9lBEqLcLyqDjhi/s4=)
````

The XML structure has been changed so much that it is now unmappable from the source usually means that the tag placement is does not match the source.
Searching for the TM key in the XLIFF in question will help you identify the problematic segment, and hopefully fix it. Comparing the source and the target against each other usually reveals the problem.

The TM key is the string which comes after the 'projectcode_tm:', in this case:
`m+vULvNWZF5teJg4zV8q5RV4frz0HYjyBOWeeQEkBdc=mJAJOo+O1NoLJDdf+n1AI5eE3u9lBEqLcLyqDjhi/s4=`

A good online tool for comparing texts:
* [http://text-compare.com](http://text-compare.com)

## Translation Workflow integration (client approval, proofreading)

### Roles

The translation workflow in Easyling is split into a maximum of four steps: *Translation* (marked by a T and the color yellow), two steps of *Proofreading* (first and second marked by a P and Q, and the colors cyan and violet, respectively), and *Client approval* (marked by the letter C and the color aqua). Any user may be assigned any combination of these steps, useful for restricting access to entries in the List View.

* **Owner**: Every project has an owner, who has unlimited powers over the project: the owner may add or remove anyone on the project, edit any entry in any language, including adding new languages, any change any setting, including the advanced ones. There can only be one owner on a project, but owners may renounce ownership, designating another user and setting their own privileges.
* **Customer** (see next section below also): Customers are designated by the Customer role, and are intended to be representatives of the customer exercising oversight over the content for translation. This role is read-only, meaning despite the target language added to the user, they are unable to actually edit the translation, instead, they are able to move pending segments to either the approved or the excluded state using the “Manage segments” item in the Content menu.
* **Linguist**s are designated using the Simplified Dashboard feature: this limits the user’s access to the dashboard and the Content menu, only permitting segment editing, and only in their designated language and phase. Linguists can also receive notification emails on project updates, and may be given the power to import/export XLIFF files.
* **Contributor**s are the default users, capable of editing any entry in their selected language and workflow step, but are prevented from doing anything else on the project. They may receive notification emails and project update emails, but they may not edit their features, nor invite anyone else, nor access any of the advanced settings.
* **Project Manager**s are designated by their power to invite others onto the project. Other features and roles can be added as well, but care must be exercised not to include other, conflicting roles, which could re-restrict their access.
* **Advanced Project Manager**s are designated by the eponymous feature. They are given the power to edit languages, as well as any entry in the project, and editing most setting, up to, and including, the URL inclusion-exclusion rules. However, they cannot change segmentation settings, publishing settings, and certain advanced settings.
* **Admin**s are designated by their *Backup Owner* role. Their powers equal that of project owners, being able to change any setting and entry, adding or removing users, and modifying the language settings.

### Client approval

Sometimes there is need for the client to view and check new segments before they enter the translation workflow.

In the **Advanced Settings** menu, default state of new segments can be set to the following:
- Pending
- Excluded
- Approved

When set to Pending or Excluded, new segments picked up will acquire that state automatically and manual approval is needed.
In the Sharing Settings menu, the customer role can be assigned for this purpose.
Important: The client role is read-only. Anyone assigned this role won't be able to edit content, but approve them for translation. If you are unable to edit segments on the Workbench, please check Sharing Settings first.


## Translation Memory (populate and confirm)

You can create your own TMs in Easyling. It is useful for example when transferring from a staging site's project to a live site's project.

**Population:**
Translation memory population is done with the populate button. After clicking Populate, all previously translated content from the project is pushed into the TM.

Easyling can then export the TM into a standard TMX file to be integrated into your offline TMs, while the same TMX standard can be used to import your TM and make use of it within Easyling.

**Inter-availability:**
Translation memories created by user under a project can be attached to another project (where the same user is owner or backup owner) without the need to export and import.

**Concordance search:**
You can input a search string in the "Search for suggestions" text area, under the Translation Memory menu. Suggestions also come up in the Workbench.

## Pre-translation (with a TM)

Easyling can use translation memories to aid in the pre-translation of the site. Memories can be imported from standards-compliant TMX files, or can be populated from the project itself. Once a memory has been created, it will remain accessible to the user across projects, to be used for pre-translation. Memories can also be exported in the same TMX format they are imported in.

During pre-translation, confidence level thresholds can be set for using the memory contents, as well as for automatically confirming these entries. Several memories can be assigned to a given project, and pre-translation will use all of them at once to draw translations from, however, only the default memory can be written to on the project.



## Layout issues (text expansion, RTL)

Easyling can inject custom CSS and JS to the proxied sites.
The injection applies to every single page served by Easyling.

**CSS Editor**: Easyling can be used to insert locale-specific CSS rules into the site being served. The most common use of this feature is to alter the writing direction for non-Latin scripts, such as Arabic.

**JavaScript Editor**: the JavaScript edited here is inserted into the `<head>` element of every page being served through Easyling. By default, it does not replace any previously present `<script>` elements, being inserted as its own element, but can be used to modify the page behavior in many ways.

Both injected JavaScript and CSS are placed at the very end of the `<head>`, thus can be used to override earlier rules and logic.
