# WPEngine issues

Due to WPEngine's *caching system* and *Redirect bots* settings you might experience any of the following issues on your **WPEngine hosted sites**:<br>
1) Scan extracts outdated content from WPEngine cache<br>
2) Scan returns **301: Moved permanently** error message for existing pages<br>
3) Translated page is redirected from HTTPS to HTTP - which results in an error due to mixed content

WPEngine caching uses different so-called _buckets_ based on request type, and they have one for bots. If the request comes from `Google` or other listed user-agents, and/or the URL has `?ver=` followed by a number, the redirect bots settings take effect.<br>
The above issues can be resolved on the WPEngine site by turning off the *redirect bots*. 
