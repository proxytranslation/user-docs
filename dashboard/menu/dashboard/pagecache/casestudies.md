# Case Studies

## Case Study 1: Freeze Site Before Translation begins

In this example, the client has declined to use a staging server, as well as declining to halt content updates for the duration of the initial translation. They do, however, insist that bleedthrough must not occur at any point in the translation process. This results in a continuously changing source that makes it nearly impossible to achieve 100% translation.

In this case, the solution is to enable the Source cache, and populate it with a Scan before the first round of translation commences. This creates what is effectively a static snapshot of the site, which remains the same regardless of the updates the client makes in the meantime, providing a stable environment for the translation and review processes.

By using a Source cache to serve the translated sites, they are decoupled from the original, and content updates there will not be reflected in the translations.

However, source content will accumulate in the meantime, and once the cache is purged, bleedthrough will occur! To counter this, the second scenario can be enacted.

## Case Study 2: Decoupling Content Update from Ingestion and Publishing

For this example, the client has declined to use a staging server to allow you to ingest the content ahead of publishing for translation. They did, however, agree to notify you once new content is published, and have acknowledged that this will cause the translated sites to lag behind the original until the translations (and possibly reviews) are completed.  Alternatively, coupling into the previous scenario, the initial translations are in place, but the source site has moved ahead in the meantime, with the translated site being served by the initial Source cache.

Once the initial translations are completed, the caches are set up according to the image below:

![Sample Cache configuration](/img/dashboard/custom_source_caches.png )

By driving the published site from a separate cache entity, you gain the ability to decouple the content ingestion cycle from the translation and update cycles.

From this point on, the published site will not reflect any updates until the assigned entity is refreshed. By specifying the update cache in the Scan Limit dialog, you write the server responses into the newly created cache, which will drive the Preview and Highlight modes, allowing you to conduct the translations and ICR using the new content. Once the client signs off on the translations, you simply switch the Source cache entities being used (and purge the Target cache, if in use).

<caption id="attachment_2645" align="aligncenter" width="654"> Once translations and reviews are completed, simply re-assign the cache entities to promote the new content to the translated "Production"</caption>

At this point, the previously-live cache entity is freed up for purging and re-building in the next update cycle. Thus, at the next crawl, the default would be selected to receive the updates, leaving the other entity untouched.

By managing which entity is being used to serve the published site and which one is being written to, it becomes possible to replicate the behavior of the staging server, albeit at the cost of increased attention to detail.
