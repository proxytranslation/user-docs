# Pre-translate

By using the Pre-translate menu, you can initiate a process which
supplies untranslated segments with a preliminary translation in order
to mitigate bleedthrough on the proxied pages. You can use
pre-translate with a Translation Memory or a Machine Translation API
of your choice. Easyling supports Google Translate, iTranslate4eu,
Bing Translate and GeoFluent.

In order to use Machine Translation, you need to go into your Account
and set up your MT account Ids/authorization keys in the "Machine
Translation" menu.

## Auto pre-translate

Automatize pre-translation: you can set up the project to
automatically execute a pre-translate process for any new content that
is found - you can hook it up with your TMs, or any Machine
Translation services you subscribed to.

Pre-translation of incoming content can be done without user
intervention or oversight. If new content is encountered, and at least
one source is configured, a user-configurable timer starts counting
down. Content is collected while this timer is running, and once it
reaches zero, translation begins from the configured sources.

Content that cannot be translated (if no matches of acceptable
confidence level were found in the TM or if the MT-engine returned no
translation) is packaged into a Work package that you can have sent as
XLIFF files to external systems, such as XTM, XTRF, or your Dropbox
account. There are links at the bottom of the dialog you can use to
visit the settins screens where you can set up these accounts.

