# Left-Right conversion

It depends on the site...

1. Best case scenario:

```
html {
    direction:rtl;
}
```


```
<html dir="rtl"> 
```


If it looks mostly OK, then all is left just some minor CSS fixes:
- flipping images (in carousel / slider)
- list elements' bullet is defined using a background image
- If text's align is defined explicitly (e.g. using WP's text editor) inline, then each and every element must be overridden using `!important`

2. Bootstrap and framework alike:
- some framework might provide a dedicated RTL css file [bootstrap-rtl.css](https://cdnjs.cloudflare.com/ajax/libs/bootstrap-rtl/3.2.0-rc2/css/bootstrap-rtl.css)


3. If this is not case, each and every element must be positioned individually


## Mixed content within text
- When it comes to actually render the text (numbers), the direction is determined by a couple of rules. Please read [this](http://dotancohen.com/howto/rtl_right_to_left.html) for the details.
- ***As a rule of thumb: during the translation (from LTR language to RTL), don't change the order of the numbers and text where the translation is with latin characters, in the CAT tool. Phone numbers like 1-800-123-1234 should be left in this order.***
- To make sure numbers are rendered properly at the end, a Left-to-Right (LRM) must be inserted before every number. The dash between numbers split them, so LRM must be inserted after them again. [Click to read more on how to insert these LRM characters](http://dotancohen.com/howto/rtl_right_to_left.html#InsertingNonprintingCharactersIntoText).
- The same holds for parenthesis, etc. Make sure you understand the rules; sometime LRM must be inserted _after_ the closing parenthesis

```
<p style="direction: rtl;">
<span>(TTY/TDD) 711 </span>
</p>
```

```
<p style="direction: rtl;">
<span>&lrm;(TTY/TDD) 711</span>
</p>
```

```
<p style="direction: rtl;">
<span>&#8234;(TTY/TDD) 711&#8236;</span>
</p>
```



- As an alternative, LRE character can be inserted _before_ the sequence, terminated by a PDF mark.
- To edit the XML (XLIFF) directly, use [Sublime](http://www.sublimetext.com/), available on Windows, OS X and Linux as well. It works very well with Regular Expressions. It's a robust way to insert these marks using their unicode symbol, such as `&#x200E;`

Further readings: 
- [http://dotancohen.com/howto/rtl_right_to_left.html](http://dotancohen.com/howto/rtl_right_to_left.html)
