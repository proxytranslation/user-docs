# Javascript editor

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

You can also use jQuery if it is present on the original site.
