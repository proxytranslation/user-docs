# Using the `hreflang` element

Google's CrawlerBot will eventually find your translated page if there are any links to it. However, if the content there is not marked appropriately, it will not be given the same SEO scores as your main content. In fact, it may even be treated as duplicate content, and a scoring penalty may be applied.

To prevent this from happening, you need to provide the GoogleBot with information on how the translated sites relate to the original. The easiest way to do this is the `<link rel="alternate" hreflang="" href="">` element.

These elements have to be placed in the page head (i.e. before the HTML body), and have two rules that must be satisfied in order for the GoogleBot to consider them:  
- `hreflang` elements must be reciprocal: if a link points to a translated site, the translated site must point back to the original as well.
- `hreflang` elements must be circular: each language must also refer to itself with a link.

Consider the following HTML snippet from an imaginary site at `http://example.com`:  
```
<html>
<head>
<title>Title Here</title>
<link rel="alternate" hreflang="en" href="http://example.com" />
<link rel="alternate" hreflang="jp" href="http://jp.example.com" />
</head>
[...]
```

and its translated counterpart at `http://jp.example.com`:  
```
<html lang="ja-JP">
<head>
<title>Title Here</title>
<link rel="alternate" hreflang="en" href="http://example.com" />
<link rel="alternate" hreflang="jp" href="http://jp.example.com" />
</head>
[...]
```

This snippet will provide proper SEO, since it satisfies both criteria: the references the English and the Japanese site are reciprocal (one refers to the other and vice versa) and the references are also circular (both languages also refer to themselves as well as their counterparts). This provides all the information GoogleBot needs to index each site in its rightful place and apply SEO scores across both domains.

For more information on this topic, see this article from Google:<br>
<https://support.google.com/webmasters/answer/189077?hl=en>
