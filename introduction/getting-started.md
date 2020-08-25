# Getting started

Let us give you a quick overview of how the proxy is used. In this section, we give you a quick introduction to the Dashboard 2.0 and we'll also set up a simple project.

## Registration & Login

To use Easyling, you need to register and set up an account for the service at [https://app.easyling.com](https://app.easyling.com). You can start using the service right away after registration.

Logging in, you will be taken to the Dashboard 2.0, which is the new and improved project management center, every detail of which we'll get to in later sections of this manual. There will be no existing projects at the outset, so let's try setting one up.

## Setting up Your First Project

To do this, click on **Create new project** dropdown at the top and choose **Add project**.

This opens the **Create new project** dialog box, where you can enter the URL of the website you would like to translate and select the website language. You can also add an alias to your project. This is an easy to remember name that you can recognise your project from. You can also decide to start a Discovery immediately after creating your project to skip the next section. <br /> Click on Advanced Settings to access extended functionality, such as custom SRX files.

![Add Project](/img/dashboard2/add_project_dialog.png)

## Running a Discovery

![Crawl wizard](/img/dashboard2/crawl_step_5.png)

The next step is to figure out what (and how much of it) to translate. You can do so using a Discovery. This effectively means running a crawler on the site and allowing the proxy to 'explore' it in its entirety. It can then provide statistics for you such as a list of pages visited and the word count.

If you decided not to immediately run a Discovery on project creation, once you click 'Create', you’ll be directed to the Crawl wizard. This 5 step wizard is designed to guide you through setting up crawls. When running your first crawl, it’s recommended to select Discovery on step 1 and 'Re-visit current pagelist & Find new pages' on step 2. On step 3, you can specify a page limit. This is the maximum number of pages that the crawler is allowed to visit. This feature lets you to start a crawl without worrying about costs getting out of control. Make sure that this field has a reasonable number and that it’s never left empty. Step 4 has some advanced settings. These can allow you to fine-tune the crawl’s settings. The defaults are safe. So click next for now. Finally, in step 5, you can review your settings and add a memo. Then you can click Start crawl.

Depending on the size and speed of the site, a Discovery can take quite some time to finish. A spinner on the Crawl list will indicate that the system is currently working.

After the process is over, you’ll receive an e-mail about the results. You can also view them in the Crawl list.

![Crawl list](/img/dashboard2/crawl_list.png)

### Add a Target Language

You will also need to add your target language(s), so use the option on the Target languages card in the Project overview to add then to the project. It's not just that there is not much to do in terms of translation without a target: many crucial features (including the Preview proxy and the entire Workbench) are entirely unavailable as long as no target languages are set.

![Add target language](/img/dashboard2/add_target_language.png)

You can add any number of target languages. You can use the search function to lookup languages based on locale code or country name.

## Giving a Quote

You can use the results of the Discovery to give a quote (based on **unique** source words) to your clients about the estimated work-hours and expenses you forecast for a given project.

The results are an accurate indication of the translation costs associated with the text. However, with websites, it is prudent to **consider other (techincal) details** before taking the word count results of the Discovery process at face value.

Investigate the source site and consider the following:

- Is there a great deal of **dynamic content**?

- Any **Site Search** functionality? A **webshop**? A **forum**?

- Any other **web apps** that would have to be localized?

- Do the **average word lengths** of the source and target languages differ significantly?

- Is the **direction of the target language** different than that of the source language?

- Which pages are targeted for translation? Which pages need to be excluded? Ask the client if they have a specific page list.

- Does the site have mixed-language content? If yes, ask the client to specify the source language(s) they need translated.

- Is there an extant Translation Memory that could be used?

- Is there any region-specific content? Does the site use geolocation?

- Is there any content behind a secure login?
  
- Are there any subdomains? Example.com and blog.example.com require two separate projects that need to be linked.

- Are there any other special requirements?

- Is there any Javascript-generated content?

If you answered yes to any of those questions, that will require some deliberation, often beyond the primary focus of translators: UI fixes and a measure of fiddling with what's under the hood - take those expenses into account when you make your quote.

If you are unsure as to how to go about translating a part of a website, feel free to contact our **Support Centre** and we'll help you get an accurate picture of the required effort and costs.

It is also advised to negotiate the expected workflow with the client at the quoting phase. The translation of a website is, in most cases, a never-ending process, as new content is added to the original site at certain intervals.

The question is, how content added *after* the initial quote should be treated - both from a technological and fiscal viewpoint. It is a good idea to ask the client about their intentions for update cycles and new content.

Do they wish to publish at the same time in all languages? Or publish on the original site without delay, and then publish the translations later, as they become available? The different options will require different approaches when you get to the maintenance phase of the project.

As a translation proxy is practically a translation layer on top of the original site, serving translations from the datastore by replacing original content on-the-fly, new content will not be replaced, as translation is not stored for that. In practice it means that newly added content will appear in the original language on the translated site. This is called *bleedthrough*. There are 2 approaches to this phenomenon: let bleedthrough happen, to make new content available right away, even if it is in a different language, or block new content from appearing until translation is done. Both have their clear advantages and drawbacks, so you have to discuss with your client which option is more acceptable for them - and set up your project accordingly.

### Sales tool for mass production

Easyling also offers a Sales Tool to help LSPs and freelancers in growing their business.

If you have a well-defined group of potential customers you'd like to offer your translation services to, like hotels or restaurants with only monolingual websites in your area, the translation proxy makes it easy for you to impress the business owners. Just collect the URL addresses, add them to the Sales Tool, and the translation proxy will automatically create a project for all webpages according to the settings you specify. Once the translation and post-editing of the translated main pages are ready, you can send a link to the business owners. If your potential clients are impressed with the translated page and the fact that no IT involvement is required on their end, you have a better chance to win the deal.

For more information see our [blog](https://www.easyling.com/blog/try-sales-tool-lsps-freelancers/) or this short [video](https://www.easyling.com/features/mass-sales-tool/)

## The Workbench

You can export all source segments, translate them in your CAT tool of choice and then reimport your results. But going through that cycle for every small change would get rapidly tedious - wouldn't it be great if you could edit & control your translations in the cloud, where it would all update in real time? You're looking for the Workbench.

In Pages list, you can right click any page and choose 'Translation workbench (list view)' and you'll be taken to the Workbench in a different tab.

If the Dashboard 2.0 is the Project Management Center in Easyling, then the Workbench is the cloud CAT tool, where translation itself takes place. There are many features you can use in the Workbench to make working with websites easier - see the 'Workbench' section of this manual for the details.

## The 3-Phase Workflow

Barring some detail (withheld for the sake of a convenient introduction) the above process is all that you need to get a website translation project going.

![Project Workflow Overview](/img/workflow.png)

Our idea of a project's lifetime can be summarized in the 3-phase Workflow.

### 1. Discover & Quote

Set up a project and Discover it. Have a Unique Word Count total and a general idea of any technical issues involved. Give your quote to the client (perhaps demo/impress them via the Live Preview). Win the bid.

### 2. Ingest & Translate

After you are entrusted with the project, collect all text content into a database (overcoming any technical issues that may arise in the process). When you have your data, export it to your CAT tool of choice or translate in the Workbench to a selection of target languages. Reimport and edit. Use our Proofreading and Workflow features to ensure quality.

### 3. Publish & Maintain

After the translation is greenlit by the proofreaders, you can verify the serving domain and publish the translated website. Add a language selector to the source site. Generally, it is with publishing a website that a deadline is met.

But don't forget that a website is a living thing, with new content arriving every day - the final stage of website localization is always maintenance - making sure that new content gets translated according to schedule, all the while ensuring that visitors to the site will not be inconvenienced by bleedthrough of untranslated content.

Maintenance is the "long tail" of website translation - there are a variety of features in the proxy that make it a lot easier than it would be otherwise.

In the following pages, You will find everything there is to know about using the proxy. Keep reading!
