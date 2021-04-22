# JSON/JS/XML processing

These features used to be under Advanced settings but as they are the most important, they were moved to their own section.

The interface is split into 2 main sections: Live JSON/JS/XML Path Config and JSON path tester.

## Live JSON/JS/XML Path Config

This section allows you to edit the settings directly. However, in case of the JavaScript translation options, we recommend that you use the JSON Path tester tool instead.

### JavaScript translation options

This field contains the capture group definitions used to extract attribute-value pairs from JavaScript files selected for translation/localization. After entering the capture parameters and re-crawling the site, the proxy will display the selected JavaScript files as translatable pages in the pagelist, from where they can be selected for translation in the List View like regular pages, and any values for the selected attributes will be made available as translatable entries, which are treated identical to regular entries.

Entering “` html`” (note that the switch is separated by a space!)  after the path specification will result in the proxy applying its HTML parser to the match instead of a plaintext parser, stripping out HTML markup and only offering the actual content for translation (otherwise, should the match contain markup, the translator must take care not to alter it, or risk breaking the translated site).

If a field of the JSON being parsed contains further JSON data in a stringified form `("key": "{\\"key\\":{\\"key\\":\\"value value value\\"}}")`, the path can be passed to a recursive JSON translator by appending “` json`” to the path, then extending the path on the next line by adding “`.json.`”.

### Mark resources as translatable

Using fully qualified URL prefixes, including protocol, host, and possibly path structures, like `https://www.example.com/path/to-be-marked/`, the Proxy can enforce dictionaries over multiple resources in a single rule. This is especially useful if the site under translation contains an API (especially CREST APIs) whose responses also require translation, and each endpoint is served on a different path. In this case, entering the root of the API here will automatically capture all responses from that path without having to individually mark them as translatable from the Resources menu.


### XPath Translation

The proxy can translate XML (eXtensible Markup Language) files sent by the remote server, according to the XPath standard of specifying elements of the XML structure. Similar to JavaScript translation, entering the “` html`” switch will result in the HTML parser being applied, while no switch will parse the match as plaintext.

## JSON path tester

![JSON Path Tester](/img/dashboard2/path_tester_default_view.png)

We'll use the following JavaScript snippet in the remainder of this section. It illustrates many use cases for JS translation:

``` javascript
(function () {

  var exampleVar = "Hello World!";

  var exampleUrl = "https://www.example.com";

  var exampleHtmlString = "<p>Hello World!</p>";

  var exampleObject = {
    "sentence01": "Hello World!",
    "sentence02": "Hello Again!",
    "nestedObject": {
      "sentence03": "Hello World!",
      "sentence04": "Hello Again!"
    },
    "exampleArray": [{ "value": "foo" },
                     { "value": "bar" },
                     { "value": "baz" }],
    "exampleNestedJS": "var nestedVar = { nestedKey: \"Nested sentence\"}",
    "exampleNestedHTMLinJS": "var nestedHTML = \"<p>Hello world!</p>\""
  };
})();
```

You can copy & paste code into the source code field or if you have the URL you can fetch the entire file via the + button on the bottom right. If the file is minified, you can use the Format code button for better readability. When you click on Analyze code, the file/text will be requested/sent for analysis in the cloud. Once it's finished, you get a highlighted representation of the same code in the Analyzed code tab.

Click on any of the blue + icons to generate a **JS path** for the string in question. They will be added to the Temporary paths field. If you generate paths for all available strings in the example , and add a few processing modes, the list of paths in the upper text field should look like this:

```
"%"."exampleVar"
"%"."exampleUrl" url
"%"."exampleHtmlString" html
"%"."exampleObject"."sentence01"
"%"."exampleObject"."sentence02"
"%"."exampleObject"."nestedObject".*
"%"."exampleObject"."nestedObject"."sentence04".! skip
"%"."exampleObject"."exampleArray".0."value"
"%"."exampleObject"."exampleArray".1."value" skip
"%"."exampleObject"."exampleArray".2."value"
"%"."exampleObject"."exampleNestedJS" javascript
"%"."exampleObject"."exampleNestedHTMLinJS"
```

Some of these paths require adjustment before they'll behave correctly.

