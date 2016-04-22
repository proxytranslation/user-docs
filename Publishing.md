+ [[Publishing, domain names (CNAME)|Publishing#publishing-domain-names-cname]]
  * [[Serving domain name|Publishing#serving-domain-mode]]
  * [[Subdirectory publishing mode|Publishing#subdirectory-publishing-mode]]
+ [[Language selector|Publishing#language-selector]]
+ [[Cache maintenance|Publishing#cache-maintenance]]  
+ [[Easyling for Wordpress|Publishing#easyling-for-wordpress]]

### Publishing, Domain names (CNAME)

The publishing interface has two options to make the site available to the web at large: serving domain mode and subdirectory publishing mode.

#### Serving domain mode

In the serving domain mode, Easyling will publish the translated site either on a subdomain of the original (the default behavior, such as `de.example.com`), or on a completely separate naked domain (such as `example.com`). In order to use this mode, you (or the client) will have to modify the DNS settings corresponding to the original domain - the three to five records (three for subdomains, five for new naked domains) that need to be inserted in your DNS settings are found below the two input fields, and will change as you enter the desired serving domain.

Each line of the table has a distinct function:
- The first line allows mapping of the subdomain in Google AppEngine, enabling us to alter the datastream and translate the site. This row is computed from the serving domain entered in the second input field, and needs to be added once per serving domain.
- The second line determines where the currently selected target language will be published. This defaults to the language code, but you are not obligated to keep it that way. This has to be entered separately for every target language you publish.
- The third line verifies ownership of the original domain. This is computed from the user's ID who is currently looking at the publishing page (i.e. different users will see different values, so one person should communicate this to the client and hit the Verify button), and needs to be added only once per serving domain as well.
You can set the subdomain and domain where the translated site will appear.

After all the settings have been entered into the DNS records, there is short time while the changes propagate and are replicated across the world. This can vary wildly with the DNS and hosting providers, taking anywhere between one and twenty-four hours. It is recommended to wait out the twenty-four hours, as Easyling will not be able to save the published domain until all checks are passed.

Additionally, if the original site was HTTPS, or the translated sites will be served over a secure channel, an appropriate certificate and its associated key will also be needed. Ideally, this would be a wildcard certificate (one certificate for all subdomain), but Extended Validation certificates can also be used, though they require more setup work.    
If needed, the Easyling support team can provide the Certificate Signing Requests needed to generate these certificates.

#### Subdirectory publishing mode

The alternative to subdomain-based publishing is to publish the site to retain your own domain, and publish the site as a subdirectory of the existing domain, i.e. the translated pages will be available on separate paths under your own domain.
However, due to the way the proxy operates, this will require a specifically configured nginx reverse proxy server to be prepared and placed in front of your own webserver. An example configuration snippet is available on the publishing interface, but this should be treated as only a guideline, to be customized according to your specific setup!

### Language selector

Easyling offers two different language selectors out-of-the-box: a sidebar-based version and a dropdown version.    
The first variant attaches itself to the right or left side of the screen, scrolling with the view, and display a set of flags allowing the user to jump between different language versions.    
The second variant is a bit more complex and feature-rich, requiring a `div` element (for example, `<div class="langselector-dropdown"></div>`) to be specified at setup, based on a CSS class (for the example, `langselector-dropdown`). The dropdown will anchor onto this element, injecting its own contents. It then displays a dropdown of all the selected target languages, with each being configurable in its display name (the language name only, language *and* locale name, or a custom name that you can define).
Both language selectors require you to insert a single line into the original site's `head`, which takes care of displaying the selectors on every page.

Although it's not strictly Easyling-based, there is a third option, implementing a language selector from scratch. While this requires development resources, it also allows practically infinite customization options regarding the look and feel of the widget. All that is required is a set of links, each pointing to a target language that you've already published; with the link pointing to the original site annotated with the `__ptNoRemap` class - otherwise, the proxy will relativize that link as well, and map it to the translated domain.

### Cache maintenance

If caches are being used on the project, care must be taken to maintain them so that the correct content is being served at all times. Cache statuses can be queried by page, from the Pages list, using the toolbar that appears when hovering over any given row in the list.

Aside from displaying the status of the caches and which cache is being served at the moment of the query, the dialog that appears also allows deleting the cache for a single page instead of a the entire project. This is useful if you change translations on a single page and want it to be displayed without affecting the rest of the site.

Checking the cache status for individual pages from the Pages List:  

[[https://github.com/easyling/public/wiki/img/dashboard-cache-status.png|alt=Cache Status]]
  
### Easyling for Wordpress  
  
If the content owner uses WordPress, Easyling provides an option to install the Translation Proxy directly to the CMS. In this case no Translation Proxy fee will be charged by Easyling, but the foreign traffic shall be handled by the content owner’s infrastructure.    
For more information see our [blog](https://www.easyling.com/blog/easyling-for-wordpress/) or the [WordPress.org](https://wordpress.org/plugins/easyling-for-wp/screenshots/).