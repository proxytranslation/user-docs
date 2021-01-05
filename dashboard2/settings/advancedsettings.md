# Advanced settings

The Advanced settings screen is the _nitty-gritty_ of the technical side of the proxy, the various features of which make complex project management and involved content extraction/management possible.

For now, this link takes you back to the old Dashboard but we'll update it shortly.

Some, such as **Freezes**, are general enough to warrant close attention from all users, others, such as the **Tweaks** checkbox list are required only in specific cases, so you can go through many, many projects without ever having to worry about them. In this section, we take a look at all options in the order that they appear on the Dashboard.

**Pattern matching**: there is often a great deal of text on a website that is not targeted for translation, because it is highly repetitive or numeric in nature, usernames, timestamps and prices fall into this category of content, to mention a few of many possible cases where Pattern Matching might come handy.

You can construct regular expressions and add them here, one regular expression per line.

If that regex has a capturing group, anything that is **matched by that capturing group** will be treated as **translation-invariable**.

It is important to note that if you add regexes here later into the project, your existing segments will remain in the Workbench. Pattern matching does **NOT** delete or exclude any segments.

**Example: filtering usernames and dates**

```
Posted by youTuTroll on Apr. 4, 13:22, 2010
Posted by joey0405 on Apr. 6, 03:29, 2010
Posted by cunning_linguist on Apr. 6, 03:45, 2010
Posted by bornToBe27 on Apr. 6, 10:01, 2010
Posted by OMEGA on Apr. 7, 11:59, 2010
```

Repetitive and inconsequential from a translation/word count viewpoint, the usernames and dates should be made translation-invariant in the content above. You can add a regex for it (such as the one below) in the textbox and the translation proxy will exclude whatever is matched within a capturing group.

`Posted by ([\w]+) on ([\w]{3}\.\s[0-9]{1,2},\s[0-9]{2}:[0-9]{2},\s2[0-9]{3})`

We recommend that you visit <http://www.regex101.com> and test your regular expressions with example snippets before setting them on a live project.

## Freeze

The following are important options for when translation has already begun in earnest on a batch of content. At this point, it is a good idea to __freeze__ the page list and the segments - that is, prevent _inadvertent_ addition of new text or pages to the list you are currently working on.

**WARNING:** These settings can be overriden via explicit user action: adding Pages via the blue icon in the page list, or running Scans with the appropriate settings in place.

As you based quote on a specific Discovery/Scan (in other words, a specific state of the site at a given time), it wouldn't do to return a few days after winning the project only to find that the news section was expanded with two new items and you have 4500 new source words to deal with - indelibly added to the project, but not part of the original deal.

The following features are available:

**Freeze pagelist**: Prevent new pages from being added to the pagelist. If you turn this option on, you can use the various preview modes withouht having to worry about new content.

**Handle unknown pages as externalized**: Pages that are not already in the pagelist will be _externalized_, that is, not translated _at all_, the same as if the page was manually excluded. Be aware that on a live site, this may result in an SEO penalty (due to duplicate content being detected by the crawler)!

**Freeze translation memory**: No new translatable segments will be added to a project as long as this Freeze is turned on (automatically enables Page Freeze).

## Group pages

Specify path rules to group pages into one entry, preventing new pages from being added, but not removing preexisting pages, and making the grouped pages share a single dictionary, necessitating translation of only one. The pages will be grouped according to the path rules specified in the textbox, one path per line.

This feature is not meant to and does not decrease the amount of pages a Discovery has to crawl, but it makes project maintenance easier, as it prevents your page lists from being overcrowded with repetitive URLs.

## Additional Remote Request Headers

If the remote server requires certain headers to be present to serve legal responses, it will not be crawlable by default, as the crawler will not supply these. Entering the required headers here will result in them being appended to every request sent by the proxy, including the crawler requests, letting you crawl the site as required.

## Ignore Classes

If a certain class of elements are not ought to be translated, they can be entered here. Elements with these classes will be treated as if they had the `<translate=no>` attribute, and will be treated as translation-invariant.

## Ignore IDs

Similar to the “Ignored classes” option, this allows the treating of specific elements as translation-invariant, this time through HTML IDs.

## Process Custom HTML Attributes

