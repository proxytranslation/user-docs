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

If a language selector is already present on the site, by far the easiest method to integrate the translated subdomains/subdirectories is to add them to the existing selector (although it does require the development resources of the site owner). An important feature of the proxy is the “__ptNoRemap” class, which can be used to prevent the links within the language selector from being changed over the proxy. Adding it to the link `<a>` tags or other functionally equivalent markup will allow the proxy to keep these links intact. It is especially prudent to protect the original site’s link (the proxy should not remap the link to the original site in the language selector). You may also wish to use the translate=”no” attribute in places where you want the proxy to ignore the textual content of the HTML element.
