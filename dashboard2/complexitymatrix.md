Complexity Matrix
=================

The Complexity Matrix (CM) is two things: first, it is a **note-taking application** where you can order your knowledge of a site and various issues in relation to the project. Second, it is the first feature to showcase the look & feel of the **Dashboard 2**. Feedback is welcome!

You'll recall from the introduction that there are a number of questions to ask when you embark on a new project, so as to create better forecasts for your project expenses and the required amount of work to get the project going. The CM is meant to make this easier via a screen that you can use to track issues from within the project itself.

# Accessing & Using the CM

While incremental development of the Dashboard 2.0 is ongoing, the old interface remains available. From there, go into the Dashboard menu and click on **Complexity Matrix** to access the new Dashboard and the CM screen.

## Navigating the CM

[Complexity Matrix Screen](/img/dashboard2/complexity-matrix.png)

Expect the left-side menu to have additional items added as development of the new interface progresses. For now, it contains the menu entries for the Complexity Matrix itself and a link to what we have now retroactively dubbed *Dashboard 1.0*, the old user interface. The left-side menu itself can be hidden using the hamburger menu icon on the left-side of the header.

The header also contains a search field and drop-down that you can use to search in your projects. Click on any of them to open their associated Complexity Matrix.

In the CM, a project consists of four distinct aspects you can use to categorize various issues:

1. **QA Test: Possible Issues/Bugs**

2. **Code**

3. **Layout**

4. **User Experience**

You can open and close each entry with a single click. When opened, they will reveal further, more granular categorization of potential issues that warrant attention (discussion of which follows below).

Each categorization has an associated dropdown on the left that you can use to mark it as present. You can mark an issue as causing "**MINOR**", "**MAJOR**" or "**SEVERE**" problems over the proxy. Otherwise, you can leave the dropdown in its original position of "**NONE**".

Each of the categories can be clicked to reveal an editing field that you can use to keep track of the various issues that you detect on the site. The text fields support markdown/basic HTML.

In the following sections, we'll discuss the various aspects of a project's potential complexity using the various available categories in the Complexity Matrix, and list a few examples that are worth documenting if you come across them.

# QA Tests

QA tests should be considered as part of the project setup phase. In the remainder of this documentation page, You will find a non-exhaustive list of possible issues that warrant careful consideration.

## JavaScript

### Content in JavaScript

The proxy will find all translatable content in the HTML source, but such is not the case with JS: the appropriate JS Translation paths need to be worked out and added to the Advanced settings. Use the x-proxy after Discovering/Scanning a site to reveal any content that was not found by the crawl.

If you notice that specific parts, such as the navigation bar or a user account page are not x-ed out in the x-proxy, it is likely that that content is in JS in `<script>` tags, or discrete JavaScript Resources that are requested as the page is loading.

Investigating the original site and the proxy preview for content in JavaScript increases project setup time.

**Things to Note**

- *Watch the **domain of origin** for JS resources. Translatable content on external domains takes longer to set up.*

- *string concatenation (especially that of HTML markup) is difficult to overcome. The example below is a **sign of trouble**!*

```javascript
var exampleVar = "world"
var htmlContent = "<div><p>Hello " + exampleVar + "</p></div>"
```

#### URLs in JavaScript

JS code often contains URLs or pathnames that are referred to elsewhere when making requests (both for intra and extra-domain Resources). Since the proxy will remap the project domain according to its own preview and publishing settings, it is possible that the JS URLs will point to the wrong place.

**Things to Note**
- *Fully qualified, non-concatenated URLs can be remapped via a tweak available in Advanced settings.*

## Functionality

### HTTP and HTTPS

If you notice that a site uses HTTPS, pay attention. Since the proxy preview domains are certified themselves, you can go a long way without realizing that the Live target language sub-domains will also require certification. Procuring an appropriate SSL certificate takes time, and it can become blocking in the Publishing phase.

**Things to Note**

- *An SSL certificate for the published sub-domains is necessary.*

### Site Search

Most large-scale websites nowadays have a site search functionality that requires additional work on the proxy end of things to intergrate appropriately.

**Things to Note**

- *Evaluation of the Site Search functionality increases project setup time.*

- *The proxy supports Google's Custom Search Engine. The integration has to happen via JavaScript page modifiers to maintain the original look and feel of the site - this, however, means coding work.*

### Language Selector

Many sites already have some sort of localization solution in place. Investigate the current language selection mechanism for potential issues.

**Things to Note**

- *If a language selector is already present, it might require some tweaking on the original server to better handle the **link mapping** that happens over the proxy. The `__pTNoremap` class needs to be added to `href` attributes that should not be remapped.*

- *If there is no selector, it will have to be implemented,or one of the default proxy selectors used. This requires action from someone who has **access to the source** on the original server - these changes can increase the time it takes for a project to go live.*

### Plugins

### External i18n Modules

Closely related to the Language Selector, the presence of i18n modules can life easier or more difficult, depending on what you can do with them. Consider whether these modules can be reused in the context of the proxy or if new translations will have to be provided.

**Things to Note**

- *Is the i18n module part of minified code? Is it dynamic content? These are usually extremely difficult to reliably reuse.*

### User Sessions & Logins

Sites often have sections that require login credentials. The proxy can handle these sections if it is passed the appropriate **session cookies**.

**Things to Note**

- *Extracting session cookies is an additional step that needs to be executed for each Scan/Content Ingestion Cycle.*

### Query Parameters

Sometimes, the project page list will contain many instances of the same path with different query parameters after a Discovery. The thing about query parameters is that they do not necessarily imply unique content for the specific settings they engender. For example,

https://example.com/products?sort=asc

https://example.com/products?sort=desc

could plausibly serve exactly the same content, only in different order. Conversely, it could also be requesting an entirely different set of data to use in the browser. This requires careful combing of the site to make sure that all necessary content is extracted, but no superfluous pages are kept.

**Things to Note**

- *The proxy can ignore or group specified query parameters, but figuring out which ones to keep and which ones to throw away will add to project setup time.*

- *Consider also that independently made changes to the original site might instantly deprecate your current project settings - this also has implications for the maintenance phase of a project.*

## Dynamic Content

### XHR, AJAX, XML and JSON

**Things to Note**
- *Dynamic content has to be extracted manually **via the Preview***.

### Webshops

### Single-Page Applications (Angular, etc.)

## Layout & CSS

### Word lengths

English and German, for example, differ considerably in their average word lenght. While not normally an issue in the case of paragraphs, this can become an issue if some part of the site layout is too tight (for example, a navigation header with widths declared in pixels). If too many assumptions are ingrained in it about the amount of content that has to fit in a given element, that might need some tweaks.

Other times, enclosing elements (such as border boxes) will change their size based on the amount of text they contain. This potentially requires some target-language specific tweaking of the layout via CSS/JS Page modifiers.

**Things to Note**

- *Some things can be made to fit via CSS tricks and Page Modifiers. In other cases, only rewording will help if extensive reworking of the site layout is not an option.*

### Text Direction

### Responsive Layout

# Code Issues

## Translatable Content in JavaScript

## External Content, Project Linking, Forms, *<iframe>* tags

### Hubspot & Marketo

# Layout

## Responsive Layout

## Proxy Compatibility

# User Experience

## Wording, Layout

## Content Access

## Consistency
