# Staging Domains

Use Staging Domains to change the origin server to use in Preview or crawls.

Website maintainers like to test any changes they make on a development or staging server before unleashing them on the Live site. The same staging server that is in place on the site can be used over the proxy as a testing ground for any translatable updates. Add a Staging Domain option to extract and use data from that domain staging server in the various proxy modes.

If the project URL is `example.com`, and a staging server exists at `dev.example.com`, you can enter that URL into the Staging Domain field and click on "Add Staging Domain". The domain is added to the menu below the text field automatically and enabled as default.

All requests going through the proxy (regardless of initiator, such as a user session in Preview or a content extraction Scan) will be mapped to that domain, regardless of the original project URL - the project domain might be `example.com`, but the Preview will be displaying content from `dev.example.com`.

*Very important:* Translations are propagated after extraction as usual, but this comes with an important warning: *previous translations* will only show up appropriately if the path structures of the original site and the staging server match 100%. If this is not the case, then a new project page is created in the project.

## Default and Live Default Staging domains

Click the three-dot action button to reveal four options. *Edit*, *Set/Unset default staging*, *Set/Unset as live*, and *Delete*.

![Staging Domain Example](/img/staging_domain.png)

Click on "Make Live default" to enable the staging domain for the live published site. A tick icon will be displayed next to the staging domain when this option is enabled.

The same goes for *Default*, which applies to all other proxy modes (such as the Highlight View in the Workbench, the Preview domain or the X-proxy). Click on *Delete* to remove a Staging Domain.

Naturally, only one staging domain can be designated as Live or Preview default at one time, but it is possible to enable one domain to be both. 

## When to Use Staging Domains?

### Content Decoupling

The staging domain feature of the proxy is beneficial when updates to the original site are regularly tested on the staging server first. 

Staging domains let you make that same content available through the proxy for translation work without disturbing the translation quality over the published domain in the meantime.

The idea is to extract content from the staging domain and begin translation work early -- by the time the changes on the original site are moved from the staging domain to the main one, all target language entries will have their translations ready.

### Domain Name Changes

An alternative use of the staging domain feature is when the original site changes domains. As you know, project addresses cannot be changed once a project is created. However, migrating an entire project due to a simple name change might not be a very optimal solution.

In these cases, you can use the Staging Domain option to set up the new address as a staging server on the project. By following up on the name change in the Publishing settings, you can transform both the origin and the published domains to the new address (but note that the project address will remain the same, however).
