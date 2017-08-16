# Staging Domains

While it is true that the project URL is a property that cannot be changed once created, there is no reason why you should not be able to change/swap the *source* of the content entirely. 

Website maintainers like to do test runs on any changes they make in the context of a devserver, and the same devserver can also serve as a testing ground for any untranslated content - you can use the Staging Domain option just to do that. 

If the project URL is `example.com`, and a devserver exists at `dev.example.com`, you can enter that URL into the Staging Domain field and click on "Add Staging Domain". The staging server is added to the menu below the text field automatically and enabled as default in all Preview domains. 

As long as a staging domain is enabled for a proxy mode, all requests going through the proxy (regardless of initiator, such as a user session in Preview or a content extraction Scan) will be mapped to that domain, regardless of the original project URL.

Content translations are propagated like in all cases, but it important to keep in mind that *previous translations* will only show up appropriately if there is a 100% matching between the path structures of the original site and the staging server. That is, any entries translated on `/three/level/deep/path.html` will not be

Hover over the staging domain name to reveal a menu with three options. *Live default*, *Default* and *Delete*. Click on "Make Live default" to enable the staging domain for the live published site. A tick icon will be displayed next to the staging domain with this option enabled. The same goes for *Default*, which applies to all other proxy modes (such as Highlight View in the Workbench, PReview or the X-proxy). Click on *Delete* to remove a Staging Domain.

Naturally, only one staging domain can be designated as Live or Preview default at one time.

## When to Use Staging Domains?

### Content Decoupling

### Domain Name Change
