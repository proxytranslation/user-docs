# Moving Around

The Workbench has a single viewport, so every feature you'd need to navigate between pages and segments is always just a couple of clicks away.

You may switch between pages, search for text, filter for segments based on a variety of metadata, such as Approval state, containing block element, translation source and so forth. This section deals with the various ways to do that.

## Workbench Page List

A segment is tied to the specific page it was found on. You can use the Page list dropdown right next to the logo to get a list of all pages currently within the scope of translation.

![Page list](/img/workbench/page_list.png)

You can click on any page entry in the list to visit that page and get an overview of all segments associated with that page. Websites can get very large with a huge list of pages - use the search field embedded in this dropdown to locate a specific page (you may use regular expressions with the usual format of including them between two slashes like this: `/[regular expression]/`).

There are three options at the top of the dropdown that bear special mention:

### Show All Entries

Most of the time, you will want segments displayed for a specific page, but you may also use this option to get an overview of all segments across all pages.

**WARNING!** Only **List View** is available in this view, all other View buttons will be unavailable!

The All Entries list doesn't flood your browser with every last segment all at once: segments will be loaded in batches of 500. The Workbench will automatically fetch a new batch of entries as you scroll down.

### Show Pending Entries

By default, Scans will pick up new entries in "Approved" state, which in this case means "Approved for Translation", immediately available for translation. You can change this default behavior, by going into the Dashboard and changing it in <a href="/en/latest/dashboard/menu/dashboard.html#advanced-settings">Advanced settings</a> to either Pending or Excluded.

By clicking on "Show pending entries" in the page list, the list of all entries that are currently waiting for Approval is displayed. In their current state, They will not be included into exports unless the relevant option is selected at export-time, and will not appear for translation unless filtered for specifically.

Project or backup owners, or users with the Customer role can move these into either one of the other two states, by **approving** them or **excluding** them entirely from the scope of translation.

### Show Swap Entries

Swap entries are those segments that have had the "EL_swap" class added to their enclosing tags on the source site.

They are special in that they are added to the Workbench without processing their tags. They will be displayed verbatim, allowing you to edit the source content markup directly. That content will be sent as-is by the proxy for each request.

![Swap entries](/img/workbench/swap_entry.png)

Take caution when editing swap entries. All responsibility of rendering them successfully _and_ safely is delegated to the requesting browser.

### Filters

There is a comprehensive assortment of filters available. Click on the Filters icon in the toolbar to get a an overview of all available filters:

![Filters Icon](/img/workbench/filters_icon.png)

Use the checkboxes to define your filtering settings in the dialog and click on "Set Filters".

You can filter for the roles that edited segments, their status and the date range they were last modified.
Both the before and after dates are optional. If "after" date is omitted, it means the filter should display segments that were modified until the "before" date. If "before" omitted, it means the filter should display segments that were modified after the "after" date. Providing both will set a filter that displays segments in a given date range where both after and before dates are inclusive. 
In general, everything that modifies the translation of an entry (translation, pre-translation etc.) is considered to be a modification. There are a couple of exceptions that aren't currently tracked:
* a segment is confirmed or its workflow status changes
* a segment is locked 

![Filters Dialog](/img/workbench/filters_dialog2.png)

The dialog will close and a new element will appear in the toolbar, indicating that user-defined Filtering settings are currently active, and the segment list is updated accordingly. Click on the "X" to disable filtering. You may also click anywhere else on the toolbar indicator to open the Filters dialog again and fine-tune your settings.

![Filtering Indicator](/img/workbench/filters_indicator.png)

These filters work with the various types of metadata associated with an Entry (such as currently assigned workflow role, enclosing block element in source, approval state or source of translation), **not** content - use the **Search** functionality to filter for source or target text.

## Searching for segments

![Search field in corner](/img/workbench/search.png)

Use the full-text Search field in the upper-right hand corner of the screen to search for segments. When you click on the Search field, the Workflow part of the black menu bar will be superimposed with a search field right above the Viewport.

![Search field](/img/workbench/active_search.png)

Normal full-text search and regular expressions are supported. The normal search can be a bit misleading, as it is a forward-from-word-boundary search. If, for example, you'd like to find `"translation"` in a source segment, a search query for `"translatio"` will turn up all segments containing any words that start with that exact set of strings (and likely end with `n`,`ns`, or `nese`, perhaps ). Searching for `"ranslation"` only, however, will return zero matches.

Use regular expressions to search between word boundaries: to extend the previous example, a query for `/.ranslation/` will show all segments that contain any character (except newline) exactly once, followed by the literal string `ranslation`. The same as with the Page list, a string is interpreted as a regular expression if you enclose it between slashes.

You may select between displaying segments or whole entries using the radio buttons next to the Search field.

### Closing the Search Field

It is important to remember that the search field is also a **filter**: as long as it is active, segments will be filtered based on its contents regardless of being in All entries view or on a specific page.

If you wish to restore full view of segments, clear the search field and send an empty search.Use the close button next to the Search display options to close the search field.

If a search string is still present, it will be preserved and displayed in the upper right corner Search field in orange, like this:

![Search with string](/img/workbench/search_orange.png)

### Deletion of Segments

![Delete segments](/img/workbench/segment_delete_dialog.png)

You might be wondering what this has to do with navigation, but executing a regex search reveals another feature of the Workbench you might ordinarily look for someplace else: that of deleting segments. If you click on the Magnifying glass icon while the regex search is active (a bottom-facing triangle will indicate availability), the dialog above will open.

The non-discoverability of this feature is premeditated. Skulls & Bones warnings would generally apply to **any** situation where the words "delete" and "regex" are found in the same sentence. That being said, to give you a measure of peace of mind, deletion of segments is not as final as we seem to make it out to be: when TM Freeze is **disabled**, you can re-add segments anytime by Scanning or visiting in Preview the page that contains the deleted segments.

_But that is new words added each time_. So, if for no other reason, be careful about deleting segments in order to avoid unnecessary expenses. Buyer, beware!

![The Mallard on Deletion](/img/misc/mallard_delete.png)

## Preview

By clicking on the "Eye" icon, you can visit the temporary domain to check your translations in their original context. In the "All Entries" view, this function is disabled if no segment is selected - without picking a segment, the Workbench has no information on which page to show you. Otherwise, if a Page view is open, the selected page will be loaded.

If you select a segment in All Entries view, the Preview proxy will open on the page where it was seen by the crawler for the first time.

![Preview Icon](/img/workbench/preview_eye_icon.png)

The icon on the Workbench will take you to the Preview mode, but there are a few different Proxy modes available besides that. See here for details.
