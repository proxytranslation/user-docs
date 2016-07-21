Page Caches
...........

[[Screenshot of the Easyling Caching model]]

By default, Easyling sends all requests to the remote server and lets
through any and all new content it finds during the process (in case
of a Preview or a Scan). Normally, when the source of the proxied site
is unlikely to undergo significant changes, this shouldn't be a
problem.

However, if the page has dynamic content or is likely to be updated
frequently, then precious translated content might get replaced by
incoming new content on the proxy, leading to lowered translation
ratio and a spotty translation quality. We call the sudden appearance
of untranslated content on the proxy **bleedthrough**. Such a state of
affairs seldom satisfies the owner of the site, and of course there is
always the issue of control - you want content to ride shotgun, while
you take the wheel yourself.

It also often happens that some projects require frequent/careful
maintenance. Perhaps you'd like to separate (_decouple_) content that
you want to serve through the proxy from the content you want to see
in your Workbench. For example, you would probably prefer untranslated
text to be waiting for you on the Workbench, but not served on the
proxy until the its translation is ready.

Enter **Multi-Caching**.

Easyling supports two kinds of caches: **Source Caches** and **Target
Caches**. The term _Multi-Caching_ refers to the fact that Easyling
users can create and maintain multiple caches for both types.

**WARNING: Source Caches and Target Caches are entirely different
entities, they are NOT shared resources in any sense!**

Currently, the maximum allowed number for a given type of Cache is
**5**. That is, you can have a maximum of 5 Source Caches and 5 Target
Caches for any given project.

We discuss the two different kinds of caches in separate section.



.. toctree::
   pagecache/sourcecache
   pagecache/targetcache
