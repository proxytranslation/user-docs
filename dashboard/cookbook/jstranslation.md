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

#### JSON Path tester

Go to Advanced settings > JavaScript translation options, and click on the "JSON Path tester tool" link right below text field to open the tester dialog. It looks like this:

![JSON Path Tester](/img/dashboard/path_tester_default_view.png)

We'll use the following JavaScript snippet in the remainder of this section. It illustrates many use cases for JS translation:

``` javascript
(function () {

  var exampleVar = "Hello World!";

  var exampleUrl = "https://shadowcat.skawa.hu";

  var exampleHtmlString = "<p>Hello World!</p>";

  var exampleObject = {
    "sentence01": "Hello World!",
    "sentence02": "Hello Again!",
    "nestedObject": {
      "sentence03": "Hello World!",
      "sentence04": "Hello Again!"
    },
    "exampleArray": [{ "value": "foo" },
                     { "value": "bar" },
                     { "value": "baz" }],
    "exampleNestedJS": "var nestedVar = { nestedKey: \"Nested sentence\"}",
    "exampleNestedHTMLinJS": "var nestedHTML = \"<p>Hello world!</p>\""
  };
})();
```

You can copy & paste code into the upper field (or fetch the entire file via the field & button on top if you have the URL) and click on "Analyze script". The file/text will be requested/sent for analysis in the cloud, when it's finished, you should get a highlighted representation of the same code in the dialog.

Click on any of the blue icons to generate a **JS path** for the string in question. If you generate paths for all available strings in the example , the list of paths in the upper text field should look like this:

```
"%"."exampleVar"
"%"."exampleUrl"
"%"."exampleHtmlString"
"%"."exampleObject"."sentence01"
"%"."exampleObject"."sentence02"
"%"."exampleObject"."nestedObject"."sentence03"
"%"."exampleObject"."nestedObject"."sentence04"
"%"."exampleObject"."exampleArray".0."value"
"%"."exampleObject"."exampleArray".1."value"
"%"."exampleObject"."exampleArray".2."value"
"%"."exampleObject"."exampleNestedJS"
"%"."exampleObject"."exampleNestedHTMLinJS"
```

Some of these paths require adjustment before they'll behave correctly.

Supported strings are highlighted in **red**, and those that are already covered by a listed JS path are be highlighted **green**. Your results should look

![Path results](/img/dashboard/path_tester_results.png)

When you have all the JS paths you need, copy & paste them into the main JS translation text field in Advanced settings. Click on "Save" to apply your changes.

#### Keys / Variables

Translatable elements are specified by a dot-separated list of words, each optionally double quoted and constituting either a.) a valid JS variable/JSON key name or b.) a token specifying one or more hierarchical levels (anonymous function, array index or globbing mark).

```
var exampleVar = "Hello World!";
```
The simplest possible case would be `"exampleVar"` to mark the value of the top-level element `exampleVar` as translatable. Anonymous function calls are denoted with `"%"`, and since the entire block of variables is wrapped by an anonymous function `(function () { ... })()`, this leading ampersand shows up in each case. Paths for dynamic JSON responses should be prefixed with `"json"`.

#### Globs

Use an asterisk (or Kleene-star) to collapse a single hierarchical level. E.g., the value of`"exampleArray"` is an array of objects. To include every index in the array, you can roll three rules into one:

```
"%"."exampleObject"."exampleArray".*."value"
```

Double asterisks are even more inclusive: they recursively glob all child nodes. Exact specification can be restarted by following `**` with a double-quoted form. That is, the rule

```
`%`.**."value"
```
marks any variable or property called `value` it finds *at any hierarchical level* within an anonymous function call. If a JS path *ends* with the `**`, then the entire subtree is marked as translatable. Incautious use of this construct is not recommended.

#### Processing Modes

Nodes are processed as plain text by default, but you can enable specific processing modes with whitespace-separated postfixes. The available processing modes are `url`, `html` and `javascript`.

##### URL

Variables can contain either *the project URL* or some other important location (such as that of a *linked project*) that you would prefer to have **remapped** over the proxy. Don't give in to the temptation to localize URLs in JS as plain text! Instead, use the `url` postfix to map them:

```
"%"."exampleUrl" url
```

##### HTML

`exampleHtmlString` demonstrates the fact that JS variables frequently hold markup (for better or worse). The `html` postfix lets you process these strings as HTML.

```
"%"."exampleHtmlString" html[@process]
```

![Extraction with and without HTML-processing](/img/workbench/js_entry_wo_markup_comparison.png)

The screenshot above demonstrates the difference HTML-processing makes. Picking up HTML-markup explicitly as text is generally considered error-prone and disadvantageous from a localization viewpoint, and isn't recommended.

`[@process]` is optional. By adding it, you instruct the proxy to apply the translation-invariable regular expressions currently set on the project.

##### Nested Javascript

Although JS paths are mostly specified in a single line, the `javascript` postfix bends this rule. It tells the proxy to apply the rule in the *next line* to the value of the postfixed JSON path. One level of nesting is supported. It is rarely needed, but invaluable when it is called for.

Plain text:

```
"%"."exampleObject"."exampleNestedJS" javascript
"%"."exampleObject"."exampleNestedJS"."nestedVar"."nestedKey"
```

HTML:

```
"%"."exampleObject"."exampleNestedHTMLinJS" javascript
"%"."exampleObject"."exampleNestedHTMLinJS"."nestedHTML" html
```
Note that the JSON Path tester tool is not equipped to display the nested use case.

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
