# Page Content Overrides

The proxy relies on the original site for substance: both translatable content and server-side services are provided by the original. The proxy relays and processes request-responses between that server and the visitor.

PCOs, as they are usually abbreviated, are an exception to this rule. They are “virtual” pages that are either created completely from scratch (and thus may not even have a counterpart on the original) or they override URLs that are accessible on the original server with wholly custom content over the proxy.

If a visitor requests an URL over the proxy that has an associated PCO, then the corresponding request is not sent to the origin (even if the URL is made unique by query parameters) and the PCO is served instead. A PCO, in a similar fashion to responses from the original site, will go through the translation pipeline. This bears repetition: **the contents of a PCO can be extracted and translated**.

## Headers

### Content Types

The source need not be HTML: any custom content-type can be entered (as long as it is a textual type), such as `text/xml` or `application/javascript` along with customized cache headers and status codes. 

Of the many content types that can be used, the behavior of `text/html` is special in an important way: CSS and JS page modifiers on the project will be **injected** into such PCOs. The corresponding `<style>` and `<script>` tags are injected even if the PCO is a simple HTML snippet (that is, it lacks an `<html>` or `<head>` tag).

Syntax highlighting is automatically activated for a subset of content types after the Header field is filled out.

### Cache Control & Pragma

Loading overrides over the proxy also [count as page requests](../../cookbook/pageviewsandcaching.html), so it is recommended that you add an optimized `max-age` value to each PCO and make them publicly cacheable. Placeholders in each field indicate reasonable defaults. At the same time, you'll want to set `max-age` to a smaller value *during testing*, in order to avoid having incomplete or work-in-progress PCOs cached for a long time over the network.

### Response Codes & Location

The 300-family of status codes requires the Location header to be defined as well, to specify the target of redirection. Note also that only those HTTP status codes can be used that are permitted by the Java Servlet class!

## Search result pages

The fact that URLs associated with a PCO are never requested from the origin server can be beneficial when [implementing site search](../../cookbook/sitesearch.html). If a distinct result page is used to display results, an empty version of that original can be copied verbatim into a PCO. This is particularly useful in cases where site search load is considerable over the proxy and the origin server would benefit from not having to handle search requests that it is not equipped to answer.

## Scripts/Libraries

The PCO feature lets you add JS libraries or CSS stylesheets over the proxy as PCO with the appropriate Content-Type. A script declared in this fashion can be included in the `<head>` tag by going to Page modifiers > Javascript editor and **adding a reference to the PCO URL** at the top.

This approach is not recommended for jQuery or similar standard libraries. Inclusion of a script accessible via CDNs should be done using those external URLs, if not for any other reason, then because such external domain requests do not cost money over the proxy.

If, however, a standard library has to be changed in some small way over the proxy, PCOs can come in very handy.

## Placeholders / Redirection

PCOs can be used to create "Under construction" pages or to ensure that the user is steered away from a specific URL via a redirection. But keep in mind that there is no prefix support for PCOs: they are always **exact URLs** and can only be applied as overrides in a targeted manner.

## Binary Content

Binary content PCOs (including images and webfonts) are not supported. Use the resource localization features to replace images over the proxy with their translated counterparts.

