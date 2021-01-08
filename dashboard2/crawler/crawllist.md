# Crawl List - history

![Crawl list](/img/dashboard2/crawl_list.png)

In this section, you can see information about your crawls. On the right side, you can see all of them sorted by their status (active, queued & completed). In the middle, you'll see all the details that are available for the selected crawl.

The first secion contains some basic information: start and finish times, the number of pages visited, the reason of termination and any memos that were added.

The **Statistics** section gives you an overview on the content the crawl found. This card has a separate section dedicated to it [here](statistics.html) 

The **Crawl settings summary** is similar to step 5 of the Crawl wizard. This can help you to identify the crawl in case you forgot to add a memo. It can also be particularly useful when diagnosing crawl-related issues (like a crawl that found no new content). In the CrawlJob log links section, you find a button taking you to the [Crawl analyzer](../crawlanalyzer.html).

The **Cost projection** estimates the cost of using the proxy for this site. Note that this assumes an empty database meaning that this is an estimation of the *total costs* of the project not just the new content.

**Request summary** gives you information on the requests the proxy sent. The number of requests aren't necessarily the same as the number of links added to the project because it's necessary to send a request to determine the type of a link which may not be added in the end.