Some Content Management Systems may employ non-standard HTML attributes on various elements to style the page or otherwise affect aspects of their operation. If some of these attributes contain translatable text, you can enter them into the “As text” field to instruct the proxy to extract them. If they contain URLs that need to be mapped to the translated domain, you can use the “As link” field to instruct the proxy to map those non-standard link elements as well.

In case they contain HTML or JavaScript/JSON that contains translatable text, you can enter them into the "As HTML" or "As JavaScript" fields respectively. These will go through the regular HTML or JS parser to pick up content. Note that in case of JSON in an attribute, you still need to mark the JSON paths in the JSON/JS processing menu of the Dashboard 2.0.

You may want to further filter where a given attribute should be translated. You can do so with CSS-like advanced selectors. These are written after the name of the attribute (before the semicolon denoting the next one). Let’s see a few examples: 
- If you want to translate the `content` attribute but only on `meta` tags, you can write `content meta`. 
- If you need to further narrow down the scope, you can specify that `content` should only be translated on `meta` tags where a `name` attribute is present like so: `content meta[name]`.
- You can also specify the value of the `name` attribute. When you write `content meta[name=foo]`, the `content` attribute will only be translated on `meta` tags if the attribute `name` with the value `foo` is also present.
- It’s also possible to chain these values. You can specify that you need an `id` to be present on top of the previous example’s rules by adding it to the end: `content meta[name=foo][id]`

In some cases, you can’t specify the exact value of an attribute that you wish to filter for. In this case, you can use the following operators:
- `^=`: looks for a string prefix
- `$=`: looks for a string suffix
- `#=`: searches for a regexp match

Both the attribute name and the match value are strings. If they contain any character other than letters, you must wrap them in quotes. You can also use raw strings with `r""` where the backslash character won’t escape the ones after it. See the table below for reference:

<table style="margin-bottom: 24px">
    <tr>
        <td><strong>Literal</strong></td>
        <td><strong>Value</strong></td>
    </tr>
    <tr>
        <td><code class='docutils literal notranslate'><span class='pre'>some-value</span></code></td>
        <td><code class='docutils literal notranslate'><span class='pre'>some-value</span></code></td>
    </tr>
    <tr>
        <td><code class='docutils literal notranslate'><span class='pre'>Jyväskyla</span></code></td>
        <td>error, only characters of the English alphabet, dash and underscore can be unqoted</td>
    </tr>
    <tr>
        <td><code class='docutils literal notranslate'><span class='pre'>"Jyväskyla"</span></code></td>
        <td><code class='docutils literal notranslate'><span class='pre'>Jyväskyla</span></code></td>
    </tr>
    <tr>
        <td><code class='docutils literal notranslate'><span class='pre'>"quoted\nvalue"</span></code></td>
        <td><code class='docutils literal notranslate'><span class='pre'>quoted⏎value</span></code></td>
    </tr>
    <tr>
        <td><code class='docutils literal notranslate'><span class='pre'>r"quoted\nvalue"</span></code></td>
        <td><code class='docutils literal notranslate'><span class='pre'>quoted\nvalue</span></code></td>
    </tr>
    <tr>
        <td><code class='docutils literal notranslate'><span class='pre'>"quoted\u0020value"</span></code></td>
        <td><code class='docutils literal notranslate'><span class='pre'>quoted value</span></code></td>
    </tr>
    <tr>
        <td><code class='docutils literal notranslate'><span class='pre'>r"quoted\u0020value"</span></code></td>
        <td><code class='docutils literal notranslate'><span class='pre'>quoted\u0020value</span></code></td>
    </tr>
</table>

## Tweaks

In this section, you'll find checkboxes for settings that apply to very specific circumstances. For those special snowflakes and occassions. When in doubt, contact us!

- **Retaining original DOCTYPEs**: By default, the proxy generates an HTML5 standards-compliant file to send to the client. If, for some reason, this causes problems due to the site relying on HTML4 standards for operation, some of which may be deprecated by HTML5, enabling this option will cause the Proxy Application to retain the original DOCTYPE declaration of the source page.

- **Determine document type by** `GET` **instead of HEAD**: some servers may return different responses to the HEAD request we use to determine document type than the GET request used to download content. Enabling this option forces the proxy to use GET requests for all operations, getting the correct content type from the server (as far as server-side configurations will allow).

