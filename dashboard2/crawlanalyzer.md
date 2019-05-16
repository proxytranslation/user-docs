Crawl Analyzer
==============

After using the _Crawl Wizard tool_, and running a _Wordcount (Discovery)_ or a _Content extraction (Scan)_, you can check its results under the _List_ section by either downloading the `.log` file, or using the _Crawl log visualization filter_.

When you click on the filter button, a new window will pop up, where you can narrow down the results of the log.

![Open crawl log filter](/img/dashboard2/open_crawl_log_filter.png)

### Crawl status

![](/img/dashboard2/crawl_log_filter.png)
<br/>
Crawl log filter

**Processed:** The page was successfully added to the pages list, the crawler was able to process it.

**Skipped:** In this case, the Proxy could not process the page, because of its `content-type`, or because of the configuration of the collectible resources in _Crawl wizard_. There are four main reasons behind this status:

- _No content type, page collection is disabled_: The crawler hadn't received a content-type before, and also the collection of new HTML pages is disabled.
- _HTML page, page collection is disabled_: The content-type is text/html, but the collection of new HTML pages is disabled.
- _Not HTML page, resource collection is disabled_: The URL points to a resource (e.g. the content-type is text/javascript or text/css), but the collection of resources is disabled.
- _Content with type < content-type > is not processed during this crawl_: The content-type header designates an unprocessable type, for example if the header is proprietary (such as "application/example-script"), or it is an unsupported content-type, for example text/plain.

**Failed:** The proxy was not able to process the content, you can see below the list of the reasons behind this status:

- _Path is externalized_: The page is externalized
- _Request sending failed_: The crawler wasn't able to send a GET request
- _Content is not an HTML page_: The content is not HTML, the crawler wasn't able process it
- _Not processable_: The crawler wasn't able process the given content-type
- _Too large, size: < size of content >, limit: 1048576_: Files above 1.5 MB are not handled
- _Parsing error_: Invalid script, or HTML format for example
- _Proxy request failed_, _Response not processable_, _Response processing was aborted_,  _Skipped because processing failed_: Error during processing. Sometimes it is not quite obvious at first glance why the crawler failed, but in this case we can check our logs for you


### Response type

You can also filter the log results by content-types, for example, you can select different resource types, like CSS, JS, images etc.


### Response code

With this filter you can narrow down the log list by [HTTP status](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) codes:

**1xx (Informational):** The request was received, continuing process

**2xx (Successful):** The request was successfully received, understood, and accepted

**3xx (Redirection):** Further action needs to be taken in order to complete the request

**4xx (Client Error):** The request contains bad syntax or cannot be fulfilled

**5xx (Server Error):** The server failed to fulfill an apparently valid request  


### Regexp

Inserting here links or other texts, will be treated as strings, but you can specify `java/util/Pattern` regular expressions as well.
You can test your regex [here](http://www.regexplanet.com/advanced/java/index.html).
