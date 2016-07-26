# Target Cache

Target cache option is used to achieve great boosts in page serving speed by enabling the proxy to skip processing the page instantly if the remote server’s response matches the response that was used to generate the cache during building. By not having to insert the translations separately, page serving can be accelerated by several milliseconds, which can add up to a noticeable speedup in the case of larger pages with lots of translated

The Target cache is built or overwritten every time a page is loaded through the proxy, with a few notable exceptions. The cache is not overwritten if the content served matches the content received (i.e. no processing was done on it), nor are entities larger than the hard-coded maximum entity size (960kb) saved. Furthermore, if a site changes its contents too fast (there are too many cache misses, i.e. the cached content differs from the actual), the Proxy will stop caching the given entity to prevent overusing the database. Should this happen, caches must be cleared manually to restore normal operation and reset the cache miss limit.

## What is it for?

The purpose of the Target Cache is to reduce the number of requests to the **source site** and decrease response times on the proxy by skipping the content replacement process (which is basically the entire document pipeline) if the content on the **source site** or - if enabled - in the Source Cache remains _unchanged_.

## Enabling Target Cache

Go into the **Page Cache** menu in the Dashboard and enable Target Cache in the dialog that open. You can also add a maximum of **5** custom-named Target Caches.

## Building the Target Cache

After you enable it, the Target Cache is filled exclusively by Page visits on the pretty (published) domain. Previews/visits to the temporary domain will have absolutely no bearing on the contents of the Target Cache.

While separate from the Source Cache, the contents of the Target Cache will nevertheless be determined by your Source Cache settings. If you have no Source Cache, then the Target Cache will be filled by whatever is returned from the source site for a request (a page visit). If you have a Source Cache, then the Target Cache will contain whatever the currently enabled Source Cache is making available to the visitor on the proxy.

## The 'Keep Cache Strategy'

The Keep cache is actually a serving mode of the Target cache, used mainly to prevent the source language bleed-through effect, or Bleeding Effect in short. It operates by checking the cached content’s translation ration against the remote server’s response. If the cached content is found to have a more complete translation (i.e. its translation ratio is higher), the remote response is discarded and the cached content is served instead. This does not mean an increase in page load speed, but by preventing yet-untranslated elements from appearing in the served page, the Bleeding Effect is eliminated entirely. As new translations are entered into the database, either manually or via XLIFF imports, the difference between the cached response and the actual response decreases, and the newly-translated elements are displayed automatically. Additionally, this check is run every time the source content is found.
