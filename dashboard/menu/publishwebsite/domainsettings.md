# Domain settings

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

## Serving domain mode (de.example.com)

In the serving domain mode, Easyling will publish the translated site
either on a subdomain of the original (the default behavior, such as
`de.example.com`), or on a completely separate naked domain (such as
`example.com`). In order to use this mode, you (or the client) will
have to modify the DNS settings corresponding to the original domain -
the three to five records (three for subdomains, five for new naked
domains) that need to be inserted in your DNS settings are found below
the two input fields, and will change as you enter the desired serving
domain.

### CNAME settings

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

### HTTPS & SSL certificates

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

## Subdirectory publishing (example.com/de)

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
