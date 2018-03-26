# Site Search

Transparent multilingual search is a frequently required (though often belatedly acknowledged) part of website translation. We recommend a client-side approach to search (the approach to which the proxy translation model lends itself best), a comparatively involved use case of code injection. Given its pervasiveness and importance, it warrants detailed treatment in our documentation. 

**Part I** of this recipe provides the general description of site search over the proxy and the reasoning behind our most familiar approach. **Part II** details one such integration in specific terms (for a hypothetical site). This latter section may serve as an in-depth **page modifier tutorial** as well.

## Part I - General

### The Problem

Visitors will assume that if they can access a website in a given language, they will be able to feed queries in that langauge into search fields and receive appropriate results.

Let's say that a visitor uses the search field of `www.example.com` to search for the word "**product**". Upon pressing enter, they are navigated to `https://www.example.com/search?q=product`. The server uses the value of the `q` parameter and runs whatever server-side search mechanism it uses to search for the term, assemble a list of results and construct a result page to respond with.

On a proxied site, requests are automatically relayed to the original server. If a visitor were to type "**produkt**" on the German domain (resulting in an URL navigation to `https://de.example.com/search?q=produkt`), that is the same as relaying a search query with German language content to the original site. Not possessing a _German language index_, the response is almost certain to return 0 results.

The fact that the proxy is quite CMS-agnostic and generally doesn't require that translated content be shared with the original site's backend also means that translated content will not be available to the indexing/search software that is running there.

### Solution

The original site might not be storing the translations, but the proxied pages themselves are  _publicly available & indexable_. _Search vendors_ can be relied on to provide localized search capability via client-side JavaScript.

(to-be-written)

### Third-party Integrations

#### Bing

## Part II: Example

Description of an integration

### Page Modifiers

How integration works

### Search result page

The specific page where search results are usually displayed, and why it is important.

### Overrides

How to override input fields and elements.

### Request

How search results are received.

### DOM

How to add the result to the DOM.

### Indexing

How to get the vendor to index.