Supported strings are highlighted in **red**, and those that are already covered by a listed JS path are be highlighted **green**. Your results should look

![Path results](/img/dashboard2/path_tester_results.png)

When you have all the JS paths you need, click Save paths (Replace live config, if there are existing paths) or Add paths to live config. Unless you know for sure that you don't need the previous live config, we recommend that you simply add the new paths.

### Keys / Variables

Translatable elements are specified by a dot-separated list of words, each optionally double quoted and constituting either a.) a valid JS variable/JSON key name or b.) a token specifying one or more hierarchical levels (anonymous function, array index or globbing mark).

```
var exampleVar = "Hello World!";
```
The simplest possible case would be `"exampleVar"` to mark the value of the top-level element `exampleVar` as translatable. Anonymous function calls are denoted with `"%"`, and since the entire block of variables is wrapped by an anonymous function `(function () { ... })()`, this leading percent sign shows up in each case. Paths for dynamic JSON responses should be prefixed with `"json"`.

### Globs

Use an asterisk (or Kleene-star) to collapse a single hierarchical level. E.g., the value of`"exampleArray"` is an array of objects. To include every index in the array, you can roll three rules into one:

```
"%"."exampleObject"."exampleArray".*."value"
```

Double asterisks are even more inclusive: they recursively glob all child nodes. Exact specification can be restarted by following `**` with a double-quoted form. That is, the rule

```
`%`.**."value"
```
marks any variable or property called `value` it finds *at any hierarchical level* within an anonymous function call. If a JS path *ends* with the `**`, then the entire subtree is marked as translatable. Incautious use of this construct is not recommended.

### Processing Modes

Nodes are processed as plain text by default, but you can enable specific processing modes with whitespace-separated postfixes. The available processing modes are `url`, `html` and `javascript`.

#### URL

Variables can contain either *the project URL* or some other important location (such as that of a *linked project*) that you would prefer to have **remapped** over the proxy. Don't give in to the temptation to localize URLs in JS as plain text! Instead, use the `url` postfix to map them:

```
"%"."exampleUrl" url
```

#### HTML

`exampleHtmlString` demonstrates the fact that JS variables frequently hold markup (for better or for worse). The `html` postfix lets you process these strings as HTML.

```
"%"."exampleHtmlString" html[@process]
```

![Extraction with and without HTML-processing](/img/workbench/js_entry_wo_markup_comparison.png)

The screenshot above demonstrates the difference HTML-processing makes. Picking up HTML-markup explicitly as text is generally considered error-prone and disadvantageous from a localization viewpoint, and isn't recommended.

`[@process]` is optional. By adding it, you instruct the proxy to apply the translation-invariable regular expressions currently set on the project.

#### Nested Javascript

Although JS paths are mostly specified in a single line, the `javascript` postfix bends this rule. It tells the proxy to apply the rule in the *next line* to the value of the postfixed JSON path. One level of nesting is supported. It is rarely needed, but invaluable when it is called for.

Plain text:

```
"%"."exampleObject"."exampleNestedJS" javascript
"%"."exampleObject"."exampleNestedJS"."nestedVar"."nestedKey"
```

HTML:

```
"%"."exampleObject"."exampleNestedHTMLinJS" javascript
"%"."exampleObject"."exampleNestedHTMLinJS"."nestedHTML" html
```
**Note:** The JSON Path tester tool is **not equipped** to display the nested use case.

#### Skip

Use this processing mode to mark child node not to be translated. **Order is important!**
If you use `*` or `**` to select child nodes to be translated, you can use the `! skip` processing mode to select a child element as non-translatable, but please note, that skip rules must come after the generic `*` rule. Skip is the lowest level mode, but you can increase the priority by adding `!` or `!{number}`. The `!` switch is not only for skip rules, any rule can be appended to increase its priority above other matching rules.
You can also comment out elements by adding `#` at the start of a line. In this case the parser won't process the given rule at all.

```
#"%"."exampleUrl" url
"%"."exampleObject"."nestedObject".*
"%"."exampleObject"."nestedObject"."sentence04".! skip
"%"."exampleObject"."exampleArray".1."value" skip
```
