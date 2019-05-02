Publish website
===============

In this menu, you are provided with the means of publishing your website on a pretty domain after translation tasks have finished.

The publish wizard has two options to make the site available to the web at large: serving domain mode and subdirectory publishing mode.


## Domain settings

This screen opens by default after clicking on a _Target locale_ in your list. The following settings and fields are available:

### Access control

You can add basic HTTP authentication to the proxied site in order to restrict access to it. Select the proxy modes that you'd like to limit access to, add a user by entering a username and password. You can add multiple users to the list.

### Publish website wizard

Under this menu, you will be able to publish your website either in Serving domain mode or Subdirectory publishing mode.

#### STEP 1 - Serving domain

As a first step, you need to provide the domain name on which the translated website is to be published.
The proxy will only publish a project on one domain name at a time, the question is which one should be the primary - naked domain (example.com) or subdomain (www.example.com)? Once that question is decided, you should then set up server-side redirection to the "main" domain (best practice prefers the `HTTP301 MOVED PERMANENTLY` status code with the `Location` header).

#### STEP 2 - Publishing mode

##### Serving domain mode (fr.example.com)

In the serving domain mode, the translation proxy will publish the translated site either on a subdomain of the original (the default behavior, such as fr.example.com), or on a completely separate naked domain (such as example.com). In order to use this mode, you (or the client) will have to modify the DNS settings corresponding to the original domain - the three to five records (three for subdomains, five for new naked domains) that need to be inserted in your DNS settings are found under the _Verification_ menu. These records will change as you enter or change the desired serving domain in the first step called _Serving domain_.

##### Subdirectory publishing (example.com/fr)

The alternative to subdomain-based publishing is to retain your own domain and publish the site as a subdirectory. I.e. the translated pages will appear under separate paths under the same domain as the one the project was created for (the original domain).

Due to the way the proxy works, this requires a reverse proxy configuration to be placed in front of the web server. A variety of load balancer/reverse proxy solutions are available on the market, with `nginx`, `CloudFlare` and `AWS CloudFront` being three of the most well-known solutions available. See the vendor documentation for the details of setting up a reverse proxy (do note that nowadays, reverse proxies are monumentally powerful network solutions, and discussion of all their features is beyond the scope of this introductory description).

#### STEP 3 [Selected publishing mode: Serving domain] - Verification

There are three CNAME settings that are required on your domain to enable publishing of your website. Each of the lines in the table that is displayed has a specific function:

**CNAME 1** Allows mapping of the subdomain in Google AppEngine, enabling us to alter the datastream and translate the site. This row is computed from the serving domain entered in the first step called _Serving domain_, and needs to be added once per serving domain.

**CNAME 2** The second line determines where the currently selected target language will be published. This defaults to the language code, but you are not obligated to keep it that way. This has to be entered separately for every target language you publish.

**CNAME 3*** The third line verifies ownership of the original domain. This is computed from the user’s ID who is currently looking at the publishing page (i.e. different users will see different values, so one person should communicate this to the client and hit the **Verify** button), and needs to be added only once per serving domain as well. You can set the subdomain and domain where the translated site will appear.

After all the settings have been entered into the DNS records, there is short time while the changes propagate and are replicated across the world. This can vary wildly with the DNS and hosting providers, taking anywhere between one and twenty-four hours. It is recommended to wait out the twenty-four hours, as you will not be able to click on the Next button until all checks are passed.

##### HTTPS & SSL certificates

Additionally, if the original site was HTTPS, or the translated sites will be served over a secure channel, an appropriate certificate and its associated key will also be needed. Ideally a wildcard certificate (one certificate for all subdomain), but Extended Validation certificates can also be used, although they require more setup work.

Our support team can also provide you with the *Certificate Signing Requests* necessary for the generation of these certificates - this will also have the added benefit of not having to send the private keys over the wider web for recording in AppEngine.

