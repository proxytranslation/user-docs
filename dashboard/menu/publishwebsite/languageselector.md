# Language Selector

As translation of a website is nearing completion, it is usually necessary to prepare a language selector to make the various languages more accessible. There are two options:

    1. develop a custom selector in-house
    2. use one of the proxy default selectors.

In all cases, the addition of a language selector will need to be done on the original server and then propagated to the translated domains through the proxy.

## Proxy Solutions

To spare you the expense and time of developing a custom language selector, we have prepared two default solutions you can use. Each of these require the minimum possible intervention on the original site for deployment. Note, however, that seamless visual integration of the selector requires some fiddling with the CSS rules. The following two types of language selectors are available:

### Sidebar

The sidebar is an easy-to-deploy-and-use language selector (with limited customization options) that doesn’t require any changes on the original site beyond the addition of a single `<script>` tag to the source code. The language selector is a hovering sidebar which displays the flags of the selected target languages.

The sidebar is an easy-to-deploy language selector that displays flags for each specified target locale on the left or right side of the website. The horizontal orientation and display names are settable.

**Set-up steps**

*On the Dashboard:*

1. Click on the Publish Website menu
2. Select “Sidebar”
3. Select “Left Side” or “Right Side” according to your preference
4. Specify the Target languages by enabling the last checkbox on the screen

Note: You may also declare custom language names to be displayed by using the dropdown selector or choose “Language” to display only the language, but not the Country.

*On the original site:*

5. Finally: copy the embed code from the textbox and add it to the end of `<head>` tag on the original site.
With the tag added to the original site, a reload should reveal the language selector.

### Dropdown

The Dropdown is the more customizable option. One bit of additional adjustment in the original source is necessary, however: besides adding the `<script>` tag, a dedicated `<div>` tag is also necessary – since the dropdown is more closely integrated with the site structure (that is, it has to be positioned in relation to other elements), this `<div>` tag will be used to locate the designated location of the dropdown.

**Setup steps:**

*On the Dashboard:*

1. Click on Publish Website menu
2. Select “Dropdown” (default)
3. Declare a unique class name for the `<div>` that will contain the language selector. The default is `el-dropdown` but you may specify any class name that does not clash with any other classnames in the original HTML. For the purposes of this tutorial, the classname will be `el-dropdown`
4. Select a display template. You may choose between “Language ( Country )”, “Language” or entirely custom names according to your preference.
5. Specify the Target languages by enabling the last checkbox on the screen.
6. Copy the embed code from the textbox.

*On the original site:*

1. Locate the position in the markup that you wish to insert the Dropdown
2. Extend the HTML markup with a `<div>` tag. Furnish it with the previously specified class. In this case, it would look something like this:
`<div class=”el-dropdown”></div>`
3. In addition, Add the embed code copied from the Dashboard to the `<head>` tag of your page.

**Post-setup:**

At this point, the language selector is displayed after reloading the page in your browser (the JavaScript referenced in the `<script>` should take care of downloading and rendering it).
The language selector contains a menu button, a container and target language entries you can customize via CSS rules. The language selector is self-contained for convenience, so it uses in-line styling. Postfix your CSS rules with “!important” to make sure that they are applied.

### RYO or Existing Selector

It is possible that site undergoing translation is also running (or was previously running) a different localization solution, in which case a language selector is usually already present. It is relatively straightforward to extend an existing language selector with the proxy-published target languages.

Since that language selector is also proxied, it is important to protect the link pointing to the original language site from being remapped in the process.

In order to do this, the `__ptNoRemap` special class can be used to indicate to the proxy that it should not change any links in the given tag.

A brief example of how the original site link can be protected from remapping with `__ptNoRemap`:


``` html
<div class="selector-container">
    <ul id="selector">
        <!-- PREVENT REMAPPING OF ORIGINAL LINK - this requires a full domain-->
        <li id="en-US" class="language selected"><a href="//www.example.com" class="__ptNoRemap">English</a></li>
        <ul class="dropdown">
            <li id="de-DE" class="language"><a href="//de.example.com">Deutsch</a></li>
            <li id="fr-FR" class="language"><a href="//fr.example.com">Francais</a></li>
        </ul>
    </ul>
</div>
```


You may also wish to use the translate=”no” attribute in places where you want the proxy to ignore the textual content of the HTML element.

#### Example

