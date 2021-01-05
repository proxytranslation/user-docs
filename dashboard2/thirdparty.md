# Third party integrations

The proxy can integrate with quite a few third party services. The integration can simplify your translation workflow or the management of the source and target files.

These services can be configured either in the Dashboard 2.0 for the project or in the Account settings page. By default, the project level credentials are used with the account level as fallback. You can prevent the fallback using the "Disable fallback to account level credentials" checkbox.

Note that the cost of these services isn't included in the proxy fee.

## GeoFluent

[GeoFluent](https://developers.lionbridge.com/geofluent/index.html) is a machine translation engine that enables real-time translation of text (or audio). It can also detect the language of the source text. This can be especially useful when the source site is pre-localised and you need to ensure that you only pick up content in the source language.

To enable it, you'll need to have your Account key and secret as well as the endpoint that the proxy must call.

## Google Translate

I doubt [Google Translate](https://en.wikipedia.org/wiki/Google_Translate) needs much of an introduction. Both the traditional dictionary-based and the new neural translation modes are supported as well as source language detection. You can read more in [Google's Official Documentation](https://cloud.google.com/translate/)

To set it up, you must generate an API key in Google Cloud Platform ensuring that the "Accept requests from these server IP addresses" field is empty. Then, you can enter your key and enable Google Translate for your project.


## SYSTRAN Translate

Aside from high-quality translations enabled by its industry-specific translation models [SYSTRAN translate](https://translate.systran.net/translationTools/text) also supports the usual machine translator features such as source language detection.

It can be enabled by entering your API key. The default endpoint, `https://api-translate.systran.net/`, can also be overridden should you need to do so.

## Microsoft Translator

Successor of the Bing Translation API, the [Microsoft Translator API](https://www.microsoft.com/en-us/translator//) can be used for manual or automatic pre-translation, source language detection as well as suggestions on the Workbench. 

To enable, simply enter your Subscription key.

## Dropbox

The Proxy is capable of installing a Dropbox connector in your account, that allows it to export into and import from a specific folder in the account. The proxy root folder needs to be specified once, during account linking, after which the proxy will create new folders within based on the project code as needed.

During export, the option to submit to Dropbox will place the exported ZIP file into the `export` folder of the given project, allowing you to download and handle the file rapidly. After processing, the contents of this folder can be deleted freely.

The `import` folder is used to re-import translated content into the database. Once a file is placed in this folder, the project owner receives an email notification of the fact. From the Import dialog, they can then choose which files they want imported, which are then imported directly from Dropbox. By default, on switching to the Dropbox tab in the import dialog, only files added *after* the last import will be selected, making distinction easy.

To add a new account, click "Select Dropbox account". You can then select an account that you added to any other project or you can log in with a valid Dropbox account and authorize the Translation Proxy Dropbox app to access your storage. 

## XTM

The proxy can export content in XLIFF format into XTM, creating projects as necessary, and listen for workflow completions to commence import. XTM has also integrated the preview functionality, allowing live verification of translations.

After configuring XTM access under the Account screen, submitting to XTM as an external system becomes available at export-time, or from the Previous Exports dialog. Upon submission, the proxy creates the relevant project within XTM and imports the XLIFF into the project. Afterwards, a listening service starts, periodically polling XTM for the workflow state of the project. When the project is set to completed, the proxy detects this during its next polling cycle, and imports the translated XLIFF back into the proxy project.

XTM has also integrated the proxy preview. Using information in the exported XLIFF, XTM's online interface can display the translated page, allowing in-context verification of the translations.

**Nota Bene**: the live-updating preview does **not** mean that translations are streamed to the proxy for inclusion! You will still need to save the XLIFF file and import it (either manually or by completing the XTM project) to return the translations to the project!

## XTRF

Similarly to Dropbox and XTM, the proxy can export content to XTRF. The workflow is very similar to XTM.

## MemoQWeb

The proxy can also export content to a MemoQWeb instance and retrive the translations. Additionally, when you open an XLIFF file from the proxy in MemoQ, you can see a live preview using the MemoQ plugin.

**Nota Bene**: the live-updating preview does **not** mean that translations are streamed to the proxy for inclusion! You will still need to save the XLIFF file and import it (either manually or through MemoQWeb) to return the translations to the project!