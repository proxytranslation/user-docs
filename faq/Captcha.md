# Captcha doesn't work on the translated site

This issue is most likely results from page caching.
Certain captcha solutions, like WP plugins are hardcoding the image URL into the HTML, instead of sending it asynchronously. During the crawl that builds up the Source cache for the project one hash is saved, so it becomes static, while it should be changing on each occasion. As a result, the server rejects the request because of the outdated verification image.

**Troubleshooting:**
- disable caching altogether to make captcha work
- use caching without captcha
- use another CAPTCHA system that uses async requests to retrieve the verification image, like Google's ReCaptcha solution

Another possible cause can be the CORS-header. If the proxied page is not listed as an allowed origin, the browser blocks the page when it tries to load the image.