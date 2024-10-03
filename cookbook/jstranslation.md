# JS/JSON/XML Translation

In this section, we describe the process of translating content in JavaScript files and dynamic (JSON or XML) responses.

## General

Translation of HTML is mostly automated over the proxy. But websites rely on many additional resources besides the document itself, such as JS libraries, CSS stylesheets, webfonts, dynamic requests and images. Not all of these resource types require translation, but JSON and XML responses frequently do. Such responses can also present significant challenges for both translators and proxy specialists.

One of the problems is detection: proxy crawls/analyses do not operate in a browser-like environment. There is no headless browser or VM running in which a page load could be initiated or JavaScript evaluated for content detection purposes. Inherent complexity is another issue: the enormous diversity (to put it charitably) of web technologies in use nowadays prevents reliable automation of such a process.

But, though JS/dynamic content can slip under the radar at first, the proxy can easily translate it with some help.

## Finding Content

An early investigation will reveal content that is unavailable to the crawler by default, and will save you trouble (of having to deal with untranslated content as late as in the review phase, for instance).

### X-proxy

To check how a website is doing over the proxy, open it in the **X-proxy** mode, a specialized Preview mode available through the Dashboard Pages list. Right-click on any of the pages and select X Proxy to view the page in the Preview mode.

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

You can mark a resource as translatable manually on the Resources screen (second tab in the Pages list) or using the Send to Pages feature under the JSON/JS/XML processing menu item.

### Manual

All collected resources are listed in Pages list > Resources. All "pages" and files that are not of the `text/html` content type will be collected under these tabs.

It's important to note that collected images will also land here, you can read about how to replace them with localized versions [here](./../cookbook/resourcetranslation.html).

What sets resources apart from pages is that by default, they have no associated *source entries* or translations. Marking a resource as translatable means declaring that it does have translatable text that can be stored as source entries (and accessed via the Workbench).

So, to mark a resource as translatable:

![Click on it in the Resources tab](/img/dashboard2/mark_as_translatable.png)

and click Mark as translatable in the panel on the right side.

Then click Manage translations in the same panel. Here, you can provide the link the proxy should serve.

![Translate Resource](/img/dashboard2/manage_translations.png)

You can also move the Resource to the Pages list, if it's under the same domain as your project (or a [linked project](./../dashboard2/dashboard2.html#linked-projects)).

![Click on Send to Pages for content processing](/img/dashboard2//move_resource_to_pages.jpg)

### Mass link replacement

You can mark multiple links at once to be replaced when serving the translated version of your site. Go to Mass link replacement under Pages. Go through the steps one-by-one, but the second step is where you need to copy & paste the URLs of your choice.

![Mark Multiple Resources](/img/dashboard2/mass_link_replacement.png)

You are free to add as many of them as you like.

### Prefixes

You can also mark resources to be moved under the Pages list en masse by specifying path prefixes for them. This feature is available under the JSON/JS/XML processing menu item. You have to scroll down in the first tab (Live JSON/JS/XML path config tab) until you see this ![content box](/img/dashboard2/send_to_pages_by_prefix.png)

This feature is made available because cherry-picking resources for translation is not always feasible. For instance, versioned URLs are liable to create new resources on a project whenever a file is updated on the original site (the proxy keeps these URLs separate by default), but the new resources are not marked automatically.

You will recognize those cases where you want to apply the exact same translation rules and process to a set of URLs that differ in minimal ways. A resource prefix will let you do this without having to mark things one-by-one as they come.

You can add as many prefix rules here as you like.

## Annotating JS/JSON

Picking up JSON/JS/XML content *wholesale* would be both costly and unwieldy. When you have successfully identified the source of content and earmarked it for translation, the last major task is to annotate those parts of it that really want to translate. **JS/JSON paths** and **Xpaths** can be used for this purpose.

### JS/JSON paths

Go to JSON/JS/XML processing on the Dashboard 2.0, and select the JSON path tester tab. This tool can be used to mark specific string in JavaScript or in JSON as translatable. You can more about it [here](../../dashboard2/settings/jptt.html)

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

This implies that those instances of string concatenation where *no* token of the expression is computable are supported. This is indeed so, and provided that the appropriate tweak is enabled in [Advanced settings](../settings/advancedsettings.html#tweaks), the proxy can perform string concatenation *upfront* and handle the resulting string as a whole.
