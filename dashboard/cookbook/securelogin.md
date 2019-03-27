# Secure Login - Passing Cookies to Scans

To scan content behind secure login, please follow this procedure:

1. Open your project and navigate to the **Content** menu.<br>
2. Open the **Pages** list.

3. Visit the page with the login, if it is listed, and click **Preview** (you'll need at least one target language on the project for **Preview** to be selectable!).

**OR**

- Go to the **Preview** of the front page (the "/", the first one on
  the Pages list). It will give you the front page through the
  proxy.<br>

- Go to the address bar and type in the URL of the login-protected
  page.<br>

![Login page through the proxy](/img/preview_login.png)

4. Enter your login details.<br>

5. Open your browser's DevTools from the Menu (F12 on Windows).<br>

6. Go to **Network** and reload the page.<br>

![Getting the cookie](/img/network_dev.jpg) 

7. Scroll up to the first item and click on it.<br>

8. Under headers scroll to the cookie header (among request headers),
   and copy the entire header.<br>

![Cookie header](/img/cookie_header.jpg) 

9. Pass it to the Proxy: go back to your project and start a new crawl in the Crawl Wizard. Proceed as usual to step #4 (Fine-tune), then paste the contents of the cookie you just copied to the **Session Cookie** tab.<br>

![Passing the cookie to the proxy](/img/pass_cookie.png)

10. configure the rest of the crawl and launch it as usual.
