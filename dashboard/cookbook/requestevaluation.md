# Investigating Page Requests using the Chrome DevTool

A crucial statistic of the original site is the number of requests needed to load and build a given page. This has monthly cost implications over the proxy. In this tutorial, we provide some pointers on how to get a working estimate for this number. We investigate the English Wikipedia as an example.

Request evaluation is often necessary since website owners/maintainers usually focus on tracking the number of *page visits*, a useful metric to gain knowledge about visitors to a site, but different from the individual HTTP *requests* in the stricter, technical sense.

# Opening the DevTool

Investigation of the number of requests can be done on the original site. With the site open and selected in a tab, press **F12** to open the DevTool for that specific URL. By default, the DevTool will be docked within the browser screen, but you can also unlock it into a separate window.

    1. Click on the Network tab.
 
    2. Select "All" to track all requests.
    
    3. Enable "Use large request rows".
    
    4. You can leave the "Hide data URLs" option on
    
![Chrome DevTool Settings](/img/misc/devtool/settings.png)
    
At this point, since you have opened the DevTool after the site has already loaded, the Network tab will be completely empty.

    4. Refresh the site to start logging requests.
    
You will see a flurry of activity as the site reloads. After it has finished, you can start analyzing the various requests in the list. 

# Filter Requests on the same Domain

    5. Enable "Regex" for filtering

You are free to ignore all requests that go to external domains that will not be part of any linked projects. If you have enabled the "large request rows" option, the DevTool will helpfully list the paths below the resource names.

![Request Locations](/img/misc/devtool/request-list.png)

The DevTool provides detailed information, but not all of it is needed in this case. As soon as you have the full list in view, you can remove from view those requests that go to external domains. The easiest way to do this is to add the "^/" regex to the filtering options on top.

![Domain Filter](/img/misc/devtool/filter-for-domain.png)

At this point, the first relevant statistic becomes available at the bottom of the request list - the number of currently displayed requests / total number of requests will be a good first indication of the number of requests that *potentially* have to go through the proxy when the page is served.

# Considerations

## What Cache Headers are present?

If you click on a request in the list, a new sidebar will appear with information about that particular request. For evaluation purposes, the `Header` tab, and the `cache-control` directive is especially important. 

`Cache: private` or `Cache: no-cache` indicate a request that the original server expressly states to be non-cacheable - usually, it is not a good idea to change this haphazardly. It is better to count these requests as necessary for the construction of the page.

## Is the resource static?

PNG/JPG images, JS and CSS files are those resources that tend not to change rapidly. You can override the Cache Headers of such Resources in Dashboard > Path settings  - with the effective result being that the burden of serving that content is offloaded to independent caching nodes on the global network. 

Re-caching happens for each cached entity after the duration of the `max-age` directive passes. Using `max-age`, you declare a timeframe during which you will enlist the help of the network to serve the content in unchanged form. `max-age` can be used to fine-tune the time that you'll allowa specific cached instance of a resource to persist. 

**NOTE** While Cache Header overrides work in the great majority of cases, strictly speaking, there is no law to force caching nodes to respect them: consequently, the pace at which various Resources are cached/re-cached on the global network is, to a degree, arbitrary. 

While technically possible, making Document resources cacheable requires careful consideration and is best avoided entirely.

## Does the requested resource change often/constantly according to context?

### Dynamic Resource

XHRs/AJAX calls/dynamic content cannot be cached without rapidly running into many problems on the published site. Rather, they simply can not be cached. This also applies to those requests that are sent throughout the user session on the page after loading it (and in lieu of hard data, it is very difficult to forecast the number of dynamic requests a given user will start).

Salient examples are search field handler scripts, webshop endpoints, PHP scripts, backend endpoints and other similar sources that give wildly varying responses based on the parameters sent in the requests.

### Frequently Iterated Resource

If a site is undergoing development, for example, it is usually not a good idea to add Cache Header overrides (certainly not overly long ones). This  would in effect delay propagation of any changes by the value of `max-age`, resulting in syncing problems between the original site and its translated counterparts.
