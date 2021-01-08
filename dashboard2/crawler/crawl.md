Crawl
=====

Presumably, one of the most important tools for your working process is the crawler, since it allows you to map out sites by running a _Wordcount (Discovery)_ for proposals for instance or start _Content extraction (Scan)_ for
 translation. There are two more crawling options, and we will discuss these as well in this article. You can set up crawls using the [Crawl wizard](crawlwizard.html).

You can also read a more technical description of the crawler [here](../../tech-manual/crawler.html).

## Wordcount (Discovery)

Before you can translate a website, you need to extract the content from it using the Content extraction (Scan) function. Scans, however, write to the database, which, as you know from our pricing model, will cost you money. In that sense, it would be risky to let loose an unlimited Scan on a website you’re not familiar with. To forego Content Extraction and limit the crawler’s actions to finding out about the structure and word count of a given web site, a more tentative approach is needed: a Discovery.

**The process maps the structure of the site by scanning each page for link elements and trying to follow these links. The content of the website is not stored, only the URL address of the visited pages, together with their status info.** Any page that is verified to exist is marked as Discovered, and the ones that returned an error message (most commonly redirection (HTTP301-302) and page not found (HTTP404)) are marked _Unvisited_ in the page list. For more information on HTTP status codes, see [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). Although this process doesn’t extract content, it provides a preliminary wordcount and a repetition rate as well. It has a cost of 1 EUR or 1.2 USD per thousand pages.

**IMPORTANT!
If you exclude pages during discovery, changing the rules only will not include them in the new discovery; you have to add them manually through the “Add pages” dialogue.**

Your primary choice is between limited and unlimited Discoveries.

A limited Discovery is the best way to “get to know” a website - if you set a reasonable safety number, such as the default 100, you can be sure the process won't go overboard when it finds an enormous forum or a structurally complicated web-shop.
Based on what a limited Discovery tells you about a site, you can set prefix exclusion rules in the page list or cherry-pick unnecessary pages for exclusion.
By increasing the page limit and running Discoveries in succession while adjusting your inclusion/exclusion rules, you can work your way through a site structure incrementally.
Of course, if you have a clear idea of the size of the site, you can always set up an unlimited Discovery, wait for it to finish and set up your exclusion rules afterwards. We don't recommend running unlimited crawls. It's always safer to add a large limit instead.

Once the discovery is ready, you will receive an e-mail notification and the statistics will show up on the _Crawl list_ page. Based on this you can give a rough estimation for the website translation cost - both in time and money.

## Content extraction (Scan)

The main difference between Wordcount (Discovery) and Content extraction (Scan) is that Wordcount does not extract or store content. They are used for statistical purposes, such as providing a word count or mapping a site’s URL structure.

A Content extraction (Scan), however, writes into the database. It extracts and stores the source content to be translated. New source words added to the database are billed, therefore care must be taken when starting Scans. If you are not really sure about a site, stick to Discovery until you gain a better understanding of its structure! Unlimited Scans especially require attention: they will relentlessly add all content to the database according to the specification you set for them and are likely to only stop when your wallet is depleted.

Settings you used to experiment with Discoveries can also be used to initiate Scans - for a detailed explanation of the different settings, please take a look at the menu called [_Crawl Wizard_](crawlwizard.html).

There is a card called _Database word & repetition analysis_ on the _Project overview_ menu, which shows the number of words written into the database and will only change when you Scan the page.

## New content detection

New Content Detection is basically a hybrid between the Wordcount (Discovery) and Content extraction (Scan). It runs through the set of pages selected for translation, but it does not store content at all, it's just providing a wordcount statistics based on pre-existing source entries.

## TLS Content extraction (Scan)

If you select the tweak called _Target language specific content_ in Advanced settings, then you will be able to run a _Target Language Specific Content extraction (Scan)_ in Crawl wizard.

When the translatable site has various content by target languages, and the remote server would serve the requests based on the given locale codes, you can ingest the content with this type of crawl. The proxy uses the `X-TranslationProxy-Translating-To` header during the crawl, containing the four-letter locale code used for the request, so the remote server should process this header, and serve the request based on the provided locale code.
