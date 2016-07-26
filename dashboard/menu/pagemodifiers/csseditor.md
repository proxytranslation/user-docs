# CSS editor

The proxy can be used to insert locale-specific CSS rules into the site being served. The rules are inserted as the last element of the head on every page served through the proxy. A very common use case for this feature is RTL conversion of a website: almost always necessary when one of the target languages is Arabic.

There are a couple of caveats:

It is good practice to make each CSS rule language specific:

```css
html[lang="de-DE"] ul.one-selector li a {
  float: left; 
}

html[lang="fr-FR"] .another-selector h2 {
  height: auto;
}
```

If you omit the `html[lang="fr-FR"]`, the CSS rule will be applied in all target languages, which might not be the behavior you expect.
