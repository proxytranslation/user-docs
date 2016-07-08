# Caches


[[Screenshot of the Easyling Caching model]]

By default, Easyling sends all requests to the remote server and lets
through any and all new content it finds during the process (in case
of a Preview or a Scan). Normally, when the source of the proxied site
is unlikely to undergo significant changes, this shouldn't be a
problem.

However, if the page has dynamic content or is likely to be updated
frequently, then precious translated content might get replaced by
incoming new content on the proxy, leading to lowered translation
ratio and a spotty translation quality. We call the sudden appearance
of untranslated content on the proxy **bleedthrough**. Such a state of
affairs seldom satisfies the owner of the site, and of course there is
always the issue of control - you want content to ride shotgun, while
you take the wheel yourself.

It also often happens that some projects require frequent/careful
maintenance. Perhaps you'd like to separate (_decouple_) content that
you want to serve through the proxy from the content you want to see
in your Workbench. For example, you would probably prefer untranslated
text to be waiting for you on the Workbench, but not served on the
proxy until the its translation is ready.

Enter **Multi-Caching**.

## Multi-Caching

Easyling supports two kinds of caches: **Source Caches** and **Target
Caches**. The term _Multi-Caching_ refers to the fact that Easyling
users can create and maintain multiple caches for both types.

##### WARNING: Source Caches and Target Caches are entirely different entities, they are NOT shared resources in any sense!

Currently, the maximum allowed number for a given type of Cache is
**5**. That is, you can have a maximum of 5 Source Caches and 5 Target
Caches for any given project.

Let us first take a look at what Source Caches do.

## Source Cache (SC)

SCs are your first line of defense against bleedthrough: it is a way
of storing and reusing content that was received and picked up from
the **remote server** (in other words, the **source site**). The goal
of Source Caches is to create a _controlled snapshot_ of the source
content that you can safely use to translate and serve content over
the proxy.

You might want to set up one Source Cache for publishing content and
another to be used during translation. The content of the Source Cache
being published should be highly translated, and new content should be
collected in a different Source Cache to be used in Preview mode and
during translation.

### Benefits of Source Caches

- If you have at least one Source Cache enabled and built, you have
  essentially decoupled new content from what you are serving over the
  proxy (you are in control of untranslated content). 
  
  **Note:** Source Caches can only be built by Scans. They will
  never pick up new content unless you expressly run a Content
  Extraction to update them.
  
  _See Case Study #1 for an in-depth coverage of this scenario._
  
- Multiple Source Caches let you decouple published content from
  untranslated material - you are free to update any Source Caches you
  are not currently using for published content over the proxy. This
  way, you are always serving 100% translated content (using the Cache
  that is highly translated), and you can schedule for translation
  updates (on all the others you are free to update anytime with a
  Scan).
  
  _See Case Study #2 for an in-depth coverage of this scenario._

### When to build?

The best time to build a Source Cache for the first time is during the
first Content Extraction. By this time, you should have used Discovery
a couple of times to gain a general understanding of the site
structure and word count, and you have all necessary exclusion rules
set up.

When you are confident in your Content Settings, set up a Source Cache
before you run Content Scan (see below for setup directions) on the
webpage and build it. This way, you will have a Source Cache that
contains all content you're basing your quote on.

### Setting up a Source Cache

You can enable and create a new Source Cache by checking **Enabled**
in the _Page cache_ menu in the Dashboard. Note that at this point,
the SC is enabled but **unbuilt**.

##### WARNING: You have to build the Source Cache before it becomes functional!

### Building the SC

After enabling the Source Cache, you need to Scan for content to build
it. In the Content Scan Dialog, some options become available:

[[Image of Scan Dialog]]

Check **Build source cache** and run the Scan. As a result of building
the SC, all content that was set to be picked up by the Content Scan
is added to the current SC. 

If you are updating a SC, you can use the dropdown menu to select the
cache you'd like to overwrite.

The '**Preserve & use existing source cache**' option ensures that a
SC will not be written to during a Scan. Having both '**Build source
cache**' and '**Preserve & use existing source cache**' enabled for a
Scan will currently result in an inconsequential action.

#### Custom settings

If you have more than one Source Caches that you've built throughout
multiple Content Scans, you can visit the Page Cache menu again and
configure which Source Cache should be used for which proxy mode, as
shown in the screenshot below:

[[ custom settings screenshot ]]

Choose a highly translated Source Cache for publishing, so that you
can be sure that visitors to the proxied site will not experience
bleedthrough.

Meanwhile, you can use other, more up-to-date Source Caches for the
preview/live test etc. proxy modes to work on the translations of new
content.

Your Source Cache setup is complete.

## Target Cache (TC)

### What is it for?

The purpose of the Target Cache is to reduce the number of requests to
the **source site** and decrease response times on the proxy by
skipping the content replacement process (which is basically the
entire document pipeline) if the content on the **source site** or -
if enabled - in the Source Cache remains _unchanged_.

### Enabling Target Cache

Go into the **Page Cache** menu in the Dashboard and enable Target
Cache in the dialog that open. You can also add a maximum of **5**
custom-named Target Caches.

### Building the Target Cache

After you enable it, the Target Cache is filled exclusively by Page
visits on the pretty (published) domain. Previews/visits to the
temporary domain will have absolutely no bearing on the contents of
the Target Cache.

While separate from the Source Cache, the contents of the Target Cache
will nevertheless be determined by your Source Cache settings. If you
have no Source Cache, then the Target Cache will be filled by whatever
is returned from the source site for a request (a page visit). If you
have a Source Cache, then the Target Cache will contain whatever the
currently enabled Source Cache is making available to the visitor on
the proxy.

### The 'Keep Cache Strategy'
