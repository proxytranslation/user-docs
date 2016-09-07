# Caching And The Proxy

## Overview
Nearly all browsers today implement local caches to accelerate page loading and prevent unnecessary requests from being sent out to the network. However, the operation of these caches is tied to the presence of certain headers on the page, such as `Pragma` and `Cache-Control` - based on their presence and the values communicated in these headers, the browser (and various systems, such as CDNs) may make a decision to intercept the request and serve up certain content without requesting it anew from the server.

Normally, the Proxy simply forwards these headers, much the same way it does with any other. The option to override their presence and values exists (see the [Path Settings](/en/latest/dashboard/menu/dashboard/pathsettings.html) option on the Dashboard), but by default, they are left unmodified, in the spirit of minimum invasion. </br>
This is not always desirable, however, as a site without such cache headers will remain uncached in the visitors' devices, and each visit to the page will result in another request that is billed.

## Inspecting Cache Headers
You can investigate how well a site may be cached using the Developer Tools in most major browsers. In Chrome, for instance, the DevTool can be summoned using by pressing the F12 key (or Alt+Cmd+I on under Mac OS), and after refreshing the page, the Network tab can be used to browse traffic associated with the tab. By selecting any entry in the list, you can view its details, in particular, the request and response headers. To tell whether or not a given resource will be requested again, you need to look at the "Response Headers" section, and look for the keys `Cache-Control` and `Pragma`. </br>
If you see `Pragma:private` and/or `Cache-control:no-cache`, it is safe to say that the given resource will not be cached and each visitor will result in another hit. Files like this will likely prove resource drains if the site receives large amounts of traffic.</br>
On the other hand, `Pragma:public` and `Cache-Control:public, max-age=\d+` (where `\d+` means at least one digit, or more) are good signs in that these files will be stored on the client's device after the first request, and will not be requested until `max-age` seconds have elapsed since the last load, and will save resources in the long run. Of course, this also means that visitors may be seeing an "outdated" version of the resource for a limited time before their caches expire and are reloaded.

There is a bit of a gray area when seeing `Cache-Control:must-revalidate`: this directive allows the cache to make the final decision based on its own algorithm, and the response **may** be stored, but not necessarily. When seeing this it is good to prepare for potential increased traffic, as the browser cache may or may not retain these responses.

## What to take away
If you're experiencing consistently large numbers of page views on a given project, it is often a good idea to suspect caches (as opposed to search bots, which cause transient spikes). In such cases, you should inspect a few pages using the DevTool, and determine whether or not the site is set up to take advantage of browser caches.

If it turns out be the case that the site is not set up to use caches, the best course of action is to notify the owners - perhaps they have a good reason for it. In any case, these headers should be added to the source, so that they provide consistent values across all languages. Alternatively, you can use the aforementioned Path Settings dialog to force the Proxy to override the cache headers and make the site cacheable, at the risk of diverging from the original, even if only for a short time.
