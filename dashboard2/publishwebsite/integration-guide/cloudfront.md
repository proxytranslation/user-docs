# Subdirectory publishing under AWS CloudFront

When you set up subdirectory publishing via CloudFront, you don't just set up a reverse proxy. CloudFront isn't just a simple web server solution after all. Instead of that, following this guide you'll set up a complete CDN in front of both your original and translated website. As such, you can also benefit from the other advantages that a CDN provides such as load balancing and global caching.

To get started, it's recommended to copy the settings provided in the Publishing wizard. These are partially project-specific. We'll use a project with the following details:

- Source domain: example.com
- Project code: `redacted`
- Translations exist for German
- We wish to publish them to example.com/de/
- Your white label is app.translationproxy.com

With these options set in the Publish wizard, we get the following configuration:

```
Alternate Domain Names (CNAMEs): example.com
Origin Domain Name: de-de-redacted.app.translationproxy.com
Behavior | path pattern: /de/*

Origin custom headers:
X-TranslationProxy-Cache-Info disable
X-TranslationProxy-EnableDeepRoot true
X-TranslationProxy-AllowRobots true
X-TranslationProxy-ServingDomain example.com


Cache Based on Selected Request Headers: Whitelist
- CloudFront-Forwarded-Proto
- CloudFront-Viewer-Country
- Origin
- Referer

Object Caching: Use Origin Cache Headers 
Query String Forwarding and Caching: Forward all, cache based on all
```

With these details on hand, you can follow the following steps:

1. Log in to your CloudFront dashboard and head to *Distributions*. Or just use [this link](https://console.aws.amazon.com/cloudfront/v3/home?#/distributions).
2. Click *Create distribution*. You'll be navigated to the distribution creation form that you must fill in.
    - Origin domain: Use the one provided by the Publish wizard. In our case it's `de-de-redacted.app.translationproxy.com`. 
    - Protocol: HTTPS only is recommended, but Match viewer can work too.
    - Origin path: leave empty.
    - Name: enter a memorable name. We recommend `translationproxy-language`.
    - Add custom header: add the headers provided by the Publish wizard under *Origin custom headers*
3. Scroll further down to *Cache key and origin requests* and set it to *Legacy cache settings* and use the following settings:
    - Under *Headers* select *Include the following headers*
    - Select the headers provided by the Publish wizard under *Cache Based on Selected Request Headers*
    - Ensure *Object caching* is set to *Use origin cache headers*.
4. In the *Settings* section, just a bit further down, add the *Alternative domain name (CNAME)* as specified by the Publish wizard. In our case, it's `example.com`
5. Click *Create distribution*
6. Navigate back to the *Distributions* section and select the newly created Distribution from the list. You'll be navigated to the details page of the Distribution that has multiple tabs.
7. On the *General* tab, ensure that an SSL certificate is available. If not, create and upload one.
8. On *Origins*, 
    - Ensure that the `translationproxy-language` origin we created above is present
    - Click *Create origin* and enter the following:
        - Original domain: the source site, in this example it should be `example.com`.
        - Protocol: HTTPS only is recommended, but Match viewer can work too.
        - Origin path: leave empty.
        - Name: enter a memorable name. We recommend the domain of the original site `example.com`.
        - Click *Create origin* to save.
    - **NOTE:** If you later wish to add additional languages, you don't need to create a completely different distribution, just add them here and follow the note under the following step too.
9. On *Behaviors*, (which should really be spelled Behavio**u**rs, my spellchecker is complaining)
    - Click *Create behavior* and use the following details
        - Path pattern: as specified by the Publish wizard - `/de/*`
        - Origin and origin groups: select the `translationproxy-language` origin added previously
        - Click *Create behavior* to save
    - **NOTE:** To add further languages, do this again with the appropriate Path patterns and Origins
    - At this point, you should have behaviors set for every target language, but we'll also need one for the case when the visitor wants to see the source language site. Click *Create behavior* again and use the following details:
        - Path pattern: this depends on the structure of the site
            - If the original content is under the root, meaning that it is `example.com/path/to/page`, then enter the path you wish to move it to, like `/en/*`. 
            - If the original content is already under a language folder, enter `*`.
        - Origin and origin groups: select the `example.com` origin added previously
        - Click *Create behavior* to save
10. With that, the CloudFront configuration is complete.

These instructions are up-to-date as of 24/02/2022.