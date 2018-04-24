# HubSpot Forms

The proxy supports translation of HubSpot (or similar) forms via a combination of [project linking](../../menu/dashboard/linkprojects.html) and [JS translation](../../cookbook/jstranslation.html).

**Method #1** marshals a combination of advanced proxy features. No change on the original server is necessary (which a frequent constraint). It's benefit is that it is entirely **hands-off** from the site maintainer's perspective.

**Method #2** relies on HubSpot for localized forms and uses a proxy-compatible injected JS approach.

## Method #1: Proxy

The proxy approach traces he structure of the main and form domains via linked projects. Affected JS resources/endpoints are overridden and the responses marked as translatable.

### Project Creation & Setup

HubSpot uses several external domains to drive a form. You will see   [https://js.hsforms.net/forms/v2.js](https://js.hsforms.net/forms/v2.js) referenced in the page source. This file itself references [https://forms.hubspot.com](https://forms.hubspot.com), which is where the translatable form contents are coming from.

Domains used by a HubSpot form are related to the main project and each other in the following manner:

![HubSpot Projects](/img/dot-graphs/hs-form-w-js.png)

Assuming that `example.com` is already set up, at most two additional projects are required:

1. `js.hsforms.com`: creation of this project is *optional*, though not complicated. At the time of writing, visiting the landing page results in a `403 Forbidden` page (but this is not a problem).

2. `forms.hubspot.com`: this URL redirects you to `https://developers.hubspot.com/`. To create a project for it, **disable Redirect checking** in the Add Project dialog. Click on **Advanced settings** to reveal the option and uncheck the checkbox:

![Disabling Redirect checks](/img/dashboard/create_project_disable_redirect_check.png)

Don't forget to add every target language of the main project to each project you create.

### Link Projects

Open each project in a separate tab and link each project according to the [section on Project Linking]("../../menu/dashboard/linkprojects.hhtml"). The result should be a chain of projects leading from `example.com` to `forms.hubspot.com` with `js.hsforms.net` as an intermediary.

### Alternative: Search & Replace

The `js.hsforms.net` project is not, strictly speaking, necessary. Its true purpose is merely to expose a slightly modified version of the `/forms/v2.js` script. If its URL is referred to in a way that makes it possible, you can *sidestep* the domain using a combination of [Search & Replace](../../menu/dashboard/pathsettings.html#search-replace-override) and a [page content override](../../menu/pagemodifiers/contentoverride.html). The setup steps for this are as follows (done on the main project):

1. **create a path override** for the exact URL where the form is present (the diagram above shows `/contact` as an illustration).

2. **add a regex Search & Replace rule**: replace `https?://js.hsforms.net` with the empty string to turn the reference to`/forms/v2.js` into a relative URL (and effectively point it toward a page content override on the project domain that will be created in a moment).

### Overriding `v2.js`

This resource contains a crucial variable called `urlRoot`, which has to be **remappable** over the proxy. However, it is set via a *computed expression*, which is unsupported by the proxy for reasons discussed in [the section on JS translation](../../cookbook/jstranslation.html), so an override and a small change becomes unavoidable (regardless of the presence/absence of the intermediate project). Follow the steps below to create the override:

1. visit `https://js.hsforms.net/forms/v2.js` and **copy & paste** the contents of the JS file.

2. use the DevTool or an [online pretty printer](http://jsbeautifier.org/) before pasting the code. Though optional, it is highly recommended that you do this (such minified code is cumbersome to work with as it is).

3. create a PCO for the `/forms/v2.js` pathname in Page modifiers > Content Override. The response code default is 200, and the `Content-Type` header is `application/javascript; charset=utf-8`. We'll return to `Cache-Control` and `Pragma` later, after setup is complete.

4. Add the following line to the top of the PCO:
    ``` javascript
var HUBSPOT_URL_ROOT = "https://forms.hubspot.com";
```

5. Search for `this.urlRoot`. It is set in a line similar to the one below:

    ``` javascript
 o ? this.urlRoot = "https://f.hsforms" + e + ".net/fallback" : null != a ? this.urlRoot = "" + a : this.urlRoot = "https://forms.hubspot" + e + ".com";
```

6. Add the following line after it to make it use the "accessible" value:
    ``` javascript
this.urlRoot = HUBSPOT_URL_ROOT
```

7. Use the *Mark multiple resources as Translatable* text field in Advanced settings. Simply add the pathname prefix of the PCO to the list:
   ```
/forms/v2.js
```

8. URL Translation & HTTP/HTTPS
   Finally, add the following JS path to the list of translatable paths in Advanced settings:
   ```
"HUBSPOT_URL_ROOT" url
```

Open the PCO link over any one of the proxy preview domains to test it. If all projects are correctly linked and you followed the setup steps correctly, the `HUBSPOT_URL_ROOT` variable will hold an appropriate proxy-mapped domain (and consequently `this.urlRoot` will be set to the same value). 

### Form Contents

Set up the HubSpot content endpoint as translatable on the project for `forms.hubspot.com` [according to the JS translation section](../../cookbook/jstranslation.html). In summary:

1. locate the form request using the DevTool and add it to the "Mark multiple resources as translatable" list of prefixes. For any given HubSpot form, translatable content will usually be associated with a  prefix similar to the one below (it will also have a `callback` query parameter).
   ``` 
/embed/v3/form/{numericId}/{formId}
```

2. use the JSON path tester tool in Advanced settings to process the response. HubSpot forms come in a response format called JSONP or padded JSON (a function call such as `hs_request_0` with the form data passed to it as argument). It is not necessary to prefix JS paths with `"json"` in this case.

3. use the x-proxy to test your JS paths, and use Preview for content extraction.

### Publishing & Caching

All projects need to be published together in all target languages. Note that you don't need to publish on a subdomain of the original server: you are free to proxy the German version of `forms.hubspot.com` through `hs-de.mydomain.com`, for example.

Once setup, translation and publishing is complete, you are free to set an appropriate Cache Header on your page content overrides (either on the PCO itself or [on a prefix-basis](../../menu/dashboard/pathsettings.html)) to reduce page request costs.

## Method #2: HubSpot & Injected JS

If you don't mind having a separate form for each language, you can use HubSpot itself to localize the form property names after [cloning your form for each target language](https://community.hubspot.com/t5/Lists-Lead-Scoring-Workflows/Translation-of-contact-properties-for-different-forms/td-p/8109). JavaScript can drive the forms on the client-side for each target language, resulting in an arguably cleaner approach.

The proxy sets the `lang` attribute of the `<html>` tag to the appropriate locale code on each target language domain, which you can use for branching. The code below demonstrates one example of how such code could look in practice:

``` javascript
var lang = document.querySelector("html").getAttribute("lang");

var HSFormId = {
  "en-US": "English9-bb4c-45b4-8e32-21cdeaa3a7f0",
  "fr-FR": "Frenche9-bb4c-45b4-8e32-21cdeaa3a7f0",
  "de-DE": "Germane9-bb4c-45b4-8e32-21cdeaa3a7f0"
};

// refer to the HubSpot documentation for further customization at
// https://developers.hubspot.com/docs/methods/forms/advanced_form_options
hbspt.forms.create({
  portalId: "portalId",
  formId: HubSpotFormId[lang]
})
```
