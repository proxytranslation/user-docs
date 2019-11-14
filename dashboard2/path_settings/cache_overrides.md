# Cache and Cookie Overrides

## Overview

This override allows you to declare the `Cache-Control` and `max-age` headers for a prefix or URL and optionally clear the cookies. 

![An example of a typical cache override (/wp-content)](../../../img/dashboard/path_settings_cache_override.png)

The path seen in the screenshot above is a typical use case: it ensures that resources on the `/wp-content` prefix, associated with WordPress sites, can be cached for 24 hours.

Setting ` cache-control: public, max-age=86400` on a URL/prefix in this way broadcasts to the network that the resource(s) there can be publicly cached. Depending on the location of the caching node and the pathway of the request, the content will be served from caches instead of going through the proxy pipeline. 

This is beneficial for both speed and cost reasons. What is otherwise tolerable server load on the original site might be unnecessary page view cost overhead over the proxy (with speed overhead not being much of a concern). We provide this capability as a useful cost optimization strategy. 

**Important!** Do NOT add overly general paths or too large `max-age` values without considering the effects! Please read through [our description of the issue](../../cookbook/pageviewsandcaching.html) before using the feature.

**Only one** cache & cookie override may be present on each path or prefix.

## Parameters

+ _Cache Override_: One of _Private_, _Public_, or _Ignore_
    + _Private_: sets `cache-control: private`, preventing caching at all
    + _Public_: sets `cache-control: public`, allowing caching
    + _Ignore_: leaves the header as-is, without modifying the directive
+ _Max age_: the maximum age of a cached resource, in seconds.
+ _Cookie override_: preserve or clear the `set-cookie` headers - may improve caching, but break functionality!
