# Moving around

The Workbench is the cloud CAT tool to create, edit and fine-tune
translations associated with the various segments that were collected
during Scans.

Below is an overview and explanation of the various parts of the Workbench:

![The Workbench](/img/workbench/full_screen.png)

(numbered explanations)

## Workbench Page List

Click on the Page list right next to the logo to get an overview of
all the pages that contain segments to be translated.

![Page list](/img/workbench/pagelist)

You can click on any page entry in the list to visit that page and get
an overview of all segments associated with that page. Websites can
get very large with a huge list of pages - use the search field
embedded in this dropdown to locate a specific page (you may use
regexen with the usual format of including them between two slashes
like this: `/[regular expression]/`).

There are three options at the top of the dropdown that bear special
mention:

### Show All Entries

Most of the time, you will want segments displayed for a specific
page, but to get an overview of all segments, this is the option to
use.

**WARNING!** Only **List View** is available in this view, all other
View buttons will be unavailable!

The All Entries list doesn't flood your browser with every single
segment all at once: segments will be loaded in batches of 500. The
Workbench will automatically fetch a new batch of entries as you
scroll down.

### Show Pending Entries

By default, Scans will pick up new entries in "Approved" state, which
in this case means "Approved for Translation", immediately available
for translation. You can change this default behavior, by going into
the Dashboard and changing it in
[Link to Header](#advanced-settings)Advanced settings to either
Pending or Excluded.

![Pending entries](/img/workbench/pending_entry.png)

By clicking on "Show pending entries", you will get a list of all
entries that are currently waiting for Approval. In their current
state, They will not be included into exports unless the relevant
option is selected at export-time, and will not appear for translation
unless filtered for specifically.

Project or backup owners, or users with the Customer role can move
these into either one of the other two states, by **approving** them
or **excluding** them entirely from the scope of translation.

### Show Swap Entries

Swap entries are those segments that have had the "EL_swap" class
added to their enclosing tags on the source site.

They are special in that they are added to the Workbench without
processing their tags. They will be displayed verbatim, allowing you
to edit the source content markup directly. That content will be sent
as-is by the proxy for each request.

![Swap entries](/img/workbench/swap_entry.png)

Take caution when editing swap entries. All responsibility of
rendering them successfully _and_safely is delegated to the requesting
browser.

## Searching for segments

![Search field in corner](/img/workbench/search.png)

Use the full-text Search field in the upper-right hand corner of the
screen to search for segments. When you click on the Search field, the
Workflow part of the black menu bar will be superimposed with a search
field right above the Viewport.

![Search field](/img/workbench/active_search.png)

Normal full-text search and regular expressions are supported. The
normal search can be a bit misleading, as it is a
forward-from-word-boundary search. If, for example, you'd like to find
`"translation"` in a source segment, a search query for `"translatio"`
will turn up all segments containing any words that start with that
exact set of strings (and likely end with `n`,`ns`, or `nese`, perhaps
). Searching for `"ranslation"` only, however, will return zero
matches.

Use regular expressions to search between word boundaries: to extend
the previous example, a query for `/.ranslation/` will show all
segments that contain any character (except newline) exactly once,
followed by the literal string `ranslation`. The same as with the Page
list, a string is interpreted as a regular expression if you enclose
it between slashes.

You may select between displaying segments or whole entries using the
radio buttons next to the Search field.

### Closing the Search Field

It is important to remember that the search field also operates as a
**filter**: as long as it is active, segments will be filtered based
on its contents regardless of being in All entries view or on a
specific page. 

If you wish to restore full view of segments, clear the search field
and send an empty search.Use the close button next to the Search
display options to close the search field.

If a search string is still present, it will be preserved and
displayed in the upper right corner Search field in orange, like this:

![Search with string](/img/workbench/search_orange.png)

### For Advanced Users: Deletion of Segments

![Delete segments](/img/workbench/segment_delete_dialog.png)

A regex search reveals another feature of the Workbench you might need
elsewhere: that of deleting segments. If you click on the Magnifying
glass icon while the regex search is active (a bottom-facing triangle
will indicate availability), the dialog above will open.

![The Mallard on Deletion](/img/misc/mallard_delete.png)

The location of this feature is decidedly non-obvious. The warning
above would generally apply to any situation where the words
"_delete_" and "_regex_" appear in the same sentence, but to give you
a measure of peace of mind, it is true that deletion of segments is
not as _final_ as we make it out to be: when **TM Freeze** is
**disabled**, you can re-add segments anytime by Scanning or visiting
in Preview the page that contains the deleted segments.

But that is new words added each time. So, if for no other reason, be
careful about deleting segments in order to avoid unnecessary
expenses.

## Preview

By clicking on the "Eye" icon, you can visit the temporary domain to
check your translations in their original context. This function is
disabled as long as no segment is selected from the list.

If you select a segment in All Entries view, the Preview proxy will
open on the page where it was seen for the first time.

![Preview Icon](/img/workbench/preview_eye_icon.png)

The icon on the Workbench will take you to the Preview mode, but there
are a few different Proxy modes available besides that. See here for
details.
