# Work packages

Work package generation is the recommended method of dealing with exports/new content. Along with the general import and export features, work package generation becomes available after the first round of Scanning (Content Extraction) has finished and translatable content (segments) has been placed in the database.

Initially, the Work package list will be empty, you can create one using the Work package wizard.

## Work package wizard

![Work package wizard](/img/dashboard2/work_package/work_package_wizard.png)

This wizard is designed to simplify the creation process of Work packages. It is split into 3 tabs.

### Generation settings

This is where the most important settings are. In most cases, you won't need to leave this tab. It has lots of options. Let's take a look at them one by one.

**Work package name:** You can name your work package any way you like. As a suggestion, it is recommended that you give it a name that accurately reflects its contents, so as to make project management using work packages easier. So
, for example, if you generate a work package for Arabic as a target language on April 10th, 2020 for all new content, you would name it something like _ar-SA-untranslatedContent-2020-04-10_ and so on.

**Source language:** The source language for the project is displayed in this field (it can be changed on the old Dashboard main screen).

**Work package languages:** You can add multiple target languages for the Generation Process, but remember that a separate Work Package will be created for each target language.

**Options** Miscellanious options you can use to fine-tune the properties of your Work Package.

Split your package at preset words to create easily manageable chunks to assign to translators. Disable it to put everything in one big file (Note, however, that Work packages will be automatically split at 30.000 words)

You can choose to create separate work packages for hidden elements, and set the Work package generation to automatically take care of exporting for you. As with the general import function, you may elect to export only those entries that have no translation yet.

If you configured XTM, XTRF or Dropbox to integrate with the proxy, you may instruct the software to automatically send the exported XLIFF files to either one of those services. Use the dropdown menu to make your choice (only available if the checkbox is checked).

### Source filters

**Source contains:** Add a Java regular expression. Only segments where the source matches will be included.

**HTML tag:** Enter a comma separated list of tags that you wish to include. Only content found in those tags will be included.

**HTML class:** Add specific classes that must or must not be on a specific element for it to be included in the Work package.

**Timeline (always selected):** You can specify which Content Extraction cycle you'd like to see in the Work Package that is to be generated. By default, it's from `Project created` until `Now`. Click on either of the dropdown menus to change the start or end dates.

**Filter pages (always selected):** You have 3 options here:

- *Current selection* refers to your selection in the Pages list. If you select this, the Work package will follow the inclusion/exclusion rules you set there.

- *Selected pages*: You can specify a list of pages that you wish to add.

- *Selected folders*: Add include and exclude rules for this Work package. This is completely separate from those in the Pages list. 

### Target filters

**Filter by trasnslation source**: You can specify whether you want segments with machine or human translations. This can be very useful if you had to machine translate some part of the website to meet deadlines but want to go back and have them reviewed by humans.

**By publish state**: This setting is only applicable if manual publishing is turned on.

**Segment assigned to**: Any workflow state in the Workbench. The available options are influenced by the workflow of the project (set on the Miscellaneous options card of the Project overview).

**Has unresolved comment** refers to the comments in the Workbench.

**By comment (or target) contents**: A Java regular expression to filter targets. This can be used if you need to fix the spelling of `donut` to `doughnut` everywhere in a British English text.

**By date range** refers to the date the segment was last edited.

**Last modified by**: Select a user whose translations you wish to include. Can be useful when reviewing translations.

## Work package list

![Work package list](/img/dashboard2/work_package/work_package_list.png)

You will receive e-mail notification about your generated work packages and they will appear in the list. In the middle, you can see the settings used to create the selected package. On the right, in the list, every element has a context menu with important actions:

**Generate progress report**: Generate a detailed report on the progess made on this package. This will be emailed to you. The same information is available on the Progress report card.

**Refresh progress report**: Refreshes the Progress report card

**Export XLIFF**: Open the export as XLIFF dialog and export this package as XLIFF. It will be emailed to you and will become available in the Previous expprts menu.

**Pre-translate**: Open the Pre-translate dialog with settings preset to translate this Work package.

**Create new Work package with the same settings**: Opens the Work package wizard preset to match the settings of this package. You can change its settings then click generate.