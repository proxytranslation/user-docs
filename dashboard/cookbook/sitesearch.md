# Site Search

If a site includes a search function of any kind (ex.: product search in a webshop), visitors expect to be able to search for things in the language of the website -- to input any term into the search fields and receive appropriate results immediately.

**A pretty standart example**

Let's say that a visitor uses the search field of `www.example.com` to search for the word "**product**". Upon pressing enter, they are navigated to `https://www.example.com/search?q=product`. The server will detect and use the value of the `q` parameter and runs whatever server-side search mechanism it uses to search for this term, assemble a list of results and construct a result page to send to the browser.

Because the server is the one, who does the actual searching, we call this approach _server-side search_. 

**This introduces a potential issue**

On a proxied site, however, we run up against a problem: the original does not know about the translations. Requests are automatically relayed to the original server. If a visitor were to type "**produkt**" on the German domain (resulting in an URL navigation to `https://de.example.com/search?q=produkt`), that is the same as relaying a search query with German language content to the original site.

Not possessing a _German language index_, the response is certain to contain 0 results. The fact that the proxy is CMS-agnostic and that it generally doesn't require that translated content be shared with the original server also means that this same content will not be available to the indexing/search software that is running on the original.

Luckily, the server-side approach isn't the only option, when it comes to having some search functionality on a website!

**Recommended solution**


The fact, that proxied pages themselves are  _publicly available for indexing by search engine bots_ comes in handy. A search engine that supports site-specific queries can provide localized search via __client-side__ AJAX requests.

There are two aspects to this kind of solution that you should consider:

On the one hand, such a site search has to be coded in JavaScript in the form of an override (an example with a detailed explanation follows below), and depending on how ornate/feature-laden the original's search functionality is, complexity of the override implementation can vary from the relatively simple to the astonishingly complex.

On the other hand, familiarity with the various indexing-related conditions of your chosen vendor is also important (we provide pointers to some documentation for Bing, since it is the vendor used in the example). In our experience, it is not at all unusual for search engines to act leisurely in their pace. (Remember that a site can only be indexed after it is published over the proxy.)

