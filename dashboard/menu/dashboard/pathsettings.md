## Path settings - Cache & Cookie, Content Type Overrides

Here, you can add target domain paths and define Cache and Cookie overrides for them. Enter a new path (you can set it to be a prefix or an exact URL), then click on Add Path. A New rule dropdown is displayed. You can choose either Cache and Cookie Overrides, Content Type Overrides, or both. After selecting one, the dropdown will disappear, but you'll still be able to add the other using the plus icon that appears next to the path.

By clicking on 'Edit rule', you can set the Cache override to public, private or ignore according to your needs. set the maxAge and override type (whether to clear or use cookies) and you're set.

Use the Save icon next to the rule name or the blue 'Save all' button to save your settings.

You can always return here and add new paths and rules using the 'Add new path' button if there is a need for it.

### Cache Header Overrides

Loading a page in the browser usually involves multiple requests for resources on the original site and other domains. A page can use multiple static resources (such as images) that require no localization. 

If an image is referenced by relative name, such as `/logo.jp`, the hand of the proxy is forced: it has to assume the domain to be the proxy domain. The access path of the resource will become `fr.exmaple.com/logo.jp` assuming a French translation of `example.com`. This is a page request over the proxy, and therefore costs money. 

Another common issue that lead to this feature is that  static resources often have suboptimal Cache Headers. This leads to the same, unchanging content being served from the original server for each request individually, potentially decreasing the efficiency of the site and certainly adding to the number of requests that would have to go through the proxy. The Path Settings dialog can be used to override the default Cache Headers of resources of a given path or exact URL):

![Cache Override](/img/dashboard/path_settings_cache_override.png)

The screenshot above shows an override that will operate on all images that are located on the `/res/img` path and override their Cache Headers to the following default values:


```
cache override: public 
max-age: 86400
cookie override: clear cookies
```

This way, the resources become publicly cache-able on various independent nodes on the network. Depending on the location of the caching node and the pathway of the request, the content will be served from caches instead of going through the proxy pipeline. 

The result is a considerable lightening of server load, and a decrease in the number of page requests that go through the proxy. 


#### Important Notes!

    1. The feature is meant to be used in specific cases with binary/static resources that are unlikely to be changed quickly and often. Although any type of resource can be marked as publicly cache-able, these settings should not be applied to dynamic content (be warned of the **likely discrepancies** between the original and cached content!). **Careful Consideration Required!**

    2. Since Public Caching relies on the network to offload the burden of serving resources, changes take time to propagate. The `max-age` directive of the Cache Header indicates how long a cached instance of a resource will stay cached - the default is 24 hours. When the time declared for `max-age` is up, the resource is cached again via a request for the original.
