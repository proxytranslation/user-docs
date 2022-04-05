# Subdirectory publishing via CloudFlare Workers

Cloudflare Workers is a serverless application platform. As it can work with HTTP requests, it can be used instead of a complex reverse proxy setup for subdirectory publishing of the translated website.

To get started, it's recommended to copy the settings provided in the Publishing wizard. These are partially project-specific. We'll use a project with the following details:

- Source domain: example.com
- Project code: `redacted`
- Translations exist for German
- We wish to publish them to example.com/de/
- Your white label is app.proxytranslation.com

With these options set in the Publish wizard, we get the following configuration:

```javascript
addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request))
})
/**
 * Fetch and redirect or continue to Proxy
 * @param {Request} request
 */
async function handleRequest(request) {
    const redirectPaths = ['de']
    const proxyUrls = {
        'de': 'de-de-redacted.app.proxytranslation.com'
    };

    const url = new URL(request.url);
    const { pathname } = url;
    const [, topLevelDirectory] = pathname.split('/');
    if (topLevelDirectory && redirectPaths.includes(topLevelDirectory)) {
        // The request's URL must be overwritten to send it to the Proxy
        request = new Request(
            `${url.protocol}//${proxyUrls[topLevelDirectory]}${pathname}${url.search}`
        )
        request.headers.set('X-TranslationProxy-AllowRobots', 'true')
        request.headers.set('X-TranslationProxy-Cache-Info', 'disable')
        request.headers.set('X-TranslationProxy-EnableDeepRoot', 'true')
        request.headers.set('X-TranslationProxy-ServingDomain', 'example.com')
        request.headers.set('Host', proxyUrls[topLevelDirectory])
        return fetch(request);
    } else {
        // Regular request. Forward to origin server.
        return fetch(request);
    }

}
```

With these details on hand, you can follow the following steps:

1. Log in to your CloudFlare dashboard and head to the *Workers* section.
    - If you've not used CloudFlare Workers before, you must choose a subdomain and a plan. For the purposes of this guide, we'll assume that the domain chosen is `translationproxy-worker`. 
2. Click *Create a Service*
3. Fill in the *Service name* field with an appropriate name. `translationproxy-domainname` would be suitable in general so in our case, we'll just use that: `translationproxy-example`.
4. You don't need to change the starter, we'll overwrite it anyway, so you can simply click *Create service*. You'll be navigated to the settings section of the newly created Worker.
5. Click on *Quick edit*. You'll be navigated to the code editor. 
6. Delete all the example code that CloudFlare provides and add the snippet we provide.
    - **NOTE:** If you wish to add more target languages, change the `redirectPaths` and `proxyUrls` variables accordingly. 
7. Click *Save and Deploy*
8. Test it by opening the URL of the Worker on the translated path. In our case, that would be https://translationproxy-worker.translationproxy-worker.workers.dev/de/. It should load the translated site.
9. Head back to the settings section of the Worker and click on *Triggers*
10. Click on *Add route*
11. Enter your domain. In our example it is `*.example.com/*`.
    - **NOTE:** Only routes of hostnames configured on Cloudflare can be specified, so if your domain isn't yet configured, you must do so via the *Add site* button in the top bar. Adding further DNS records is likely required to do so.
12. Your environment will now respond to requests to `*.example.com/*`. You can verify that the translated site loads at, in our case, https://example.com/de/
13. With that, the CloudFlare Worker configuration is complete.

Make sure that [Rocket Loader](https://support.cloudflare.com/hc/en-us/articles/200168056-What-does-Rocket-Loader-do-) is disabled when using CloudFlare!

These instructions are up-to-date as of 04/03/2022.