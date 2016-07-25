# Proxy modes - X, P, live

## X-proxy (testing, JS bugs, JS fix domains , CORS)

The X-proxy is great for testing. You can spot content that does not
get picked up by default, and make your configurations to your
project, and check for success.

There are a couple of situations, when the X-proxy comes in handy:

* Testing regular expressions, for example on e-commerce sites.

* Testing JSON (JavaScript) and XML translation.

* Just browsing through a site, for evaluation purposes.

An example X-proxy URL:
`https://de-de-{project_code}-x.app.easyling.com`

The X-proxy can be accessed from the pages list under Content (or
Discovery) by clicking on the Preview button in the hover toolbar,
while holding down the Ctrl/Cmd button, or you can just replace the -p
for a -x in the normal preview's URL for the same effect.

## P - Preview

The standard proxy mode to view the translated website before
publishing. However, the preview can be used for a couple of other
things:

* Cookie header extraction to get behind logins

* Visiting pages manually, to ingest content

An example Preview-proxy URL: `https://de-de-{project_code}-p.app.easyling.com`

## C - Channel

## Live serving mode

After publishing the website, the proxy serves content on the chosen
domain.
