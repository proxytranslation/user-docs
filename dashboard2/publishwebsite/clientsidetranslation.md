# Basic publishing: Client-side translation

**Basic publishing is currently the recommended publishing method.**

## What is CST?

To summarize briefly, Client-side translation is a **publishing method** that lets you use your translations on the original domain. 

As opposed to the proxy method, which involves standing between the user request and the original site, translating responses on-the-fly, Client-side translation does not require the proxy pipeline to serve content.

That is, instead of being processed in the Cloud, translation of the page will happen in the user's browser, using a JavaScript based dictionary file that can be exported from your project and embedded right in the original site's HTML source.

### Pros & Cons

Basic publishing is suited for most websites be it small or large. It especially excels when it comes to websites and web applications mainly driven by JavaScript. As the translation engine runs in the browser, it can work on the DOM of the website as opposed to the proxy that can only work on the source code of the site. This means that Client-side translation works better out of the box. This is particularly useful in case of smaller websites where the engineering effort necessary can be almost zero, ensuring a fast turnaround.

The main drawback of Client-side translation is that the source content must be loaded before the translations can be replaced. In a nutshell, this means that the original text will be visible for a bit before the translations are put in place.

## Publishing process

Client-side publishing consists of two steps:

### Dashboard - Publish Your Translations

There are three things you must do on the Dashboard. First, head to the _Export_ section. Under _File format_, select _Client-side translation (JS, export only)_. The rest of the options change to the correct values by default. You'll be notified via email when the process is finished. Once it arrives, go to _Previous exports_. Find the latest JavaScript export and in the action menu, select _Publish_. Finally, go to _Language selector_, select the target language(s) and click save.

### Add stub.js reference to original site

Like embedding a video, including your published translations involves adding a single `<script>` tag to the original HTML source. The script tag looks like the following:

```
<script type="application/javascript" src="http://${PROXY_APP_DOMAIN}/client/${PROJECT_CODE}/0/stub.js"></script>

```

We have a dedicated integrators' guide that you can find [here](../../tech-manual/crest).

Once the script is placed on the original site, a dictionary file of published translations will be downloaded by the site automatically and a language selector will be displayed. You can just select a new target language.

### Published and possible

It's important to mention how the target languages in the selector are calculated. It uses what we call the _Published and Possible policy_. In order for a given target language to show up, it should be selected under _Language selector_ on the Dashboard. This is what we refer to as _Published_. Additionally, you'll need a JavaScript export created and published, the _Possible_ part of the mantra.

If at any point, a target language doesn't show up, it's likely due to one of these conditions missing. In this case, remember the _Published and Possible policy_ or just reach out to our support team.