On the same note, the [publishing method](../../dashboard/index.html#publish-website) you use can also have a bearing on the way search & indexing will work, so a case-by-case analysis is a must. (Note that the Client-Side Translation publishing method is *not compatible* with a site search integration of the type described here.)

### Third-party Integrations

#### Bing

Bing's Web Search API can be used for site search integration purposes over the proxy. In order to access Bing's API, you will need to purchase an API key. See the details on [Microsoft Azure](https://azure.microsoft.com/en-us/try/cognitive-services/?api=bing-web-search-api) on procuring one, and see the [pricing page](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/search-api/web/) for a detailed description of the various service tiers.

Consult the [Webmaster Tools Documentation](https://www.bing.com/webmaster/help/help-center-661b2d18) concerning general usage-related matters. You can submit a domain for indexing in Bing [here](https://www.bing.com/toolbox/submit-site-url). Submission of specific URLs is possible [here](https://www.bing.com/webmaster/help/submit-urls-to-bing-62f2860a), but this feature is limited to root domains at the time of writing: until such time as this limitation is lifted, you might only be able to use this targeted indexing feature with subdirectory publishing.

##### Bing: Verification of subdomains

If you want to track the indexing of your subdomains in Webmaster Tools and do SEO tracking, you'll need to verify ownership of the target language subdomains. The available methods are [described here](https://www.bing.com/webmaster/help/how-to-verify-ownership-of-your-site-afcfefc6).

The XML-based approach is the simplest to implement over the proxy (it can be done without having to apply any changes on the origin): create a temporary [Page Content Override](../../menu/pagemodifiers/contentoverride.html) with the contents of `BingSiteAuth.xml` (content type should be `text/xml`). This exposes the authorization XML over the proxy domains. From then on, you are free to add the target language subdomains in Webmaster Tools and verify them one-by-one.

## Part II: Example

In the rest of this documentation page, let us detail how a simple site search integration could be implemented as injected JavaScript over the proxy using [v7 of the Microsoft Web Search API](https://docs.microsoft.com/hu-hu/rest/api/cognitiveservices/bing-web-api-v7-reference).

### Page Modifiers

Customized JavaScript can be injected into the `<head>` tag of each page over the proxy. This capability is the entryway for a search override. To add injected JavaScript you'll find an editor in Page Modifiers > Javascript editor, where you can type or copy & paste Javascript code. After saving the modifier, it will show up in the page source over the proxy after a refresh (but note that cache settings might get in the way of an instantaneous update on the live domain!).

Site search functionality is frequently displayed to the visitor in the form of an input field and a button. We'll go with this familiar scenario and use the following minimal webpage for this tutorial:

``` html
<html>
  <head>
    <script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
  </head>
  <body>
    <script>
     function showResults(){
       document.querySelector("#results")
               .setAttribute("style", "display:block;");
     }
    </script>
    <div id="search">
      <form id="form" action="javascript:showResults();">
        <label for="#input">Search:</label>
        <input id="input" type="text"/>
        <button id="button" action="submit">Submit</button>
      </form>
      <div id="results" style="display:none;">
        <div class="result-item">
          <h2><a href="#">Result title</a></h2>
          <p>Result summary</p>
        </div>
      </div>
    </div>
  </body>
</html>

```

### First steps

`showResults()` simulates the original search functionality of a site. The goal of our search integration is to prevent the original from running and replace it with a client-side dynamic request. A site search integration is no different from any other client-side code, and the skeleton that we described previously on the [Page Modifiers documentation page](../../dashboard/menu/pagemodifiers/javascripteditor.html) is a safe starting point:

``` javascript
(function (){

  "use strict";

  $(document).ready(overrideSearch);

  function overrideSearch () {
    ...
  }

})();
```

We use jQuery's `$(document).ready()` to wait until the DOM is ready to be manipulated. The IIFE wrapper isolates our modifier from the global namespace, and we never leave the house without `use strict`.

(We could define a callback on `document.onreadystatechange`, but this approach suffers from potential problems: we'd be setting our modifier on a publicly accessible property of `document`, exposing us to the possibility that some other script might inadvertently redefine it (or we could be the ones doing the redefining).

We would also end up having to pool different page modifiers in one function definition, which goes against the principle of separation of concerns. For these and similar reasons, vanilla JavaScript's `document.addEventListener`s or jQuery are a better fit.)

With basic scaffolding in place, we move on to the nitty-gritty of search. The integration needs to do three things:

1. override search elements on the page
2. send search request based on user input and handle response
3. build the results page based on the response

We take each of these responsibilities in turn to see how they can be implemented.

### Overriding Elements

Having prepared this basic scaffolding, we consider the contents of `overrideSearch()`. We would like to attach our event handlers to all search-related elements:

``` javascript
function overrideSearch () {
  $("#form").on("keydown", overrideInput);
  $("#button").on("click", overrideClick);
}
```

Next, we implement the callbacks. For the input field, we  ensure that the user is not disturbed by the modifier needlessly, which only steps in if the Return key is pressed:


``` javascript
function overrideInput () {
  if (event.keyCode === 13) {
    event.preventDefault();
    sendRequest($("#input").val(), renderResult);
  }
}
```

The button is straightforward to override. The use of `this.previousSibling` is featured here as a suggested alternative to selectors.


``` javascript
function overrideClick(){
  event.preventDefault();
  sendRequest(this.previousSibling.value, renderResult);
}
```


We are done with the override part. The error message `Uncaught ReferenceError: sendRequest is not defined` should appear in the console if we try to search at this point. The default event might have been a navigation or a dynamic request of the original site's own, but we prevent it from executing and call the function `sendRequest` instead, which we'll implement next.

### Sending the Request

We assemble a `GET` request using the search term passed to `sendRequest` and send it to the Bing endpoint. For example:

``` javascript
function sendRequest (term, callback) {
  $.ajax(createRequest(term)).success(function (resp) {
    callback(resp);
  })
}
```

`createRequest` is an important part of this process, where various API-related parameters to construct and return the request are sent. Using Bing, it could look something like this:


``` javascript
function createRequest (term, offset) {
  return {
    beforeSend: function (xhr) {
      xhr.setRequestHeader("Ocp-Apim-Subscription-Key", config.API_KEY);
    },
    error: function (xhr, error, thrown) {
      console.log("Error during request!");
    }
    url: config.API_URL,
    type: "get",
    data: {
      q: "site:" + config.DOMAIN + "/ " + term,
      count: 10,
      offset: offset || 1
    }
  };
};
```

`beforeSend` sets the **Ocp-Apim-Subscription-Key** header, which contains the API key to authenticate the request. We introduce Bing's **site-specific search** feature into the request by prefixing the value of the `q` property with "site:"(which works the same way as on [bing.com](https://www.bing.com)).

It is also at this point that the code should handle the publishing method you use. If you publish your project in a subdirectory of the original domain, then in addition to the "site:" prefix, you would also have to add the target-language directory prefix (e.g "/ja/" or "/de/"). If you are publishing in multiple languages, you can use the `lang` attribute of the `html` tag (the value of which is always the current locale) to make this part of your code target-language specific.

A variable called `config` was also introduced to hold search-related config parameters in one place. This variable can go to the top of the modifier:

``` javascript
var settings = {
  API_KEY: "nmtcxylkj56lkjmnnj3mg782nmvf23gz",   // example only!
  API_URL: "https://api.cognitive.microsoft.com/bing/v7.0/search",
  DOMAIN: location.host
}
```

If the API key is valid and version-compatible with the endpoint, Bing responds with a JSON to each request, details of which can be found [here](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-web-api-v7-reference#searchresponse). The `webPages.value` property of this response is particularly important, a JSON array containing the first batch of search results.

Note that `settings.DOMAIN` is set to `location.host`. Encoded in this fact is the assumption that `location.host` (the site in which the code is running) is to be used for searches and it is already indexed.

During development and testing, however, no proper search result might be available yet. For dev purposes, it can be useful to change `DOMAIN` to e.g `en.wikipedia.org` temporarily to receive proper search results. The use of a mock responses is also an option.

Search engine APIs have many features that you can provide in your implementation beyond this example, but we will not discuss all the possibilities in this tutorial.

We pass the response to the final component of our override, the DOM handler, `renderResult`. We already mentioned it in passing to the `sendRequest` calls.

### Building the Results

Astute readers will notice that there is hardly any site-specific information in the code above (practically none, except the element selectors). We'd be inclined to think that plugging a `form` and `button` selector into the functions and changing the API_KEY will get us on our way on any similar site -- and to the extent of element overrides and request handling, that might very well be the case. `renderResult`, however, does not enjoy the benefit of generality.

The DOM handler is responsible for *displaying* search results on the proxied site in a way that seamlessly integrates with the original appearance, making this part of a site search integration heavily dependent on the specific context of the website that we are dealing with.

In order to work out the imlementation for our example webpage, we turn our attention from `#search` to `#results` and research the structure of a search result item.

In the same breath, we can add the basic structure of `renderResult` right away. The bare minimum functionality is to clear the result list and add the one that was received and passed as argument.

``` javascript
function renderResult(response) {
  $("#results").empty();
  if (typeof response.webPages.value !== "undefined") {
    for (var hit in data.webPages.value)
      $("#results").append(createResultItem(data.webPages.value[r]))
  }
}
```

`createResultItem` constructs an element for a result item using information provided by Bing, but copying the element structure from the original, which has a huge benefit: existing CSS styles will apply to the search integrated results automatically. Inspecting the search results produced by the original server, we learn that a search result item looks like this:

``` html
<div class="result-item">
  <h2><a href="#">Result title</a></h2>
  <p>Result summary</p>
</div>
```

Knowing this, we can implement `createResultItem` in the following simple fashion:

``` javascript
function createResultItem (result) {
  return $("<div>").attr("class", "result-item")
    .append($("<h2>")
      .append($("<a>").attr("href", result.url).text(result.name)))
    .append($("<p>").text(result.snippet))
};
```

Among the available options for creating DOM elements (`document.createElement`, string contatenation, etc.), the jQuery-based approach is clear and concise. Many bells and whistles can be added to a DOM handler, such as a pager, for example, which would require that we handle offsets (only hinted at by `createRequest` in this tutorial) and add Previous/Next buttons, etc.

Our tutorial, however, does not extend to those details and we conclude it here.

### Notes

Some frequent, but non-essential complexity of client-side search is omitted from our example:

- offsets (a Bing-specific term) are only alluded to. Any search API will support requests for the next batch of search results for the same search query. This is usually exposed to the end user in the form of a pager that, when clicked, sends the same request but increments the `offset` by 10. Such a feature causes both `renderResult` to manage the concept of a pager and `sendRequest`/`createRequest` to have to keep tabs on tne current `offset`.

- a search field is also generally available on all pages on a site, not just the search results page.  This means that an integration needs to ensure that the user is redirected to the search results page and that query parameters are appropriately handled. Besides using the values of the input field (a user-driven query after page load), a search integration usually has to be able to extract `produkt` from `https://de.example.com/search?q=produkt` to start a default search on the search results page when it loads for the first time. This is usually not difficult, but as we've said previously, much depends on specific circumstance.

- a search integration also has to be prepared to display a "No results." search result page if the search engine returns no hits. Such natural language has to exposed in a way that can be translated using the proxy.

### Code

We repeat the code from the discussion above in its entirety. In summary, when injected into the example webpage, it will override both the search field and the button to request search results from Bing via an AJAX call and then displays those search results in-place.


``` javascript
(function (){

  "use strict";

  var config = {
    API_KEY: "nmtcxylkj56lkjmnnj3mg782nmvf23gz",   // example only!
    API_URL: "https://api.cognitive.microsoft.com/bing/v7.0/search",
    DOMAIN: location.host
  };

  $(document).ready(overrideSearch);

  // OVERRIDE
  function overrideSearch () {
    $("#form").on("keydown", overrideInput);
    $("#button").on("click", overrideInput);
  };

  function overrideInput () {
    if (event.keyCode === 13) {
      event.preventDefault();
      sendRequest($("#input").val(), renderResult);
    }
  };

  function overrideClick(){
    event.preventDefault();
    sendRequest(this.previousSibling.value, renderResult);
  };

  // REQUEST
  function sendRequest (term, callback) {
    $.ajax(createRequest(term)).success(function (resp) {
      callback(resp);
    })
  };

  function createRequest (term, offset) {
    return {
      beforeSend: function (xhr) {
        xhr.setRequestHeader("Ocp-Apim-Subscription-Key", config.API_KEY);
      },
      error: function (xhr, error, thrown) {
        console.log("Error during request!");
      },
      url: config.API_URL,
      type: "get",
      data: {
        q: "site:" + config.DOMAIN + "/ " + term,
        count: 10,
        offset: offset || 1
      }
    };
  };

  // DOM
  function renderResult(response) {
    $("#results").show().empty();
    if (typeof response.webPages.value !== "undefined") {
      for (var hit in response.webPages.value)
        $("#results").append(createResultItem(response.webPages.value[hit]))
    }
  };

  function createResultItem (result) {
    return $("<div>").attr("class", "result-item")
      .append($("<h2>")
              .append($("<a>").attr("href", result.url).text(result.name)))
      .append($("<p>").text(result.snippet))
  };

})();
```
