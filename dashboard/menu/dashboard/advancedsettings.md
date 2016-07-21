# Advanced settings

It is not an exaggeration that the Advanced settings screen is where
you can get a first taste of the advanced capabilities (the
nitty-gritty) of Easyling.

Some, such az Freezes, are general enough to warrant close attention
from all users, others, such as the Tweaks checkbox list are required
only in specific cases, so you can go through many, many projects
without ever having to worry about them. Let's take these features one
by one.

**Pattern matching**: there is often a great deal of text on a website
that is not targeted for translation, because they are highly
repetitive (usernames, dates) or numeric in nature (prices), just to
mention a few possibilities.

You can construe regular expressions and add them here, one regular
expression per line, and if that regex has a capturing group, anything
that is **matched by that capturing group** will be treated as
translation-invariable.

It is important to note that if you add regexes here later into the
project, your existing segments will remain in the Workbench. Pattern
matching does **NOT** delete any segments.

**Example: filtering usernames and dates**

Let's say you have content like the following on a site:

```
Posted by youTuTroll on Apr. 4, 13:22, 2010
Posted by joey0405 on Apr. 6, 03:29, 2010
Posted by cunning_linguist on Apr. 6, 03:45, 2010
Posted by bornToBe27 on Apr. 6, 10:01, 2010
Posted by OMEGA on Apr. 7, 11:59, 2010
```

Repetitive and inconsequential from a translation/word count
viewpoint, the usernames and dates should be made
translation-invariant. You can add a regex for it (such as the one
below) in the textbox and Easyling will exclude whatever is matched
within a capturing group.

`Posted by ([\w]+) on ([\w]{3}\.\s[0-9]{1,2},\s[0-9]{2}:[0-9]{2},\s2[0-9]{3})`

We recommend that you visit regex101.com and test your regular
expressions with example snippets before setting them on a live
project.

### Freeze

These options become important after translation has begun in
earnest. At this point, it is a good idea to __freeze__ the page list
and the segments - that is, prevent _inadvertent_ addition of new
text or pages to the list you are currently working on.

**WARNING:** These settings can be overriden via explicit user action:
adding Pages via the blue icon in the page list, or running Scans with
the appropriate settings in place.

As you based quote on a specific Discovery/Scan (in other words, a
specific state of the site at a given time), it wouldn't do to return
a few days after winning the project only to find that the news
section was expanded with two new items and you have 4500 new source
words to deal with - indelibly added to the project, but not part of
the original deal. 

The following features are available:

**Freeze pagelist**: Prevent new pages from being added to the
pagelist. If you turn this option on, you can use the various preview
modes without having to worry about new content.

**Handle unknown pages as externalized**: Pages that are not already
in the pagelist will be _externalized_, that is, not translated _at
all_, the same as if the page was manually excluded. Be aware that on
a live site, this may result in an SEO penalty (due to duplicate
content being detected by the crawler)!

**Freeze translation memory**: No new translatable segments will be
added to a project as long as this Freeze is turned on (automatically
enables Page Freeze).

## Group pages

the Proxy Application can group automatically generated pages
together, preventing new pages from being added, but not removing
already added pages, and making the grouped pages share a single
dictionary, necessitating translation of only one. The pages will be
grouped according to the path rules specified in the textbox, one path
per line, with a `\*` as the wildcard character. This does not
decrease the volume of pages that will be crawled, but it makes
project maintenance easier.

## JavaScript translation

This field contains the capture group definitions used to extract
attribute-value pairs from JavaScript files selected for
translation/localization. After entering the capture parameters and
re-crawling the site, the Proxy Application will display the selected
JavaScript files as translatable pages in the pagelist, from where
they can be selected for translation in the List View like regular
pages, and any values for the selected attributes will be made
available as translatable entries, which are treated identical to
regular entries. Entering “` html`” (N. B. The switch is separated by
a space!) after the path specification will result in the Proxy
Application applying its HTML parser to the match instead of a
plaintext parser, stripping out HTML markup and only offering the
actual content for translation (otherwise, should the match contain
markup, the translator must take care not to alter it, or risk
breaking the translated site).

If a field of the JSON being parsed contains further JSON data in a
stringified form `("key": "{\\"key\\":{\\"key\\":\\"value value
value\\"}}")`, the path can be passed to a recursive JSON translator
by appending “` json`” to the path, then extending the path on the
next line by adding “`.json.`”.

## XPath Translation

the Proxy Application is able to translate XML (eXtensible Markup
Language) files sent by the remote server, according to the XPath
standard of specifying elements of the XML structure. Similar to
JavaScript translation, entering the “` html`” switch will result in
the HTML parser being applied, while no switch will parse the match as
plaintext.

## Mark multiple Resources as Translatable

Using URL prefixes (N.B. fully qualified URL prefixes, including
protocol, host, and possibly path structures!), the Proxy Application
can enforce dictionaries over multiple resources in a single
rule. This is especially useful if the site under translation contains
an API (especially CREST APIs) whose responses also require
translation, and each endpoint is served on a different path; in this
case, entering the root of the API here will automatically capture all
responses from that path without having to individually mark them as
translatable from the Resources menu.

## Additional Remote Request Headers

If the remote server requires certain headers to be present to serve
legal responses, it will not be crawlable by default, as the crawler
will not supply these. Entering the required headers here will result
in them being appended to every request sent by the Proxy Application,
including the crawler requests, letting you crawl the site as
required.

## Ignore Classes

If a certain class of elements are not ought to be translated, they
can be entered here. Elements with these classes will be treated as if
they had the `<translate=no>` attribute, and will be treated as
translation-invariant.

