# Project maintenance##

The translation project of a website is a continuos task, as new content is regularly added to the site. So  uploading the initial translation is not the end of the project, but the beginning of a new phase. This phase is practically a repetitive cycle of the following activities:  

- checking the site for new content  
- extracting new content for translation  
- translation of the new content  
- uploading the new translation  
- and, of course, error fixing, if needed  


### Automation possibilities
The first two activities can be set to be carried out automatically at daily, weekly or monthly intervals, depending on how frequently content is updated on the website. This is called **scheduled crawl**.<br> If you turn on this feature, changes will be checked and retrieved for translation at the specified intervals, and e-mail notification will be sent to all project participants. The new content is available right away for translation in the online editor interface, and you can also download an XLIFF for translation.<br>
**Please note that this check is technically content extraction, so it has an associated cost of EUR 2 per 1000 words.**  

You can enable this option in **Content > Settings > Look for changes**. (Of course, you can set it to **Only manually**, if the site does not update frequently.)  

![Scheduled Scan](/img/scheduledScan.png)  

The process can automatically extract new content, apply the associated translation memories and machine translation services, prepare a work package and the XLIFF export. This is particularly useful for fast-moving sites where content arrives quickly and time spent untranslated needs to be minimized (possibly at the expense of real-time human oversight).  

**Automatic pre-translation**<br>
Easyling can automatically pre-translate incoming content without user intervention or oversight, feeding its translation engine from saved translations (from an Easyling Translation Memory) above a certain confidence level or using configured machine translation engines (Google Translate, Bing Translate, iTranslate4EU, and GeoFluent, currently).
If new content is encountered, and at least one source is configured, a user-configurable timer starts counting down. Content is collected during this timer, and once zero is reached, translation begins from the configured sources. Any content that cannot be translated with the assigned sources (no matches of the desired confidence are found in the TM or the MT-engine returns no translation) is packaged into an auto-generated Work Package and exported into an XLIFF file (being pushed directly to XTM, if an integration is configured). The resulting export can then be translated in any external system and imported back normally.
