# Target Cache

## What is it for?

The purpose of the Target Cache is to reduce the number of requests to
the **source site** and decrease response times on the proxy by
skipping the content replacement process (which is basically the
entire document pipeline) if the content on the **source site** or -
if enabled - in the Source Cache remains _unchanged_.

## Enabling Target Cache

Go into the **Page Cache** menu in the Dashboard and enable Target
Cache in the dialog that open. You can also add a maximum of **5**
custom-named Target Caches.

## Building the Target Cache

After you enable it, the Target Cache is filled exclusively by Page
visits on the pretty (published) domain. Previews/visits to the
temporary domain will have absolutely no bearing on the contents of
the Target Cache.

While separate from the Source Cache, the contents of the Target Cache
will nevertheless be determined by your Source Cache settings. If you
have no Source Cache, then the Target Cache will be filled by whatever
is returned from the source site for a request (a page visit). If you
have a Source Cache, then the Target Cache will contain whatever the
currently enabled Source Cache is making available to the visitor on
the proxy.

## The 'Keep Cache Strategy'

