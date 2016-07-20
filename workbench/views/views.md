# Views

There is more than one way of looking at content on the Workbench, and
the default, the List View is only one of them. In this section, we go
over the various in-context 'Views' you can access from the Workbench
and use to edit your translation while making sure that it is behaving
exactly as it should in the original context.

## List View

![List View Icon](/img/workbench/listview_icon.png)

While not necessarily the most impressive, the List View is certainly
one of the most useful views on the Workbench. You can use it to go
over each segment being translated and edit, filter and search for any
subset. 

The List view provides various features to use with each entry. The
currently selected Entry will be highlighted in yellow, hovering will
causes the Entry under the cursor to highlight in blue. The
presentation of Entries is clear and simple. yet there are a variety
of features you can use with each. Let's take a detailed look at an
entry and see what each part of a line does.

### Anatomy of an Entry

![Segment](/img/workbench/segment_list_view.png)

1. **Select Checkbox**: check this box to select the entry or segment
   in question. You may use the "Bulk Actions" icon to batch process
   selected entries (i.e. confirm, exclude or approve them)

2. **Source Entry**: contains the text that was found within a given
   block element on the source site. You may set the text direction
   using the "Align source text" icon in the toolbar. Otherwise, the
   Source Entry is not editable.

3. **Entry No. + Containing Block Element**: use the "Go to Segment"
   icon to jump to a segment with a given number. This number is
   assigned to entries in order of arrival (new entries can be found
   at the bottom of the list). Additionally, the tag that contained
   the text on the original site is displayed below it (useful when
   you want to identify a segment in the HTML source).

4. **Target entry**: The translation, provided by a variety of
   sources: Manual Editing, Translation Imports, Machine Translation
   or Translation Memory.

5. **Lock Segment**: Prevent any changes from influencing the current
   content of the Target Entry. Especially useful when you want to run
   batch processes on your segments, but you want to exclude an entry
   from the scope.

6. **Comment on Segment**: Use this icon to add comments to an Entry
   either as a note-to-self, or as part of a collaborative translation
   effort. All comments have a checkbox next to them, allowing you to
   mark them as settled.

7. **Chain link**: indicates that the segment is repeated verbatim
   (102% match) in the current view. Click on the icon to jump to the
   next repetition.

8. **Confirm Tick** click on the tick to Confirm the segment for the
   current workflow and send it to the next stage. Confirmed entries
   remain editable as long as they are unedited by the next workflow
   role.

9. **Workflow Status Indicator**: Display the current workflow state
   of the segment. Note that this might differ depending on which user
   in which workflow role is currently looking at the segment.

10. **Flag**: Display current translation source.

### Workflow Tags

Depending on what Workflow role you're currently in, the following
Workflow tags will be displayed for each segment, influencing their
availability for editing:

![Workflow Tags](/img/workbench/workflow_tags.png)

**T** - Translator

**P** - Proofreader

**Q** - Proofreader 2 (**Q**uality Check)

**C** - Customer (or Client)

See the section on Workflow roles for a detailed description of the
various workflow roles.

### Flags

## Highlight View

![Highlight View Icon](/img/workbench/highlight_view_icon.png)

The highlight view is a true in-context editing view that makes the
Workbench popular with Translators, and _the_ solution to the problem
of adequate context during website localization. 

By selecting an Entry in List view and clicking on the Highlight View
on the Workbench, you will be shown the text on the original webpage

![Highlight View](/img/workbench/highlight_view.png)

You may click on any part of a website and have a highlighting frame
appear around that segment. At the same time, the editing box below
will jump to the segment in question, where you can add/edit your
translations in-place. 

Really, the Highlight View is simplicity itself with very little in
the way of hidden gotchas. Select a page, point & click, and translate
away!

But keep in mind that while you are using the Highlight View with a
page, links will be unclickable - use Free-click View to navigate on
the original site from within the Workbench.

**NOTE** The Highlight view is a wonderful tool we are very proud of,
but don't forget that much of the textual content of a website is not
clickable. Check the other modes and the Preview to make sure that
everything is covered!

## Free-Click View

![Free-click View Icon](/img/workbench/free_click_view_icon.png)

The Free-Click View is much like the Highlight View, but it allows you
to use the links on a site to visit other parts of the
website. Alternate between Free-click view and Highlight View to
translate segments as you explore the website.

Free-click view will offer to reload your segment list based on which
page you are on. The following dialog will be displayed.

![Reload Segment List](/img/workbench/reload_segments_redirecting.png)

Highlight View will only work if the segment list is that of the
current page.

## Pop-out View

![Pop-out View Icon](/img/workbench/popout_view_icon.png)

The Workbench is a single-viewport application, and the Pop-out View
is a feature meant to allow you to have the Highlight View and the
List View on your screen **at the same time**. Select an Entry from
the list and click on the Pop-out view icon to open a Highlight View
in a separate pop-up window.

Modern browsers block popup windows by default, so you will most
likely have to **enable popups** for the Workbench for this feature to
work.
