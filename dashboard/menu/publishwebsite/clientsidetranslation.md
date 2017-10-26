# Client-Side Translation

**CST is currently in a live-tested beta phase.**

# What is CST?

To summarize briefly, Client-side Translation is a **publishing method** that lets you use your translations on the original domain. 

As opposed to the proxy method, which involves standing between the user request and the original site and translating responses on-the-fly, Client-Side translation does not require the proxy pipeline to serve content.

That is, instead of being processed in the Cloud, translation of the page will happen in the user's browser, using a JavaScript based dictionary file that can be exported from your project and embedded right in the original site's HTML source.

## Pros & Cons

Client-side translation is especially suited to lightweight, streamlined sites with comparatively few pages, or sites that are not publicly accessible, such as intranets.

It does not require the proxy pipeline to serve content, which means that there is no monthly cost involved. 

Image translation is supported.

On the other hand, given the nature of the translation process, the target language content cannot be indexed by search engines. 

Additionally, automatic change detection is not an option with a JS-based publishing method, so the only way to detect changes is by setting up a recurring crawl. 

# Publishing process

The publishing method is in open beta phase and is available for testing and live use with a bit of help from our end. If you are interested in taking it for test drive, please contact our support team and we'll help you set it up. 

Client-side publishing consists of two steps:

## Add stub.js reference to original site

Like embedding a video, including your published translations involves adding a single `<script>` tag to the original HTML source. The script tag looks like the following:

```
<script type="application/javascript" src="http://${PROXY_APP_DOMAIN}/client/${PROJECT_CODE}/0/stub.js"></script>

```

Once the script is placed on the original site, a dictionary file of published translations will be downloaded by the site automatically. Besides selecting the language, no further change on the original site is necessary.

## Dashboard - Publish Your Translations

This step currently requires a "toggle" on our end, but keep an eye on our release logs until the publishing method becomes available as an automatized step!
