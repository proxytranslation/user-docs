# Domain settings

This screen opens by default after clicking on "Publish website". The following settings and fields are available:

**Target language** Choose which target language you would like to configure a serving domain for.

**Temporary domain** This is the preview proxy you can use to preview your translations live (this is immutable).

**Access control** you can add basic HTTP authentication to the proxied site in order to restrict access to it. Click on _Configure access control..._. Select the proxy modes that you'd like to limit access to, enter your username and password. You can add multiple users to the list.

## Serving domain mode (de.example.com)

In the serving domain mode, the translation proxy will publish the translated site either on a subdomain of the original (the default behavior, such as `de.example.com`), or on a completely separate naked domain (such as `example.com`). In order to use this mode, you (or the client) will have to modify the DNS settings corresponding to the original domain - the three to five records (three for subdomains, five for new naked domains) that need to be inserted in your DNS settings are found below the two input fields, and will change as you enter the desired serving domain.

### CNAME settings

There are three CNAME settings that are required on your domain to enable publishing of your website. Each of the lines in the table that is displayed has a specific function:

**CNAME 1** allows mapping of the subdomain in Google AppEngine, enabling us to alter the datastream and translate the site. This row is computed from the serving domain entered in the second input field, and needs to be added once per serving domain.

**CNAME 2** The second line determines where the currently selected target language will be published. This defaults to the language code, but you are not obligated to keep it that way. This has to be entered separately for every target language you publish.

**CNAME 3** The third line verifies ownership of the original domain. This is computed from the user’s ID who is currently looking at the publishing page (i.e. different users will see different values, so one person should communicate this to the client and hit the Verify button), and needs to be added only once per serving domain as well. You can set the subdomain and domain where the translated site will appear.

After all the settings have been entered into the DNS records, there is short time while the changes propagate and are replicated across the world. This can vary wildly with the DNS and hosting providers, taking anywhere between one and twenty-four hours. It is recommended to wait out the twenty-four hours, as the translation proxy will not be able to save the published domain until all checks are passed.

### HTTPS & SSL certificates

Additionally, if the original site was HTTPS, or the translated sites will be served over a secure channel, an appropriate certificate and its associated key will also be needed. Ideally a wildcard certificate (one certificate for all subdomain), but Extended Validation certificates can also be used, although they require more setup work.

Our support team can also provide you with the *Certificate Signing Requests* necessary for the generation of these certificates - this will also have the added benefit of not having to send the private keys over the wider web for recording in AppEngine.

