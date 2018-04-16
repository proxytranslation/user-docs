## Page requests, CDNs and Caching

The number of page requests sent when a page loads predicts monthly costs on a project. The goal of this page is to provide an in-depth description (and an upfront summary) of the matter and offer suggestions for cost reduction.

### Summary

Page requests (in the strict technical sense of an **HTTP request**) are a primary concern over the proxy as they form the basis of monthly costs. Since each HTTP request that hits the proxy is billed, it is useful to consider various ways of reducing the number of hits.

The three methods discussed here, **URL remap prevention**, **use of CDNs** and **public caching**  have the potential to dramatically reduce monthly costs (and can be combined according to need).

### Page Views vs. HTTP requests

The difference between a *page view* as generally seen and a *page request* as understood as part of pricing is crucial to keep in mind.

#### Views

Website owners/maintainers usually focus on tracking the number of *page views* (via Google Analytics, for example). This is a useful metric to gain insight about the visitors to a site and make various predictions/business decisions based on user traffic.

Such analytics count *end user visits*, where we generally expect one additional page view to show up in our Google Analytics View each time a user loads a page on the site.

Requests from bots of search engines and request where Javascript is not run (e.g. a JS-disabled browser, `HTTtrack` or command-line tools such as `cURL` and `wget`) do not result in a "visit".

The proxy pricing system **does not** refer to this understanding of a page request.

#### HTTP Requests

Refreshing the page with a devtool's Network tab openend, or using the Content Breakdown section of [www.webpagetest.org](https://www.webpagetest.org) for a page shows you that a modern webpage heavily relies on multiple resources (HTML, CSS, JS files, images, fonts etc.) over several domains to construct the unified whole shown to the user. By *page requests*, then, we mean the number of distinct **HTTP requests** for such resources.

It is this sense that the pricing system uses the term. The proxy is a technical solution to process and translate HTTP requests between the visitor and the original site, and any HTTP request that has to be relayed between the user and the server is counted as 1 page request.

This is regardless of the type of content: whether HTML, an [XHR/AJAX request](https://en.wikipedia.org/wiki/Ajax_%28programming%29) or a static resource, it will be counted as a page request if the proxy has to process it.

It is easy to see now why understanding the number of requests going into a page load is important -- they act as a multiplier on the number of **page visits** and become an important predictor of monthly project costs.

The ideal case, of course, is 1 page request per 1 user visit (meaning that only the HTML document has to be translated and served). Although this ideal case might not be attainable in all cases, it very often is.

See the next section for a suggested manual approach of evaluating a page load.

In this section, we'll go over the various ways you can *reduce the number of requests* and consequently, project costs.

### Possible approaches

Optimization means preventing HTTP requests from reaching the proxy. In practice, there are three general approaches:

1. prevent URL remapping for non-localized resources

2. ensure that "auxiliary" content such as CSS and JS files and images is served from a CDN

3. caching intra-domain resources

#### Remapping

The proxy billing system is only concerned with those requests that are forced to go through it, so the simplest way of preventing an HTTP request from going through the proxy is to prevent it from being re-mapped from the original site to the translated domain entirely.

If *www.example.com* is being translated into German and published on *de.example.com*, any URLs in the source that point to the original server (that is, are intra-domain) will be **remapped** to refer to the translated domain over the proxy.

But useful exceptions should be made. For example, images that are not localized do not get mapped by default, which means that the image will be downloaded from the original *www.example.com* site instead of the TL domain, naturally preventing an HTTP request from going through the proxy. Altough a tweak exists in Advanced settings to force images through the proxy, you should consider the cost implications of this tweak before turning it on (and look into the subsection on caching to offset increased costs).

The `__ptNoRemap` HTML class is handled specially by the proxy. If this class name is detected, the `href` or `src` attribute of the given element will not be mapped to the proxy (avoiding the request cost).

```
/* ... */
```

If sed*** in a systematic manner, this change would have to be applied on the origin server, which is a potential downside if you don't have source/admin access. It bears mentioning that the class is reported to have solved one-off problems by being search & replaced into targeted spots in the page source)***.

#### CDNs

The simplest way to prevent an HTTP request to the project domain is to offload it from the original server, too. Content Delivery Networks are servers that are capable of providing source (non-localized) content in a reliable way across the globe.

#### Public Caching

(_Note: not to be confused with Source and Target caches!_)

Many static resources need no processing whatsoever by the translation proxy, and become cost overhead if funneled through it. But it is also often the case that it impossible to avoid having these request go through. What to do in these cases? Enter public caching.

HTTP supports what is called a `Cache-Control` header that can be added by the server to a response. The content of this header instructs public caching nodes on the network on how to store a static copy of the resource for a time.

A cache (usually affecting a given geographical area or specific network pathway) will serve the resource to visitors until the "Time-To-Live" of the cached resource expires. This TTL is defined by the value of `max-age` in the `Cache-Control` header, and its current value is tracked in the `Age` header.

Until such time as this time is up, requests coming in from a place served by the cache will not, in fact, reach the proxy. After `max-age` expires, the cache will re-request the original for another `max-age` term - during that time, however, a cache can serve a multitude of requests without having to burden the original server (& proxy for it).

Declaring a `max-age` of 86,400 on the image `/about-us/logo.jpg`, for example, broadcasts on the network that for the duration of one day, any public caching node should feel free to cache the resource -- it's up to them, but if possible, they should not re-request it until then.

This way, the caching/serving/trafficking burden evens out on the network, and many of the repeating requests can be avoided (i.e. an intently browsing user might load the same resource over and over again, but most of those requests will be served from a cache).

Keep the following important points in mind:

1. Caching naturally introduces **update delays**. A user getting cached content will have to wait for it expire before seeing a new version.

2. Frequently updated HTML pages (such as those with a newsstream) should not be targeted for caching, and URLs serving **dynamic resources should never be cached!**

3. Public caching works best with **static resources** (JS, CSS and images) and **versioned URLs**.

4. It is **impossible** to reach a cached resource coming in from the server side. Neither the original site, nor the proxy can tell a node to throw a cached version away. Only expiry will do that. This is architectural, the HTTP protocol does not provide a method to send cache invalidation notifications to arbitrary nodes. The upshot is that while it might seem sensible (from a cost-reduction perspective) to add as huge `max-age` values as possible, this is highly recommended **against**. Unless the URL of the given resource is versioned to allow for updates anytime, users may end up "walled out" by a cache storing an image for weeks, for example.

A measure of carefulness is advised!

##### Cache-Header Setting

If you find that very sensible defaults are coming in from the original server, that is very good news, but it is also a fact that such is not always the case.

To adjust `Cache-Control` on the proxy-side, go to Dashboard > Path settings to override headers on a URL or prefix-basis. See the [Path settings](../../dashboard/menu/dashboard/pathsettings.html) documentation to learn more about overriding/fine-tuning Cache-Control headers.

### References

See [HTTP caching](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching) in Google's Web Fundamentals on public caching.

See [RFC 7234](https://tools.ietf.org/html/rfc7234) for the full technical detail on HTTP `Cache-Control`.