Depending on how involved it is, a language selector may have to react to user input/animate dropdowns/start XHR requests, etc. Its appearance and behavior depend on the number of languages, publishing method, site layout & design etc, which is beyond the scope of this manual. But to get you started with a suggestion, a commented minimal example in vanilla JS/CSS follows below, which is also available in a slightly modified form as a JSFiddle [here](https://jsfiddle.net/entjj497/).


``` javascript
(function () {
    "use strict";
    /* The target locale code, a two-letter language code plus a two
       letter country code, separated by a dash, is added
       automatically over the proxy. Either this value or the HTML
       markup might have to be adjusted to be applicable on the
       original site */
    var lang = document.querySelector("html").getAttribute("lang") || "en-US";
    /* The usual "readystatechange" event listener works if
       you need to wait

       document.addEventListener("readystatechange", function () {
            if (document.readyState === "complete") init();
       }))
    */

    init();

    function init () {
        selectDefault();
        setEventHandlers();
    }

    function setEventHandlers () {
        var items = document.querySelectorAll("div.selector-container li.language a");
        for (var i = 0; i < items.length; i++) {
            items[i].addEventListener("click", function (e) {
                selectLanguage(e.target.parentNode);
            })
        }
    }

    function selectDefault () {
        /* See if we can select anything in the language selector
           based on our locale code. */
        var base = document.querySelector("div.selector-container li#" + lang);
        /* ...and try to default to anything we've found */
        if (base !== "undefined") selectLanguage(base);
    }

    function selectLanguage (target) {
        /* 'click' event was triggered on any of the language selector
           entries. */
        var selected = document.querySelector("li.selected");
        var dropdown = document.querySelector(".dropdown");

        /* don't do anything if we would be switching to the same
           language */
        if (target === selected) return;

        /* SWITCH LANGUAGE.

           ...but we are only "swapping elements" in the menu (the
           code doesn't navigate in actuality). A target language
           domain or a CST query parameter could result in a page
           load.

           The "dropdown" approach showcased here is also an
           illustration of a frequent issue: when selectLanguage() is
           called, the selected target language is replacing the
           current one in the dropdown list. So, if you are particular
           about the target languages being listed in a set order, a
           hide/show approach might work better than DOM element
           swapping. */
        target.setAttribute("class", "language selected");
        selected.setAttribute("class", "language");

        selected.parentNode.replaceChild(target, selected);
        dropdown.insertBefore(selected, dropdown.firstChild);
    }
})()

```

Below are the associated CSS rules.

```
div.selector-container ul {
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5) !important;
  list-style: none;
  margin: 0;
  padding: 0;
}

ul#selector {
  list-style-type: none;
  text-align: center;
  background-color: #f5f5f5;
  max-width: 100px;
}

ul#selector li {
  list-style-type: none;
  list-style: none;
  padding-top: 10px;
  padding-bottom: 10px;
}

ul#selector a {
  color: black;
  text-decoration: none;
}

ul#selector li.selected:hover a {
  color: grey;
}

ul#selector li.selected:hover + ul.dropdown {
  display: block;
}

ul#selector ul.dropdown:hover {
  display: block;
}

ul.dropdown {
  display: none;
}

ul.dropdown li.language {
  padding-top: 10px;
  padding-bottom: 10px;
}

ul.dropdown li.language:hover {
  background-color: chartreuse;
}
```

#### RYO selector + Client-Side Translation

If a project is published using Client-side translation, either an existing language selector needs to be used, or a new one developed to trigger translations after selection.

CST translation is activated when the target locale code is stored in the browser with the help of the `__ptLanguage` query parameter.

In order to trigger language selection/translation in-browser, add this query parameter with the appropriate published locale codes as values. Note that in order for the method to work, URL navigation has to happen once, which means a full reload is required in order to change languages.

Let's modify the exampe above to suit the needs of CST:


``` html
<ul id="languageSelector">
    <li class="language selected">English</li>
    <ul>
        <li><a href="/?__ptLanguage=en-GB">English</a></li>
        <li><a href="/?__ptLanguage=de-DE">Deutsch</a></li>
        <li><a href="/?__ptLanguage=fr-FR">Francais</a></li>
    </ul>
</ul>
```

The value of `__ptLanguage` will persist across sessions, the JS file will rely on it until the user changes their mind about their preferred language.

Visiting `www.example.com/?__ptLanguage=ja-JP` will change target languages into Japanese and store the setting. Visiting `www.example.com` the next time around will result in the site being translated into Japanese automatically.

The default browser locale can be detected successfully to be a published target language, CST will attempt a locale-specific translation without having had a query parameter provided to it.

Although that is about it, it is useful to keep in mind a few things when setting up a language selector to work with CST.

Somewhat different from the proxy method, CST requires that we provide all locale codes explicitly, especially the **original** language. Since CST *stores* the user's selection in the browser's local storage, the query parameter is necessary in order to allow the user return to the original language version.

CST publishing does not require any proxy traffic, but the Workbench In-Context editing screen remains available. This can sometimes result in the Client-Side Translation getting mixed up with the proxy-based translations, so if you are using the proxy modes for your translation work while publishing with Client-Side translation, it is generally a good idea to ignore the language selector in Preview.
