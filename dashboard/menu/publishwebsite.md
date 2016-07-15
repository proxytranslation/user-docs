## Publish Website

In this menu, you are provided with the means of publishing your
website on a pretty domain after translation tasks have finished.

The publishing interface has two options to make the site available to
the web at large: serving domain mode and subdirectory publishing
mode.

### Domain settings

This screen opens by default after clicking on "Publish website". The
following settings and fields are available:

**Target language** Choose which target language you would like to
configure a serving domain for.

**Temporary domain** This is the preview proxy you can use to preview
your translations live (this is immutable).

**Access control** you can add basic HTTP authentication to the
proxied site in order to restrict access to it. Click on _Configure
access control..._. Select the proxy modes that you'd like to limit
access to, enter your username and password. You can add multiple
users to the list.

#### Serving domain mode (de.example.com)

In the serving domain mode, Easyling will publish the translated site
either on a subdomain of the original (the default behavior, such as
`de.example.com`), or on a completely separate naked domain (such as
`example.com`). In order to use this mode, you (or the client) will
have to modify the DNS settings corresponding to the original domain -
the three to five records (three for subdomains, five for new naked
domains) that need to be inserted in your DNS settings are found below
the two input fields, and will change as you enter the desired serving
domain.

##### CNAME settings

There are three CNAME settings that are required on your domain to
enable publishing of your website. Each of the lines in the table that
is displayed has a specific function:

**CNAME 1** allows mapping of the subdomain in Google AppEngine,
enabling us to alter the datastream and translate the site. This row
is computed from the serving domain entered in the second input field,
and needs to be added once per serving domain.

**CNAME 2** The second line determines where the currently selected
target language will be published. This defaults to the language code,
but you are not obligated to keep it that way. This has to be entered
separately for every target language you publish.

**CNAME 3** The third line verifies ownership of the original
domain. This is computed from the user’s ID who is currently looking
at the publishing page (i.e. different users will see different
values, so one person should communicate this to the client and hit
the Verify button), and needs to be added only once per serving domain
as well. You can set the subdomain and domain where the translated
site will appear.

After all the settings have been entered into the DNS records, there
is short time while the changes propagate and are replicated across
the world. This can vary wildly with the DNS and hosting providers,
taking anywhere between one and twenty-four hours. It is recommended
to wait out the twenty-four hours, as Easyling will not be able to
save the published domain until all checks are passed.

##### HTTPS & SSL certificates

Additionally, if the original site was HTTPS, or the translated sites
will be served over a secure channel, an appropriate certificate and
its associated key will also be needed. Ideally a wildcard certificate
(one certificate for all subdomain), but Extended Validation
certificates can also be used, although they require more setup
work. Our support team can also provide you with the Certificate
Signing Requests necessary for the generation of these certificates -
this will also have the added benefit of not having to send the
private keys over the wider web for recording in AppEngine.

See the pertaining section of the documentation here.

#### Subdirectory publishing (example.com/de)

The alternative to subdomain-based publishing is to publish the site
to retain your own domain, and publish the site as a subdirectory of
the existing domain, i.e. the translated pages will be available on
separate paths under your own domain. However, due to the way the
proxy operates, this will require a specifically configured nginx
reverse proxy server to be prepared and placed in front of your own
webserver. 

An example configuration snippet is available on the publishing
interface, but this should be treated as only a guideline, to be
customized according to your specific setup!

There are a variety of options at your disposal when implementing
subdirectory publishing on your domain. You may choose to use `nginx`,
`CloudFront` or any similar solution to use as a reverse proxy.

### Language selector

The "finishing touch" is to add a language selector to your published
project. There are two ways you can do this: use one of the language
selectors provided by default and customize that according to your
needs, or implement your own solution in-house.

We'll focus on the internally provided solutions. There are two types
of language selectors available: the **Dropdown** and the **Sidebar**.

Use the **Language selector tye** option to select between the two
types. You'll notice that the menu changes somewhat based on your
choice, and the currently active language selector choice is displayed
in a preview window on the right. Both types contain the source
language site by default.

At the same time, the embed code text box changes and displays the
<script> tag that needs to be embedded within the original site's
`<head></head>` tags.


#### Sidebar

The sidebar is an easy-to-deploy language selector that displays flags
for each specified target locale on the left or right side of the
website. The horizontal orientation and display names are settable.

#### Dropdown

This variant is a bit more complex and feature-rich. It requires an
**additional div element on the original page** besides the `<script>`
tag. For example, you may insert `<div
class="langselector-dropdown"></div>` into the original site
structure, then specify the **Dropdown CSS class name** as
`langselector-dropdown`. The dropdown will anchor onto this element
and inject its own contents to display a dropdown of all selected
target languages.

At the bottom of the menu, you can configure the **display names** for
the different languages. 

#### RYO selector

The third option, implementing a language selector from scratch, does
require development resources, but it also allows practically infinite
customization options regarding the look and feel of the widget. 

All that is required is a set of links, each pointing to a target
language that you’ve already published.

**WARNING** By default, the proxy **remaps** the links to the original
site! To prevent this from happening, add the ` __ptNoRemap` class to
the link in the HTML - otherwise, the proxy will relativize that link
as well, and map it to the translated domain (making it impossible to
return to the original site from proxied site).

### Wordpress plugin

Clicking on this menu will take you to the Wordpress site where you
can download the Easyling Wordpress plugin.

The proxy provides an option to install the Translation Proxy directly
to the Wordpress CMS. In this case no Translation Proxy fee will be
charged, but the foreign traffic shall be handled by the content
owner’s infrastructure. For more information see our blog or the
WordPress.org.
