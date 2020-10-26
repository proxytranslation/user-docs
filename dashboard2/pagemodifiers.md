# General

The proxy makes translation of websites relatively easy, but the web is an admittedly complex environment that can surprise in countless ways: changes to the page language can cause various layout issues to surface, especially if the developers of the site did not anticipate that the site might get translated.

Word length differences between the source and target languages might cause the menu to crowd. 

Differences between the lengths of different text blocks can cause otherwise well-designed CSS rules to behave in unexpected ways. 

The plethora of plugins that run on a modern website - there is a big pool of possible glitches right there.

Fortunately, changing the site content over the proxy is relatively easy. The Page Modifiers function is made available for this reason: to empower you to add your own CSS rules and JavaScript snippets to influence the way a given proxied site looks to the user.

Because the datastream must pass through the proxy to have the translation embedded, the proxy can insert JavaScript modifiers, modify style sheets, even embed entire pages that do not exist on the original site.

Note that CSS rules and JavaScript are injected into each page that is served over the proxy, including page content overrides defined in Dashboard 2.0 > Content override.

