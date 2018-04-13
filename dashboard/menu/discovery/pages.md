# Pages

The page list lets you keep track of the various URLs that are (or were) present on the proxy. There are two places you can access the list from: the Discovery and Content menus.

Aside from the overview of and direct access to content on the individual pages, the page list also allows you to visit the various proxy preview domains, fine-tune inclusion/exclusion settings and check your translation progress.

## Side menu

The overview presented can be influenced by the various filters available in the left-side menu. 

![Side menu](/img/dashboard/page_list_filters.png)

The following filters are available:

### Language

One of the more important filters available in the side menu. The information displayed in translation progress bars will apply to the selected language, and both the List and Highlight Views will open to the Target language. The same applies to the available Preview links.

**Ensure that you have selected a target language.** If none is selected, or if there is no target language on the project (in which case, the source language is selected), neither the Workbench links, nor the Previews are available, greyed out like this:

![Inactive Hover Menu](/img/dashboard/page_list_hover_menu_inactive.png)

#### Update Translation Progress link

By clicking on this link, you can update the translation progress bars for the selected target language. An update is normally run every 24 hours, but you can force it on a language-basis here. Please note that the process can take some time depending on the amount of content on the various pages.

### Timeline

Use this dropdown to filter for those pages that registered new content before or after a given set date when content was added to the project. Set the value to "After Project creation" or click on Reset timeline to undo this filter. The dialog looks like this:

![Timeline Filter Dialog](/img/dashboard/page_list_timeline_filter_dialog.png)

### Filters

This general-sounding dropdown lets you filter for pages currently in a given state. The possible options are

1. **Visited (Scanned) only**: filter for pages that have been Scanned already. These pages will show a status of "NEW" or a translation progress bar, indicating that they are in-progress.

2. **Unvisited only**: filter for pages that are referenced on some other visited page and their URLs were added to the page list, but neither a Discovery nor a Scan has had a chance to process them yet.

3. **Discovered only**: filter for pages that were Discovered and included in a word count crawl. Note that the "Discovered" note to the right of a page does not tell you *which crawl succeeded in Discovering the page*.

4. **All items**: use this option to disable filtering in this dropdown.

### Exclusion State

![Exclusion filter](/img/dashboard/page_list_exclusion_filter.png)

A project can have many URLs (query parameters, for example, especially in combination tend to increase their number), potentially crowding the page list and much unnecessary scrolling. Use the exclusion filters at the bottom of the side menu (together with the search field) to get a clearer view of your currently selected or excluded set of URLs (see below for the details of exclusion/inclusion rules). 

## Top Menu

![Page List Top Menu](/img/dashboard/page_list_top_menu.png)

The following features are available in the top menu:

1. Export page list
2. Add New Pages
3. MAss Exclusion of URLs
4. Include/Exclude
5. Search

See below for the details of each feature.

### Page list export

Clicking on this icon presents you with your current selection of pages in an easy to copy & paste format (autoselected).

![Page list export](/img/dashboard/page_list_export_pages.png)

Above a certain reasonable threshold, the Dashboard will not render the whole page list in the dialog, and you will receive a message that the page list is too big. The option to export as XLS remains avaialble in both cases.

### Add New Pages

Though unassuming in appearance, the Add pages dialog is nevertheless a powerful feature: that of *page-specific crawls*. it allows you to add new pages based on a list and to refresh already extracted pages "surgically"

Perhaps a specific set of pages could benefit from a Scan or you would like to add a few images for localization (only a small percentage of images tend to require translation). 

Use the Add Pages dialog to do all these things without the overhead of a full-blown crawl.

![Add Pages](/img/dashboard/page_list_add_pages_dialog.png)

Most of the features involving the limiting of a crawl's scope will be missing from the dialog. The capability to add various types of resources is present, and source cache settings are also available.

### Mass Exclusion

![Mass Exclusion](/img/dashboard/page_list_mass_exclusion.png)

The proxy can exclude pages in a targeted manner or based on a prefix. It can sometimes happen that a prefix-based approach is too inclusive, but exclusion of large numbers of URLs would be tedious. Use this dialog to exclude (or re-include) a set of URLs in one fell swoop.

### Inclusion/exclusion rules

When you click on the "Sheet & Gear" icon, both the Top Menu and the search bar is temporarily transformed into the inclusion / exclusion rule editor as shown in the screenshot below:

![Inclusion/exclusion menu](/img/dashboard/page_list_inclusion_exclusion_rule_editor.png)

There are many places on the Dashboard where inclusion/exclusion rules are called for (such as auto-pretranslation or work packages), but the rules declared here are special in that influence the state of the entire project (including live serving of pages).

An excluded page will remain *entirely* untranslated over the proxy domains (both Preview and Live), and excluded pages will be ignored by Discoveries and Scans.

Exclusion of individual pages is rather simple to undo, but be careful about using too general inclusion rules. 

You can copy & paste URLs into the dialog



## Page List

### Hover menu

![Hover Menu](/img/dashboard/page_list_hover_menu.png)

#### Translate in List View & Highlight View

#### Preview

#### Cache

#### Exclude

### Translation State

## Page deletion
