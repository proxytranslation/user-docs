# Content override

The Proxy Application can create a “virtual” page in the site or
override an existing one with custom code. For any requests to an
overridden page, the corresponding remote server request is not sent,
and the override contents are used as the basis of the
translation. The source is not required to be HTML, custom
content-types can be entered, along with customized cache headers, and
status codes (HTTP status codes are restricted to those permitted by
the Java Servlet class!) - note that the 300-family of status codes
requires the Location header to be defined as well.