- **Detect JavaScript content type**: JavaScript may not be explicitly declared as such on the server, being sent to the client with misleading content types. This causes the proxy to mis-identify such streams and not offer operations reserved for JS files. Enabling this option will force a deep check on each file sent to the client, to determine if they are indeed JavaScript code, regardless of their declared content type.

- **Download images through the proxy**: this will instruct the Proxy Application to attempt to map all `<img src>` attributes to the proxied domain. This is especially useful if the images are served only after authentication.

- **Attempt to place tags according to punctuation when using TM-based pre-translation**: if using a TM-based pre-translation, the Proxy Application may encounter segments where it cannot replace the XLIFF tags automatically, due to overly large differences between the contexts (possibly because of a changed site). If this option is enabled, the translator will try to replace the XLIFF tags according to their positions relative to punctuation marks in the segment. If successful, the TM entry’s confidence score will be increased by 0.1.

- **Translate excluded pages when viewing them in Preview mode (but still not in live serving mode)**: It may be necessary sometimes to view excluded pages as if they were translated, in order to assess their layout, without actually making them available on the live site. Enabling this option allows just that, by propagating translations to the excluded pages if viewed in Preview mode, but keeping them untranslated in Live serving mode.

- **Translate** `javascript:` **attribute**: The Proxy is capable of extracting and translating code from the onclick attribute of elements. This feature may be used when a site uses this attribute to store translatable content inlined into the attribute and requires this content to be translated. Currently we only process the onclick event’s contents, all other events in the javascript attribute will be ignored.

- **Detect and handle JSON-in-string responses, like** `"{\\"ResponseCode\\":\\"BadRequest\\"}`: string-escaped JSON-format responses can be handled by activating this tweak. If active, the proxy will first attempt to string-unescape the response before passing it to the JSON parser, in order to recreate its base form.

- **Make content in** `<script type="text/html"></script>` **translatable as a whole (don't try to parse it as HTML)**: Script blocks may contain template data requiring translation, which is often signified by the text/html content type (instead of the more usual application major type). In such cases, HTML parsing can be undesirable, and can be bypassed by activating this option.

- **Send a canonical link http header pointing to the original page on externalized pages**: the proxy can insert a Link header into externalized pages, in order to avoid the SEO penalty associated with duplicate content. This header will point to the original address, and have `rel=Canonical` added, to designate the relationship.

- **Perform string concatenation in JavaScript before parsing.**: the proxy will perform string concatenation and treat the result as a whole when translating/extracting it. This tweak is only useful if *no computable expression* is featured in a given concatenation.

## Manual Publishing

*Manual Publishing* is advanced project control feature that gives project owners the ability to withhold the translations from being published on the live page (but not the preview, as it will always display the latest translation available!) until further notice.

The feature can be activated from the Advanced Settings page. Once activated, it will affect all translations going forward, but already-existing ones will not be “un-published”.

Once active, a new item will appear in the Bulk Actions menu of the Workbench: “Publish”. Running this action will cause all selected segments to be synchronized with their displayed translations, and once the action finishes, the markers in the status bar on the right of the entries will change to reflect this. If the action encounters an error, the server will attempt to rectify this by publishing the entire entry, after confirmation from the user. If the error is not recoverable, it will list the segments in error.

## Default segment state

By default, the proxy will add new segments during a crawl as “Approved”, making them available for translation immediately. However, if the user/client so desires, this behavior can be changed to adding new segments in one of the two other states, “Pending” or “Excluded”. If the default setting is changed, the project owner, backup owners, or users with the Customer Role can alter segment states.

“**Pending**” segments are those that are awaiting a decision on translation. They will not be included in exports unless the relevant option is selected at export-time, and they will not appear in the Workbench for translation unless filtered for specifically. Those users able to alter segment states may change the state of these segments either by approving them for translation or excluding them altogether.

“**Excluded**” segments are those that have been deemed as not requiring translation at all. Unless the relevant option is selected, they are not included in exports and will not appear for translation unless filtered for specifically. Excluding a segment is not final, however: those users able to alter segment states may approve them for translation, making them available again.
