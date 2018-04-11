# Javascript editor

An editor with syntax highlighting support is available on the Dashboard. You can add JavaScript code here, which will be injected into the `head` tag of each page. By default, it contains placeholder code that demonstrates page modifier use. The following snippet also demonstrates a plausible page modifier:

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

**IIFE**s (Immediately Invoked Functional Expressions), such as in the script above, are a generally good pattern to use with a page modifier. In this way, a programmer can continue to work within the confines of their local scope, and the function and variable definitions will not intrude on the global namespace - when it comes to page modifiers, it is very important that the modification has as little chance to clash with site code as possible (unless in a considered move).

The structure below can serve as an even simpler skeleton for a page modification:

``` javascript
(function () {

    "use strict"

    $(document).ready(modifyPage); // if jQuery is present

    function modifyPage () {
        console.log("modifications go here");
    }

})()
```

Of course, the possibilities of code injection are endless. See our tutorial for [site search integration](../../dashboard/cookbook/sitesearch.html) for a comparatively detailed example to help you get a glimpse of the possibilities of injected JavaScript. 

The code injection feature puts the power of all client-side coding at your fingertips, and a truly in-depth discussion of the core web technoliges is not possible in this documentation. The excellent [Mozilla Developers Network](https://developer.mozilla.org/) contains all the details you could ever need, and the [W3mschools](https://www.w3schools.com/) website contains useful tutorials on various web-related topics if you are just starting out.

Development Tip: a userscript extension, such as Tampermonkey can be used to develop page modifiers locally. While the Dashboard editor is adequate for basic editing, it is not meant to replace the many powerful editors available. Tampermonkey can `@require` your script from the filesystem if it is granted `file://` access (supported by Google Chrome), in which case you can use your editor of choice and retain preview-on-refresh capability.

But keep security in mind!

