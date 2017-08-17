# WPEngine issues

## Redirections during crawling

Due to WPEngine's *caching system* and *Redirect bots* settings you might experience any of the following issues on your **WPEngine hosted sites**:

1. Scan extracts outdated content from WPEngine cache<br>

2. Scan returns **301: Moved permanently** error message for existing pages<br>

3. Translated page is redirected from HTTPS to HTTP - which results in an error due to mixed content

WPEngine caching uses different so-called _buckets_ based on request type, and they have one for bots. If the request comes from `Google` or other listed user-agents, and/or the URL has `?ver=` followed by a number, the\ redirect bots settings take effect.
 
 The above issues can be resolved on the WPEngine site by turning off the *redirect bots*.

## Intermittent `HTTP403` on proxied pages

WPEngine automatically blocks traffic from "problem" IP addresses, typically those that generate large amounts of traffic in a short time. Due to the nature of the proxy, requests from several users may appear to have come through one IP, leading to WPEngine blocking that node due to their perception of "increased traffic".

If that happens, and you note random pages of the proxied site not loading intermittently, call or chat WPEngine Customer Service with the following:

> In relation to issue #874002, please enable proxy access on our installation.

According to an agreement with WPEngine, they will enable an alternate method of IP resolution that should no longer prevent access to the translated pages.