Additionally, we have a *Managed Certificate* program, where the proxy handles SSL certification automatically for published websites. The *Managed Certificate* program has a cost of 50EUR (60USD)/proxied domain/**year** or 100EUR (120USD)/proxied domain/**three** years.

See the pertaining section of the documentation [here](../../cookbook/ssl_certificates.html).

#### STEP 3 [Selected publishing mode: Subdirectory publishing] - CDN / Reverse proxy

We tried to provide you the absolute minimum example configurations required to achieve a workable reverse proxy using the three most popular webserver systems (Nginx, Apache httpd, and Microsoft Internet Information Systems), and also an example configuration for AWS Cloudfront CDN.

If you select an option, for example _Multiple locales as a subdirectory at depth 1_, it will only show you a different configuration as an example, but as we wrote previously, you need to set up your own reverse proxy or CDN, configured appropriately. You can also setup path prefix rules under the menu _Path Specific Settings_, and we will discuss about these configuration options later.

The goal of any reverse proxy configuration interoperating with a translation proxy domain requires that its configuration reflect the intent of the configuration examples.

Let's clarify these snippets with a more general, high-level explanation of a reverse proxy in operation.

##### Example:

Suppose that we know the following about a translation project about to be published using a reverse proxy.

1. The origin server domain is `www.example.com`.
2. Source language is English.
3. Translation exists for German
4. German serving domain: `de-de-gereblye.app.proxytranslation.com`

![Reverse proxy setup](/img/dot-graphs/reverse-proxy.png)

The task of the reverse proxy, standing right at the beginning of the pipeline that will serve a client request, is to decide which target language is requested by the user and to ensure that the request is relayed to the appropriate domain that can respond with content in the appropriate language.

In our example scenario, the reverse proxy has to make one decision: is the user requesting a resource in English or in German?

###### Translation proxy

From our perspective, The most interesting case is when a user from Germany requests `www.example.com/de/about`, the reverse proxy decides that the target language should be served via Translation proxy. It relays the request to the Google Cloud, where it is resolved to what we call the **temporary serving domain**, defined as `de-de-gereblye.app.proxytranslation.com`. In the serving subdomain mode, this domain is hidden from the user by the DNS settings added. In subdirectory publishing, the reverse proxy hides the temporary domain.

You can see that `de-de-gereblye.app.proxytranslation.com` will -- same as with subdomain publishing -- relay the request and all necessary request headers to the origin server, which will respond accordingly with source language content that the Proxy then processes on the way back and sends long to the client in a translated form.

Setting aside the exact details of that cloud translation pipeline, that's about it.

###### Source language request

Requesting the original content is a relatively straightforward process that we should nevertheless describe in brief for the sake of completeness.

If a user in England requests `www.example.com/en/about`. The reverse proxy strips the `/en` prefix, decides on the language to be served and relays the request to the origin server.

In this case, there is no more proxy mediation (that is, no Translation Proxy) between the origin server and the requesting client, so the server response is returned and the user can peruse the webpage in the original language.

Note that on the origin server, the `/en` prefix does not exist as part of the directory structure - it is a virtual prefix used by the reverse proxy to dispatch to different domains based on the target language.

If the origin server is capable of providing content in more than one target language, the reverse proxy should presumably do the same thing for each of those target languages. If a request for `www.example.com/de/about` can be fulfilled by the origin server alone, the reverse proxy will relay that request straight to the origin server (where it is assumed that the server backend will make the decision based on the HTTP request headers received).

#### STEP 4 - Summary

After configuring your publishing mode, in this last step, you will see a short summary. By clicking on the **PUBLISH** button, you need to accept all of the options in the _Disclaimer_ popup in order to be able to publish your translated website.

If the publishing is successful, then the serving domain name will appear in the Live domain column.

#### Unpublish

There are basically two options available for you:

- **Unpublish:** In this case, the related entities from our database will be removed, and it would make an error page appear when the translations are requested, which means that the publishing is disabled by our side. When you select this option, the serving domain name will be visible under the column called _Verified domain._
Alternatively, if you or your client removes the DNS records relating to the projects (especially the ghs.domainverify.net or ghs.googlehosted.com records), the requests will no longer reach the proxy, and translations will cease to be served.

- **Delete:** Removing the target locale will disable the translated website and make all the translated segments disappear. However, translations are retained in case of deleted languages as well, which means that the language can be re-added and the translations will be immediately available.


### Path specific settings

#### Roots (path prefix manipulation)

Please be aware that the path mapping tester would be available only on published locales.
We gathered below a few examples for you, in order to show you the behavior of these configurations.

_Publish translated content on www.example.com at directory depth_ `1`

If your publishing mode is subdirectory publishing, then this value will change automatically from 0 to 1.

_Translated path prefix (removed from original path, added to translated)_ `/en/`

Removed from original path means that the original / remote server will never receive this path prefix, it will be visible only in the client translated URL, as you can see below:

![Translated path prefix test](/img/dashboard2/translated_path_prefix.png)

However, be aware that the directory depth number will increase according to the number of path prefix you describe in this field:

![Translated path prefix second test](/img/dashboard2/translated_path_prefix2.png)

_Original path prefix (added to original path, removed from translated)_ `/en/`

Using together Translated and Original path prefix options, they can be used to swap the root element of the link:

![Translated path prefix second test](/img/dashboard2/original_path_prefix.png)

#### Path segment translation

With this option, you will be able to add paths segments (words between two forward slashes) here to translate them. You are limited to 50 entries at any time, but these will be translated _wherever_ they occur, for example:

www.example.com/example --> www.example.com/translation

www.example.com/notexample/nottranlated/example/text --> www.example.com/notexample/nottranlated/translation/text
