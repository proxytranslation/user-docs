# Translation of Segments

We are getting to the primary purpose of the Workbench, which is of
course, translation of text. In this section, we'll talk about the
different ways of doing that.

It bears mentioning right off the bat that the Workbench is not meant
to selfishly yank you out of your CAT tool of choice. As the proxy
supports exporting segments in the industry-standard XLIFF format, you
can always employ any tool of you preference, SDL Trados and MemoQ,
for example, being two major players in the field. The choice is
yours.

Nevertheless, you will find that the Workbench is closer to where the
website really is - up there in the cloud, and therefore immensely
useful during the editing process. You'll see it truly begins to shine
when your XLIFF files have done their first round-trip to and from
external CAT tools.

There are multiple ways of translating content on the Workbench:

- manual Translation using the Target editor

- using Translation Memories

- using Machine Translation

- importing translated XLIFF files

The following sections provide an overview of the translation methods
listed above.

## Editing segments

Editing of segments happens in the Target editor located on the bottom
of the Workbench:

![Editing window](/img/workbench/target_editor.png)

You can use the Highlight View or the List View to select a segment,
and the editor will reflect your selection. The Source entry is
displayed to the left, the translation (Target) to the right. Only the
target is editable.

### Editing Window

Editing translations on the Web means going around/avoiding/leaving
intact the forest of HTML tags that the text os usually embedded
on. The Workbench abstracts away these markup details to ease working
with text (the first and foremost task of translators), but doesn't,
and will never attempt to hide the fact of their existence.

Tags are represented as numbered grey widgets around certain parts of
the text, which you can use as a yardstick to place your translations
in the appropriate tag context without having to worry about what
those tags actually do.

Two things:

- **You can Drag & Drop the Numbered Tags**

- **You can NOT delete them**

Adding translations is otherwise straightforward text
input. Untranslated entries will contain the Source text as a
placeholder until such time as a change is made to the contents of the
Target, at which point both the List View and the Segment contents are
updated.

There are a few smaller buttons in various parts of the Target
editor. In the middle, you'll see these three buttons:

![Source-and-Target Edits](/img/workbench/st_edit_buttons.png)

These contain editing functions that relate the contents of the Source
and the Target in different ways. Use the top "**Equal**" button to
copy the Source contents to the Target, rendering them identical. You
can use the middle, "**Tag**" button to copy the tag structure of the
Source to the Target. The lower "**Eraser**" button will delete the
translation and restore the placeholder.

There is another set of four buttons to the right:

![Target Editing Buttons](/img/workbench/t_edit_buttons.png)

They all deal with the Target. In descending order, these are:

1. **Toggle sidebar**: use this to hide the Suggestions & History
   sidebar above the button.

2. **Preserve Whitespace**: prevent trimming of whitespaces in the
   segment

3. **Insert non-printing characters** There are a number of
   non-printing characters you might need during a translation
   project, especially if you are dealing with languages that have a
   Right-to-Left writing direction, such as Arabic. See the section on
   RTL conversion for further details.

4. **Split segment from group**

### Saving changes

Click on "Save & Next" to save your work on the given Entry and jump
to the next segment. You can also use Ctrl+Up or Ctrl+Down to do
this. This is an explicit, although not strictly necessary action, as
any edits are **automatically saved** upon leaving an entry.

## Automatic Translation

There are a number of Auto-translation features that you can employ to
ensure quality on the proxy.

The option to run pre-translation or set it up to run automatically is
also available on the Dashboard. Here, we discuss the options
available after clicking on the "Pre-translate" icon in the toolbar:

![Pre-translate Icon](/img/workbench/pretranslate_icon.png)

The following dialog is displayed:

![Pre-Translate Dialog](/img/workbench/pretranslate_dialog.png)

### Pseudo-translation

This function is admittedly not translation in a meaningful sense, but
string-reversing each and every word of every segment on the spot is
very effective during a demo. Use it, then go to Preview to
demonstrate to the client that website localization is as painless as
using CAT tools in tandem with the Proxy. Good for the
wow!-factor. Pseudo-translation can also be used to test the various
editing features available on the Dashboard and the Workbench.

### Translation Memory

## History

### Translation Memories

### Segment History
