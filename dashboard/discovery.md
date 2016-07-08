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

Once the discovery is ready, you receive an e-mail notification, and
the statistics will show up on the Discovery page. Based on this you
can give a rough estimation for the website translation cost - both in
time and money.

![Discovery statistics](/img/discovery-statistics.png)

## Statistics

See here for a detailed explanation of how statistics work in
Easyling.

# Discovery settings

## Pages

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
match your query. This is a forward-Search (regexp is not supported in
the Page list).

## Resources

## External links
