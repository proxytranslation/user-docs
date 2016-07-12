## Discovery

**So, what is a Discovery?**

Before you can translate a website, you need to **extract** all
content from it using the Scan function. A Scan, however, writes to
the database, which, as you know from our pricing model, will cost you
money. In that sense, it would be risky to let loose an unlimited Scan
on a website you're not familiar with. To forego Content Extraction
and limit the crawler's actions to finding out about the structure and
word count of a given web site, a more tentative approach is needed: a
Discovery.

![Run discovery](/img/discovery.png)

The process maps the structure of the site by scanning each page for
link elements and trying to follow these links. The content of the
website is not stored, only the URL address of the visited pages,
together with their status info. Any page that is verified to exist is
marked as Discovered, and the ones that returned an error message
(most commonly redirection (HTTP301-302) and page not found (HTTP404))
are marked Unvisited in the page list. For more information on HTTP
status codes, see here. Although this process doesn't extract content,
it provides a preliminary wordcount and a repetition rate as well. It
has a cost of 1EUR per thousand pages.

**IMPORTANT!**

**If you exclude pages during discovery, changing the rules only will
not include them in the new discovery; you have to add them manually
through the "Add pages" dialog.**

Your primary choice is between limited and unlimited Discoveries.

A limited Discovery is the best way to "get to know" a website - if
you set a reasonable safety number, such as the default 100, you can
be sure the process will go overboard when it finds an enormous forum
or a structurally complicated web-shop.

Based on what a limited Discovery tells you about a site, you can set
**prefix exclusion rules** in the page list or **cherry-pick**
unnecessary pages for exclusion.

Wordpress sites, for example, tend to create links such as
"/?page=2332" for every page, and it is obvious from the get-go that
there is no real content behind these links. A limited Discovery will
inform you of their presence, so that you can exclude them at.

By increasing the page limit and running Discoveries in succession
while adjusting your inclusion/exclusion rules, you can work your way
through a site structure incrementally.

Of course, if you have a clear idea of the size of the site, you can
always set up an unlimited Discovery, wait for it to finish and set up
your exclusion rules afterwards.

![Discovery limit](/img/discovery-limit.png)

Once the discovery is ready, you will receive an e-mail notification
and the statistics will show up on the Discovery page. Based on this
you can give a rough estimation for the website translation cost -
both in time and money.

![Discovery statistics](/img/discovery-statistics.png)

### Statistics

See here for a detailed explanation of how statistics work in
Easyling.

### Discovery settings

Fine-tuning Discoveries and dispatching them on a site is the
bread-and-butter of Easyling, and arguably the most important part of
the setup-phase of a project. In this section, we take a look at the
various settings, convenience features that are at your disposal. Some
of the most important overarching settings will be displayed in the
main screen of the Discovery screen, others will be revealed by the
Discovery dialog, which opens after you click on the blue **Discover
now** button. Let's take a look at each of those.

#### Discovery Screen

**Ignore queries:** Add any query parameters to this field, separated
by commas, to ignore them during Discoveries.

By default, the following URLs will turn up in the Page List as two
separate pages:

`http://www.example.com/examplepage.html`

`http://www.example.com/examplepage.html?querystring_1=foo&querystring_2=bar`

Query strings can influence the content that will be served, but it is
also common for a page to be completely unchanged regardless of their
presence or absence. In such cases, query parameters are somwehat
bothersome: they cause the Discovery to revisit the same page multiple
times, they overcrowd the page list with unnecessary entries and
divert attention from the real page that holds the content to be
translated. It is a good idea to trim the list and exclude these
superfluous pages using this feature.

**Group pages by ignoring query parameters:** In the same vein, you
can also group pages based on ignored query parameters by adding those
query parameters to this field. Also be sure to check out the Page
grouping feature in Advanced settings.

**Discovery cookies** You may extract the cookies from a user session
and pass them to a Discovery. This feature is most useful when you
need to deal with login walls and content that is only revealed within
the context of a user session.

Note that we cannot guarantee that the cookie extraction method works
with all proprietary logins, as there are several solutions which can
use additional security measures such as IP checking, or checking the
User-Agent header. As all the requests from the proxy and the crawler
come from the Google Cloud, it is necessary for the target site to not
block them. The success of a Discovery via the use of session cookies
is highly dependent on the implementation details of a site.

**Discovery page limit:** It is usually not a very good idea to
unleash unlimited Discoveries right off the bat, not unless you have a
100% understanding of a site's structure. Granted, Discoveries don't
really cost much, so you are in no danger of incurring any serious
expenses. But a Discovery can take time - and the shorter the time
span required to create a quote with high confidence levels, the
better.

For this and other reasons, it is a good idea to start with a "feeler"
Discovery and take it from there, adjusting query string settings,
adding prefix-based exlusion rules for unnecessary subsections,
fine-tuning the settings as needed - this way, you can safely shape
the Discovery incrementally, until it visits only those pages that you
deem necessary.

**Discovery history:** By running subsequent limited Discoveries using
progressively refined settings, you will also get contextual clues
about site state by checking the Discovery History. By clicking on the
small **view history** link under the timestamp of the last Discovery,
you can avail yourself of all the statistical information revealed by
your previous Discoveries by using the "Show info" button in the
opening dialog. You can also verify the status and end state
(termination reason) of your Discovery processes here.

**Referred domains** Links pointing to a different domain than the
project website address will be treated as external referred domains
and listed here for your convenience. Note that specific instances of
external links (such as links to streamed media) can be
localized(replaced) over the proxy. See Content > External links for
further details.

#### Discovery Dialog