## Ignore IDs

similar to the “Ignored classes” option, this allows the treating of
specific elements as translation-invariant, this time through HTML
IDs.

## Process Custom HTML Attributes

Some CMS-es may employ non-standard HTML attributes on elements to
style the page or otherwise affect certain aspects of their
operation. If some of these attributes contain translatable text, you
can enter them into the “As text” field to instruct the Proxy
Application to extract them. If they contain URLs that need to be
mapped to the translated domain, you can use the “As link” field to
instruct the Proxy Application to map those non-standard link elements
as well.

On request, it is also possible to activate an HTML parser for certain
attributes, should they contain HTML formatting in their values.

## Tweaks

In this menu, you'll find checkboxes for settings that apply to very
specific circumstances. For those special times, when you come across
the occassional special snowflake. When in doubt, contact us!

- **Retaining original DOCTYPEs**: By default, the Proxy Application
  generates an HTML5 standards-compliant file to send to the
  client. If, for some reason, this causes problems due to the site
  relying on HTML4 standards for operation, some of which may be
  deprecated by HTML5, enabling this option will cause the Proxy
  Application to retain the original DOCTYPE declaration of the source
  page.

- **Determine document type by** `GET` **instead of HEAD**: some
  servers may return different responses to the HEAD request we use to
  determine document type than the GET request used to download
  content. Enabling this option forces the Proxy Application to use
  GET requests for all operations, getting the correct content type
  from the server (as far as server-side configurations will allow).

- **Detect JavaScript content type**: JavaScript may not be explicitly
  declared as such on the server, being sent to the client with
  misleading content types. This causes the Proxy Application to
  mis-identify such streams and not offer operations reserved for JS
  files. Enabling this option will force a deep check on each file
  sent to the client, to determine if they are indeed JavaScript code,
  regardless of their declared content type.

- **Download images through the proxy**: this will instruct the Proxy
  Application to attempt to map all `<img src>` attributes to the
  proxied domain. This is especially useful if the images are served
  only after authentication.

- **Attempt to place tags according to punctuation when using TM-based
  pre-translation**: if using a TM-based pre-translation, the Proxy
  Application may encounter segments where it cannot replace the XLIFF
  tags automatically, due to overly large differences between the
  contexts (possibly because of a changed site). If this option is
  enabled, the translator will try to replace the XLIFF tags according
  to their positions relative to punctuation marks in the segment. If
  successful, the TM entry’s confidence score will be increased by
  0.1.

- **Translate excluded pages when viewing them in Preview mode (but
  still not in live serving mode)**: It may be necessary sometimes to
  view excluded pages as if they were translated, in order to assess
  their layout, without actually making them available on the live
  site. Enabling this option allows just that, by propagating
  translations to the excluded pages if viewed in Preview mode, but
  keeping them untranslated in Live serving mode.

- **Translate** `javascript:` **attribute**: The Proxy is capable of
  extracting and translating code from the onclick attribute of
  elements. This feature may be used when a site uses this attribute
  to store translatable content inlined into the attribute and
  requires this content to be translated. Currently we only process
  the onclick event’s contents, all other events in the javascript
  attribute will be ignored.

- **Detect and handle JSON-in-string responses, like**
  `"{\\"ResponseCode\\":\\"BadRequest\\"}`: string-escaped JSON-format
  responses can be handled by activating this tweak. If active, the
  Proxy Application will first attempt to string-unescape the response
  before passing it to the JSON parser, in order to recreate its base
  form.

- **Make content in** `<script type="text/html"></script>`
  **translatable as a whole (don't try to parse it as HTML)**: Script
  blocks may contain template data requiring translation, which is
  often signified by the text/html content type (instead of the more
  usual application major type). In such cases, HTML parsing can be
  undesirable, and can be bypassed by activating this option.

- **Send a canonical link http header pointing to the original page on
  externalized pages**: the Proxy Application can insert a Link header
  into externalized pages, in order to avoid the SEO penalty
  associated with duplicate content. This header will point to the
  original address, and have `rel=Canonical` added, to designate the
  relationship.

## Manual Publishing

*Manual Publishing* is advanced project control feature that gives
project owners the ability to hold back the translations from being
published on the live page (but not the preview, as it will always
display the latest translation available!) until further notice.

The feature can be activated from the Advanced Settings page. Once
activated, it will affect all translations going forward, but
already-existing ones will not be “unpublished”.

Once activated, a new item will appear in the Bulk Actions menu,
“Publish”. Selecting this action will cause all selected segments to
be synchronized with their displayed translations, and once the action
finishes, the markers in the status bar on the right of the entries
will change to reflect this. If the action encounters an error, the
server will attempt to rectify this by publishing the entire entry,
after confirmation from the user. If the error is not recoverable, it
will list the segments in error.

## Default segment state

By default, the Proxy Application will add new segments during a crawl
as “Approved”, making them available for translation immediately
after. However, if the user/client desires, this behavior can be
changed to adding new segments in one of two states, “Pending” or
“Excluded”. If the default setting is changed, the project owner,
backup owners, or users with the Customer [role][Sharing Settings] can
alter segment states.

“**Pending**” segments are those that are awaiting a decision on
translation. They will not be included into exports unless the
relevant option is selected at export-time, and will not appear for
translation unless filtered for specifically. Users able to alter
segment states may move these into either one of the other two states,
by approving them for translation, or excluding them entirely.

“**Excluded**” segments are those that have been deemed as not requiring
translation at all. Unless the relevant option is selected, they are
not included in exports and will not appear for translation unless
filtered for specifically. Users able to alter segment states may
approve them for translation, making them available.