# JavaScript publishing

This section contains key settings for [Basic publishing](clientsidetranslation.html) as well as the one line of JavaScript to embed the translations to the original website. There are four sub-sections.

## Embed code

This part is the most important for the publishing process. You can embed the client-side translator engine via one line of JavaScript code that you can find here. Use the *Copy to clipboard* button, then add it to the website.

![Embed code screen](/img/dashboard2/crest-settings/embed_code.png)

## Tweaks

These checkboxes are fairly similar to those that you can find on the *Advanced settings* section. They influence the behaviour of the translator script.

Note that the majority of these tweaks change the embed code, so after changing them, please make sure to update the code on the website.

![Tweaks screen](/img/dashboard2/crest-settings/tweaks.png)

There are seven options:

- *Include all the default parameters*: By default, the embed code is kept as short as possible. To achieve this, tweaks that aren't enabled aren't included in the URL. This tweak allows you to include them all.
- *Language parameter*: By default, you can change the target language by appending `?__ptLanuguage=${target_language}` to the URL of the site. With this option, you can change it from `__ptLanguage`.
- *Storage parameter*: By default, the user's language choice is stored in LocalStorage under `__ptStorage`. Change it with this option.
- `noXDefault`: By default, the translator adds an `x-default` link element to the translated website. With this option, you can prevent this.
- *Rewrite URL*: By default, the target language is hidden in the URL. Use this tweak to ensure that `?__ptLanuguage=${target_language}` is always present in the URL.
- *Script URL is base*: The injected script loads further translator scripts, one for each target language. Use this tweak to try loading them from the original site's domain. Use this feature if the JavaScript exports are uploaded to the original server.
- *Disable selector*: The translator script adds the sidebar language selector by default. Use this tweak when a custom language selector is in place.

## Selectors

In this section, you can enter CSS selectors to influence the behaviour of the translator script.

### Block selector

HTML documents, such as webpages, have block and inline elements. W3Schools has [a great page](https://www.w3schools.com/htmL/html_blocks.asp) about them. The translator engine treats them differently by default. Block elements become their own entry in the Workbench. If you need to treat an inline element as its own block element, just enter its CSS selector here.

### Re-process after changes

The translation algorithm translates every element on the page once. When the text of an element is changed, but the element itself isn't, it isn't re-translated because at that point it may contain mixed-language content.

You can enter CSS selectors to force a translation update on change here.

**WARNING**: Using this feature can result in translated content, or partially translated content, being ingested as source content.

![Selectors screen](/img/dashboard2/crest-settings/selectors.png)

## Injection

Here, you can specify JavaScript files that are injected to the website, even when the source language is selected. This way, you can make any change required both to the original and the translated websites. You can use this feature, for example, to customise the language selector or to add an overlay while the translations are being added to the website.

**TIP**: Write your JavaScript code to a Page content override making sure that the content type is set to `application/javascript`. Then, you can inject the temporary domain of this override.

![Injection screen](/img/dashboard2/crest-settings/injection.png)
