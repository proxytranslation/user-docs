# Automatic pre-translation

The proxy can automatically pre-translate incoming content without user intervention or oversight, feeding its translation engine from saved translations (from the translation proxy Translation Memory) above a certain confidence level or using configured machine translation engines (OpenAI, Google Translate, DeepL, SYSTRAN Translate and GeoFluent currently).

If new content is encountered, and at least one source is configured, a user-configurable timer starts counting down. Content is collected during this timer, and automatically translated using the configured sources. At the end of the configured window, any content that cannot be translated with the assigned sources (no matches of the desired confidence are found in the TM or the MT-engine returns no translation) is packaged into an auto-generated Work Package and exported into an XLIFF file (being pushed directly to an external TMS or a Dropbox account, if an integration is configured). The resulting export can then be translated in any external system and imported back normally.

![Automation possibilities](/img/dashboard2/apt_dialog.png)
