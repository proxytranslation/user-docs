# Page Request Evaluation 

In this recipe, we go over one possible method of evaluating a page for the number of *HTTP requests* that it sends to the project domain when it loads.

### Opening the DevTool

Investigation of the number of requests can be done on the original site. With the site open and selected in a tab, press **F12** to open the DevTool for that specific URL. By default, the DevTool will be docked within the browser screen, but you can also unlock it into a separate window.

    1. Click on the Network tab.

    2. Select "All" to track all requests.

    3. Enable "Use large request rows" (to the right of "View" in the toolbar).

    4. You can leave the "Hide data URLs" option on

![Chrome DevTool Settings](/img/misc/devtool/settings.png)

At this point, since you have opened the DevTool after the site has already loaded, the Network tab will be completely empty.

    5. Refresh the site to start logging requests.

You will see a flurry of activity as the site reloads. After it has finished, you can start analyzing the various requests in the list.

### Filter Requests on the same Domain

    6. Enable "Regex" for filtering

You are free to ignore all requests that go to external domains that will not be part of any linked projects. If you have enabled the "large request rows" option, the DevTool will helpfully list the paths below the resource names.

![Request Locations](/img/misc/devtool/request-list.png)

The DevTool provides detailed information, but not all of it is needed in this case. As soon as you have the full list in view, you can remove from view those requests that go to external domains. The easiest way to do this is to add the "^/" regex to the filtering options on top.

![Domain Filter](/img/misc/devtool/filter-for-domain.png)

At this point, the first relevant statistic becomes available at the bottom of the request list - the number of currently displayed requests / total number of requests will be a good first indication of the number of requests that *potentially* have to go through the proxy when the page is served.

## Considerations

### What Cache Headers are present?

If you click on a request in the list, a new sidebar will appear with information about that particular request. For evaluation purposes, the `Header` tab, and the `cache-control` directive is especially important.

`cache-control: private` or `cache-control: no-cache` indicate a request that the original server expressly states to be non-cacheable - usually, it is not a good idea to change this haphazardly. It is better to count these requests as necessary for the construction of the page.

### Is the resource static?

PNG/JPG images, JS and CSS files are those resources that tend not to change rapidly. You can override the Cache Headers of such Resources in Dashboard > Path settings  - with the effective result being that the burden of serving that content is offloaded to independent caching nodes on the global network.

Re-caching happens for each cached entity after the duration of the `max-age` directive passes. Using `max-age`, you declare a time-frame during which you will enlist the help of the network to serve the content in unchanged form. It can be used to fine-tune the time that you'll allow a specific cached instance of a resource to persist.

**NOTE** While Cache Header overrides work in the overwhelming majority of cases, there is no "law" to force caching nodes to respect them: consequently, the pace at which various Resources are cached/re-cached on the global network is, to a degree, arbitrary.

While technically possible, making Document resources cacheable requires careful consideration, but as little as 10 to 60 minutes can be very useful. Consider that in most cases, the landing page receives the most page requests. Consequently, allowing it to be cached with a controlled  `max-age` value means considerable savings on the proxy (with the caveat that any changes will take at most the time declared for `max-age` to propagate across the network).

### Does the requested resource change often/constantly according to context?

#### Dynamic Resource

XHRs/AJAX calls/dynamic content cannot be cached without rapidly running into many problems on the published site. It is better to say that they simply can not be cached. This also applies to those requests that are sent throughout the user session on the page after loading it (and in lieu of hard data, it is very difficult to forecast the number of dynamic requests a given user will start).

Salient examples are search field handler scripts, web-shop endpoints, PHP scripts, backend endpoints and other similar sources that give wildly varying responses based on the parameters sent in the requests.

#### Frequently Iterated Resource

If a site is undergoing development, for example, it is usually not a good idea to add Cache Header overrides (certainly not overly long ones). This  would in effect delay propagation of any changes by the value of `max-age`, resulting in syncing problems between the original site and its translated counterparts.

## Overriding Cache Headers

Evaluation of the number of requests is most useful when estimating the monthly cost associated with serving a site. For overriding cache headers on the Dashboard, see the [Path Settings](../../dashboard2/pathsettings.html) section of this documentation. Enable the public caching tweak in Dashboard 2.0 → *Advanced settings* to facilitate further speedups on the proxy side.

## Example Scenario & Conclusions

If the following information is available:

    * The original site has 50,000 monthly user visits
    * A single target language sub-domain is expected to receive about half of that, 25,000
    * Each page uses between 50-70 requests to build

Using the consideration points above, it is determined that most of those requests can be counted out and the rest cached for 24 hours. The site will require 3 non-cacheable requests from a user coming in from a location where there is no caching node on the way. 

From this you will be able to conclude the following:

    * 2 requests are necessary, so 25,000 * 3 = 75.000 expected page requests
    * BUT: consider also the number and visit frequency of revisitors - each time a cached entity's max-age (24 hours in this hypothetical scenario) expires, that resource has to be re-cached, which will increase the number of requests going through the proxy with a certain amount (although this amount is usually negligible).
    
With the appropriate Cache Headers, Google's geographically specific Edge Cache, the public internet, the various ISP caching nodes, and at the other end of the process, the user's browser cache will participate in offloading the page request from the proxy's translation pipeline.

## Conclusion

Armed with this knowledge of an overarching view of requests that will have go through the proxy, you will be able to provide accurate estimates for the monthly costs of the proxy
