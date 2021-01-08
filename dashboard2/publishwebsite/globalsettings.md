# Global settings

![Global settings screen](/img/dashboard2/global_settings.png)

This menu contains publishing settings that apply to every target language at the same time.

## Access control

This option is also present on a per-language basis but here it affects all languages. This can save you some work if you'd add the same settings to all of the languages anyways. Add username/password combinations and tick the modes that you wish to protect using [Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). The settings you add here and per-language are merged and both are applied.

## Stale content for good bots

Bot traffic can significantly increase the maintenance costs of proxy sites. Some of this bot traffic is useful, e.g. the search engines. With this feature, you can serve a cached response to these bots and thus reducing the number of page requests they generate.

Note that with this feature enabled, bots won't be notified about changes to the site until the caches expire so their indices may be outdated for some time.

## Blocking bad bots

There are bots, however, that aren't useful to the site owners at all. These can be blocked completely based on their `User-Agent`. Enter a Java regular expression to specify the agents that you wish to block. These will receive a `403: Forbidden` response when trying to visit proxied pages.

**Important**: Do not enter 2 pipe symbols (`|`) one after the other. It will block every user and bring the whole translated site down. Consider the following regular expression `[Mm]alicious[Bb]ot||[Ee]vil[Ss]pider`. This matches "MaliciousBot", "" (the empty string) and "EvilSpider". As every user agent contains the empty string every user will be flagged as a bad bot and will be blocked.

## Externalized page redirection handling

Using this feature, you can avoid duplicate content (and the SEO penalty that comes with it). Externalized pages aren't translated and by default shown as the source language. You can change this behaviour to redirection (either via `301: Moved Permanently` or, `302: Moved Temporarily`) or disable serving these pages (`401: Access Denied` or `404: Not Found`)