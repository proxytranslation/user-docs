# Language Selector

The "finishing touch" is to add a language selector to your published project. There are two ways you can do this: use one of the language selectors provided by default and customize that according to your needs, or implement your own solution in-house.

We'll focus on the internally provided solutions. There are two types of language selectors available: the **Dropdown** and the **Sidebar**.

Use the **Language selector tye** option to select between the two types. You'll notice that the menu changes somewhat based on your choice, and the currently active language selector choice is displayed in a preview window on the right. Both types contain the source language site by default.

At the same time, the embed code text box changes and displays the `<script>` tag that needs to be embedded within the original site's `<head></head>` tags.

## Sidebar

The sidebar is an easy-to-deploy language selector that displays flags for each specified target locale on the left or right side of the website. The horizontal orientation and display names are settable.

## Dropdown

This variant is a bit more complex and feature-rich. It requires an **additional div element on the original page** besides the `<script>` tag. For example, you may insert `<div class="langselector-dropdown"></div>` into the original site structure, then specify the **Dropdown CSS class name** as `langselector-dropdown`. The dropdown will anchor onto this element and inject its own contents to display a dropdown of all selected target languages.

At the bottom of the menu, you can configure the **display names** for the different languages.

## RYO Selector

The third option, implementing a language selector from scratch, does require development resources, but it also allows practically infinite customization options regarding the look and feel of the widget.

All that is required is a set of links, each pointing to a target language that you’ve already published.

**WARNING** By default, the proxy **remaps** the links to the original site! To prevent this from happening, add the ` __ptNoRemap` class to the link in the HTML - otherwise, the proxy will relativize that link as well, and map it to the translated domain (making it impossible to return to the original site from proxied site).
