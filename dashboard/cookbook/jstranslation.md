# JS/JSON/XML Translation

In this section, we describe the process of translating content in JavaScript files and dynamic (JSON or XML) responses.

## General

Translation of HTML is mostly automatized over the proxy. But websites rely on many additional resources besides the document itself, such as JS libraries, CSS stylesheets, webfonts, dynamic requests and images. Not all of these resource types require translation, but JSON and XML responses frequently do. Such responses can also be very inhospitable to the translator and proxy specialist.

One of the problems is detection: proxy crawls/analyses do not operate in a browser-like environment. There is no headless browser or VM running in which a page load could be initiated or JavaScript evaluated for content detection purposes. Inherent complexity is another issue: the enormous diversity (to put it charitably) of web technologies in use nowadays prevents reliable automation of such a process.

But, though JS/dynamic content can slip under the radar at first, the proxy can easily translate it with some help.

## Finding Content

An early investigation will reveal content that is unavailable to the crawler by default, and will save you trouble (of having to deal with untranslated content as late as in the review phase, for instance).

### X-proxy

To check how a website is doing over the proxy, open it in the **X-proxy** mode, a specialized Preview mode available through the Dashboard page list. Click on Preview in the hover menu while holding `Ctrl` to open it.

Note that you need to *add at least one target language *and* select it in the left side menu* to access the preview.

The X-proxy replaces text it recognizes with x-es. Though not too impressive visually, it is an excellent research tool. It lets you *home in on undetected content*. To utilize it most effectively, combine it with your browser's DevTool.

Major browsers such as Firefox and Chrome allow you to do full-text search on (almost) all resources/requests used during and after page load. In Chrome, for example, you can press `Ctrl`  + `Shift` + `F` to start a full text search in the DevTool.

The following screenshot demonstrates how the X-proxy can make untranslated/undetected content obvious:

![x-proxy example](/img/x_proxy_example.png)

Having removed all known text from the equation, you are free to concentrate on the "untranslated" parts. Findings will naturally be site-specific, but there are some familiar, recurring scenarios:

1. **content is in `<script>` tags**: this is the simple case, as there isn't even a distinct resource to mark as translatable. `text/html` pages are translated by default, and JS content in them can be annotated right away.

2. **content is a string in a JS file**: aside from the necessary annotation process, you'll also need to ensure that the resource in question is marked as translatable.

3. **content is requested dynamically**: dynamic content can be tough to dig up. Many DevTools don't support full text search in XHR response bodies. If content is in plain sight on a webpage but the DevTool is not reporting any of it, then the content could have arrived via an XHR request. Check the "XHR" section in the Network tab after a reload. Aside from the inconvenience of locating them, dynamic request endpoints can be annotated and marked in the same way as JS files.

4. **content is on an external domain**: this scenario requires some work. External domains require separate, but linked projects (add to this that you also have to ensure that URL references are mapped well, which can be difficult in a JS file), and the resources have to be marked and annotated on those projects to be translated.

5. **content is in an image**: though not strictly connected with the topic of JS translation, an "honorable" mention goes to natural language content *as image data*, also frequently revealed by the x-proxy.

There are many ingenious ways in which webpages encode content, and the proxy has various levels of support for all these schemes (usually involving a combination of features). When in doubt, feel free to contact support for advice!

## Marking Resources

You can mark a resource as translatable manually on the Resource screen or using a prefix in Advanced Settings.

### Manual

All collected resources are listed in Discovery > Resources and Content > Resources. All "pages" and files that are not of the `text/html` content type will go here.

What sets resources apart from pages is that by default, they have no associated *source entries* or translations. Marking a resource as translatable means declaring that it does have translatable text that can be stored as source entries (and accessed via the Workbench).

So, to mark a resource as translatable:

![Switch to List View](/img/dashboard/resources_list_view_filter.png)

1. switch from thumbnail view to list view

2. click on the "Translate" button in the hover menu of a resource

![Translate Resource](/img/dashboard/resources_list_view_translate.png)

The resource is moved to the page list and from that point onward, it can be opened on the Workbench. Note, however, that we have not yet told the proxy what and how to translate in it.

### Prefix

You can do the marking via prefixes. Go to Advanced settings to find the "Mark Multiple Resources as Translatable" text field. Copy & paste the prefixes of your choice and click on Save to apply your changes.

![Mark Multiple Resources](/img/dashboard/advanced_multiple_resources.png)

Note that in the screenshot above, HTTP and HTTPS prefixes are handled separately, a recommended practice for sites that support both kinds of traffic. Prefixes are treated as simple strings by the proxy when matching them against a pathname. You are free to add as many of them as you like.

This feature is made available because cherry-picking resources for translation is not always feasible. For instance, versioned URLs are liable to create new resources on a project whenever a file is updated on the original site (the proxy keeps these URLs separate by default), but the new resources are not marked automatically.

You will recognize those cases where you want to apply the exact same translation rules and process to a set of URLs that differ in minimal ways. A resource prefix will let you do this without having to mark things one-by-one as they come.

## Annotating JS/JSON

Picking up JSON/JS/XML content *wholesale* would be both costly and unwieldy. When you have successfully identified the source of content and earmarked it for translation, the last major task is to annotate those parts of it that really want to translate. **JS/JSON paths** and **Xpaths** can be used for this purpose.

### JS/JSON paths

Go to JSON/JS/XML processing on the Dashboard 2.0, and select the JSON path tester tab. This tool can be used to mark specific string in JavaScript or in JSON as translatable. You can more about it [here](../../dashboard2/jptt.html)

### Xpaths

Xpaths for XML AJAX responses in a similar way as JS/JSON paths do for their respective content types. For example, `/ajax-response/component[1]/text() html`
assumes that the first `<component>` node contains translatable HTML markup.

Due to space constraints, we decline to reproduce a full Xpath tutorial in this documentation, and direct the reader's attention to the many tutorial resources available online. The W3Schools [summary of Xpath syntax](https://www.w3schools.com/xml/xpath_syntax.asp) serves as a good starting point.

### Limitations

#### Content extraction

A simple content extraction crawl takes care of JS content in the source of an HTML document. But in many cases, such content is requested **as part of a page load** or **via user action**. The same limitation still applies, however: the page is not available to the crawler in a way that would allow for such "interactive" requests to start.

The solution is to extract content **via Preview**. Open the page in Preview mode and go through the required user actions to trigger all necessary events. The proxy will take care of extracting content from the affected dynamic responses (provided that your setup is correct).

Note the influence of **TM Freeze** on this approach: you need to disable it temporarily for Preview-based content extraction to work.

#### String Concatenation & Computed Values

JS translation cannot be used with values such as `var string = "You have " + getCartItems().length + " items in your basked"`). In these cases, you either have to forego translation or change the content so that no *computed expression* is present among the concatenated elements.

This implies that those instances of string concatenation where *no* token of the expression is computable are supported. This is indeed so, and provided that the appropriate tweak is enabled in [Advanced settings](../../menu/dashboard/advancedsettings.html#tweaks), the proxy can perform string concatenation *upfront* and handle the resulting string as a whole.