**Discovery limit** Repeated from the main screen, you can limit the
Discovery to a set amount of pages before exiting.

**Add & process newly found pages** any pages the Discovery process
finds during a crawl will be added to the page list. Note that this is
explicit action by the user, therefore the Page Freeze setting has no
effect in this case.

**Add & process newly found resources** Instruct the Discovery to add
newly found Resources, such as *.js files to the project. The proxy
makes collecting Resources a trifle, and there is a plethora of
in-depth methods to translate content embedded within them. But
translation of Resourecs is also known to be one of the trickiest
parts of website localization. Beware, and woe betide the unready!

**Add & process newly found image resources** By enabling this option,
image content found on the site is added to the Resources screen,
where you can add localized counterparts and instruct the proxy to
serve those in place of the original.

There is often a great deal of image content on websites, so indexing
all of them can take a very long time to finish; it is a good idea to
turn this option off the first time around, and enable it only later,
when it is clear that image localization is also going to play a part.

**Skip content type check if already determined**
(to be added)

**Limit crawl depth** There is more than one way of limiting the scope
of a Discovery. In scenarios where you have to Discover richly
interlinked pages (a wiki, for example) you can use the crawl depth to
limit how deep the Discovery should be allowed to follow links.

**Ignore pages matching the following regular expression** You can
specify any regex to apply to all URLs and ignore the given page if
there is a match. This is a user- and crawl-specific setting. As
always, we recommend that you test your regular expressions on
regex101.com before using them. In this case, you can export your page
list from Discovery > Pages and use that list as a test string for
your regex.

**Limit number of simultaneous requests** Control the number of
requests a Discovery is allowed to send to the original site
simultaneously. Use this function to prevent the Discovery from
flooding a smaller server with requests.

**Exclusion rules** You can set Discovery-specific exclusion rules by
selecting _Use temporary exclusion rules_ from the menu and adding
your prefixes to the field that opens - use the buttons on the right
to choose whether the prefix entered is an inclusion or exclusion rule.

By default (_"Use current exclusion rules"_), a Discovery will use the
exclusion rules that you've set up on the Pages list screen.

**Build Source Cache** Source Caches have to be built during Discovery
or Content Extraction crawls. This checkbox becomes available after
you have enabled Source Caches in Dashboard > Page Cache. A dropdown
menu will also appear, where you can select which of the Source Caches
you'd like to use for the current Discovery. Please see the Source
Caches section of this manual for the details. The option to keep the
current Source Cache intact (_"Preserve & use existing source cache"_)
is also available - these to options override each other, you should
turn the latter off when you're building a Source Cache.

After clicking on the blue "Discover" button, the Discovery starts and
you will be returned to the main Discovery screen, where you can
follow the word count statistics and check the status of the currently
running process.

### Pages

The Page List is accessible from both the Discovery and Content
menus. By default (before starting any Discoveries or Scans), only the
root path ("/") will be present. Later, all pages/paths added manually
or found during Discoveries and Scans will listed here.

Clicking on a pathname will take you to that URL on the original
site. If you hover your cursor over it, a menu will appear to the
right:

![Hover menu](/img/plhovermenu.png)

The first two buttons, "Translation in List View" and "Translation in
Highlight View" will take you to the workbench. To learn more about
the various editing modes, please visit the **Workbench** part of the
documentation.

**NOTE!** Most of these buttons are disabled and unclickable as long
as no target language is selected in the Language dropdown on the left
side of the Page list!

By clicking on the third button, "Preview", you will be introduced to
the preview proxy mode, which you can use to review your translation
efforts in the full context of the original website over the proxy. By
holding Ctrl and clicking on the Preview button, you will be taken to
another useful mode, the x-proxy. We'll get into these proxy modes in
detail later on in this manual (see **here** for the details).

At the top, you will see a few icons you can click to access detailed
function accessible from the page list. They are as follows:

**Copy current URL list to clipboard** will open a new dialog
containing project information and all pages in a pre-selected list.
You can copy & paste this list, or click on Export to receive an XLS
spreadsheet in an e-mail.

**Search bar** When the page list gets too long to scroll through
manually, you can use the Search Bar to look up any path names that
match your query. This is a forward-search (note that regexen are not
supported in the Page list).

### Resources

Resources are binary content, such as images, PDFs, CSS and textual
sources such JS files, etc. It is important to remember that the
content of these resources is not extracted for translation, so you
have to translate / edit them separately.

When you open this screen, a subset of all Resources collected during
a previous crawl will be listed. Scroll down to load more, or use the
search field for lookup (as some websites are quite Resource-heavy,
the search function is recommended). 

Hover and click over any Resource to display a localization dialog for
it. You can click on the green "plus" icon to mark the Resource as
translatable. After doing so, a few fields will be added to the
dialog: a source and a target language text box you can use to
transcribe the Resrouce, and a target URL field which will contain the
the URL of the localized Resource on the proxy. Use the "Choose File"
button to upload a localized Resource.

Note that you can only localize Resources _one at a time_ and on a
_strictly target language basis_ (make sure you have the appropriate
target language selected on the left side of the screen).

You can click on the flags on the lower left side of the frame to
check the localized and original versions of a Resource (especially
images, which will be displayed within the dialog). Document browsing,
however, is not supported on the Resources screen.

### External links

All external links will be collected (and all external domains will be
listed in Discovery), and sometimes, external links need to be
localized, such as when documents, data files and downloads are served
from an external domain. If you are translating www.example.com, but
it's downloads section is filled with links to files on
files.example.com, you can use this feature to replace the links to
point to a localized Resource of your own choosing.
