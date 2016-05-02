# Publishing issues

### Translated page doesn't show up  

**Issue:**<br>
**I've just uploaded the translation of some new pages, but they don't show up on the translated site / they still appear in the source language.**

**Fixing:**<br>
You experience this problem because Target cache is enabled, and you need to clear the Cache to update content to be served.
The very reason for using a Target cache is to mask unfinished translation and avoid bleed-through. The Target cache shows the last fully translated version of the pages - so if content changes on the original page, it remains hidden on the translated site until a fully translated version is available.  
To fix the issue you need to explicitly delete the page from the Cache, so that the updated content could be loaded in upon the very first viewing of the page.  
If you have several languages, it might be more convenient to clear the entire Target cache by clicking the Trash icon.  


### Translated page is not listed in Google search results

**Issue:**<br>
**The pages served from the Proxy are not listed in Google search results.**

**Fixing:**<br>
Google has never indexed the site in the first place, most likely due to the fact that there are no "hreflang" links on any of the pages, so the Googlebot has no idea there are other pages to look for. More information on the element and how it affects Google rankings may be found at [https://support.google.com/webmasters/answer/189077?hl=en](https://support.google.com/webmasters/answer/189077?hl=en)

Additionally, creating and submitting a sitemap (more information at [https://support.google.com/webmasters/answer/2620865](https://support.google.com/webmasters/answer/2620865)) to Google in order to force an indexing of the pages can also help. Even so, without the hreflang attributes, it may mean that some penalty is applied to the rankings, due to perceived duplicate content.