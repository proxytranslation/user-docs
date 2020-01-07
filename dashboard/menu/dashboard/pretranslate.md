# Pre-translate

By using the Pre-translate menu, you can initiate a process which supplies untranslated segments with a preliminary translation in order to mitigate bleedthrough on the proxied pages. You can use pre-translate with a Translation Memory as well as any of the supported Machine Translation APIs.

In order to use Machine Translation, you need at least one API configured for your project. You can access configuration for available Machine Translators by clicking (configure) next to the desired Trasnlator, or by selecting them on in the menu bar.

## Auto pre-translate

Automatize pre-translation: you can set up the project to automatically execute a pre-translate process for any new content that is found - you can hook it up with your TMs, or any Machine Translation services you subscribed to.

Pre-translation of incoming content can be done without user intervention or oversight. If new content is encountered, and at least one source is configured, a user-configurable timer starts counting down. Content is collected while this timer is running, and once it reaches zero, translation begins from the configured sources.

Content that cannot be translated (if no matches of acceptable confidence level were found in the TM or if the MT-engine returned no translation) gets packaged into a Work package that you can have sent as XLIFF files to external systems, such as XTM, XTRF, or your Dropbox account.

