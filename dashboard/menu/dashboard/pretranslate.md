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

Auto pre-translate is self-explanatory in that it is the
automatization of pre-translation: you can set up the project to
automatically execute a pre-translate process for any new content that
is found - you can hook it up with your TMs, or Machine Translation
services.

Easyling can automatically pre-translate incoming content without user
intervention or oversight, feeding its translation engine from saved
translations (from Translation Memories) above a certain confidence
level or using configured machine translation engines (supported are
Google Translate, Bing Translate, iTranslate4EU, and GeoFluent). If
new content is encountered, and at least one source is configured, a
user-configurable timer starts counting down. Content is collected
during this timer, and once zero is reached, translation begins from
the configured sources. 

Any content that cannot be translated (no matches of acceptable
confidence are found in the TM or the MT-engine returns no
translation) is packaged into a Work package that you can have sent as
XLIFF files to external systems, such as XTM, XTRF, or your Dropbox
account. There are links at the bottom of the dialog you can use to
visit the settins screens of these accounts.

