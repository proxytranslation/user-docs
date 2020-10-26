# Extractor

## Overview
In some cases, the remote server response deviates severly from the industry standards, but still requires translation. In order to handle these, the proxy has to slice up the incoming stream to extract the relevant contents, then restore the original after processing. This is achieved by using regular expressions to designate patterns requiring handling within unprocessable strings.

> All regular expressions are _Java Patterns_. See the [official documentation](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html) for the finer points.

## Parameters
+ _Content-type pattern_: a regular expression that designates `content-type`s susceptible to the extractor operation.
+ _Check first regexp_: a regular expression that is applied to the _incoming content_ to see if it should be extracted.
+ _Extractor pattern_: a regular expression that locates and extracts content from the incoming string. _Must_ contain at least one capture group!
+ _Content prefix_: an _optional_ prefix that is prepended to the extracted string before handling. Will be stripped before content is re-inserted into the original!
+ _Content suffix_: an _optional_ suffix that is appended to the extracted string before handling. Will be stripped before content is re-inserted into the original!

Note that at least one of the last 3 input fields must be filled in. 

## Example
For example, consider the following snippet being sent:

```
xxx#It's so beautiful!#It's not so beautiful!#xxx
```

1. First of all, the content type must be verified to avoid trying to process images and the like:  
_Content Type Pattern_: `text/.*`
2. Then the content is validated to see if starts with at least one `x`:  
_Validation Pattern_: `x+`
3. The content is targeted:  
_Extractor Pattern_: `\\#(.*?)\\#`
4. Optionally, HTML-processing may be forced using prefixes and suffixes to transform the content prior to handling:  
_Content Prefix_: `<p>`  
_Content Suffix_: `</p>`

Internally, the proxy will see the following when translating:

```
xxx# <p>It's so beautiful!</p> # <p>It's not so beautiful!</p> #xxx
```

This is then transformed:

```
xxx# <p>Es ist so schön!</p> # <p>Es ist eigentlich nicht schön!</p> #xxx
```

Finally, the original form is restored before the content is sent out:

```
xxx#Es ist so schön!#Es ist eigentlich nicht schön!#xxx
```
