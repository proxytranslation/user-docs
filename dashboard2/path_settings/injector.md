# Inject JavaScript or CSS

You can provide JavaScript or CSS code to change the default appearance and/or behaviour of the translated pages. The code will be included in the HEAD section of each and every tranlslated page for the prefix or URL

There are 4 options:

- JavaScript content injection: enter the code you want to inject

- JavaScript link injection: enter a link pointing to the code

- CSS content injection: enter the CSS rules that you want to inject

- CSS link injection: enter a link pointing to yhe stylesheet
 
 Note that the links you inject must be present on the project domain. In layman's terms, this means that if your project is created on `example.com`, you can't inject `notexample.com/cool-styles.css`. You can circumvent this restriction by creating a Content override and inject it as a link.