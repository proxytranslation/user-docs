# Introduction

Easyling is a cloud-based translation proxy solution designed to make
websites available in several languages. Easily.

**What does it mean?**<br>

If you are a **business owner**, it can help you reach a wider
customer-base through providing information to your potential
customers in their native language. What's more, you can do more than
just translating the text on your website, you can ***localize*** it:
you can also adapt your message, the images displayed, or even your
product range offered to the targeted culture. And all this without
the need of heavy upfront investment in IT infrastructure and
personnel, and the hassle with regular maintenance and
upgrade. Easyling takes care of the IT part, so that you could
concentrate on the content - and growing your business.

If you are a **language service provider** (LSP), you can offer
cutting-edge website localization services to your customers - even
under your own brand name! Easyling provides the technology, takes
care of the IT infrastructure, leaving you to concentrate on your core
business: cross-cultural communication. What's more, your translators
don't need to learn using just another tool, they can keep using their
own preferred CAT-tools.<br> 

***Sounds good?***

There are several challenges both business owners and language service
providers face during website translation. The "ideal" workflow would
be to create the content in the original language, get it translated
into the desired languages, and then publish all language variants at
the same time, from the website owner's own content management system
(CMS) - right from the very first page on the website. But reality is
different. Apart from the fact that not many CMSs are capable of
handling several languages, usually website localization comes into
the picture at a later stage, when there is already a huge amount of
data published on the website. And, in most cases, the website owner
can't extract the content for translation. If they can't extract the
original, there's no easy way to load the translated content back
either. Furthermore, if the website owner can't extract the content
into translatable format, it is impossible to get a proper estimate
for the translation costs in time and money...

Easyling can, however, discover the website by following links and
grabbing translatable and localizable content - and convert it into a
translatable format. This gives a realistic view of the magnitude of
the translation task, and, thanks to the translation proxy, even a
partially translated site can give full user experience on the website
visitor's side.  

Data can be extracted with a couple of clicks - and the publication of
the translated site is similarly easy.

## Features

- processes HTML, handle JavaScript/AJAX/JSON, XML (note: translation
  of Flash is not supported)
  
- Use the X-Proxy to determine what would be currently translated. If
  it doesn't, use the Advanced Settings to fine-tune the JSON/XML path
  settings
  
- The crawler can discover static pages / HTML content only. You have
  to manually add any extra AJAX URLs, with the proper parameters.

- When you run the crawler, always use Discovery first, and be
  incremental: "Unlimited" really means unlimited, and as such, can
  yield to very-very high cost. Running an unlimited crawl on an
  e-commerce website is a very-very bad idea.

- Based on the initial, limited crawls, fine-tune the "Ignore query"
  parameters, to help the crawler decide what URLs to handle as same,
  and what to visit in hope of new content to be discovered.

- Always check all the forms for error messages, congratulation
  messages, etc.

- Check all the images; some website like to bake the text into the
  image. Those will require your attention.

- Pay attention to forms etc included from domains outside of
  Easyling. Typical examples: Marketo, optimizely.com, etc. You'll
  have to create new Easyling project for them, then linking together
  the projects.

- Never underestimate the power of injecting CSS and/or JS into the
  translated pages

- Regular expression is a great way to reduce the amount of content to
  be translated.
  
## Getting started 

In this section, we give you a quick overview of how you'll be using
the Dashboard and we'll set up a simple Project.

## Registration & Login 