Additionally, we have a *Managed Certificate* program, where the proxy handles SSL certification automatically for published websites. The Managed Certificate program has a cost of 50EUR (60USD)/proxied domain/year or 100EUR (120USD)/proxied domain/**three** years.

See the pertaining section of the documentation [here](../../cookbook/ssl_certificates.html).

## Subdirectory publishing (example.com/de)

The alternative to subdomain-based publishing is to retain your own domain and publish the site as a subdirectory. I.e. the translated pages will appear under separate paths under the same domain as the one the project was created for (the original domain). 

Due to the way the proxy works, this requires a reverse proxy configuration to be placed in front of the webserver. A variety of load balancer/reverse proxy solutions are available on the market, with `nginx`, `CloudFlare` and `AWS CloudFront` being three of the most well-known solutions available. See the vendor documentation for the details of setting up a reverse proxy (do note that nowadays, reverse proxies are monumentally powerful network solutions, and discussion of all their features is beyond the scope of this introductory description).

If you go to the Dashboard and go to the Publish Website menu, you'll see that the *Subdirectory Publishing* option displays an example `nginx` configuration. Below is a list of the absolute minimum configurations required to achieve a workable reverse proxy using the three most popular webserver systems (Nginx, Apache httpd, and Microsoft Internet Information Systems)

### Nginx

```
location ~* ^/(jp) {
    resolver 8.8.8.8;

    set $xhost ja-jp-gereblye.app.proxytranslation.com;

    proxy_set_header X-TranslationProxy-Cache-Info   disable;
    proxy_set_header X-TranslationProxy-EnableDeepRoot true;
    proxy_set_header X-TranslationProxy-AllowRobots true;
    proxy_set_header X-TranslationProxy-ServingDomain $host;
    proxy_set_header Host $xhost;

    //old nginx
    //  proxy_pass $scheme://$xhost;
    //new nginx:
    proxy_pass $scheme://ghs.googlehosted.com;
}
```

### Apache httpd

```
<VirtualHost *:80>
	Define domain example.com
    Define previewDomain http://ja-jp-gereblye.app.proxytranslation.com
    ServerName ${domain}

	<LocationMatch "/jp/(.*)">
		RequestHeader set X-TranslationProxy-ServingDomain "${domain}"
		RequestHeader set X-TranslationProxy-Cache-Info "disable"
		RequestHeader set X-TranslationProxy-EnableDeepRoot "true"
		RequestHeader set X-TranslationProxy-AllowRobots "true"
		RequestHeader set Host "${previewDomain}"
		
		ProxyPass "${previewDomain}"
	</LocationMatch>
</VirtualHost>
```

### Microsoft IIS

*Please note that for IIS, server variables need to be whitelisted before this configuration is applied correctly!*

```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <rewrite>
            <rules>
                <remove name="ReverseProxyInboundRule1" />
                <rule name="ReverseProxyInboundRule1" stopProcessing="true">
                    <match url="^/jp(.*)" negate="false" />
                    <action type="Rewrite" url="http://ja-jp-gereblye.app.proxytranslation.com{R:1}" />
                    <serverVariables>
                        <set name="X-TranslationProxy-EnableDeepRoot" value="true" />
                        <set name="X-TranslationProxy-ServingDomain" value="example.com" />
                        <set name="X-TranslationProxy-Cache-Info" value="disable" />
                        <set name="X-TranslationProxy-AllowRobots" value="true" />
                    </serverVariables>
                </rule>
            </rules>
        </rewrite>
    </system.webServer>
</configuration>
```


The goal of any reverse proxy configuration interoperating with a translation proxy domain requires that its configuration reflect the intent of the configuration example above.

Let's clarify this pithy snippet with a more general, high-level explanation of a reverse proxy in operation.

### Example:

Suppose that we know the following about a translation project about to be published using a reverse proxy.

1. The origin server domain is `www.example.com`.
2. Source language is English.
3. Translation exists for German
4. German serving domain: `de-de-gereblye.app.proxytranslation.com`

![Reverse proxy setup](/img/dot-graphs/reverse-proxy.png)

The task of the reverse proxy, standing right at the beginning of the pipeline that will serve a client request, is to decide which target language is requested by the user and to ensure that the request is relayed to the appropriate domain that can respond with content in the appropriate language. 

In our example scenario, the reverse proxy has to make one decision: is the user requesting a resource in English or in German?

##### Translation proxy

From our perspective, The most interesting case is when a user from Germany requests `www.example.com/de/about`, the reverse proxy decides that the target language should be served via Translation proxy. It relays the request to the Google Cloud, where it is resolved to what we call the **temporary serving domain**, defined as `de-de-gereblye.app.proxytranslation.com`. In the serving subdomain mode, this domain is hidden from the user by the DNS settings added. In subdirectory publishing, the reverse proxy hides the temporary domain.

You can see that `de-de-gereblye.app.proxytranslation.com` will -- same as with subdomain publishing -- relay the request and all necessary request headers to the origin server, which will respond accordingly with source language content that the Proxy then processes on the way back and sends long to the client in a translated form.

Setting aside the exact details of that cloud translation pipeline, that's about it.

#### Source language request

Requesting the original content is a relatively straightforward process that we should nevertheless describe in brief for the sake of completeness.

If a user in England requests `www.example.com/en/about`. The reverse proxy strips the `/en` prefix, decides on the language to be served and relays the request to the origin server. 

In this case, there is no more proxy mediation (that is, no Translation Proxy) between the origin server and the requesting client, so the server response is returned and the user can peruse the webpage in the original language.

Note that on the origin server, the `/en` prefix does not exist as part of the directory structure - it is a virtual prefix used by the reverse proxy to dispatch to different domains based on the target language.

If the origin server is capable of providing content in more than one target language, the reverse proxy should presumably do the same thing for each of those target languages. If a request for `www.example.com/jp/about` can be fullfilled by the origin server alone, the reverse proxy will relay that request straight to the origin server (where it is assumed that the server backend will make the decision based on the HTTP request headers received).
