# Origin Snapshots

Origin Snapshots are your first line of defence against bleedthrough: it is a way of storing and reusing content that was received and picked up from the remote server (in other words, the source site). The goal of Origin Snapshots is to create a controlled snapshot of the source content that you can safely use to translate and serve content over the proxy. 

You might want to set up an Origin Snapshot for publishing content and another to be used during translation. The content of the Snapshot being published should be highly translated, and new content should be collected in a different Snapshot to be used in Preview mode and during translation. 

## Benefits of Origin Snapshots

- If you have at least one Origin Snapshot built and enabled, you have essentially decoupled new content from what you are serving over the proxy (you are in control of untranslated content). 
  
  **Note:** Origin Snapshots can only be built by Scans. They will never pick up new content unless you expressly run a Content Extraction to update them.
  
  _See [Case Study #1](casestudies.html#case-study-1-freeze-site-before-translation-begins) for an in-depth coverage of this scenario._
  
- Multiple Origin Snapshots let you decouple published content from untranslated material – you are free to update any Origin Snapshots you are not currently using for published content over the proxy. This way, you are always serving 100% translated content (using the Snapshot that is highly translated), and you can schedule for translation updates (on all the others you are free to update anytime with a Scan). 
  
  _See [Case Study #2](casestudies.html##case-study-2-decoupling-content-update-from-ingestion-and-publishing) for an in-depth coverage of this scenario._

## When to build?

The best time to build an Origin Snapshot for the first time is during the first Content Extraction (Scan). By this time, you should have used Discovery a couple of times to gain a general understanding of the site structure and word count, and you have all necessary exclusion rules set up. 

When you are confident in your Content Settings, set up an Origin Snapshot before you run a Content Scan (see below for setup directions) on the webpage and build it. This way, you will have an Origin Snapshot that contains all content you’re basing your quote on. 

## Setting up an Origin Snapshot

You can create and enable a new Origin Snapshot by checking **Enabled** in the Snapshot menu in the Dashboard 2.0. Note that at this point, the Snapshot is enabled but **unbuilt**. 

**WARNING!**: You have to build the Origin Snapshot before it becomes functional! 

## Building the Origin Snapshot

After enabling the Origin Snapshot, you need to Scan for content to build it. In step 4 (Fine-tune) of the Crawl Wizard some options become available:

![Build Snapshot Screen](/img/dashboard/scan_dialog_cache_settings.png)

Select the Snapshot you want to build and choose one of the 3 options. By choosing to reuse existing pages, you instruct the Crawler to skip the ones that are already in the Snapshot you chose and thus reduce the building cost. The choice whether or not add new pages gives you the possibility to simply ignore the new pages that were added to the source site. Selecting not to add them (the second option) allows you to build a snapshot that has the pages updated but no new ones added. This option is useful if you made changes to the JSON Paths and as a consequence need to rebuild the Snapshot. As a result of building the Snapshot, all content that was set to be picked up by the Content Scan is added to the current Snapshot.

### Custom settings

If you have multiple Origin Snapshots that you’ve built throughout multiple Content Scans, you can visit the Snapshot menu again and configure which Origin Snapshot should be used for which proxy mode, as shown in the screenshot below: 

![Custom Origin Snapshot Settings](/img/dashboard/custom_source_caches.png)

Choose a highly translated Origin Snapshot for publishing, so that you can be sure that visitors to the proxied site will not experience bleedthrough. 

Meanwhile, you can use other, more up-to-date Snapshots for the preview/live test etc. proxy modes to work on the translations of new content. 

Your Origin Snapshot setup is complete. 
