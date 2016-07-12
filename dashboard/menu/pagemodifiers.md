## Page modifiers

While translation over the proxy makes website localization easy, it
is also a fact that UI issues can sometimes surface when a page is
proxied.

Suddenly served in a different language from the one the UI designers
anticipated, websites can display a variety of UI quirks. As website
translation is still, sadly, more often than not an afterthought,
these issues have to be dealt with in the translation pipeline.

Word length differences between the source and target languages might
cause the menu to crowd. Differences between the lengths of different
text blocks can cause otherwise well-designed CSS rules to behave in
unexpected ways. Not to mention the plethora of plugins that run on a
modern website - there is a big pool of possible glitches right there.

Fortunately, changing the site content over the proxy is relatively
easy. The Page Modifiers function is made available for this reason:
to empower you to add your own CSS rules and JavaScript snippets to
influence the way a given proxied site looks to the user.

Because the datastream must pass through the proxy to have the
translation embedded, the proxy can insert JavaScript modifiers,
modify style sheets, even embed entire pages that do not exist on the
original site.

CSS rules and JavaScript are injected into each page that is served
over the proxy.

### CSS editor

he Proxy Application can be used to insert locale-specific CSS rules
into the site being served. The rules are inserted as the last element
of the head on every page served through the proxy. A very common use
case for this feature is RTL conversion of a website: almost always
necessary when one of the target languages is Arabic.

There are a couple of caveats:

It is good practice to make each CSS rule language specific:

```css
html[lang="de-DE"] ul.one-selector li a {
  float: left; 
}

html[lang="fr-FR"] .another-selector h2 {
  height: auto;
}
```

if you omit the `html[lang="fr-FR"]`, the CSS rule will be applied for
all target languages, which might not be the behavior you expect.

### Javascript editor

Here is a partial, but plausible example of a JavaScript Override:


```javascript 

(function() { 
    
    "use strict";
    
    document.addEventListener("readystatechange", function() {
        if (document.readyState === "interactive") {
            resizeTextBoxOnContactPage();
        }
    }, false);
    
    window.addEventListener("resize", function() {
        resizeTextBoxOnContactPage();
    }, false);

    // make function page-specific. Altenatively, add check to eventListener above
    function resizeTextBoxOnContactPage() {
        if (document.location.pathname !== "/contact-us") { return };
            // implementation details here
    }

    // more function definitions here
    
})();

```

**IIFE**s, such as in the script above, are a generally good design
pattern for Page Modifiers, since the programmer can work within the
confines of their local scope. The function and variable definitions
will never escape into the global namespace - which is a conversely
bad idea, as it could potentially conflict with original code on a
site.

An in-depth discussion of JavaScript is not possible in this manual,
but there is generally no limitation on the type of code that can be
injected via Page Modifiers. **Security implications should always be
considered when adding custom code to sites.**

You can also use jQuery if it is present.

### Content override

The Proxy Application can create a “virtual” page in the site or
override an existing one with custom code. For any requests to an
overridden page, the corresponding remote server request is not sent,
and the override contents are used as the basis of the
translation. The source is not required to be HTML, custom
content-types can be entered, along with customized cache headers, and
status codes (HTTP status codes are restricted to those permitted by
the Java Servlet class!) - note that the 300-family of status codes
requires the Location header to be defined as well.



