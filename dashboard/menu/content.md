## Content

The main difference between Discoveries and Scans is that Discoveries
do not extract or store content. They are used for statistical
purposes, such as providing a word count or mapping a site’s URL
structure.

A Content Scan, however, writes into the database. It extracts and
stores the source content to be translated. New source words added to
the database are billed, therefore care must be taken when starting
Scans. If you are not really sure about a site, stick to Discovery
until you gain better understanding of its structure! Unlimited Scans
especially require attention: they will relentlessly add all content
to the database according to the specification you set for them.

Settings you used to experiment with Discoveries can also be used to
initiate Scans - for a detailed explanation of the different settings,
please take a look at the Discovery chapter of this section.

There is button on the main screen that you will not find in the
Discovery menu, that is "Update word count", which you can use to
refresh the statistics window during or after an extended Scan.

### Pages & Resources & External links

These screens are duplicated between the Discovery and Content menus
for ease of access. See the pertaining documentation of them in the
Discovery part of this section.

### Manage segments

By clicking here, you will be taken to the Workbench on a new tab. The
Workbench is the working end of the proxy service - please visit the
Workbench section of this manual for the details of how to use it.

### Proxy migration

(to-be-written)

### Work packages

Work package generation is the recommended method of dealing with
exports/new content. Along with the general import and export
features, work package generation becomes available after the first
round of Scanning (Content Extraction) has finished and translatable
content (segments) has been placed in the database.

Initially, the screen will be empty, but if you click on the blue
"plus" icon, a dialog will pop up where you can generate new work
packages using a variety of settings at your disposal. Let's take a
look at them one by one.

#### Work package generation 

**Work package name** You can name your work package any way you
like. As a suggestion, it is recommended that you give it a name that
accurately reflects its contents, so as to make project management
using work packages easier. So, for example, if you generate a work
package for Arabic as a target language on April 10th, 2016 for all
new content, you would name it something like
_sa-AR-untranslatedContent-2016-04-10-_ and so on.

**Source language** The source language for the project is displayed
in this field (settable from the Dashboard main screen).

**Work package language** You can add multiple target languages for
the Generation Process, but remember that a separate Work Package will
be created for each target language.

**Timeline** You can specify which Content Extraction cycle you'd like
to see in the Work Package that is to be generated. Click on "change"
and use the timeline window to specify the time period, and the
generator will limit its attention to just that timeframe. Select any
two timestamped buttons to define the start and end of the timeframe.

**Filter pages** You can use your current selection (set on the Pages
list screen), or define specific selected pages (both paths and full
URLS are allowed) or folders using path prefixes. When you use a
predefined list of pages (selected pages) the additional option of
including both the HTTP and HTTPS versions of pages will be displayed
as a checkbox.

**Options** Miscellanious options you can use to fine-tune the
properties of your Work Package. 

Split your package at preset words to create easily manageable chunks
to assign to translators. Disable it to put everything in one big file
(Note, however, that Work packages will be automatically split at
30.000 words)

You can choose to create separate work packages for hidden elements,
and set the Work package generation to automatically take care of
exporting for you. As with the general import function, you may elect
to export only those entries that have no translation yet. 

If you configured XTM, XTRF or Dropbox to integrate with the proxy,
you may instruct the software to automatically send the exported XLIFF
files to either one of those services. Use the dropdown menu to make
your choice (only available if the checkbox is checked).

#### Work package list

You will receive e-mail notification about your generated work
packages and they will appear in the list. You can use the refresh
button to get an up-to-date view of your work packages.

If you hover over a work package, a floating menu will appear to the
right with two options: XLIFF export and Progress report generation.

### Import translation

When your XLIFF files have made a round in your favourite CAT tool, it
is time to reimport them, which is a straightforward process - click
on "Import translation" and the Import dialog will pop up, where you
can click on "Choose file" to browse for your translated XLIFF
files. Click on "Import translation" and wait for the import process
to finish.

You may optionally set the workflow status of imported segments to
Translated-CONFIRMED, and you can use the second tab in the dialog
window to reimport translations from your Dropbox account.

**NOTE!** Importing is not instantaneous, it may take some time to
finish depending on the size of your XLIFF!

### Export translation

By clicking on this link, the general Export dialog will open. Most of
the options will be familiar from the Work package generation
dialog. Choose a file format of your preference (with XLIFF being the
_de facto_ industry standard, it is recommended that you go with this
option, as it is more structured than CSV. Use JS if you are using
Client-Side Translation).

**Languages to export** You can choose to export more than one target
languages in one go, or choose to export them all.

**Export range** Click on "change" and use the timeline window to
specify the time period, and the export function will be limited to
that timeframe. Select any two timestamped buttons to define the start
and end of the time frame.

**Export** You can choose between exporting only those entries that
lack a translation, or include all entries.

**Unique segments only** Check this option to ensure that identical
segments are not duplicated in your exported XLIFF file.

**Skip exlcuded and pending segments from export** Export only those
segments that have been approved for translation on the Workbench.

**Trim export to contain as few tags and whitespaces as possible** Use
this option to clean the source segments of tags for the purposes of
translation.

**Split** enter the number of segments that you'd like to have in a
single file, and the export will split your segments into separate
files accordingly.

**Copy source to target where empty**

**Send XLIFF files** Choose among your XTM, XRTF or Dropbox accounts
to send your exported files to. Each of these accounts has a link at
the bottom of the dialog that will take you to the given account's
setting screen.

Click on Export to execute. Wait for the process to finish - you will
receive an e-mail when your files are ready.

### Previous exports

Although the notification e-mail does contain the link to your
exported file, there is no reason to track it from your mailbox. This
dialog will list and organize all previous exports for your viewing
with the appropriate timestamp, target language and word count
displayed right next to an Export list entry.

Currently running processes are also displayed, with a spinner
indicating that the Export is still underway.