To use easyling, first you need to register and set up an account for
the service at [https://app.easyling.com](https://app.easyling.com).

Right after registration you can start using the service. When you log
in for the first time, you can select if you are a Website owner, a
Freelance translator or a Language Service Provider. This is for
statistical purposes only, it has no influence at all on the User
Experience later on.

## Introducing the Dashboard

After logging in, you will be taken to the Dashboard. This will be
your project management centre, and we'll get into the details of it
shortly. But there won't be any projects the first time around -
we'll have to set one up. 

## Setting up Your First Project 

To do this, click on **Create new project** and choose **Add project**
from the drop-down menu.

This opens the **Add project** dialog box, where you can enter the URL
of the website you would like to translate, and also select the
website language; this sets the source language of the translation
project.

## Running a Discovery

![Run discovery](/img/discovery.png)

Discovering a website means running a ``crawler`` on it and allowing
Easyling to 'explore' all its content to provide Statistics for
you. As you can see in the 'Add project' dialog window, the Dashboard
is set up to automatically start a Discovery on a webpage after
creating a project - but don't worry! After clicking on the **Add
project** button, a new dialog will open where you get to set up
additional details of the Discovery before the process can run in
earnest.

There are many interesting details that go into setting up an
effective Discovery, but let's set those aside for the moment. For
now, simply Click on the 'Add project' button and after the Discovery
dialog opens, click on Discover to start a crawl on the website.

Depending on the size of the site, a Discovery can take quite some
time to finish (a spinner on the Discovery page will indicate that the
system is currently working, and there is a 100 page limit set by
default). After the process is over, you'll receive an e-mail about
the results. You also have your first Statistics from the Discovery -
a word count total from all Discovered pages.

## Giving a Quote 

You can use the results of the Discovery to give a quote (based on
**unique** source words) to your clients about the estimated
work-hours and expenses you forecast for a given project.

Please note that While the results themselves are a very good
indication of the translation costs, it is prudent to consider other
(technical) details before taking the word count results of the
Discovery process at face value.

Investigate the source site and consider the following questions: is
there a lot of **dynamic content**?  Is there a **search engine** in
place? A **webshop** or a **forum**? Some **web apps** that would
require localization? Do the **average word lengths** of the source
and target languages differ significantly? Is the **direction of the
target language** different than that of the source language?

There are yet a few additional considerations that may require input
from the client:

- which pages are targeted for translation? Which pages need to be
  excluded? Ask the client if they have a specific page list.

- does the site have mixed-language content? If yes, ask the client
  to specify the source language(s) they need translated.

- is there an extant Translation Memory that could be used?

- is there any region-specific content? Does the site use geolocation?

- is there any content behind a secure login?
  
- are there any subdomains? example.com and blog.example.com require
  two separate projects that need to be linked.

- are there any other special requirements?

- is there any Javascript-generated content?

Some of these issues will require attention, such as UI fixes and a
measure of fiddling with the technology under the hood - take them
into account when making your quote.

If you are unsure about a functionality on a site, you can always
contact our **Support Centre** and we'll help you get an accurate
picture of the required effort and costs.

It is also advised to negotiate the expected workflow with the client
at the quoting phase. The translation of a website is, in most cases,
a never-ending process, as new content is added to the original site
at certain intervals.

The question is, how content added *after* the initial quote should be
treated - both technically and financially. It is a good idea to ask
the client how they intend to treat new content. 

Do they wish to publish at the same time in all languages? Or publish
on the original site without delay, and then publish the translations
later, as they become available? 

In the first case you need a staging server. The second option raises
another question.

As a translation proxy is practically a translation layer on top of
the original site, serving translations from the datastore by
replacing original content on-the-fly, new content will not be
replaced, as translation is not stored for that. In practice it means
that newly added content will appear in the original language on the
translated site. This is called *bleedthrough*. There are 2 approaches
to this phenomenon: let bleedthrough happen, to make new content
available right away, even if it is in a different language, or block
new content from appearing until translation is done. Both have their
clear advantages and drawbacks, so you have to discuss with your
client which option is more acceptable for them - and set up your
project accordingly.

### Sales tool for mass production

Easyling also offers a Sales Tool to help LSPs and freelancers in
growing their business.

If you have a well-defined group of potential customers you'd like to
offer your translation services to, like hotels or restaurants with
only monolingual websites in your area, easyling makes it easy for you
to impress the business owners. Just collect the URL addresses, add
them to the Sales Tool, and easyling will automatically create a
project for all webpages according to the settings you specify. Once
the translation and post-editing of the translated main pages are
ready, you can send a link to the business owners. If your potential
clients are impressed with the translated page and the fact that no IT
involvement is required on their end, you have a better chance to win
the deal.

For more information see our
[blog](https://www.easyling.com/blog/try-sales-tool-lsps-freelancers/)
or this short [video]
(https://www.easyling.com/features/mass-sales-tool/)

## On the Workbench

Easyling makes it possible for you to export source segments,
translate them in your CAT tool of choice and then reimport your
results. But going through that cycle for each little change you make
would get rapidly tedious - wouldn't it be great if you could edit &
control your translations in the cloud, where it would all update in
real time? That's what the Workbench is for.

In Pages View, you can hover over any page - a menu will show up right
next to it - choose 'Translation in List View' and you'll be taken to
the Workbench in a different tab.

If the Dashboard is the Project Management Center in Easyling, then
the Workbench is the cloud CAT tool, where translation itself takes
place. There are many features you can use in the Workbench to make
working with websites easier - see the 'Workbench' section of this
manual for the details.

## The 3-Phase Workflow 

Barring crucial details (withheld for the convenience of introduction)
the above process gets you started on a website translation project.

The Easyling idea of that project can be summarized in the 3-phase
Workflow.

### 1. Discover & Quote 

Set up a project and Discover it. Have a Unique Word Count total and a
general idea of any technical issues involved. Give your quote to the
client (perhaps demo/impress them via the Live Preview). Win the bid.

### 2. Ingest & Translate

After you are entrusted with the project, collect all text content
into a database (overcoming any technical issues that may arise in the
process). When you have your data, export it to your CAT tool of
choice or translate in the Workbench to a selection of target
languages. Reimport and edit. Use our Proofreading and Workflow
features to ensure quality.

### 3. Publish & Maintain 

After the translation is greenlit by the proofreaders, you can verify
the serving domain and publish the translated website. Add a language
selector to the source site. Generally, it is with publishing a
website that a deadline is met.

But don't forget that a website is a living thing, with new content
arriving every day - the final stage of website localization is always
maintenance - making sure that new content gets translated according
to schedule, all the while ensuring that visitors to the site will not
be inconvenienced by bleedthrough of untranslated content.

Maintenance is the "long tail" of website translation - there are a
variety of features in Easyling that render it a lot more
convenient than it would ordinarily be.

Keep reading and find out all about it.

## Pricing

See [https://easyling.com/pricing](https://easyling.com/pricing) for
detailed information about our service fees.

## Glossary

We use a set of recurring terminology in this manual and also in our
Support Channels - we collect them here for your reference.

<dl>
<dt>Scan</dt><dd>Extracting content from the website for translation</dd>
<dt>Discovery</dt><dd>Checking the website for translatable content</dd>
<dt>Resource</dt><dd>Binary content found on the website (images, PDFs, CSS and JS files, etc.)</dd>
<dt>Workbench</dt><dd>The online editing view of Easyling</dd>
<dt>List view</dt><dd>The main view of the Workbench; a simple editor for online translation</dd>
<dt>Highlight view</dt><dd>The secondary view mode of workbench, allowing for in-context editing</dd>
<dt>Bleedthough</dt><dd>When newly added, untranslated content appears on the translated site in the original language</dd>
<dt>Keep Cache Strategy</dt><dd>The strategy used to avoid bleedthrough. The last fully translated version is available on the translated pages, and new content is only added when the translation is ready</dd>
<dt>Exclusion rule</dt><dd>A rule specified for explicitly excluding pages from the translatable list</dd>
<dt>Inclusion rule</dt><dd>A rule specified for explicitly including pages in the translatable list</dd>
<dt>Page freeze</dt><dd>No new items can be added to the page-list marked for translation</dd>
<dt>Dictionary freeze</dt><dd>No new items can be added to the translation memory. Only available when Page freeze is activated.</dd>
<dt>102% match</dt><dd>Strong contextual repetition. Every single segment within a block is a 101% match, and all tags are identical.</dd>
<dt>101% match</dt><dd>Contextual repetition. Tags within the segment and the neighbouring segments are repetitions / exact matches as well.</dd>
</dl>

## Further information

**Tutorials**

  - [https://www.youtube.com/watch?v=S47kArNiJ1o](https://www.youtube.com/watch?v=S47kArNiJ1o)
  - [https://www.youtube.com/watch?v=8VsBy2bGo64](https://www.youtube.com/watch?v=8VsBy2bGo64)
  - [https://gitlab.com/easyling/wikis/home](https://gitlab.com/easyling/wikis/home)
  - [https://drive.google.com/open?id=0Bw53oZELMrf8V1FIUnhmNEtubTA](https://drive.google.com/open?id=0Bw53oZELMrf8V1FIUnhmNEtubTA)

  - [http://lesson101.tutorial.easyling.com/](http://lesson101.tutorial.easyling.com/)
  - [http://lesson102.tutorial.easyling.com/](http://lesson102.tutorial.easyling.com/)
  - [http://lesson103.tutorial.easyling.com/](http://lesson103.tutorial.easyling.com/)
  - [http://lesson105.tutorial.easyling.com/](http://lesson105.tutorial.easyling.com/)

**Release notes**

  - [https://www.easyling.com/category/blogpost/release-notes/](https://www.easyling.com/category/blogpost/release-notes/)
  - [https://www.easyling.com/change-logs/](https://www.easyling.com/change-logs/)
